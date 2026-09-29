# Exit ticket

Đọc `docs/10-svm360-reading-vi.md` trước khi trả lời câu 1–2. Các câu về zone, `why`, rework, parking và sampling
đã nằm trong file tương ứng nên không hỏi lại ở đây.

1. Một vật ở vùng seam giữa hai camera thật xuất hiện với hai box khác nhau: đó là lỗi `DUPLICATE` hay cần một quy
   tắc riêng? Vì sao? Cần một quy tắc riêng (Camera overlap/Seam logic) thay vì gán cứng lỗi `DUPLICATE`. Lý do là vật thể nằm ở vùng giao nhau sẽ xuất hiện trên cả 2 camera (đó là tính chất vật lý của hệ thống, không phải lỗi vẽ thừa). Cần có quy định rõ: gộp hai box thành một dựa trên thuật toán fusion, hoặc quy định camera nào làm chính.
2. Một vật đi qua nhiều frame trên cùng camera: khi nào giữ cùng track ID, khi nào thêm keyframe hoặc trạng thái
   Outside? Nêu bằng chứng sẽ cần trước khi nối track qua hai camera. Giữ cùng track ID khi vật thể liên tục xuất hiện. Thêm keyframe khi vật thay đổi hướng di chuyển, kích thước hoặc bị che khuất một phần. Đặt Outside khi vật hoàn toàn biến mất khỏi khung hình. Bằng chứng để nối track giữa hai camera: Cần thời gian trùng khớp (timestamp) và vị trí không gian liên tiếp (nằm trong vùng overlap của hai camera).
3. Nhìn lại cả buổi: một chỗ bạn tin nhãn mình đúng nhưng reference hoặc người soát nghĩ khác (dẫn frame/`object_ref`),
   bạn đã xử lý thế nào, và nếu làm lại slice này bạn sẽ đổi gì trong cách làm? Ở frame `adasind_236370.jpg` L3 (Bike), người soát lỗi cho rằng box chưa bao trọn phần thân trên của người lái xe. Tôi đã xử lý bằng cách chuyển action thành `rework` (nếu đúng là vẽ hụt) hoặc `keep_with_reason` (nếu tôi tin box đã sát viền). Rút kinh nghiệm lần sau sẽ quan sát kỹ hơn phần đầu và vai của rider để chắc chắn gộp chung vào box Bike.
