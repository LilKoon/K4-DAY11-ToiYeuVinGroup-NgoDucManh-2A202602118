# Phản hồi QA nhận được — B3-center

Nguồn nguyên văn: ../r2_qa/received_review_B3-center.md. Mã F7CC-04EB khớp lock của r1_craft. File không ghi người review; chưa xác nhận tác giả chỉ từ nội dung file.

| Nhận xét | Đối chiếu | Quyết định hiện tại |
|---|---|---|
| 152940: bỏ sót xe máy và xe công nông phía sau bên trái | Báo cáo local_quality xác định R5 Truck và R6 ThreeWheeler không có box tương ứng. Ảnh có các xe nhỏ ở nền trái; chưa đủ định vị để đồng nhất “xe máy” của QA với R6. | Chấp nhận yêu cầu rà vùng nền trái; yêu cầu QA chỉ tọa độ/đối tượng và đo H≥40. Không tự đổi ThreeWheeler thành Bike theo tên gọi trong nhận xét. |
| 167700: bỏ sót xe tải xa ở giữa | Báo cáo có R7 và R8 Truck thiếu; R2 Bike cũng thiếu. QA chưa chỉ rõ đang nói R7 hay R8. | Rà cả hai Truck trên compare.html và ảnh gốc, xác nhận chiều cao và phạm vi trước khi thêm box. |

Đã nhận r1-v2.zip và khóa rework 1879-C103: matched 12→14, missing 6→4, spurious 1→1. Đây là cải thiện tổng hợp, chưa đủ để khẳng định mọi đối tượng QA nêu đã được sửa đúng; phần định vị/class chưa phân xử vẫn để mở. Xem rework/delta.md và selfqc.md.

Theo xác nhận trực tiếp của người học, duong review vanh/B1-mid. Đã chuẩn hóa rule_id và chuyển bốn nhận xét vào findings r2_qa, why để trống. Không yêu cầu export B4-edge; giữ team.json như cấu hình chia slice ban đầu, quyết định đổi vòng ghi trong decision log.
