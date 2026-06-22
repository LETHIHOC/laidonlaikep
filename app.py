 import streamlit as st

# Giữ nguyên ảnh hiển thị đầu trang
st.image("1781888688474_269653485332215076_7657796446612170719_a27d91ccef475fe90505bccad974295c.jpg")

# Tiêu đề ứng dụng
st.title("💰 TÍNH THUẾ THU NHẬP CÁ NHÂN_Lê Thị Học")

LUONG_GROSS = 45.0     
SO_NGUOI_PHU_THUOC = 1  

# 1. Quy đổi sang tiền Đồng để tính toán chính xác
gross_vnd = LUONG_GROSS * 1000000

# 2. Tính bảo hiểm bắt buộc của Người lao động (10.5% bao gồm 8% BHXH, 1% BHTN, 1.5% BHYT)
bao_hiem_vnd = gross_vnd * 0.105

# 3. Các khoản giảm trừ gia cảnh
giam_tru_ban_than = 15500000     # 15.5 triệu đồng
giam_tru_phu_thuoc = SO_NGUOI_PHU_THUOC * 6200000  # 6.2 triệu đồng/người

# 4. Tính thu nhập tính thuế
thu_nhap_tinh_thue = gross_vnd - bao_hiem_vnd - giam_tru_ban_than - giam_tru_phu_thuoc
thu_nhap_tinh_thue = max(0.0, thu_nhap_tinh_thue)

# 5. Áp dụng Biểu thuế lũy tiến 5 bậc mới theo hình ảnh của bạn để tính thuế
if thu_nhap_tinh_thue <= 10000000:
    # Bậc 1: Đến 10 triệu (5%)
    thue_tncn_vnd = thu_nhap_tinh_thue * 0.05
elif thu_nhap_tinh_thue <= 30000000:
    # Bậc 2: Trên 10 triệu đến 30 triệu (10%)
    thue_tncn_vnd = (thu_nhap_tinh_thue * 0.10) - 500000
elif thu_nhap_tinh_thue <= 60000000:
    # Bậc 3: Trên 30 triệu đến 60 triệu (20%)
    thue_tncn_vnd = (thu_nhap_tinh_thue * 0.20) - 3500000
elif thu_nhap_tinh_thue <= 100000000:
    # Bậc 4: Trên 60 triệu đến 100 triệu (30%)
    thue_tncn_vnd = (thu_nhap_tinh_thue * 0.30) - 9500000
else:
    # Bậc 5: Trên 100 triệu (35%)
    thue_tncn_vnd = (thu_nhap_tinh_thue * 0.35) - 14500000

# 6. Tính lương NET thực nhận
net_vnd = gross_vnd - bao_hiem_vnd - thue_tncn_vnd

# Hiển thị kết quả ra màn hình web
st.subheader(f"Kết quả tính toán cho mức lương: {LUONG_GROSS} triệu")
st.write(f"📌 Tiền đóng bảo hiểm (10.5%): **{bao_hiem_vnd / 1000000:,.2f} triệu đồng**")
st.write(f"📌 Mức giảm trừ gia cảnh áp dụng: **{(giam_tru_ban_than + giam_tru_phu_thuoc) / 1000000:,.2f} triệu đồng**")
st.write(f"📌 Thu nhập tính thuế sau giảm trừ: **{thu_nhap_tinh_thue / 1000000:,.2f} triệu đồng**")
st.write(f"📌 Thuế TNCN phải nộp: **{thue_tncn_vnd / 1000000:,.2f} triệu đồng**")
st.success(f"💰 **Lương NET thực nhận: {net_vnd / 1000000:,.2f} triệu đồng**")
