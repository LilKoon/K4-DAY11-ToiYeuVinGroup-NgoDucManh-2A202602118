# Error analysis card

## Zone × block

| zone | block | what | count |
|---|---|---|---:|
| center | B3 | ATTRIBUTE | 1 |
| center | B3 | MISSING | 6 |
| center | B3 | SPURIOUS | 4 |
| center | B3 | WRONG_CLASS | 1 |
| edge | B3 | MISSING | 2 |
| edge | B3 | SPURIOUS | 3 |
| mid | B3 | ATTRIBUTE | 1 |
| mid | B3 | IGNORE_SCOPE | 2 |
| mid | B3 | MISSING | 7 |
| mid | B3 | SPURIOUS | 3 |
| unknown | B3 | IGNORE_SCOPE | 3 |

## Top defects
- MISSING: 15 (ví dụ frame adasind_152940.jpg)
- SPURIOUS: 10 (ví dụ frame adasind_152940.jpg)
- IGNORE_SCOPE: 5 (ví dụ frame adasind_167700.jpg)

## Phân tích của bạn

Hai bảng trên do `python3 lab11.py card` tính từ `findings.csv`; chạy lại lệnh sẽ cập nhật bảng và giữ nguyên mục này. Viết cho lỗi nổi bật nhất, dẫn frame/`object_ref`.

- MISSING là nhóm xung đột phổ biến nhất trong findings. Đây là số dòng qua nhiều vòng và nhiều phía L/R/M, không phải 15 vật bị người học bỏ sót. Local quality riêng bản L có FN=6; một FN do sai class, năm do chưa ghép được box. Không cộng các dòng lặp giữa r1_craft và r3_diag thành lỗi độc lập.
- 167700 L1+R4 có L=Truck, R=Car, IoU=0.854. WHAT là WRONG_CLASS theo phép so; WHY giữ E5_unresolved vì chưa có phân xử loại xe theo R04. Các ca M_only/LR_noM cần ai_team kiểm confidence, class, NMS và scope trước khi gọi là lỗi domain.
- XML thiếu ego_body ở cả ba frame, ảnh có bộ phận xe bên trái/đáy; annotator cần bổ sung vùng loại trừ theo R07 và xử lý L7/L8 IGNORE_SCOPE ở 167700 theo R09. Chỉ báo hoàn thành khi export v2 và delta có thật.
- Bằng chứng: r1_craft/annotations.xml, r1_craft/selfqc.md, r1_craft/compare.html, r3_diag/local_quality_conflicts.csv và r2_qa/received_review_B3-center.md. Chưa có screenshot cận cảnh theo finding; cần bổ sung trước khi nộp. Ticket 152940 yêu cầu reviewer định vị hai vật được nhắc tới.

## Cập nhật sau nhận v2

Đã có export rework khóa 1879-C103 và delta: matched 12→14, missing 6→4, spurious 1→1. Các nhận xét “chưa có v2/delta” phía trên mô tả thời điểm trước cập nhật. V2 vẫn thiếu ego_body ba ảnh và K12 có ba cặp; các nghi vấn chưa phân xử không tự được đóng. QA thực tế đã xác nhận là duong→vanh/B1-mid; có bốn dòng findings QA và ba ảnh minh họa từ overlay. Xem REPORT.md để đọc trạng thái mới nhất.
