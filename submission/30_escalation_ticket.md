# Escalation ticket

## Ticket 1 — định vị ca thiếu ở 152940

- **Frame:** adasind_152940.jpg; ứng viên R5/R6, chưa xác nhận trùng đối tượng người QA mô tả.
- **Ảnh nguồn:** assets/images/adasind_152940.jpg; overlay: submission/r1_craft/compare.html. Chưa có screenshot cận cảnh của reviewer; cần bổ sung trước khi đóng ticket.
- **Expected impact:** thêm sai vật hoặc sai class có thể biến một nhận xét QA thành FP/WRONG_CLASS; không suy tác động an toàn từ zone.
- **Owner:** qa.
- **Recommendation:** người review đánh dấu vị trí hai vật, đối chiếu H≥40 và R04; annotator xác nhận box/class, sau đó mới rework. Dùng E5_unresolved trong lúc chưa đủ chứng cứ.
- **Trạng thái:** escalated, chờ định vị và ảnh minh chứng. Chưa gửi thông điệp ra ngoài repo.

## Ticket 2 — vòng QA nhóm (đã giải quyết)

- Cấu hình ban đầu giao duong→manh, nhưng người học đã xác nhận thực tế review vanh/B1-mid.
- Quyết định: chấp nhận B1-mid là phạm vi QA được người dùng chỉ định; không yêu cầu thêm B4-edge.
- Bằng chứng: r2_qa/qa_review.md, qa_overlay.html và ba ảnh minh họa trong screenshots/.
- Trạng thái: resolved; thay đổi vòng ghi trong decision log.
