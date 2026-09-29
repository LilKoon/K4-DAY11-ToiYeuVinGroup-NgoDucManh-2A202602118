# Quan sát vạch ô đỗ

- Hai vạch `parking_line` đã vẽ (mô tả vị trí trong ảnh): Các đường sơn trắng ở tiền cảnh (góc dưới cùng) làm nhiệm vụ phân chia ranh giới rõ ràng của các ô đỗ xe cạnh nhau.
- Một vạch/dấu sơn hoặc biên **không** vẽ, và vì sao: Mép viền của làn đường/lối đi chính giữa bãi (không vẽ vì đó không phải ranh giới phân định một ô đỗ cụ thể cho xe nào).
- Polygon `free_space` dừng ở đâu; có phần bị che nào không: Khoanh khu vực lối đi trống ở giữa bãi; dừng lại ở mép vỉa hè và sát mép các xe ô tô đang đỗ, không khoanh xuyên qua thân xe hoặc gốc cây bị che khuất.
- Ca chưa chắc cần hỏi người soát (nếu không có, ghi “không có”): Không có.
