# Zone table (slice của bạn)

Lệnh `python3 lab11.py model` tự ghi bảng số (cùng cách đếm với `r1_craft/compare.md` và `model_compare.md`); chạy lại lệnh sẽ cập nhật bảng và giữ nguyên phần nhận xét. Bạn chỉ viết mục Nhận xét.

| Zone | n_ref | L missing | L spurious | M missing (`LR_noM` + `R_only`) | M thừa (`LM_noR` + `M_only`) | Lỗi L chính (`what`) |
|---|---:|---:|---:|---:|---:|---|
| center | 7 | 2 | 3 | 3 | 7 | SPURIOUS (2) |
| mid | 11 | 2 | 2 | 5 | 7 | WRONG_CLASS (1) |
| edge | 2 | 0 | 0 | 0 | 1 | ATTRIBUTE (1) |

## Nhận xét

- Với nhãn người L, center có tổng missing + spurious lớn nhất: 2 + 3 = 5, so với mid là 2 + 2 = 4 và edge là 0. Với model M, mid lớn nhất: 5 missing + 7 thừa = 12, center là 3 + 7 = 10, edge là 0 + 1 = 1. Đây là số xung đột với reference theo phép ghép của lab, không phải số lỗi đã được xác nhận bằng mắt. Một vật sai class có thể đóng góp cả missing lẫn thừa.
- Các ca cần phân xử cụ thể: ảnh 014670, L6/M3 gọi Bus nhưng R5 gọi Truck; ảnh 032280, M5/M9 gọi Car tại xe ba bánh L3/R6 và L1/R2; ảnh 034080, model tách người ngồi xe thành Pedestrian trong khi R03 yêu cầu một Bike bao người và xe. Các hiện tượng này gợi ý cần kiểm ánh xạ class và quy tắc rider trước khi kết luận ảnh fisheye gây lỗi model. Không đủ bằng chứng để gán E4_model_domain chỉ từ ba frame.
- Độ nhạy IoU: tăng 0,3 lên 0,7 làm matched L ở center giảm 6 xuống 4, matched M ở center giảm 4 xuống 1. Mid của L giữ 9; edge của L/M giữ 2. Vì vậy một phần khác biệt ở center liên quan hình học/ngưỡng ghép. Car L3 với R2 ở ảnh 034080 là ví dụ cần soi lại cạnh box thay vì đếm thành hai vật khác nhau.
- Local quality tại IoU 0,5: TP=16, FP=5, FN=4; precision micro=0,762, recall=0,800, accuracy=0,667; mean IoU trên các cặp TP=0,868. IoU trung bình này không bao gồm box không ghép được nên không chứng minh toàn bộ box đều sát vật. Xung đột Truck(reference) → Bus(export) tạo một FP Bus và một FN Truck; không tự chứng minh Bus là class sai.
- ThreeWheeler có TP=4, FP=2, FN=1 và precision=0,667, thấp hơn Bike/Car trong các class có TP. Bus/Truck có chỉ số thấp do bất đồng class trên số mẫu rất nhỏ. Cần đọc confusion CSV và ảnh cùng nhau, không lấy worst-class làm kết luận năng lực tổng quát.
- Giới hạn: chỉ ba frame từ một camera; center/mid/edge là vị trí bán kính trên ảnh, không phải khoảng cách tới xe hay cấp độ nguy hiểm. Edge chỉ có 2 box reference nên không kết luận edge dễ hơn. Không suy chất lượng bốn camera SVM hoặc gold set từ các số này. Phần vùng thân xe mang camera nằm ngoài phạm vi nhận xét theo yêu cầu người nộp.
- Findings r3_diag đã có nhận xét theo từng object, tọa độ, rule và phép kiểm tiếp theo. Những nguyên nhân chưa được người soát xác nhận giữ E5_unresolved và action=escalate; đây là đề xuất chuyển phân xử, chưa phải đã gửi ticket hay nhận phản hồi. Không sửa nhãn để ép khớp reference. Chưa nhận review B1-mid từ thành viên khác nên chưa thể điền câu trả lời thay họ.
