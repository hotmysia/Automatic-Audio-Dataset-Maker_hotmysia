import subprocess
import os

def main():
    download_cmd = "huggingface-cli download KimberleyJSN/melbandroformer --local-dir /home/eleven/jecca/Automatic-Audio-Dataset-Maker/tools/denoiser/Mel-Band-Roformer-Vocal-Model/models/mel_band_roformer"
    subprocess.run(download_cmd, shell=True, check=True)
    

    if not os.path.exists("DENOISED"):
        os.makedirs("DENOISED")

    inference_cmd = "python /home/eleven/jecca/Automatic-Audio-Dataset-Maker/tools/denoiser/Mel-Band-Roformer-Vocal-Model/inference.py --config_path /home/eleven/jecca/Automatic-Audio-Dataset-Maker/tools/denoiser/Mel-Band-Roformer-Vocal-Model/configs/config_vocals_mel_band_roformer.yaml --model_path /home/eleven/jecca/Automatic-Audio-Dataset-Maker/tools/denoiser/Mel-Band-Roformer-Vocal-Model/models/mel_band_roformer/MelBandRoformer.ckpt --input_folder /home/eleven/jecca/Automatic-Audio-Dataset-Maker/RAW_AUDIO --store_dir /home/eleven/jecca/Automatic-Audio-Dataset-Maker/DENOISED"
    subprocess.run(inference_cmd, shell=True, check=True)

if __name__ == "__main__":
    main()
