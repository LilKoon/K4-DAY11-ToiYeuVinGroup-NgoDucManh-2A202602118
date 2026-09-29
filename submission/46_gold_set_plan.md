# Đề xuất gold set theo camera — tình huống giả lập

Đầu bài giả lập 50.000 frame, ngân sách 200 frame; chưa có bộ dữ liệu bốn camera thực để xác nhận chất lượng. 200 là ngân sách ứng viên review, không mặc nhiên là 200 frame gold đã duyệt.

| camera_id | Normal và hard case cần chọn | Vì sao dễ sai | Annotation space / calibration cần giữ | Cách review trước khi gọi là gold |
|---|---|---|---|---|
| front | Normal: đường sáng, vật tách biệt. Hard: ngược sáng, xe/người nhỏ, giao cắt | Thiếu vật nhỏ, sai class, che khuất | Ảnh fisheye gốc, resolution, intrinsics/distortion, extrinsics, timestamp | Annotator vẽ; reviewer độc lập theo R01/R03/R04; người phân xử chốt bất đồng |
| rear | Normal: bãi đỗ sáng. Hard: lùi có người/xe cắt ngang, tối, phản xạ | Nhầm phản xạ, truncated, vùng ego | Ảnh gốc camera sau; calibration/version và thời gian đồng bộ | Review người/xe và ignore riêng; kiểm polygon theo ảnh, phân xử trước phê duyệt |
| left | Normal: vật bên hông rõ. Hard: xe hai bánh sát biên, seam trước-trái/sau-trái | Méo mạnh, rider và identity | Ảnh gốc trái; extrinsics tương đối và timestamp | Review R02/R03/R05, giữ cả box đa camera khi policy yêu cầu |
| right | Normal: lề đường rõ. Hard: người dắt xe, curb/xe đỗ, seam | Nhầm người dắt xe với rider, biên vật bị che | Ảnh gốc phải, calibration và policy output | Reviewer khác người vẽ, đo H, kiểm class và ignore; ghi quyết định truy vết |

Chọn ứng viên phân tầng theo 45_sampling_plan.csv, tách cảnh/chuyến giữa bộ hiệu chuẩn guideline và bộ đánh giá. Mỗi frame phải được soát độc lập; unresolved không vào tập gold phê duyệt. Lưu XML, phiên bản luật, calibration, reviewer, adjudicator và mã hash; khóa phiên bản sau duyệt.

Refresh khi đổi camera/lens/vị trí gá, calibration/resolution, preprocessing, taxonomy/guideline hoặc phát hiện lỗi lặp lại/điều kiện mới. Tái kiểm các ca chịu ảnh hưởng và giữ lịch sử phiên bản.

Ca seam: cùng Bike ở front và left tại cùng thời điểm có thể cần hai box trong output per-camera. Chỉ nối identity khi timestamp đồng bộ, calibration, liên tục chuyển động và policy cross-camera đủ rõ; không xóa một box chỉ vì thấy cùng xe.

Peer agreement có thể cùng sai; teaching reference và quality report một camera không chứng minh bộ gold bốn camera. Chưa có calibration/timestamp thực nên kế hoạch này không xác nhận khả năng ghép BEV hoặc track.

## Bổ sung phần dùng chung từ main b1c9864

Nhóm đề xuất thêm ca phản chiếu/góc khuất khi lùi, vật kéo dãn ở hông trái, vỉa hè/vạch sát lề phải trong điều kiện tối/lóa. Đưa các ca này vào danh sách ứng viên hard, không coi đó là kết quả đo rủi ro.

Các phương án đối chiếu BEV, camera trước/sau hoặc LiDAR/Radar trong bản chung chỉ áp dụng nếu thật sự có dữ liệu, calibration và đồng bộ thời gian tương ứng. Bộ ADASIND của bài này không cung cấp các bằng chứng đó. Track ID không tự chứng minh hai box cùng identity nếu thiếu timestamp/calibration/policy. Giữ tiêu chí review độc lập và phân xử của kế hoạch hiện tại.
