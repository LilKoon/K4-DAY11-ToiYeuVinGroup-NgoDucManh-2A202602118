# Sensor context

Quan sát ba ảnh B3-center (152940, 167700, 212280): ảnh fisheye dọc 1080×1920, có vành tối ở trên/dưới, đường thẳng cong rõ ở rìa. Camera quan sát đường từ một phương tiện; bộ phận xe, tay/người trên phương tiện xuất hiện ở phía trái và đáy ảnh. Vị trí gá, intrinsics/extrinsics và timestamp đồng bộ không được xác nhận từ dữ liệu này.

Vòng kính phủ phần lớn chiều cao và tràn qua hai cạnh ngang; vì vậy không thể dùng biên hình chữ nhật thay vòng kính. Hai polygon lens_border có sẵn phải được kiểm theo từng frame. Bản r1 chưa có polygon reason=ego_body ở cả ba ảnh; cần bổ sung sau khi xác định đúng phần xe gắn camera, không mặc định toàn bộ người bên trái là Pedestrian độc lập.

ADASIND ở đây là một camera; center/mid/edge là zone ảnh, không phải camera hay khoảng cách vật đến xe. Kế hoạch front/rear/left/right là tình huống giả lập riêng. Ảnh parking là camera thường và không chứng minh vùng di chuyển an toàn.

## Cập nhật sau nhận v2

Đã có export rework khóa 1879-C103 và delta: matched 12→14, missing 6→4, spurious 1→1. Các nhận xét “chưa có v2/delta” phía trên mô tả thời điểm trước cập nhật. V2 vẫn thiếu ego_body ba ảnh và K12 có ba cặp; các nghi vấn chưa phân xử không tự được đóng. QA thực tế đã xác nhận là duong→vanh/B1-mid; có bốn dòng findings QA và ba ảnh minh họa từ overlay. Xem REPORT.md để đọc trạng thái mới nhất.
