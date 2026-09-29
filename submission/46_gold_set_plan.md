# Đề xuất gold set theo camera — tình huống giả lập

**Đầu bài:** 50.000 frame từ bốn camera SVM, ngân sách chọn 200 frame để review/gold. Đây là tình huống trên slide,
**không phải** 50.000 frame có trong repo. Phân bổ đúng 200 ở `45_sampling_plan.csv` cho bốn camera, mỗi camera có
normal và hard slice. “Gold set” ở đây là **kế hoạch tạo** reference sau kiểm chứng, không phải teaching reference
ADASIND hoặc nhãn bạn vừa vẽ. Nếu cần, dùng `notebooks/day11-svm360-colab.ipynb` để thử tổng phân bổ; notebook
không làm thay phần lý do.

| camera_id | Hard case cần chọn | Vì sao dễ sai | Annotation space / calibration cần giữ | Cách review trước khi gọi là gold |
|---|---|---|---|---|
| front | Người đi bộ hoặc xe máy cắt ngang | Lóa sáng ngược nắng hoặc vật chồng lấp tại rìa | Giữ đủ vùng trung tâm và rìa méo | Đánh giá chéo độc lập (Blind review) |
| rear | Xe/người đi sát đuôi xe khi lùi | Biến dạng sâu kích thước do méo thấu kính | Giữ các góc khuất quanh nắp cốp/đèn xe | So sánh trực tiếp trên BEV projection |
| left | Xe máy/vật cản đi sát mép hông | Vật cản nhỏ sát sườn bị kéo dãn | Không gian hẹp sát thân (ego_body) | Soát chéo dựa vào camera trước/sau (Seam) |
| right | Vỉa hè và vạch kẻ sát lề | Các điểm bù mù ở rìa phải quá tối hoặc lóa | Góc lệch vỉa hè và lane cận | Đối chiếu với LiDAR/Radar nếu có |

- Khi nào cần refresh gold set (đổi camera, calibration hoặc rule): Khi có sự thay đổi về bộ tham số calibration của camera fisheye, hoặc có update lớn trong guideline về ranh giới box/ignore region.
- Một ca seam/cross-camera cần policy và evidence trước khi ghép hai box: Khi một vật thể nằm chéo qua góc xe (hiện trên cả camera trước và hông), cần ID tracking để không tính là 2 vật thể riêng biệt.
- Vì sao peer agreement hoặc quality report trên ảnh một camera chưa chứng minh gold set đúng cho cả bốn camera: Fisheye méo ở mỗi góc camera khác nhau, điểm giao cắt (seam) giữa 4 góc mới là vùng hay sinh lỗi model nhất, 1 cam thì không thể hiện được tính BEV 360 độ.
