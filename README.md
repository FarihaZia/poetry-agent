

---

# 📜 Poetry Analyzer — Gemini + OpenAI Agent SDK

This project leverages **OpenAI’s Agents SDK** and **Gemini API** to analyze poems.
A user inputs a short poem (2 stanzas), and the system automatically detects its type—**Lyric**, **Narrative**, or **Dramatic**—then hands it off to the appropriate agent for detailed analysis (*tashree*).

---

## ✨ Features

* 🧠 **AI-based classification** of poems
* ✍️ **Tashree** (analysis) based on poem type
* 🧾 **Simple user input** interface
* 🔄 **Agent-to-agent handoff** using OpenAI Agents SDK
* 🔷 **Gemini model integration** for poem generation

---

## ⚙️ How It Works

1. The user inputs a **2-stanza poem**.
2. The **Triage Agent** identifies the poem type:

   * **LyricAgent**
   * **NarrativeAgent**
   * **DramaticAgent**
3. Based on the type, the corresponding agent provides a **detailed explanation**.
4. Output is **displayed to the user**.

---

