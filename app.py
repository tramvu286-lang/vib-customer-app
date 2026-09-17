import streamlit as st
import pandas as pd
from io import BytesIO


# ==========================================
# CẤU HÌNH
# ==========================================

st.set_page_config(
    page_title="VIB - Quản lý khách hàng",
    page_icon="🏦",
    layout="wide"
)


# ==========================================
# KHỞI TẠO DỮ LIỆU
# ==========================================

if "customers" not in st.session_state:
    st.session_state.customers = []


if "care_history" not in st.session_state:
    st.session_state.care_history = []


if "appointments" not in st.session_state:
    st.session_state.appointments = []


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ==========================================
# HÀM XUẤT EXCEL
# ==========================================

def export_excel():

    df = pd.DataFrame(
        st.session_state.customers
    )

    output = BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Khách hàng"
        )

    return output.getvalue()


# ==========================================
# ĐĂNG NHẬP
# ==========================================

if not st.session_state.logged_in:

    st.title("🏦 VIB")

    st.subheader(
        "HỆ THỐNG QUẢN LÝ KHÁCH HÀNG"
    )

    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        username = st.text_input(
            "Tên đăng nhập",
            placeholder="Nhập tên đăng nhập"
        )

        password = st.text_input(
            "Mật khẩu",
            type="password",
            placeholder="Nhập mật khẩu"
        )

        if st.button(
            "ĐĂNG NHẬP",
            type="primary",
            use_container_width=True
        ):

            if (
                username == "vibstaff"
                and password == "123456"
            ):

                st.session_state.logged_in = True

                st.rerun()

            else:

                st.error(
                    "❌ Tên đăng nhập hoặc mật khẩu không đúng."
                )

    st.stop()


# ==========================================
# MENU
# ==========================================

st.sidebar.title("🏦 VIB")

st.sidebar.caption(
    "HỆ THỐNG QUẢN LÝ KHÁCH HÀNG"
)

page = st.sidebar.radio(
    "MENU",
    [
        "📊 Tổng quan",
        "👤 Nhập khách hàng",
        "📋 Danh sách khách hàng",
        "📞 Chăm sóc khách hàng",
        "📅 Lịch hẹn",
        "🔐 Admin",
        "🚪 Đăng xuất"
    ]
)


# ==========================================
# TỔNG QUAN
# ==========================================

if page == "📊 Tổng quan":

    st.title("📊 TỔNG QUAN")

    st.write(
        "Tổng quan tình hình quản lý khách hàng."
    )

    st.divider()
total_customers = len(
        st.session_state.customers
    )

    total_care = len(
        st.session_state.care_history
    )

    total_appointments = len(
        st.session_state.appointments
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "👥 Tổng khách hàng",
        total_customers
    )

    col2.metric(
        "📞 Lượt chăm sóc",
        total_care
    )

    col3.metric(
        "📅 Lịch hẹn",
        total_appointments
    )

    st.divider()

    if total_customers == 0:

        st.info(
            "📭 Chưa có dữ liệu khách hàng."
        )

    else:

        df = pd.DataFrame(
            st.session_state.customers
        )

        st.subheader(
            "📋 Khách hàng gần đây"
        )

        st.dataframe(
            df.tail(5),
            use_container_width=True,
            hide_index=True
        )


# ==========================================
# NHẬP KHÁCH HÀNG
# ==========================================

