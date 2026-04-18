# AttentionX AI: Multimodal Creator Intelligence 

AttentionX is a high-performance AI pipeline designed for the **Creator Economy**. It transforms raw video content into actionable "Viral Signals" by combining automated speech recognition (ASR) with computer vision-based engagement tracking.


##  Core Features
- **Multimodal Analysis:** Orchestrates text (Whisper) and visual (MediaPipe) data streams simultaneously.
- **Active Speaker Tracking:** Real-time face detection to measure creator presence and engagement.
- **Automated Transcription:** High-speed, timestamped audio-to-text conversion using `faster-whisper`.
- **Media Engineering:** Automated audio extraction and frame-sampling pipelines.
- **Modern Architecture:** Decoupled FastAPI backend and React (Vite) frontend for production-grade scalability.

##  Technical Stack
| Layer | Technology |
| :--- | :--- |
| **Frontend** | React.js (Vite), Tailwind CSS, Lucide Icons |
| **Backend** | FastAPI (Python), Uvicorn |
| **AI Models** | Faster-Whisper (ASR), MediaPipe (Face Mesh/Detection) |
| **Media Engine** | OpenCV, MoviePy, FFmpeg |
| **Workflow** | Docker, Git, REST API |

##  Project Structure
```text
attentionx-ai-app/
├── backend/                # FastAPI + AI Processing Logic
│   ├── main.py             # API Entry point
│   ├── processor.py        # AI Orchestration (Whisper + MediaPipe)
│   └── requirements.txt    # Python dependencies
├── frontend/               # React + Tailwind UI
│   ├── src/                # UI Components & State Management
│   └── package.json        # Frontend dependencies
└── docker-compose.yml      # Root orchestration for one-click setup
