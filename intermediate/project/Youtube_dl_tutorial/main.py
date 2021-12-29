import youtube_dl

# 여러 영상을 받을 수 있고 플레이리스트도 가능함. 동영상 링크, 플레이리스트 링크 사용
download_list = [
    'https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC',
    'https://www.youtube.com/playlist?list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81'
    ]

# 옵션은 아래 링크에서 확인
# https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312
# https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/options.py
ydl_opt = {
    # 파일 이름은 '제목 해상도.확장자명'
    'outtmpl': '%(title)s $(resolution)s.%(ext)s',
    # 비디오 형식 선택 : 'bestvideo/best'(최상품질), 'best[height>=1080]'(1080p 이상 해상도), 'best[filesize<=10M](파일 사이즈 10M 이하)
    'format': 'bestvideo/best'
}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(download_list)