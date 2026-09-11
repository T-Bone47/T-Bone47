<p align="center">
  <img src="https://github.com/T-Bone47/T-Bone47/blob/main/assets/asish-engineering-banner.svg?raw=true" alt="ASISH OLIVER M — Motorsport Software Engineer and AI/ML Engineer" width="100%" />
</p>

<h1 align="center">ASISH OLIVER M</h1>

<p align="center">
  <strong>Motorsport Software Engineer · AI/ML Engineer</strong><br/>
  Building software, simulation, telemetry and intelligent systems for engineering problems.
</p>

<p align="center">
  <a href="https://github.com/T-Bone47">GitHub</a> ·
  <a href="https://www.linkedin.com/in/asish-oliver-56b454324">LinkedIn</a> ·
  <a href="mailto:dreamteamoliver@gmail.com">Email</a>
</p>

---

## ENGINEERING PROFILE

I build systems at the intersection of **motorsport, software engineering, simulation, telemetry and AI/ML**.

My engineering approach is:

```text
DATA → MODELS → SYSTEMS → SIMULATION → INTELLIGENCE → ENGINEERING DECISIONS
```

The goal is not to use AI for its own sake. The goal is to build software that can ingest real data, model a problem, validate the result, expose uncertainty and turn the output into a useful engineering decision.

**Primary domains**

`Real-Time Systems` `Telemetry` `Race Strategy` `Numerical Simulation` `Vehicle Performance` `AI/ML` `Data Engineering` `Decision Support`

---

## SIGNATURE SYSTEMS

### 01 · LIVE F1 INTELLIGENCE
**Real-time Formula 1 data + deterministic race intelligence**

A production-grade F1 intelligence platform built around provider abstraction, canonical event modelling, provenance, recording/replay and deterministic analysis. The public repository documents real captured-data validation and backtesting.

| Verified result | Value |
|---|---:|
| Canonical events | **1,067,193** |
| Malformed records | **0** |
| Throughput | **~2,650 events/s** |
| p50 processing latency | **~0.10 ms/event** |
| Peak memory | **99 MB** |

**Core systems:** OpenF1 · F1 SignalR abstraction · FastF1 · Jolpica · replay pipeline · canonical schemas · provenance · validation/dedupe · timing/sector analysis · rolling pace · tyre-degradation estimation · battle FSM · strategy primitives.

