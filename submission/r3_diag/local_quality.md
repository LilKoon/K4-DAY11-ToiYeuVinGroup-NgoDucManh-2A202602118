# Đối chiếu chất lượng cục bộ — rectangle

Teaching reference, không phải gold set đã phê duyệt; không có điểm đạt tự động.
Nguồn: export r1_craft đã khóa SHA256 `9bb2e044e39cb8050e58ef1963b3ebe33fe83bc59a2dde25911c835c0c4d7094`; slice `B1-mid`.
Ghép hình học greedy một-một theo IoU ≥ 0.50, rồi so class; H ≥ 40 px.
Box trái nằm chủ yếu trong ignore_region reference không tính. Polygon, polyline, track không được chấm.
Đây là phép tính offline của lab, không phải báo cáo hay kết quả tương đương CVAT Premium.

Frame được tính: adasind_014670.jpg, adasind_032280.jpg, adasind_034080.jpg. Frame thiếu trong export: không.
TP=16; FP=5; FN=4; số lần đối chiếu=24; mean IoU của TP=0.868.

| Chỉ số | Micro | Macro | Nhãn thấp nhất |
|---|---:|---:|---:|
| accuracy | 0.667 | 0.937 | 0.875 |
| precision | 0.762 | 0.536 | 0.000 |
| recall | 0.800 | 0.558 | 0.000 |
| jaccard | 0.640 | 0.473 | 0.000 |
| dice | 0.780 | 0.546 | 0.000 |

| Nhãn | TP | FP | FN | Accuracy | Precision | Recall | Jaccard | Dice |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bike | 3 | 1 | 1 | 0.917 | 0.750 | 0.750 | 0.600 | 0.750 |
| Bus | 0 | 1 | 0 | 0.958 | 0.000 | 0.000 | 0.000 | 0.000 |
| Car | 4 | 1 | 1 | 0.917 | 0.800 | 0.800 | 0.667 | 0.800 |
| Pedestrian | 5 | 0 | 0 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| ThreeWheeler | 4 | 2 | 1 | 0.875 | 0.667 | 0.800 | 0.571 | 0.727 |
| Truck | 0 | 0 | 1 | 0.958 | 0.000 | 0.000 | 0.000 | 0.000 |

| Frame | TP | FP | FN | Accuracy | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| adasind_014670.jpg | 4 | 2 | 1 | 0.667 | 0.667 | 0.800 |
| adasind_032280.jpg | 6 | 1 | 0 | 0.857 | 0.857 | 1.000 |
| adasind_034080.jpg | 6 | 2 | 3 | 0.545 | 0.750 | 0.667 |

Confusion matrix: hàng = teaching reference; cột = export đã khóa.
`<missing>` là thiếu box; `<extra>` là box thừa. Xem `local_quality_confusion.csv`.

| Reference \ Export | Bike | Bus | Car | Pedestrian | ThreeWheeler | Truck | <missing> |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bike | 3 | 0 | 0 | 0 | 0 | 0 | 1 |
| Bus | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Car | 0 | 0 | 4 | 0 | 0 | 0 | 1 |
| Pedestrian | 0 | 0 | 0 | 5 | 0 | 0 | 0 |
| ThreeWheeler | 0 | 0 | 0 | 0 | 4 | 0 | 1 |
| Truck | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| <extra> | 1 | 0 | 1 | 0 | 2 | 0 | 0 |

Chi tiết xung đột trong `local_quality_conflicts.csv`; dữ liệu máy đọc trong `local_quality.json`.
Mismatching label đóng góp một FP cho class vẽ và một FN cho class reference; attribute khác được báo riêng.
Micro accuracy đếm mỗi cặp ghép sai class là một lần đối chiếu; Jaccard đếm cả FP và FN.
Macro/worst bỏ nhãn không xuất hiện ở cả hai phía; chỉ số không có mẫu là N/A.
