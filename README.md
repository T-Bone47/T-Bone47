# Asish Oliver M

**Motorsport Software Engineering · Telemetry & Simulation · AI/ML**

Integrated M.Tech Computer Science student (VIT-AP University) working across software engineering, AI/ML and motorsport data. I've been building proprietary lap-simulation and race-strategy software as an independent Race & Strategy Engineer for eSports/sim-racing teams since 2025, and I'm currently an AI/ML Intern at IGNICT. All performance claims cite measured results from working implementations.

---

## About

Building toward a career in high-performance motorsport software engineering: real-time telemetry ingestion, numerical and data analysis, race-strategy modelling, performance analysis, vehicle-performance engineering, lap simulation, and the AI/ML layers that turn raw data into engineering decisions.

## Motorsport Engineering

**Independent Motorsport / eSports — Race & Strategy Engineer** · Remote · 2025–Present

Proprietary lap-simulation and race-strategy software for eSports/sim-racing teams, using performance data and simulation to evaluate lap performance, race scenarios, tyre strategy and pit-window decisions, and translate model outputs into actionable race strategy.

## Featured Projects

### [live-f1-intelligence](https://github.com/T-Bone47/live-f1-intelligence)
Real-time Formula 1 data and race-intelligence platform. Multi-provider ingestion (OpenF1, F1 SignalR, FastF1, Jolpica), canonical event modelling with provenance tracking, deterministic replay, and a deterministic analysis engine covering timing, sectors, rolling pace, tyre-degradation regression, a battle-detection state machine, race-control state, strategy candidates, qualifying intelligence and practice intelligence. Tested and backtested against real captured F1 data.

| Metric | Result |
|---|---:|
| Canonical events processed | 1,067,193 |
| Malformed records | 0 |
| Throughput | ~2,650 events/s |
| Processing latency | ~0.10 ms p50/event |
| Peak memory | 99 MB |

`Python` `FastAPI` `PostgreSQL / TimescaleDB` `WebSockets` `React` `TypeScript`

### [RaceMind-AI](https://github.com/T-Bone47/RaceMind-AI)
AI-assisted race-engineering software for **sim racing** — a game-agnostic telemetry abstraction (Codemasters F1 titles implemented; Assetto Corsa/ACC/iRacing/rFactor2 planned), a real UDP telemetry listener, a rule-based strategy engine (pit windows, undercut/overcut, tyre & weather modelling), telemetry-driven driver coaching, and an LLM-driven AI Engineer for session Q&A. Backend implemented and tested against SQLite and real Postgres. Frontend and desktop application not yet built. Per-game packet decoding beyond Codemasters F1 titles remains stubbed.

`FastAPI` `SQLAlchemy 2.0 (async)` `PostgreSQL` `Alembic` `WebSockets` `JWT`

### VyaparPulse
Team project (Smart India Hackathon) — an AI-powered financial intelligence platform for micro-businesses, combining voice-driven transaction entry (Vosk speech-to-text) with XGBoost-based revenue forecasting.

## AI/ML Engineering

AI/ML is applied as an engineering layer across telemetry, race intelligence, forecasting and decision support: a grounded, validated LLM analysis layer in live-f1-intelligence (Gemini-based, with a grounding validator and dedicated test coverage), an Anthropic-API-driven AI Engineer in RaceMind-AI, an XGBoost forecasting pipeline in VyaparPulse, and an F1 lap-time regression model — preprocessing, feature engineering and evaluation with Pandas, NumPy, Matplotlib and Scikit-learn.

## Technical Stack

**Languages** — Python · C++ · C# · Java · MATLAB · SQL · TypeScript · JavaScript

**AI / Machine Learning** — XGBoost · Vosk (speech-to-text) · Pandas · NumPy · Matplotlib · Scikit-learn · LLM integration (Gemini, Anthropic) · Regression · Feature Engineering

**Backend & Software Engineering** — FastAPI · SQLAlchemy · WebSockets · Docker · Git/GitHub · Pytest · Data Validation · Deterministic Replay / Backtesting

**Data & Infrastructure** — PostgreSQL · TimescaleDB

**Motorsport Data & Telemetry** — FastF1 · OpenF1 · Jolpica F1 API · F1 SignalR · UDP Telemetry · MoTeC i2 Pro · Session Replay

**Motorsport Simulation & Vehicle Performance** — OptimumLap · OpenLAP / OpenLapSim · ChassisSim · Canopy Simulations · AVL VSM · Vehicle Dynamics Fundamentals · F1 Aerodynamics Fundamentals · CFD Fundamentals

**Interactive & Simulation Systems** — Unity · C# *(F1 Race Manager, in development)*

**Engineering Methods** — Lap/Sector Analysis · Pace Comparison · Tyre Degradation · Pit-Window Analysis · Undercut/Overcut · Fuel Modelling · Race Strategy · Race Simulation

## Currently Building

Extending live-f1-intelligence's analysis engine and hardening its AI layer; developing F1 Race Manager, an in-development Unity/C# race-management simulation covering strategy, reliability, finance and car development; continuing an AI/ML internship at IGNICT (since August 2026).

## GitHub Metrics

<div align="center">
  <a href="https://github.com/T-Bone47">
    <img src="https://github-readme-stats.vercel.app/api?username=T-Bone47&show_icons=true&hide_title=true&theme=transparent&hide_border=true" alt="Oliver's GitHub Stats" />
  </a>
</div>

## Contact

[dreamteamoliver@gmail.com](mailto:dreamteamoliver@gmail.com) · [LinkedIn](https://www.linkedin.com/in/asish-oliver-56b454324) · Trichy, Tamil Nadu, India
