pip install --no-cache-dir -U openmim 
mim install mmengine 
mim install "mmcv==2.1.0" 
mim install "mmdet==3.2.0" 
mim install "mmpose==1.1.0" 



#打开这个文件musetalk/utils/blending.py
#把方法 get_image_blending改为下面这样就行

def get_image_blending(image,face,face_box,mask_array,crop_box):
    body = Image.fromarray(image[:,:,::-1])
    face = Image.fromarray(face[:,:,::-1])
    x, y, x1, y1 = face_box
    x_s, y_s, x_e, y_e = crop_box
    face_large = body.crop(crop_box)
    mask_image = Image.fromarray(mask_array)
    mask_image = mask_image.convert("L")
    face_large.paste(face, (x-x_s, y-y_s, x1-x_s, y1-y_s))
    body.paste(face_large, crop_box[:2], mask_image)
    body = np.array(body)
    return body[:,:,::-1]


pip install torch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0  xformers   --index-url https://download.pytorch.org/whl/cu121



source /root/base/cuda12.musetalk.sh

zze muse

export FFMPEG_PATH=/root/autodl-tmp/third_requires/ffmpeg-linux-x64

python -m scripts.realtime_inference --inference_config configs/inference/realtime.yaml


nohup python -m scripts.realtime_inference --inference_config configs/inference/realtime_5_huang.yaml  > train.log &