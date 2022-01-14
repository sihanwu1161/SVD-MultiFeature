import os, shutil
from pydub import AudioSegment

if __name__ == '__main__':
    data_dir = "jamendo"
    for item in os.listdir(data_dir + "/filelists"):
        if "." not in item:
            print(item)
            with open(data_dir + "/filelists/" + item, "r") as item_f:
                cnt = item_f.readlines()
                print(cnt)
                for item_cnt in cnt:
                    item_cnt = item_cnt[:-1]
                    print(item_cnt)
                    if not os.path.exists(data_dir + "/" + item):
                        os.makedirs(data_dir + "/" + item)
                    src = data_dir + "/audio/" + item_cnt
                    des = data_dir + "/" + item + "/" + item_cnt
                    des = des[:-3] + "wav"
                    print(des)
                    print(src)
                    # shutil.copy(src,des)
                    audio_format = src[-3:]
                    sound = AudioSegment.from_file(src, audio_format)
                    sound = sound.set_frame_rate(16000)
                    sound = sound.set_channels(1)
                    sound.export(out_f=des, format="wav")
