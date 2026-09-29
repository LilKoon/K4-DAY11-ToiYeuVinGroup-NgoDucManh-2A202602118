# Kế hoạch review từ lỗi quan sát được

| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| B3-center / 167700 | TP=5, FP=1, FN=4; sai class L1 Truck/R4 Car; thiếu R2 Bike và R7/R8 Truck; L7/L8 bị báo IGNORE_SCOPE | Có cả vấn đề phạm vi, class và thiếu vật. Soát ignore trước rồi class và recall. | Ảnh gốc, compare.html, XML khóa, local_quality_conflicts.csv, screenshot trước/sau |
| B3-center / 152940 | TP=4, FP=0, FN=2; thiếu R5 Truck/R6 ThreeWheeler; nhận xét QA chưa định vị chính xác | Làm rõ bất đồng giữa mô tả QA và reference, tránh thêm nhãn theo suy đoán. | received_review_B3-center.md, ảnh nền trái có đánh dấu, đo H và rule R01/R04 |

212280 có TP=3 FP=0 FN=0 ở phép so rectangle, nhưng chưa chứng minh ego_body/attribute/K12 đều đúng. Giới hạn: ba ảnh một camera; số box ít, reference dạy học có thể sai. Không suy tỷ lệ lỗi sản xuất hay thứ hạng rủi ro từ zone.

## Chuyển sang kế hoạch bốn camera giả lập

Tám ô trong 45_sampling_plan.csv cộng 200. Giả định bốn camera có độ phủ tương đương nên khởi đầu 50 frame/camera, mỗi camera 20 normal + 30 hard. Đây là thiết kế ban đầu, không phải phân bổ tối ưu đã đo. Chia theo chuyến/đoạn thời gian trước khi chọn, hạn chế frame liên tiếp cùng cảnh; theo dõi ngày/đêm, khô/mưa, mật độ, che khuất và seam riêng từng camera. Giữ ID cảnh để không tính nhiều frame liên tiếp là ca độc lập. Dùng một tập ngẫu nhiên riêng nếu cần ước lượng tỷ lệ lỗi, vì mẫu hard được chọn có chủ đích sẽ gây lệch.
