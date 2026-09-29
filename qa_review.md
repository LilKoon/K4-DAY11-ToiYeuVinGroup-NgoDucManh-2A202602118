| frame | object_ref | rule_id | nhận xét |
|---|---|---|---|
| adasind_014670.jpg | L6 Bus | 1 | Bus bị cắt mạnh ở mép trái. XML đang để truncated=true, occluded=true nhưng edge_zone=false; nên kiểm tra lại rule edge_zone cho object sát vùng rìa fisheye. |
| adasind_032280.jpg | L6 Car | 2 | Car bị Pedestrian L7 che một phần và đã gán occluded=true; bbox vẫn bao toàn bộ xe. Đây là case phù hợp để kiểm tra rule occlusion. |
| adasind_034080.jpg | L1 Car | 3 | Car chạm đúng mép trái ảnh và truncated=true, nhưng edge_zone=false; cần đối chiếu rule edge_zone/truncated. |
| adasind_034080.jpg | L7 Pedestrian | 4 | Pedestrian nằm sát mép phải ảnh, bbox gần chạm biên nhưng truncated=false; cần kiểm tra xem người còn đầy đủ trong ảnh hay đã bị cắt. |