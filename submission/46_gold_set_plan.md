# Đề xuất gold set theo camera — tình huống giả lập

**Đầu bài:** 50.000 frame từ bốn camera SVM, ngân sách chọn 200 frame để review/gold. Đây là tình huống trên slide,
**không phải** 50.000 frame có trong repo. Phân bổ đúng 200 ở `45_sampling_plan.csv` cho bốn camera, mỗi camera có
normal và hard slice. “Gold set” ở đây là **kế hoạch tạo** reference sau kiểm chứng, không phải teaching reference
ADASIND hoặc nhãn bạn vừa vẽ. Nếu cần, dùng `notebooks/day11-svm360-colab.ipynb` để thử tổng phân bổ; notebook
không làm thay phần lý do.

| camera_id | Hard case cần chọn | Vì sao dễ sai | Annotation space / calibration cần giữ | Cách review trước khi gọi là gold |
|---|---|---|---|---|
| front | Normal: cảnh rõ; hard: ngược sáng và rider chồng xe | Nhầm class; tách người ngồi xe; thiếu vật nhỏ | Ảnh fisheye gốc; camera_id; timestamp; intrinsics và extrinsics có version | Người A gán nhãn; B review độc lập cả normal/hard; QA phân xử bất đồng theo ảnh/rule |
| rear | Normal: cảnh phía sau rõ; hard: thiếu sáng và người bị che lúc lùi | Thiếu box; nhầm truncated với occluded | Giữ raw frame và cấu hình camera sau; không trộn ảnh BEV với ảnh gốc | Review riêng camera sau; đo lại vật sát ngưỡng; QA xác nhận sau sửa |
| left | Normal: người/xe bên trái; hard: seam và méo rìa | Box hình học lệch; nhầm hai quan sát thành trùng | Calibration camera trái và cặp seam đồng bộ; lưu phép biến đổi nếu có ảnh rectified | Hai người soát độc lập; kiểm các ca seam và rider; lưu quyết định |
| right | Normal: cảnh bên phải rõ; hard: vật sát curb và bị mép ảnh cắt | Sai thuộc tính; thiếu người bị che | Calibration camera phải; timestamp và policy annotation space thống nhất | Review riêng normal/hard bên phải; không suy kết quả từ camera trái; QA chốt version |

- Khi nào cần refresh gold set (đổi camera, calibration hoặc rule): khi thay cảm biến/ống kính/vị trí gá, cập nhật calibration, guideline hoặc miền ánh sáng/cảnh. Chọn lại mẫu chịu tác động; review lại nhãn và lưu version cùng lịch sử thay đổi. Giữ một phần mẫu cũ để đối chứng, không ghi đè im lặng.
- Một ca seam/cross-camera cần policy và evidence trước khi ghép hai box: người đi bộ xuất hiện ở front-right là hai box hợp lệ nếu đầu ra per-camera. Chỉ gán chung global ID khi có timestamp đồng bộ, calibration, bằng chứng liên tục và policy giải quyết che khuất. Cả hai frame tính vào ngân sách 200 nhưng mang chung event_id.
- Vì sao peer agreement hoặc quality report trên ảnh một camera chưa chứng minh gold set đúng cho cả bốn camera: người soát có thể cùng sai hoặc cùng dựa vào reference sai; mỗi camera có vùng nhìn và méo riêng. Chỉ gọi tập là gold sau review độc lập, phân xử, sửa và xác nhận trên cả normal/hard của từng camera. Tập này mới là kế hoạch giả lập, chưa có 200 frame thật đã kiểm chứng.
