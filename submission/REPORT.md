# Báo cáo Day 11 — duong / B3-center

## Dữ liệu và nguồn

Ba ảnh 152940,167700,212280. Bản r1 khóa F7CC-04EB gồm 15 box/9 polygon; bản sau sửa r1-v2.zip khóa 1879-C103 gồm 18 box/9 polygon. Bản gốc được giữ nguyên. Parking đã có annotations.xml và observations.md. C0 nhập từ main b1c9864, khóa 424A-ABDF; đây là dữ liệu dùng chung có ghi nguồn, không phải bằng chứng người học độc lập thực hiện lại C0.

## Chất lượng bản r1

Local quality tại IoU≥0.5, H≥40: TP=12 FP=1 FN=6; micro precision=0.923, recall=0.667, accuracy=0.667, Jaccard=0.632, Dice=0.774; mean IoU TP=0.821. Truck có TP1 FP1 FN3, recall=0.25. 167700 L1 Truck/R4 Car có IoU=0.854; cần phân xử class theo R04. Đây là độ khớp teaching reference, không phải điểm rubric hoặc chứng nhận gold.

## QA

duong review vanh/B1-mid theo vòng thực tế đã xác nhận. Bốn nhận xét về Bus 014670 L6, Car/Pedestrian 032280 L6/L7, Car 034080 L1 và Pedestrian 034080 L7 được đưa vào findings với round=r2_qa, why trống và mã R02/R05 phù hợp. Các nhận xét là nghi vấn cần soát, không phải bốn lỗi đã được kết luận. Ba ảnh trong screenshots/ dựng tĩnh từ qa_overlay.html, có đánh dấu đối tượng; không phải ảnh chụp UI CVAT.

QA nhận về cho B3-center có mã F7CC-04EB khớp r1, nêu bỏ sót tại 152940 và 167700. Phản hồi ở r3_diag/qa_response.md. Người review chưa định vị cụ thể object_ref nên bất đồng class/đối tượng vẫn cần phân xử.

## Rework đã thực hiện

| Zone | Matched trước/sau | Missing trước/sau | Spurious trước/sau |
|---|---|---|---|
| center | 7 / 8 | 3 / 2 | 1 / 1 |
| mid | 3 / 4 | 3 / 2 | 0 / 0 |
| edge | 2 / 2 | 0 / 0 | 0 / 0 |
| Tổng | 12 / 14 | 6 / 4 | 1 / 1 |

Nguồn: rework/delta.md. Số liệu theo matcher của lab; không tự gọi bảng này là local_quality của v2. Bổ sung ba box làm tăng hai cặp khớp; không suy rằng mọi box thêm đều hợp lệ. Các dòng ego_body ghi “không áp dụng” vì tool không xử lý object_ref dạng này; không có nghĩa lỗi đã được sửa.

## Giới hạn và việc cần chú ý

- V2 vẫn thiếu ego_body cả ba frame; 152940 L4/L5 còn cảnh báo truncated, L6 có chiều cao <40; tên task thiếu raw_fisheye.
- K12 vẫn chỉ nhận ba cặp; cần kiểm Bike center 167700 và group_id trước khi khẳng định đủ bốn cặp.
- Chín checklist đã tick theo yêu cầu xác nhận của người học lúc gửi v2. Không hồi tố việc tự soát trước reference và không xóa cảnh báo chưa giải quyết.
- C0 dùng chung chỉ có hai polygon, chưa có box; compare ghi thiếu sáu đối tượng. Đủ file không chứng minh chất lượng C0 đạt yêu cầu.
- Ảnh minh họa được dựng từ overlay. Nếu lớp yêu cầu screenshot giao diện thật, cần bổ sung screenshot CVAT tương ứng.

## Kế hoạch bốn camera

45_sampling_plan.csv gồm tám ô: mỗi camera 20 normal +30 hard, tổng 200. Đây là phương án giả lập cân bằng độ phủ, không phải thống kê lỗi của bốn camera. Gold plan yêu cầu review độc lập, phân xử, phiên bản calibration/timestamp/policy seam và refresh; không mặc định teaching reference một camera là gold set.

## Bàn giao

Findings, decision log, guideline patch, escalation ticket, review plan, gold plan và exit ticket đã được điền. D07 xác nhận đổi vòng QA; D08 ghi bản rework; D09 ghi ý nghĩa dấu tick. Chạy python lab11.py check để xác nhận cấu trúc; các cảnh báo chất lượng trên vẫn cần được đọc riêng ngay cả khi check qua.
