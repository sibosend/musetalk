ffmpeg -hide_banner -i /data/chazing_incubator/LiveTalking/data/background4-bj.jpg -i './huang720p.25fps.noaudio3.mov' -c:v prores -filter_complex '[1:v][0:v]scale2ref[v1][v0];[v1]chromakey=0x00FF00:0.2:0.1[1v];[v0][1v]overlay,format=yuv422p10le[v]' -map '[v]'  './huang720p.25fps.noaudio3_chromakey.mov'



ffmpeg -hide_banner -i '../bg0.jpg' -i './green.mov' -c:v prores -filter_complex '[1:v][0:v]scale2ref[v1][v0];[v1]chromakey=0x33b43f:0.08:0.06[1v];[v0][1v]overlay,format=yuv422p10le[v]' -map '[v]'  './1_chromakey.mov'


ffmpeg -hide_banner -i '../bg0.jpg' -i './00000000.png' -c:v prores -filter_complex '[1:v][0:v]scale2ref[v1][v0];[v1]chromakey=0x33b43f:0.08:0.06[1v];[v0][1v]overlay,format=yuv422p10le[v]'   './1_chromakey.png'



# 抠图去绿幕
ffmpeg -y -i ./green-0001.png -filter_complex "chromakey=#33b43f:0.08:0.06" output.png



ffmpeg -y -i ./snail.jpg -filter_complex "chromakey=#02fa03:0.2:0.1" output.png


ffmpeg -i bg0.720p.jpg -i green-0001.png -filter_complex "[1]chromakey=#33b43f:0.08:0.06[in2];[0][in2]overlay"  -y output.png
