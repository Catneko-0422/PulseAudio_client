# PulseAudio_client

這是一個使用 Python 實現的音訊串流客戶端，透過 Socket 與伺服器進行連線，並使用 PyAudio 播放接收到的音訊資料。

## 使用方法

### Windows 用戶

1. **設定環境變數**：
   - 將 `sound.exe` 所在的資料夾路徑加入系統的環境變數 `PATH` 中，以便在終端機中直接執行 `sound` 指令。
   - 您可以參考以下步驟來設定環境變數：
     - 右鍵點擊「此電腦」或「我的電腦」，選擇「內容」。
     - 點擊「進階系統設定」，然後選擇「環境變數」。
     - 在「系統變數」區域，找到並選擇「Path」，然後點擊「編輯」。
     - 在編輯視窗中，點擊「新增」，然後輸入 `sound.exe` 所在的資料夾路徑。
     - 點擊「確定」以保存設定。
   - 更多關於如何設定環境變數的資訊，請參考 [Windows 11 環境變數及 Path 設定](https://zonego.tw/2022/01/07/windows11-path/)。

2. **執行程式**：
   - 打開命令提示字元（CMD）
   - 執行以下指令：
     ```
     sound [SERVER_IP] [SERVER_PORT] --RATE [取樣率] --CHUNK [區塊大小]
     ```
     其中，`[SERVER_IP]` 是伺服器的 IP 位址，`[SERVER_PORT]` 是伺服器的埠號，`[取樣率]` 和 `[區塊大小]` 是可選的參數，分別代表音訊的取樣率和每次讀取的音訊區塊大小，若未指定，將使用預設值 48000 和 1024。

### Linux/macOS 用戶

1. **執行程式**：
   - 打開終端機
   - 執行以下指令：
     ```
     sound [SERVER_IP] [SERVER_PORT] --RATE [取樣率] --CHUNK [區塊大小]
     ```
     其中，`[SERVER_IP]` 是伺服器的 IP 位址，`[SERVER_PORT]` 是伺服器的埠號，`[取樣率]` 和 `[區塊大小]` 是可選的參數，分別代表音訊的取樣率和每次讀取的音訊區塊大小，若未指定，將使用預設值 48000 和 1024。

## 注意事項

- 請確保您的系統已安裝 PyAudio，並且有適當的音訊輸出裝置。
- 若在 Windows 系統上使用，可能需要安裝適合的音訊驅動程式。
- 在執行程式前，請確保伺服器已啟動並正在運行。

## 相關連結

- [PyAudio 官方文件](https://people.csail.mit.edu/hubert/pyaudio/docs/)
- [PyInstaller 官方網站](https://www.pyinstaller.org/)
- [Windows 11 環境變數及 Path 設定](https://zonego.tw/2022/01/07/windows11-path/)
