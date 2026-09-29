# Tự soát

Slice: `B1-mid`. Bản được kiểm: `annotations.xml`, mã khóa `9BB2-E044`, gồm 3 ảnh, 21 box và 6 polygon.

Ghi chú trình tự: checklist này được bổ sung với hỗ trợ của trợ lý sau khi bản P2 đã khóa và reference đã mở. Đây không phải bằng chứng tự soát độc lập trước khóa. Đối chiếu dưới đây dựa trên XML đã khóa, ảnh gốc và R01–R09; chưa sửa nhãn hoặc khóa lại.

Phạm vi: theo yêu cầu người nộp, bản ghi này không đánh giá vùng thân xe mang camera. Đây là nhận xét có chọn lọc, không xác nhận đạt toàn bộ guideline.

## Cảnh báo tự động trong phạm vi review

- adasind_014670.jpg L6: truncated khác dự kiến
- adasind_034080.jpg L7: truncated khác dự kiến

## Checklist thủ công
- [ ] Phạm vi H=40 và vật cần vẽ
- [ ] lens_border (phạm vi review đã điều chỉnh)
- [x] Class sáu nhãn
- [x] Rider và Bike
- [ ] Geometry trên ảnh fisheye gốc
- [ ] truncated và occluded
- [ ] Vật thiếu hoặc box trùng
- [x] ignore_region có reason
- [x] Tên task raw_fisheye và export CVAT 1.1

## Kết quả kiểm từng mục

Các ô chưa đánh dấu cần xử lý hoặc xác nhận thêm; không được hiểu là đã đạt toàn bộ guideline.

1. **Phạm vi H=40 — R01:** 21 box hiện có đều cao ít nhất 40 px. Box nhỏ nhất là `adasind_032280.jpg L4` (`Bike`), cao khoảng 42,67 px, sát ngưỡng nên cần soi kỹ phần vật thực sự nhìn thấy. Chưa xác nhận tuyệt đối không còn vật bị bỏ sót ở xa/rìa ảnh; giữ mục này mở cho lần soát cuối.
2. **lens_border — R08:** Mỗi ảnh có hai polygon lens_border. Cần tiếp tục soát sát biên cong trên ảnh; không coi đủ số lượng là đạt hình học.
3. **Class — R04:** Các box dùng đúng tên class của task. Xe lớn màu vàng sát trái `adasind_014670.jpg L6` đã là `Bus`; các xe ba bánh dùng `ThreeWheeler`. Van chở người ở `adasind_032280.jpg L6` được gán `Car`, phù hợp ánh xạ của bài. Các vật nhỏ phía xa vẫn cần xác nhận khi phóng to theo mục 1.
4. **Rider — R03:** `adasind_032280.jpg L5` bao người ngồi cùng xe máy trong một `Bike`. `adasind_034080.jpg L4` bao nhóm người cùng xe máy phía trái; bản khóa không còn box nhỏ chồng lên người lái từng được phát hiện trước đó. Không có box `Pedestrian` riêng cho những người ngồi trên các xe này.
5. **Geometry — R02:** Box được vẽ trên ảnh fisheye gốc; chưa thấy box nào bao cả dãy xe. Cần kiểm độ sát mép với mức phóng to, nhất là `adasind_014670.jpg L6` có cạnh trái x = 2,8 dù xe kéo tới mép ảnh, và `adasind_034080.jpg L7` có cạnh phải x = 1079,23 sát mép ảnh rộng 1080 px. Không nắn thẳng vật méo hoặc mở box để bao phần khuất tưởng tượng.
6. **truncated và occluded — R05:** Bus `adasind_014670.jpg L6` hiện có cả hai thuộc tính bằng `true`: ảnh cho thấy xe bị mép trái cắt và một phần bị xe phía trước che. Giữ quyết định này theo ảnh; cảnh báo tự động về truncated cần đối chiếu độ sát cạnh box, không tự đổi thành false chỉ để hết cảnh báo. `adasind_034080.jpg L7` đang truncated=false dù người sát mép phải: cần phóng to xác nhận phần cơ thể có bị khung cắt; bật true nếu có. Các Car bị người/xe phía trước che ở ảnh 2 và 3 đã có occluded=true. Không nhầm vùng làm mờ riêng tư với vật khác che khuất.
7. **Thiếu/trùng — R01/R03:** Bản khóa không còn cặp box Bike chồng lên cùng nhóm người/xe đã nêu ở mục 4. Công cụ không báo cặp cùng class IoU > 0,7; phép kiểm này không bảo đảm hết box trùng hoặc hết vật thiếu. Cần rà lại vật nhỏ/rìa trước khi xác nhận mục này.
8. **Reason — R06/R09:** Cả sáu polygon hiện có đều là ignore_region với đúng một reason=lens_border. Công cụ không báo box bị ignore theo ngưỡng của lab. Nếu chỉnh polygon cần kiểm tra lại để tránh che nhầm đối tượng cần gán.
9. **Task và export:** Metadata có tên `Day11 · ADASIND · B1-mid · raw_fisheye`; XML phiên bản 1.1 chứa đúng `adasind_014670.jpg`, `adasind_032280.jpg`, `adasind_034080.jpg`. Export đã được lấy từ CVAT theo định dạng CVAT for images 1.1 và mã khóa được xác minh.

## Việc cần làm trước khi xác nhận hoàn tất

- Soát hai ca truncated/geometry đã nêu, cùng các vật nhỏ sát ngưỡng H=40.
- Save và export bản mới sau khi sửa. Giữ bản khóa hiện tại để đối chứng; nếu khóa lại phải ghi lý do và dùng quy trình relock, hoặc đưa thay đổi sang vòng rework theo hướng dẫn bài.
- Chạy lại self-QC trên bản cần nộp và đối chiếu các mục còn mở. Lệnh selfqc có thể ghi đè phần nhận xét thủ công này, nên lưu lại nhận xét trước khi chạy lại.

