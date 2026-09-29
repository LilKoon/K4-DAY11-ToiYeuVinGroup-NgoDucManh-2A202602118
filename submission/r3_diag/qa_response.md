# Phản hồi QA nhận được — B1-mid

Nguồn: [qa_review.md người gửi](../../qa_review.md). Bản đối chiếu: r1_craft/annotations.xml, mã 9BB2-E044. File QA không ghi người review hoặc mã khóa; các frame/object/thuộc tính phù hợp bản khóa đang có, nhưng chưa có bằng chứng xác nhận độc lập nguồn review. Các số 1–4 trong cột rule_id của file nhận là số thứ tự; dưới đây dẫn rule thực tế của repo, không sửa file người gửi.

| Ca QA | Quy tắc đối chiếu | Phản hồi và quyết định | Trạng thái |
|---|---|---|---|
| 014670 L6 Bus: truncated/occluded=true nhưng edge_zone=false | R05; docs/05-taxonomy-vi.md | Chạm mép ảnh không tự đồng nghĩa zone=edge. Hàm zone tính từ tâm box cho L6 là mid; vì vậy chưa có căn cứ đổi edge_zone thành true. Giữ truncated=true vì xe bị khung cắt và occluded=true vì bị xe phía trước che. Class Bus/Truck vẫn là bất đồng riêng cần QA phân xử, không được coi đã chốt chỉ từ nhận xét thuộc tính. | Giữ thuộc tính hiện tại có lý do; chưa sửa XML |
| 032280 L6 Car bị L7 che; box được mô tả bao toàn xe | R02/R05 | Giữ occluded=true. Box chữ nhật có thể chứa cả vùng bị người che khi ôm các cực trị nhìn thấy của cùng xe; điều này không tự chứng minh vẽ amodal. Cần kiểm bốn cạnh với phần xe nhìn thấy và chỉ co box nếu có cạnh kéo tới phần hoàn toàn suy đoán. Chưa có tọa độ thay thế đủ căn cứ nên giữ box hiện tại, mở khả năng sửa sau kiểm phóng to. | Giữ với giới hạn đã nêu |
| 034080 L1 Car chạm mép trái; truncated=true, edge_zone=false | R05; docs/05-taxonomy-vi.md | Tâm box thuộc mid, dù cạnh trái x=0. Giữ truncated=true và không ép edge_zone=true chỉ vì chạm khung. Quy tắc bin dùng tâm box khác quy tắc vật bị cắt. | Giữ thuộc tính hiện tại có lý do |
| 034080 L7 Pedestrian sát mép phải nhưng truncated=false | R05 | Box phải x=1079,23 trên ảnh rộng 1080 và công cụ báo khác dự kiến. Gần mép chưa đủ chứng minh cơ thể bị cắt. Cần QA phóng to tay/thân bên phải, xác định biên nhìn thấy trước khi đổi. Giữ E5_unresolved, chuyển QA phân xử; chưa tuyên bố đã sửa hoặc rework xong. | Chờ phân xử; action=escalate |

Lưu ý: docs/05 định nghĩa zone bằng tâm box và r/R; chưa thấy quy tắc riêng bắt buộc giá trị checkbox edge_zone trong docs/02. Kết quả mid là bằng chứng không nên đồng nhất hai khái niệm, không phải xác nhận chính sách checkbox đã đầy đủ.

Nhận xét được phản hồi với hỗ trợ trợ lý. Chưa có phản hồi tiếp từ người review. Bản XML đã khóa được giữ nguyên; việc ghi nhận quyết định không thay thế export và delta của P5.

Cập nhật sau đó: người nộp đã sửa trên CVAT và export v2 được khóa `7C11-C8C9`. Ca 034080 L7 của v1 hiện là L4 của v2, truncated/edge_zone đã bật true. Bus 014670 L6 của v1 hiện là L3 của v2, edge_zone cũng bật true dù tâm box vẫn thuộc mid. Chi tiết và giới hạn xác nhận nằm trong `submission/rework/delta.md`; bảng trên giữ lại quyết định tại thời điểm nhận QA, không mô tả v2 là chưa sửa.
