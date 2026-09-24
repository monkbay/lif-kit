# Lif Kit

Five commands for people who build software by describing it. For the Lifrooms and Bellhop teams.

## Cài đặt · Install

In Claude Code, run these two lines:

```
/plugin marketplace add monkbay/lif-kit
/plugin install lif-kit@migaki
```

Then restart Claude Code. Type `/` and you should see the five commands.

Khi có bản mới · To get a newer version:

```
/plugin update lif-kit@migaki
```

Rồi khởi động lại Claude Code — bản mới chỉ có hiệu lực sau khi khởi động lại.
Then restart: an update only takes effect in a new session.

You do not need to install anything else. If `/track` already finds your tickets, your board connection is fine — leave it alone.

## Năm lệnh · The five commands

| Lệnh | Bạn nhận được gì | Outcome |
|---|---|---|
| `/preview` | Ảnh của thứ bạn muốn, **trước khi** ai đó xây. Chọn 1 trong 3 cách hiểu, rồi mới tạo ticket | See it before it is built. Also how you report a bug |
| `/needs-me` | Một danh sách duy nhất: mọi thứ đang chờ bạn quyết, mỗi dòng có hạn và có mặc định | One queue of everything waiting on you |
| `/proof` | Bằng chứng nó chạy: ảnh thật của màn hình, so với ảnh đã duyệt, và **xem ở đâu** | Evidence, and where to look |
| `/track` | Gõ **tên tính năng** hoặc mô tả, không cần nhớ mã ticket. Nó đang ở đâu, chờ gì | Trace one thing by name |
| `/brief` | 24 giờ qua: xong gì, kẹt gì, cần bạn việc gì | Catch up in 30 seconds |

**Cảnh báo kẹt** — việc nào 12 giờ không nhúc nhích sẽ được nêu ngay khi bạn gõ bất kỳ lệnh nào, kèm 1 người phụ trách và 1 việc cần làm. Không có tin nhắn nào tự gửi theo giờ; plugin chỉ chạy khi có người gõ.
Stalls surface the moment anyone runs a command — with one owner and one action. Nothing is sent on a schedule: a plugin only runs when someone types.

## Ví dụ · Examples

```
/preview sơ đồ phòng chật quá, đẩy thanh bên sang phải
```
(kéo ảnh chụp màn hình vào cùng lúc — nó đọc được ảnh)

```
/proof BELL-0921-0005
/track cái quỹ tiền mặt lễ tân
/needs-me
/brief
```

## Bốn điều nó sẽ không làm · Four things it will not do

1. **Hỏi bạn về tech.** Không hỏi đường dẫn file, không hỏi bảng dữ liệu. Nếu cần quyết, nó hỏi bằng câu hỏi nghiệp vụ với 2 lựa chọn và 1 đề xuất.
2. **Nói "xong" khi chưa có bằng chứng.** Không chụp được màn hình thì nó ghi "chưa chứng minh được", không bao giờ ghi "đã xong".
3. **Sửa hàng loạt ticket.** Mỗi lần một ticket, đúng thứ bạn yêu cầu, và nó báo lại đã đổi gì.
4. **Gửi tin thay bạn.** Cần báo ai thì nó soạn sẵn, bạn bấm gửi.

Nếu chưa kết nối được bảng ticket, nó nói thẳng — không bịa ticket, không bịa ngày.
If it cannot reach your board it says so. It does not invent a ticket, a status or a date.

## Ảnh và tệp · Images and files
Kéo ảnh chụp màn hình, ảnh mockup, PDF hay bảng tính vào Claude Code như bình thường — nó đọc được, và trang xem trước sẽ dùng đúng ảnh đó.

## Góp ý · Feedback
Trên mỗi trang có nút. Bấm, ghi chú, rồi bấm **Gửi** ở dưới cùng. Không cần gõ lại trong chat.
