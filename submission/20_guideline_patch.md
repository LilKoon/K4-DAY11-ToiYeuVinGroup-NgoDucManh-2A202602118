# Guideline patch

- **Rule mới đề xuất:** Bổ sung ví dụ R04 phân biệt xe buýt/minibus, van chở người và xe tải khi chỉ thấy một phần thân ở mép ảnh. Ghi dấu hiệu cửa sổ, khoang khách/thùng hàng; không suy class chỉ từ màu xe. Nếu bằng chứng không đủ, chuyển QA phân xử thay vì mặc định reference đúng.
- **Áp dụng cho:** Bus/Truck/Car trong tập sáu class của lab; ví dụ adasind_014670.jpg L6 Bus so với R5 Truck và M3 Bus.
- **Vì sao luật hiện tại (`docs/02-rules-vi.md`) không đủ:** R04 có ánh xạ tên phương tiện nhưng chưa có ví dụ trực quan cho xe chỉ thấy một phần. Bất đồng hiện tại cho thấy cần bổ sung cách thu bằng chứng, chưa chứng minh quy tắc ánh xạ sai.
- **`rules_version` mới:** Đề xuất v1.1.0; chưa được phê duyệt, findings hiện vẫn dùng v1.0.0.
- **Hiệu lực từ:** Chỉ áp dụng ở vòng tiếp theo sau khi người phụ trách guideline phê duyệt và thông báo cho nhóm. Không tự sửa luật gốc hoặc hồi tố bản khóa.
