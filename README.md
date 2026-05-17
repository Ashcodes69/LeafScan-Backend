# 🌿 LeafScan — AI Plant Disease Detection

> Upload a leaf photo. Get an instant diagnosis.

**Live Demo → [leaf-scan-frontend.vercel.app](https://leaf-scan-frontend.vercel.app/)**

---

## What is LeafScan?

LeafScan is an AI-powered plant disease detection web app. Upload a photo of any plant leaf and the model will instantly identify the crop and diagnose any disease with 99%+ accuracy — completely free, no sign-up required.

---

## Features

- 🔍 Detects diseases across **9 crops** and **29 conditions**
- ⚡ Instant predictions with confidence scores
- 🌱 Identifies whether a plant is **healthy or diseased**
- 📱 Works on desktop and mobile
- 🆓 100% free to use

---

## Supported Crops

| Crop | Conditions Supported |
|------|----------------------|
| Apple | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| Bell Pepper | Bacterial Spot, Healthy |
| Cherry | Powdery Mildew, Healthy |
| Corn (Maize) | Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy |
| Grape | Black Rot, Esca (Black Measles), Leaf Blight, Healthy |
| Peach | Bacterial Spot, Healthy |
| Potato | Early Blight, Late Blight, Healthy |
| Strawberry | Leaf Scorch, Healthy |
| Tomato | Bacterial Spot, Early Blight, Late Blight, Septoria Leaf Spot, Yellow Leaf Curl Virus, Healthy |

---

## Tech Stack

### Machine Learning
- **PyTorch** — model training
- **Custom CNN** — built from scratch (no transfer learning)
- **ONNX** — model export format for fast inference
- **Dataset** — Plant Village Dataset (67,000+ images)
- **Training** — Google Colab (T4 GPU)

### Model Architecture
```
Input (224×224 RGB)
    ↓
Conv Block 1: Conv2d → BatchNorm → ReLU → MaxPool  (32 filters)
    ↓
Conv Block 2: Conv2d → BatchNorm → ReLU → MaxPool  (64 filters)
    ↓
Conv Block 3: Conv2d → BatchNorm → ReLU → MaxPool  (128 filters)
    ↓
Conv Block 4: Conv2d → BatchNorm → ReLU → MaxPool  (256 filters)
    ↓
Global Average Pooling
    ↓
Fully Connected (512) → Dropout(0.5) → Output (29 classes)
```

### Training Results
| Metric | Value |
|--------|-------|
| Train Accuracy | 98.38% |
| Val Accuracy | 99.27% |
| Test Accuracy | 99.19% |
| Training Time | ~105 mins |
| Epochs | 20 |

### Backend
- **FastAPI** — REST API
- **ONNX Runtime** — model inference
- **Docker** — containerization
- **Hugging Face Spaces** — free hosting

### Frontend
- **Next.js 16** — React framework
- **TypeScript** — type safety
- **Tailwind CSS** — styling
- **Vercel** — free deployment

---

## Architecture

```
User (Browser)
      ↓
Vercel (Next.js Frontend)
      ↓
Next.js API Route (proxy)
      ↓
Hugging Face Spaces (FastAPI + ONNX Model)
      ↓
Prediction Result
```

---

## Project Structure

```
LeafScan-frontend/          # Next.js app (deployed on Vercel)
├── app/
│   ├── page.tsx            # Home page (upload + result)
│   ├── supported/
│   │   └── page.tsx        # Supported plants page
│   └── api/
│       └── predict/
│           └── route.ts    # API proxy to HF Space
├── components/
│   ├── ImageUploader.tsx   # Drag & drop uploader
│   └── ResultCard.tsx      # Prediction result card
└── models/
    └── classes.json        # 29 class labels

LeafScan-backend/           # FastAPI app (deployed on HF Spaces)
├── app.py                  # FastAPI endpoints
├── classes.json            # Class labels
├── Dockerfile              # Container config
├── requirements.txt        # Python dependencies
├── plant_disease_model.onnx
└── plant_disease_model.onnx.data
```

---

## Local Development

### Frontend
```bash
git clone https://github.com/Ashcodes69/LeafScan-frontend
cd LeafScan-frontend
npm install
npm run dev
```

### Backend
```bash
git clone https://github.com/Ashcodes69/LeafScan-backend
cd LeafScan-backend
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## Limitations

- Works best with clear, well-lit leaf photos
- Potato and Tomato leaves can be confused (they look nearly identical)
- Currently supports 9 crops only — more coming soon

---

## Future Improvements

- [ ] Add more crops and diseases
- [ ] Train with real-world diverse images
- [ ] Add a crop identifier before disease detection
- [ ] Mobile app version
- [ ] Multilingual support (Hindi, etc.)

---

## License

MIT License — free to use, modify, and distribute.

---

<p align="center">Built with 🌿 by <a href="https://github.com/Ashcodes69">AshCodes</a></p>
