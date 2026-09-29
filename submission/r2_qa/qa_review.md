# QA review · B4-edge (chính), B3-center (bổ sung)

Review với hỗ trợ của trợ lý, dựa trên sáu ảnh gốc, XML của người gửi và guideline R01–R09. Không sử dụng reference hoặc model của hai slice này. Reference B1-mid đã được mở trước đó; đây là review hai slice khác. Theo yêu cầu người nộp, báo cáo này không đánh giá vùng thân xe mang camera; không coi đây là xác nhận đạt toàn bộ guideline.

## Kiểm tra đầu vào

| Slice | File nhận | Mã khóa | Kiểm tra | Vai trò |
|---|---|---|---|---|
| B4-edge | B4-egde.zip + lock-edge.txt | 3BBB-2158 | SHA-256 XML khớp đầy đủ; đủ 3 frame | Review chính theo phân công người nộp xác nhận |
| B3-center | B3-center.zip + lock-center.txt | F7CC-04EB | SHA-256 XML khớp đầy đủ; đủ 3 frame | Review bổ sung |

Center có 15 box và 9 polygon; edge có 22 box và 9 polygon. Không thay đổi export hoặc lock người gửi. L1, L2… là chỉ số box trong từng ảnh do công cụ lab đánh số, không phải ID CVAT.

## B4-edge — review chính

[Overlay edge](qa_overlay_B4-edge.html). File [qa_overlay.html](qa_overlay.html) là overlay chính của B4-edge.

Nhận xét chính: cần sửa box Bike L3 ở ảnh 236370 để bao đủ người ngồi trên xe theo R03, sau đó soát thuộc tính occluded ở ba ca dưới đây theo R05. Các nhận xét là kết quả QA, chưa xác định nguyên nhân lỗi hoặc thay thế phản hồi của người gán nhãn.

| frame | object_ref | rule_id | nhận xét |
|---|---|---|---|
| adasind_236370.jpg | L3 | R03 | Box Bike (586;829)–(879;1025) bao xe nhưng bỏ đầu/thân trên người áo xám đang ngồi trên xe, đầu khoảng y=735. Mở box bao phần nhìn thấy của cả người và xe; không thêm Pedestrian riêng cho người ngồi xe. |
| adasind_236370.jpg | L4 | R05 | Truck phía sau bị người/xe máy phía trước che một phần, nhưng occluded=false. Đề nghị bật true; không mở rộng box để tưởng tượng phần khuất. |
| adasind_258420.jpg | L10 | R05 | Car phía xa tại (206;772)–(279;819) bị người/xe hai bánh phía trước che phần dưới nhưng occluded=false. Soát phóng to và bật true nếu xác nhận che khuất. Box cao khoảng 46,81 px nên cần giữ đúng ngưỡng H=40 khi sửa. |
| adasind_310008.jpg | L3 | R05 | Người ngoài cùng trái bị người L4 phía trước che một phần nhưng occluded=false. Đề nghị bật true sau khi đối chiếu phần cơ thể bị che. Hai người có vị trí đầu riêng nên không kết luận box trùng chỉ vì chúng giao nhau. |

Điểm phù hợp: 22 box đều cao ít nhất 40 px; mỗi frame có hai lens_border. Người dắt xe ở ảnh 236370 được tách Pedestrian/Bike là phù hợp R03; riêng người ngồi xe phải được gộp trong box như nhận xét L3. Cần người gửi soát tiếp độ sát hình học tại mức phóng to.

## B3-center — review bổ sung

[Overlay center](qa_overlay_B3-center.html).

| frame | object_ref | rule_id | nhận xét |
|---|---|---|---|
| adasind_152940.jpg | L1 | R05 | Bike đỗ cạnh hàng rào tại (576;855)–(677;927) nằm trong khung ảnh nhưng truncated=true. Không thấy bị biên ảnh/vòng kính cắt; đề nghị đổi false sau khi kiểm tra ảnh gốc. Nếu bị vật khác che thì đánh giá occluded riêng. |
| adasind_152940.jpg | L2 | R05 | Bike cùng người ngồi ở mép phải có cạnh box x=1080 và xe bị khung ảnh cắt nhưng truncated=false. Đề nghị bật true; tiếp tục giữ người ngồi cùng xe trong một Bike. |
| adasind_212280.jpg | L3 | R04 | Xe bên trái đang mang nhãn Bus. Cần người gửi xác nhận van chở người hay minibus từ hình dáng thân xe/cửa sổ: R04 phân biệt Car và Bus. Chưa đủ chắc để kết luận sai class chỉ từ ảnh này. |

Điểm phù hợp: mọi box hiện có cao ít nhất 40 px; người dắt xe trong ảnh 167700 được tách Pedestrian/Bike; mỗi frame có hai lens_border với reason hợp lệ. Polygon lớp đối tượng có thể phục vụ K12, không coi chúng là box trùng. Chưa xác nhận độ sát từng polygon K12 hoặc mọi vật nhỏ ở xa đã đủ nhãn.

## Bàn giao

- Bảy nhận xét trên được ghi vào findings.csv với round=r2_qa, cell=L_only, rule_id cụ thể và why để trống. Chưa chẩn đoán nguyên nhân ở P3.
- Ca phân loại xe chưa chắc ở center là yêu cầu xác nhận, không phải kết luận sai class.
- Người gửi phản hồi từng nhận xét ở P4, kể cả quyết định giữ nhãn. Chưa có phản hồi trong lần review này.
- Overlay chuẩn chỉ vẽ box, không hiển thị polygon; kiểm reason/số polygon dựa trên XML. Nhận xét này không thay thế kiểm tra mọi biên polygon.