→ **[Explore repository](https://github.com/T-Bone47/live-f1-intelligence)**

---

### 02 · F1 LAP-TIME SIMULATOR
**Numerical vehicle-performance engineering**

A quasi-steady-state point-mass lap-time simulation project covering track modelling, tyre grip, aerodynamic downforce/drag, power-limited traction and friction-circle constraints. A Python/NumPy reference implementation is used for numerical verification while the MATLAB implementation is brought toward V1 completion.

**Engineering focus:** lap-time solving · corner-speed modelling · grip limits · aero trade-offs · sector analysis · performance decomposition · solver convergence · analytical validation.

`MATLAB` `Python` `NumPy` `Vehicle Dynamics` `Lap Simulation`

---

### 03 · RACEMIND-AI
**AI-assisted race engineering for sim racing**

A game-agnostic race-engineering backend with real UDP telemetry ingestion, strategy reasoning, tyre/weather/fuel modelling, driver coaching and an LLM-driven AI Engineer for session questions. Codemasters F1 telemetry is implemented; additional simulators are planned.

**Core systems:** FastAPI · async SQLAlchemy · PostgreSQL · WebSockets · JWT · Pytest · telemetry abstraction · strategy engine · AI Engineer.

→ **[Explore repository](https://github.com/T-Bone47/RaceMind-AI)**

---

### 04 · F1 RACE MANAGER
**F1 Team Management & Strategy Simulation Game · IN DEVELOPMENT**

A Unity/C# management simulation centred on the engineering decisions around a race team: strategy, tyre and pit decisions, weather, Safety Car/VSC, reliability, traffic, driver/staff attributes, finance, facilities and car development.

→ **[Explore repository](https://github.com/T-Bone47/race-manager)**

---

### 05 · EA FC INTELLIGENCE
**Large-scale football intelligence and recommendation system · ACTIVE**

An AI/ML project focused on building a **16,228-player FC26 intelligence and recommendation engine** — combining structured player data, feature engineering, ranking/recommendation logic and decision-oriented analysis.

`Python` `Pandas` `NumPy` `Scikit-learn` `Recommendation Systems` `Data Engineering`

---

### 06 · VYAPARPULSE
**AI financial intelligence for micro-businesses · SMART INDIA HACKATHON**

A team-built financial intelligence and ledger platform for informal merchants. Voice-first transaction capture is converted into structured records, reconciled against the ledger, and combined with an XGBoost forecasting pipeline for dynamic 7-day revenue predictions and business insights.

**Architecture:** React/Vite · Capacitor · Vosk + LLM voice agent · FastAPI · SQLAlchemy · SQLite · XGBoost · Pandas.

→ **[Explore repository](https://github.com/T-Bone47/vyaparpulse-ai)**

---

## ENGINEERING EXPERIENCE

### Independent Motorsport / eSports
**Race & Strategy Engineer · Remote · 2025–Present**

Maintain and extend proprietary lap-simulation and race-strategy software. Analyse lap performance, race scenarios, tyre strategy and pit windows, then translate simulation outputs into actionable race decisions.

### IGNICT
**AI/ML Intern · Andhra Pradesh · Aug 2026–Present**

Python-based preprocessing, model development, evaluation and testing applied to live technical problems.

---

## AI / ML — AS AN ENGINEERING LAYER

AI/ML is used where it creates engineering value rather than as decoration.

| Problem | Approach |
|---|---|
| F1 race intelligence | Grounded analysis layer + deterministic validation |
| Race engineering | LLM-assisted session reasoning + telemetry context |
| Business forecasting | XGBoost + feature engineering + confidence handling |
| Football intelligence | Large-scale player features + recommendation/ranking |
| Engineering analysis | Regression, preprocessing, numerical analysis |

**Principle:** deterministic systems establish the ground truth; ML/LLMs operate on top of validated context.

---

## TECHNICAL ARSENAL

<details>
<summary><strong>Languages & Core Engineering</strong></summary>

`Python` `C++` `C#` `Java` `MATLAB` `SQL` `TypeScript` `JavaScript`

</details>

<details>
<summary><strong>AI / Machine Learning</strong></summary>

`XGBoost` `Scikit-learn` `Pandas` `NumPy` `Matplotlib` `Vosk` `Regression` `Feature Engineering` `LLM Integration`

</details>

<details>
<summary><strong>Backend & Data Systems</strong></summary>

`FastAPI` `SQLAlchemy` `WebSockets` `PostgreSQL` `TimescaleDB` `SQLite` `Docker` `Pytest` `Git/GitHub` `Data Validation` `Deterministic Replay`

</details>

<details>
<summary><strong>Motorsport Data & Telemetry</strong></summary>

`FastF1` `OpenF1` `Jolpica F1 API` `F1 SignalR` `UDP Telemetry` `MoTeC i2 Pro` `Session Replay` `Lap/Sector Analysis` `Tyre Degradation` `Pit-Window Analysis` `Race Strategy`

</details>

<details>
<summary><strong>Simulation & Interactive Systems</strong></summary>

`Unity` `C#` `Vehicle Dynamics` `Lap Simulation` `Race Simulation` `F1 Aerodynamics Fundamentals` `CFD Fundamentals`

</details>

---

## CURRENTLY BUILDING

```text
LIVE F1 INTELLIGENCE  →  deterministic analysis + AI layer hardening
F1 LAP-TIME SIMULATOR  →  numerical validation + V1 completion
F1 RACE MANAGER        →  Unity/C# strategy-management simulation
EA FC INTELLIGENCE     →  large-scale player intelligence + recommendations
IGNICT                 →  applied AI/ML engineering
```

---

## ENGINEERING PRINCIPLES

- **Measure before claiming.** Performance numbers come from measured implementations.
- **Ground truth before intelligence.** AI should consume validated context, not invent it.
- **Simulation must be explainable.** Every important model assumption should be inspectable.
- **Real systems over demos.** Prefer replayable pipelines, tests, validation and failure handling.
- **Engineering decisions are the output.** Software is the instrument; the decision is the objective.

---

## CONTACT

Open to conversations around **motorsport software engineering, telemetry, simulation, race strategy, vehicle-performance software and applied AI/ML**.

**Email:** [dreamteamoliver@gmail.com](mailto:dreamteamoliver@gmail.com)  
**LinkedIn:** [linkedin.com/in/asish-oliver-56b454324](https://www.linkedin.com/in/asish-oliver-56b454324)  
**Portfolio:** coming online with the full engineering case-study system.

<p align="center">
  <sub>Built around DATA → MODELS → SYSTEMS → SIMULATION → INTELLIGENCE → DECISIONS.</sub>
</p>
