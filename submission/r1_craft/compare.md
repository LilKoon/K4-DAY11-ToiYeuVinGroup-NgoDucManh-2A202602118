# So sánh L với R

Chỉ số L/R là thứ tự box cao ≥ H=40 trong từng frame, theo thứ tự XML; bắt đầu từ 1.
Box L trong ignore_region được báo IGNORE_SCOPE, không tính SPURIOUS.

## adasind_014670.jpg
- L4 center SPURIOUS
- L6+R5 mid WRONG_CLASS
## adasind_032280.jpg
- L4 mid SPURIOUS
## adasind_034080.jpg
- L7+R3 edge ATTRIBUTE
- L3+R2 center BOX_GEOMETRY
- L8 center SPURIOUS
- R8 mid MISSING
- R9 center MISSING

## Theo zone
| zone | n_ref | matched | missing | spurious |
|---|---|---|---|---|
| center | 7 | 5 | 2 | 3 |
| mid | 11 | 9 | 2 | 2 |
| edge | 2 | 2 | 0 | 0 |
