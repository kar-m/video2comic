# video2comic

Video2Comic is a web application developed by BruinAI that converts video files into comic-style visuals using AI by taking key frames from the video, translating audio into text and then using style transfer and character positioning to create comics.

### Demo:
Here's a demo we made while working on the project

[Watch the video](https://drive.google.com/file/d/1kBjLuAuurJ63JmXYwCftzyK9vX6E7OzE/view)

[See the result](https://drive.google.com/file/d/1CLGmZygs2hAdrcpGy48DW7d2F7gfKG_r/view)


# Getting Started

You'll need a valid OpenAI subscription - save your API key under the environment variable `OPENAI_API_KEY`:

```bash
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" # replace me!
```

### 🧬 1. Clone the Repo

```bash
git clone https://github.com/reflex-dev/reflex-chat.git
```

### 📦 2. Install Reflex

To get started with Reflex, you'll need:

- Python 3.7+
- Node.js 12.22.0+ \(No JavaScript knowledge required!\)
- Pip dependencies: `reflex`, `openai`

Install `pip` dependencies with the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 🚀 3. Run the application

Initialize and run the app:

```
reflex init
reflex run
```

### Additional
You may have to view the pdf's with Adobe Acrobat, there is a [vscode extension](https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf) for this.

You must insert your OpenAI, Gemini, and [Cartoon API](https://api.market/store/ailabtools/ai-cartoon-generator) keys in the upper left corner




