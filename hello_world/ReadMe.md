## 1. Tạo một dagster project tên hello_worlds

yêu cầu: dùng uv để tạo venv với python 3.10
bắt buộc: Dagster, Dagster-webserver

uv code để tạo template project:
```bash
uvx create-dagster@latest project project_name
```

Dùng:
```bash
uv add pandas numpy ....
```
để install các thư viện và lưu lại vào file uv.lock (thuận tiện để uv sync)

Lưu Ý: Dagster khi install bằng uv đôi khi sẽ bị thiếu vài module đi kèm cho nên sau khi tạo dagster project xong, hãy thử test xem nó dùng

```bash
dg dev
```
hay:
```bash
dagster dev
```
Nếu nó work với dagster dev thì có thể dùng chatgpt hỏi để cài bổ sung một số thư viện để run được bằng lệnh dg dev. Vì phiên bản run bằng dagster dev có cấu trúc khá khác biệt và đã cũ.

### 1.1 Tạo một pipeline gồm 2 asset: hello, worlds

cấu trúc:

	[hello] -> [worlds]

### 1.2: set lịch auto cho nó chạy vào lúc 6h sáng hàng ngày

### 1.3 dùng ntfy để thông báo tool chạy thành công/hoặc bị lỗi
- gửi thông báo tới: ntfy.sh/dagster_hello_worlds
- docs để tự tìm hiểu: https://docs.ntfy.sh/#__tabbed_1_6

