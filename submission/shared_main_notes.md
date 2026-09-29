# Phần dùng chung nhập từ main

- Nguồn: origin/main, commit b1c986483b49c3fb1af9cc479871d4a566b6d7d7.
- Cách cập nhật: fetch và nhập chọn lọc; không merge toàn bộ lịch sử main vì chứa bài cá nhân manh/B4-edge.
- Giữ nguyên cấu hình duong/B3-center, r1_craft, r2_qa, r3_diag, rework, findings.csv, decision log và báo cáo cá nhân. Giữ nguyên bài parking hiện có.
- Sampling: cả hai bản dùng 20 normal + 30 hard/camera, tổng 200; bổ sung tình huống của bản chung vào rationale hiện có.
- Gold: bổ sung ca khó; BEV/LiDAR và nối track là phương án có điều kiện, chưa có bằng chứng thực trong repo.
- Quy tắc chung R03: rider và xe hai bánh chung một box Bike; người dắt xe là Pedestrian + Bike riêng. Đề xuất bổ sung hình minh họa so sánh hai tình huống để giảm nhầm lẫn. Đây là gợi ý của bản chung, không thay guideline patch cá nhân và chưa là luật mới được duyệt.

## C0 dùng chung

Đã nhập nguyên bộ p1_calib từ main, mã khóa 424A-ABDF và kiểm SHA256 XML khớp lock. Bản này chỉ có 2 polygon, 0 box; compare báo thiếu 6 box reference. Có đủ file kỹ thuật không đồng nghĩa đã hoàn thành gán nhãn C0.

Các dòng calib trong findings của nguồn được lưu riêng tại p1_calib/source_findings.csv để tham khảo; chưa trộn vào findings cá nhân và chưa coi nhận định của người khác là quan sát độc lập của duong. Mốc lock/reference là mốc của nguồn, không phải hoạt động mới của người học trên máy này.

REPORT.md cũ vẫn là bản mô tả trước lần nhập này. Thông tin “thiếu file C0” trong đó đã được cập nhật bởi ghi chú này; chất lượng C0 vẫn cần xử lý. Theo xác nhận của người dùng, QA thực tế là duong review vanh/B1-mid; không yêu cầu thêm B4-edge chỉ vì vòng mặc định trong team.json.

## Cập nhật sau nhận v2

Đã có export rework khóa 1879-C103 và delta: matched 12→14, missing 6→4, spurious 1→1. Các nhận xét “chưa có v2/delta” phía trên mô tả thời điểm trước cập nhật. V2 vẫn thiếu ego_body ba ảnh và K12 có ba cặp; các nghi vấn chưa phân xử không tự được đóng. QA thực tế đã xác nhận là duong→vanh/B1-mid; có bốn dòng findings QA và ba ảnh minh họa từ overlay. Xem REPORT.md để đọc trạng thái mới nhất.
