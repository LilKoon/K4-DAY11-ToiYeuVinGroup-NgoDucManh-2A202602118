# Kế hoạch review từ lỗi quan sát được

Từ `findings.csv` và `zone_table.md`, chọn **hai lát cắt của bài ADASIND một camera** cần review trước. Bảng này
giải thích dữ liệu thật bạn vừa làm; nó không thay cho kế hoạch bốn camera giả lập ở `45_sampling_plan.csv`.

| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| B4-edge | 4 lỗi QA (occluded, R03) và nhiều lỗi SPURIOUS do model | Vùng edge ảnh fisheye thường bị méo, model dễ dự đoán sai nên cần review kỹ. | Giữ lại các frame có mật độ giao thông đông đúc. |
| B3-center | 2 lỗi QA (R01 bỏ sót vật thể) | Vùng center thường chứa nhiều vật thể nhỏ ở xa chồng chéo lên nhau. | Giữ lại các frame có người và xe lọt thỏm ở xa. |

Giới hạn của kết luận từ ba frame ADASIND: Số lượng 3 frame là quá ít để đưa ra kết luận mang tính đại diện (statistically significant) cho toàn bộ dataset, cần phải mở rộng sampling.

## Chuyển sang kế hoạch bốn camera giả lập

Cách soát độ phủ của 200 frame ở `45_sampling_plan.csv` (kể cả tránh đếm nhiều frame liền nhau trong cùng cảnh
như nhiều ca độc lập), và vì sao kế hoạch đó chỉ giúp tìm ca cần soi, chưa đo được tỷ lệ lỗi: Phải dàn đều mẫu theo các camera và điều kiện ánh sáng (stratified sampling) để tránh các frame giống hệt nhau liên tiếp. Lấy mẫu có chủ đích (targeted sampling) chỉ giúp tìm "điểm nóng" dễ sai, nhưng không thể dùng để ngoại suy tỷ lệ lỗi tổng thể (overall defect rate) cho cả dataset; để đo tỷ lệ lỗi cần random sampling.
