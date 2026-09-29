# Guideline patch

- **Rule mới đề xuất:** Làm nổi bật lại quy tắc: Người đang trực tiếp điều khiển/ngồi trên xe hai bánh (rider) BẮT BUỘC phải được vẽ gộp chung vào cùng một box với chiếc xe đó. Ngoài ra cần bổ sung hình ảnh minh họa phân biệt rõ giữa "người đang ngồi lái xe" (gộp chung 1 box) và "người đi bộ đang dắt xe" (tách riêng 2 box).
- **Áp dụng cho:** Class `Bike` và `Pedestrian` (luật gộp box).
- **Vì sao luật hiện tại (`docs/02-rules-vi.md`) không đủ:** Luật `R03` hiện tại đã quy định gộp chung, nhưng phần chữ chưa đủ nhấn mạnh, khiến nhiều Annotator vẫn bị nhầm lẫn và gán nhãn người đang lái xe thành `Pedestrian` riêng biệt.
- **`rules_version` mới:** v1.1.0
- **Hiệu lực từ:** Vòng `rework` sắp tới.
