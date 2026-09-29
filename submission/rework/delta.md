# Rework delta

| zone | matched before | matched after | missing before | missing after | spurious before | spurious after |
|---|---:|---:|---:|---:|---:|---:|
| center | 7 | 8 | 3 | 2 | 1 | 1 |
| mid | 3 | 4 | 3 | 2 | 0 | 0 |
| edge | 2 | 2 | 0 | 0 | 0 | 0 |

## Findings action=rework
- adasind_152940.jpg ego_body IGNORE_SCOPE: không áp dụng
- adasind_167700.jpg ego_body IGNORE_SCOPE: không áp dụng
- adasind_212280.jpg ego_body IGNORE_SCOPE: không áp dụng

## Diễn giải

Tổng matched 12→14, missing 6→4, spurious 1→1. Bản v2 có 18 box và 9 polygon, khóa 1879-C103. “Không áp dụng” ở các dòng ego_body là giới hạn đánh giá của tool đối với object_ref này, không phải xác nhận đã sửa. Self-QC v2 vẫn báo thiếu ego_body ở ba ảnh, K12 có ba cặp, một box dưới H=40 và cảnh báo truncated/tên task. Checklist đã tick theo yêu cầu người học, không xóa các tồn tại trên.
