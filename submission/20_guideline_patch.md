# Guideline patch

- **Rule mới đề xuất:** R12 — Khi báo thiếu vật, ghi frame, tọa độ hoặc object_ref trên overlay, class dự kiến, chiều cao phần nhìn thấy trên ảnh gốc và kiểm tra ignore. Nhận xét “xe ở xa” chưa đủ để yêu cầu thêm box. Mỗi ca mơ hồ phải có crop và câu hỏi phân xử.
- **Áp dụng cho:** R01/R04, vật nhỏ ở nền, Bike/ThreeWheeler/Truck; áp dụng cho ghi chép QA và quyết định rework.
- **Vì sao luật hiện tại chưa đủ:** R01 có H=40 nhưng chưa chuẩn hóa bằng chứng tối thiểu trong lời nhận xét. QA 152940 ghi “xe máy và xe công nông”; local_quality liệt kê R5 Truck/R6 ThreeWheeler, nên chưa chắc đang nói cùng vật.
- **rules_version mới:** đề xuất v1.1.0; chưa được phê duyệt. Nhãn và findings hiện tại vẫn theo v1.0.0.
- **Hiệu lực từ:** vòng QA/rework tiếp theo sau khi người phụ trách guideline duyệt; không hồi tố sửa bản r1 đã khóa.
- **Kiểm chứng:** hai người độc lập định vị cùng vật từ nhận xét, đo H và kết luận phạm vi trước khi quyết định class; nếu bất đồng, chuyển ticket cho guideline owner.