elif page == "👤 Nhập khách hàng":

    st.title(
        "👤 THÔNG TIN KHÁCH HÀNG"
    )

    st.write(
        "Vui lòng nhập thông tin khách hàng."
    )

    st.divider()

    phone = st.text_input(
        "📱 Số điện thoại",
        placeholder="Nhập số điện thoại"
    )

    name = st.text_input(
        "👤 Tên khách hàng",
        placeholder="Nhập tên khách hàng"
    )

    email = st.text_input(
        "📧 Email",
        placeholder="Nhập email"
    )

    address = st.text_input(
        "📍 Địa chỉ",
        placeholder="Nhập địa chỉ"
    )

    occupation = st.text_input(
        "💼 Nghề nghiệp",
        placeholder="Nhập nghề nghiệp"
    )

    income = st.number_input(
        "💰 Thu nhập hàng tháng (VNĐ)",
        min_value=0,
        step=500000
    )

    product = st.selectbox(
        "🏦 Sản phẩm khách hàng quan tâm",
        [
            "Vay mua nhà",
            "Vay mua ô tô",
            "Vay tiêu dùng",
            "Thẻ tín dụng",
            "Tiền gửi tiết kiệm",
            "Tài khoản thanh toán",
            "Bảo hiểm"
        ]
    )

    need = st.text_area(
        "🎯 Nhu cầu khách hàng",
        placeholder="Nhập nhu cầu của khách hàng"
    )

    source = st.selectbox(
        "📌 Nguồn khách hàng",
        [
            "Website",
            "Mạng xã hội",
            "Khách hàng giới thiệu",
            "Khách hàng hiện hữu",
            "Chi nhánh / Quầy giao dịch",
            "Sự kiện",
            "Khác"
        ]
    )

    status = st.selectbox(
        "📌 Trạng thái chăm sóc",
        [
            "Chưa liên hệ",
            "Đang tư vấn",
            "Đã hẹn gặp",
            "Đang theo dõi",
            "Đã chuyển đổi",
            "Không tiếp tục"
        ]
    )

    note = st.text_area(
      "📝 Ghi chú",
        placeholder="Nhập ghi chú"
    )

    st.divider()

    if st.button(
        "💾 LƯU THÔNG TIN",
        type="primary",
        use_container_width=True
    ):

        if phone.strip() == "":

            st.error(
                "❌ Vui lòng nhập số điện thoại."
            )

        elif name.strip() == "":

            st.error(
                "❌ Vui lòng nhập tên khách hàng."
            )

        else:

            customer = {

                "Số điện thoại":
                    phone.strip(),

                "Tên khách hàng":
                    name.strip(),

                "Email":
                    email.strip(),

                "Địa chỉ":
                    address.strip(),

                "Nghề nghiệp":
                    occupation.strip(),

                "Thu nhập":
                    income,

                "Sản phẩm quan tâm":
                    product,

                "Nhu cầu":
                    need.strip(),

                "Nguồn khách hàng":
                    source,

                "Trạng thái":
                    status,

                "Ghi chú":
                    note.strip()
            }

            st.session_state.customers.append(
                customer
            )

            st.success(
                "✅ Đã lưu thông tin khách hàng!"
            )


# ==========================================
# DANH SÁCH KHÁCH HÀNG
# ==========================================

elif page == "📋 Danh sách khách hàng":

    st.title(
        "📋 DANH SÁCH KHÁCH HÀNG"
    )

    st.divider()

    if len(
        st.session_state.customers
    ) == 0:

        st.info(
            "📭 Chưa có khách hàng."
        )

    else:

        df = pd.DataFrame(
            st.session_state.customers
        )

        search = st.text_input(
            "🔎 Tìm kiếm khách hàng",
            placeholder="Nhập tên hoặc số điện thoại"
        )

        if search:

            df = df[
                df["Tên khách hàng"].str.contains(
                    search,
                    case=False,
                    na=False
                )
                |
                df["Số điện thoại"].str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        st.metric(
            "👥 Tổng số khách hàng",
            len(df)
        )

        st.divider()

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )


# ==========================================
# CHĂM SÓC KHÁCH HÀNG
# ==========================================

elif page == "📞 Chăm sóc khách hàng":

    st.title(
        "📞 CHĂM SÓC KHÁCH HÀNG"
    )

    st.write(
        "Ghi nhận quá trình chăm sóc khách hàng."
    )
  st.divider()

    if len(
        st.session_state.customers
    ) == 0:

        st.info(
            "📭 Chưa có khách hàng để chăm sóc."
        )

    else:

        df = pd.DataFrame(
            st.session_state.customers
        )

        customer_index = st.selectbox(
            "👤 Chọn khách hàng",
            range(len(df)),
            format_func=lambda x:
                df.iloc[x]["Tên khách hàng"]
                + " - "
                + df.iloc[x]["Số điện thoại"]
        )

        customer = df.iloc[
            customer_index
        ]

        st.write(
            "**Khách hàng:**",
            customer["Tên khách hàng"]
        )

        method = st.selectbox(
            "📞 Hình thức chăm sóc",
            [
                "Gọi điện",
                "Tin nhắn",
                "Email",
                "Gặp trực tiếp"
            ]
        )

        content = st.text_area(
            "📝 Nội dung trao đổi",
            placeholder="Nhập nội dung trao đổi"
        )

        result = st.text_area(
            "📌 Kết quả",
            placeholder="Nhập kết quả chăm sóc"
        )

        next_contact = st.date_input(
            "📅 Ngày chăm sóc tiếp theo"
        )

        if st.button(
            "💾 LƯU LỊCH SỬ CHĂM SÓC",
            type="primary",
            use_container_width=True
        ):

            care = {

                "Khách hàng":
                    customer["Tên khách hàng"],

                "Số điện thoại":
                    customer["Số điện thoại"],
