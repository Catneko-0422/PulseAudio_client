import socket
import pyaudio
import argparse

def main():
    # 設定命令列參數
    parser = argparse.ArgumentParser(description='音訊串流客戶端')
    parser.add_argument('SERVER_IP', type=str, help='伺服器的 IP 位址')
    parser.add_argument('SERVER_PORT', type=int, help='伺服器的埠號')
    parser.add_argument('--RATE', type=int, default=48000, help='音訊取樣率，預設為 48000')
    parser.add_argument('--CHUNK', type=int, default=1024, help='每次讀取的音訊區塊大小，預設為 1024')
    args = parser.parse_args()

    # 取得命令列參數
    SERVER_IP = args.SERVER_IP
    SERVER_PORT = args.SERVER_PORT
    RATE = args.RATE
    CHUNK = args.CHUNK

    # 設定音訊格式
    FORMAT = pyaudio.paInt16
    CHANNELS = 2

    # 初始化 PyAudio
    p = pyaudio.PyAudio()

    # 開啟音訊串流
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)

    # 建立 Socket 連線
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        print(f"已連線至 {SERVER_IP}:{SERVER_PORT}，開始接收音訊資料")

        try:
            while True:
                data = s.recv(CHUNK)
                if not data:
                    break
                stream.write(data)
        except KeyboardInterrupt:
            print("已中斷播放")
        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()
            print("音訊播放已停止")

if __name__ == '__main__':
    main()

