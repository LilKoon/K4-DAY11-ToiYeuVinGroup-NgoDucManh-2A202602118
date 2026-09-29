# Exit ticket

1. Hai box của cùng vật ở seam thuộc hai ảnh camera có thể hợp lệ cho output per-camera. DUPLICATE phải xét đúng phạm vi output. Cần policy giữ từng camera hay hợp nhất sang BEV, cùng timestamp/calibration trước khi kết luận trùng và xóa box.

2. Giữ track ID khi có bằng chứng liên tục cùng identity trên một camera. Thêm keyframe khi vị trí/hình dạng thay đổi khiến nội suy không còn bám vật. Đánh dấu Outside khi vật rời trường nhìn theo guideline; che khuất không tự đồng nghĩa Outside. Nối qua hai camera cần đồng bộ thời gian, calibration, vùng overlap, chuyển động/ngoại hình phù hợp và policy identity. Ba ảnh lab không đủ để chứng minh track.

3. Ca bất đồng cần xử lý là 167700 L1+R4: nhãn người là Truck, reference là Car, IoU=0.854. Bằng chứng hiện có xác nhận khác class, chưa đủ để tuyên bố một bên chắc chắn đúng; cần đối chiếu loại xe và R04 trên ảnh phóng to. Không có ghi chép chứng minh mức độ tự tin ban đầu của người học nên không dựng lại trải nghiệm đó. Lần làm tiếp nên kiểm scope trước, rà vật nhỏ theo vùng, rồi dùng checklist class và yêu cầu QA định vị từng ca. Quyết định hiện tại là chuyển phân xử, chưa báo đã sửa.

## Cập nhật sau nhận v2

Đã có export rework khóa 1879-C103 và delta: matched 12→14, missing 6→4, spurious 1→1. Các nhận xét “chưa có v2/delta” phía trên mô tả thời điểm trước cập nhật. V2 vẫn thiếu ego_body ba ảnh và K12 có ba cặp; các nghi vấn chưa phân xử không tự được đóng. QA thực tế đã xác nhận là duong→vanh/B1-mid; có bốn dòng findings QA và ba ảnh minh họa từ overlay. Xem REPORT.md để đọc trạng thái mới nhất.
