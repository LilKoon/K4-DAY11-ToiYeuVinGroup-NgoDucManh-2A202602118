# Kế hoạch review từ lỗi quan sát được

Từ `findings.csv` và `zone_table.md`, chọn **hai lát cắt của bài ADASIND một camera** cần review trước. Bảng này
giải thích dữ liệu thật bạn vừa làm; nó không thay cho kế hoạch bốn camera giả lập ở `45_sampling_plan.csv`.

| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| B1-mid / adasind_014670.jpg | 1 bất đồng class L6 Bus với R5 Truck; model M3 là Bus | Class sai làm phát sinh cả FP và FN; phải phân xử ảnh trước khi sửa theo reference | Ảnh gốc; compare.html; confusion CSV; R04; tọa độ box |
| B1-mid / adasind_034080.jpg | 1 xung đột hình học L3/R2; 1 ca nghi đếm trùng rider R8 với L4/R5 | IoU không đạt không đồng nghĩa thiếu vật; cần tránh thêm box cho người ngồi cùng xe | Ảnh gốc; model_compare.html; iou_sweep.md; R02/R03 |

Giới hạn của kết luận từ ba frame ADASIND: mẫu quá nhỏ và chỉ một camera. Đếm xung đột không phải tỷ lệ lỗi thực đã xác nhận; reference có thể sai. Vị trí center/mid/edge không nói lên khoảng cách hoặc rủi ro vận hành.

## Chuyển sang kế hoạch bốn camera giả lập

Cách soát độ phủ của 200 frame ở `45_sampling_plan.csv` (kể cả tránh đếm nhiều frame liền nhau trong cùng cảnh
như nhiều ca độc lập), và vì sao kế hoạch đó chỉ giúp tìm ca cần soi, chưa đo được tỷ lệ lỗi: kiểm đủ 8 ô camera × normal/hard, tổng 200 frame; front/rear mỗi camera 55, left/right mỗi camera 45. Trong mỗi ô phân tầng chuyến, thời điểm, ánh sáng và class. Giới hạn một frame đại diện mỗi camera trong một sự kiện ngắn; cặp seam giữ cùng event_id và timestamp, tính đúng số frame nhưng không xem là các sự kiện độc lập. Tập hard được chọn có chủ đích nên không dùng tỷ lệ lỗi thô để đại diện 50.000 frame; muốn ước lượng cần thiết kế xác suất và trọng số phù hợp. Chưa có dữ liệu bốn camera thật để kiểm chứng phân bổ này.
