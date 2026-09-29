# Exit ticket

Đọc `docs/10-svm360-reading-vi.md` trước khi trả lời câu 1–2. Các câu về zone, `why`, rework, parking và sampling
đã nằm trong file tương ứng nên không hỏi lại ở đây.

1. Một vật ở vùng seam giữa hai camera thật xuất hiện với hai box khác nhau: đó là lỗi `DUPLICATE` hay cần một quy
   tắc riêng? Vì sao? Với đầu ra per-camera, hai box có thể hợp lệ vì là hai quan sát của cùng vật. DUPLICATE trong một camera không tự áp dụng cho seam. Nếu đầu ra cần global ID, phải có policy hợp nhất và bằng chứng timestamp/calibration; chưa đủ dữ liệu thì giữ hai quan sát riêng.
2. Một vật đi qua nhiều frame trên cùng camera: khi nào giữ cùng track ID, khi nào thêm keyframe hoặc trạng thái
   Outside? Nêu bằng chứng sẽ cần trước khi nối track qua hai camera. Giữ ID khi xác nhận cùng vật qua chuỗi ảnh. Thêm keyframe khi nội suy không bám được thay đổi hình học/đường đi; dùng Outside khi vật ra khỏi trường nhìn theo policy task, không đồng nhất với bị che tạm thời. Nối track giữa camera cần đồng bộ thời gian, calibration có version, vùng chồng và bằng chứng chuyển tiếp identity cùng policy xử lý bất đồng.
3. Nhìn lại cả buổi: một chỗ bạn tin nhãn mình đúng nhưng reference hoặc người soát nghĩ khác (dẫn frame/`object_ref`),
   bạn đã xử lý thế nào, và nếu làm lại slice này bạn sẽ đổi gì trong cách làm? Ca adasind_014670.jpg L6 Bus bất đồng với R5 Truck; hình dáng xe vàng gợi ý Bus và M3 cũng gán Bus, nhưng model đồng ý không phải bằng chứng tuyệt đối. Đã giữ bản khóa và ghi E5_unresolved/action=escalate để QA phân xử theo R04, chưa nhận quyết định cuối. Nếu làm lại sẽ tự soát đủ checklist trước khóa và trước xem reference. Câu trả lời được soạn với trợ lý từ hiện vật hiện có; người nộp cần xác nhận phản ánh đúng trải nghiệm của mình.
