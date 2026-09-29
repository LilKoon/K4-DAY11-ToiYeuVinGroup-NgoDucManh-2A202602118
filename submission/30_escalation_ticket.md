# Escalation ticket

## Ticket 1

- **Frame:** adasind_014670.jpg, L6 Bus / R5 Truck / M3 Bus; bản khóa 9BB2-E044.
- **Ảnh chụp:** [So sánh L/R](screenshots/p4-compare.png) và [so sánh L/R/M](screenshots/p4-model.png), chụp từ báo cáo HTML bằng Edge. Cả hai hiển thị xe sát trái với L6 Bus, R5 Truck; ảnh model thêm M3 Bus. Đối chiếu ảnh gốc assets/images/adasind_014670.jpg và confusion CSV của P4.
- **Expected impact:** Một bất đồng class tạo FP Bus và FN Truck trong local quality; các nhóm LM_noR/R_only có thể khiến người đọc hiểu nhầm là hai vật khác nhau hoặc nhãn thiếu/thừa. Không suy điểm rubric từ xung đột này.
- **Owner:** qa; tham vấn guideline khi cần phân biệt hình dáng Bus/Truck từ phần thân xe còn nhìn thấy.
- **Recommendation:** Phóng to thân xe/cửa sổ để phân xử theo R04. Giữ L6 hiện tại trong lúc chờ; không thêm box Truck chồng lên cùng vật chỉ để khớp reference. Nếu xác nhận reference sai, cập nhật version reference qua người phụ trách; không tự sửa reference. Findings L6+M3 và R5 đang E5_unresolved/action=escalate.

Trạng thái: ticket đã soạn trong repo, chưa gửi bên ngoài và chưa có phản hồi người nhận.

## Ticket 2

- **Frame:** adasind_034080.jpg, L7 Pedestrian / R3; QA nhận được mục 4.
- **Ảnh chụp:** Cần ảnh phóng to vùng mép phải. Bằng chứng hiện có: assets/images/adasind_034080.jpg, submission/r3_diag/qa_response.md và compare.html.
- **Expected impact:** Phân xử truncated trước khi sửa thuộc tính; tránh dùng khoảng cách box tới mép như bằng chứng chắc chắn cơ thể bị cắt.
- **Owner:** qa.
- **Recommendation:** Kiểm tra phần tay/thân sát x=1080 trên ảnh gốc. Nếu cơ thể bị cắt thì đổi truncated=true; nếu vẫn đầy đủ thì giữ false và giải thích cảnh báo tự động. Không đổi chỉ để khớp reference. Quyết định QA-IN-04 đã ghi escalated trong decision log; nhãn chưa sửa.
