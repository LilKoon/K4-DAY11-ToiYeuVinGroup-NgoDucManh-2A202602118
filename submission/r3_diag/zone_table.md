# Zone table (slice của bạn)

Lệnh `python3 lab11.py model` tự ghi bảng số (cùng cách đếm với `r1_craft/compare.md` và `model_compare.md`); chạy lại lệnh sẽ cập nhật bảng và giữ nguyên phần nhận xét. Bạn chỉ viết mục Nhận xét.

| Zone | n_ref | L missing | L spurious | M missing (`LR_noM` + `R_only`) | M thừa (`LM_noR` + `M_only`) | Lỗi L chính (`what`) |
|---|---:|---:|---:|---:|---:|---|
| center | 10 | 3 | 1 | 2 | 3 | MISSING (2) |
| mid | 6 | 3 | 0 | 2 | 3 | MISSING (3) |
| edge | 2 | 0 | 0 | 2 | 3 | — |

## Nhận xét

L thiếu 3 ở center và 3 ở mid; tỷ lệ thiếu theo n_ref là 3/10 và 3/6, nên mid cao hơn về tỷ lệ. L thừa 1 ở center. Model thiếu 2 và thừa 3 ở mỗi zone; ở edge thiếu cả 2/2 reference. Chỉ có 2 reference ở edge nên không suy kết luận tổng quát.

Giả thuyết cần kiểm: bỏ sót vật nhỏ ở nền và khác class làm giảm recall; sai lớp Truck/Car có bằng chứng trong local_quality_conflicts.csv. Méo rìa có thể ảnh hưởng model, nhưng chưa đủ chứng minh E4_model_domain. Cả ba frame thiếu ego_body trong self-QC là vấn đề scope phải giải quyết riêng. Zone không biểu thị khoảng cách hoặc rủi ro an toàn.

IoU sweep: L ở 0.3 và 0.5 đều matched=12, missing=6, spurious=1; tại 0.7 là 9/9/4. Model tại 0.5 là 11/7/10. Hai phép local_quality và matcher theo class có cách đếm khác khi sai lớp; không cộng chúng như các lỗi độc lập.
