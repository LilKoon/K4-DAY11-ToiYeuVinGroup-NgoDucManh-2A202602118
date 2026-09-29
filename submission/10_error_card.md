# Error analysis card

## Zone × block

| zone | block | what | count |
|---|---|---|---:|
| center | B1 | BOX_GEOMETRY | 1 |
| center | B1 | MISSING | 5 |
| center | B1 | SPURIOUS | 12 |
| center | B3 | ATTRIBUTE | 1 |
| center | B4 | ATTRIBUTE | 1 |
| center | C0 | MISSING | 3 |
| edge | B1 | ATTRIBUTE | 1 |
| edge | B1 | SPURIOUS | 1 |
| edge | B3 | WRONG_CLASS | 1 |
| edge | B4 | ATTRIBUTE | 1 |
| edge | C0 | MISSING | 1 |
| mid | B1 | MISSING | 6 |
| mid | B1 | SPURIOUS | 9 |
| mid | B1 | WRONG_CLASS | 1 |
| mid | B3 | ATTRIBUTE | 1 |
| mid | B4 | ATTRIBUTE | 1 |
| mid | B4 | BOX_GEOMETRY | 1 |
| mid | C0 | MISSING | 2 |

## Top defects
- SPURIOUS: 22 (ví dụ frame adasind_014670.jpg)
- MISSING: 17 (ví dụ frame adasind_019560.jpg)
- ATTRIBUTE: 6 (ví dụ frame adasind_034080.jpg)

## Phân tích của bạn

Hai bảng trên do `python3 lab11.py card` tính từ `findings.csv`; chạy lại lệnh sẽ cập nhật bảng và giữ nguyên mục này. Viết cho lỗi nổi bật nhất, dẫn frame/`object_ref`.

- Nguyên nhân khả dĩ (`why`) và vì sao bạn nghĩ vậy: SPURIOUS/MISSING đứng đầu bảng nhưng bao gồm xung đột ghép/class, không đồng nghĩa mọi dòng là vật thừa/thiếu thực sự. Ví dụ adasind_014670.jpg L6+M3 (Bus) và R5 (Truck) là cùng xe; adasind_034080.jpg L3 và R2+M3 là cùng Car nhưng khác box. Giữ E5_unresolved cho nguyên nhân chưa phân xử, không kết luận model domain shift từ vài box.
- Cách sửa và ai nhận việc (`owner`): QA xác nhận Bus/Truck theo R04, kiểm geometry Car theo R02; ai_team kiểm mapping xe ba bánh và cách gộp rider theo R03. Chỉ annotator sửa ca được xác nhận, giữ bản gốc để so delta. Các action=escalate là đề nghị phân xử, chưa có phản hồi bên nhận.
- Bằng chứng (ảnh trong `screenshots/`, dòng findings, rule): assets/images/adasind_014670.jpg và adasind_034080.jpg; submission/r3_diag/model_compare.html; local_quality_conflicts.csv; findings r3_diag L6+M3/R5 và L3/R2+M3; R02/R04. Hai ảnh screenshots/p4-compare.png và screenshots/p4-model.png được chụp từ báo cáo HTML, minh chứng bất đồng Bus/Truck ở frame 014670.
