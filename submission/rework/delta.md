# Rework delta

| zone | matched before | matched after | missing before | missing after | spurious before | spurious after |
|---|---:|---:|---:|---:|---:|---:|
| center | 5 | 5 | 2 | 2 | 3 | 3 |
| mid | 9 | 9 | 2 | 2 | 2 | 2 |
| edge | 2 | 2 | 0 | 0 | 0 | 0 |

## Findings action=rework

## Thay đổi thực tế và giới hạn

- Nguồn: export mới từ CVAT task 76, ZIP `exports/P2-B1-mid-v2-20260929-183753.zip`. V1 có mã `9BB2-E044`; v2 có mã `7C11-C8C9`. V1 được giữ nguyên.
- Đã ghép đối tượng theo class và tọa độ để so sánh vì thứ tự XML đổi. Cả 21 box giữ nguyên class/hình học; không coi đổi số L là sửa box.
- `adasind_014670.jpg`: v1 L6 Bus → v2 L3; edge_zone false → true. truncated và occluded vẫn true. Đây là thay đổi người nộp đã lưu trên CVAT, chưa xác nhận đúng policy checkbox: tâm box vẫn thuộc mid theo phép tính zone của repo. Không gọi thay đổi này là cải thiện chất lượng.
- `adasind_034080.jpg`: v1 L7 Pedestrian → v2 L4; truncated false → true và edge_zone false → true. Đây là ca nhận xét QA số 4, đã cập nhật theo bản người nộp sửa; vẫn cần người soát xác nhận phần cơ thể bị cắt trên ảnh. Tâm box thuộc edge.
- Tổng matched trước/sau: 16 → 16; missing: 4 → 4; spurious: 5 → 5. Bảng đo ghép box không phản ánh đầy đủ thay đổi thuộc tính nên số không đổi là phù hợp; không sửa số bằng tay.
- Các action=escalate trước đó chưa tự chuyển thành quyết định rework đã được QA phê duyệt. Chưa có sửa hình học P1 như Car v1 L3 ở ảnh 034080. V2 là bản thay đổi thuộc tính thực tế, chưa chứng minh hoàn tất mọi yêu cầu rework P0/P1 của rubric.
