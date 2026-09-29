| frame | object_ref | rule_id | nhận xét |
|---|---|---|---|
| adasind_014670.jpg | L6 Bus | R05 | Bus bị cắt mạnh ở mép trái. XML đang để truncated=true, occluded=true nhưng edge_zone=false; nên kiểm tra lại rule edge_zone cho object sát vùng rìa fisheye. |
| adasind_032280.jpg | L6 Car | R02/R05 | Car bị Pedestrian L7 che một phần và đã gán occluded=true; bbox vẫn bao toàn bộ xe. Đây là case phù hợp để kiểm tra rule occlusion. |
| adasind_034080.jpg | L1 Car | R05 | Car chạm đúng mép trái ảnh và truncated=true, nhưng edge_zone=false; cần đối chiếu rule edge_zone/truncated. |
| adasind_034080.jpg | L7 Pedestrian | R05 | Pedestrian nằm sát mép phải ảnh, bbox gần chạm biên nhưng truncated=false; cần kiểm tra xem người còn đầy đủ trong ảnh hay đã bị cắt. |
## Phạm vi và bằng chứng

Theo xác nhận của người học, duong review bài vanh/B1-mid thay vòng mặc định. Đây là nhận xét cần soát theo ảnh, không mặc định mọi nghi vấn là lỗi. R05 quy định truncated/occluded, không tự suy edge_zone từ truncated. Ảnh minh họa dựng tĩnh từ overlay nằm trong submission/screenshots/qa_B1-mid_adasind_014670.png, qa_B1-mid_adasind_032280.png và qa_B1-mid_adasind_034080.png.
