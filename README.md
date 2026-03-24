# ISPS-VETA Clinical AI Simulation

**ISPS-VETA (Integrated Space Psychiatry System – Virtual Embodiment TeleAvatar)** is a simulation-based clinical AI decision-support prototype designed to support behavioral health triage in isolated, confined, and extreme (I.C.E.) environments.

This repository presents an early-stage **pilot simulation model** for a future clinically supervised support agent within the broader **MAGSBHO QUARTET architecture**.

## Purpose

The purpose of this project is to explore how a bounded, explainable, simulation-based AI system could support:

- early detection of behavioral or cognitive distress
- triage of support needs
- escalation to human clinicians in higher-risk situations

This repository is intentionally structured as a **simulation pilot only**.

## Important Safety Statement

ISPS-VETA is **not** a diagnostic tool, **not** a replacement for licensed clinicians, and **not** an autonomous clinical system.

All outputs are intended strictly as:

- decision-support signals
- simulation outputs for research exploration
- inputs for future clinician-supervised workflows

Any future real-world deployment would require:

- Institutional Review Board (IRB) approval
- clinician oversight
- formal validation
- medical ethics and safety review

## Relationship to MAGSBHO

ISPS-VETA is being developed as a separate pilot system and is intended to later integrate as the **fourth agent** within the **MAGSBHO QUARTET architecture**.

### MAGSBHO QUARTET Overview
- **KIRK** — Operational and Ethical Governance
- **EVE** — Non-clinical Wellness Support
- **SpaceGuardianGPT (SGG)** — Personal Reflective Support
- **ISPS-VETA** — Clinician-supervised Clinical Support

Together, the QUARTET forms a continuum of care:

**Wellness → Reflection → Ethical Alignment → Clinical Support**

All four agents operate under bounded roles, governance constraints, and human oversight; no single agent acts autonomously in high-risk conditions.

## Pilot Simulation Goal

The initial machine learning pilot tests whether structured behavioral and cognitive indicators can support safe triage decisions under simulated conditions.

### Input Features
- stress
- mood
- sleep quality
- cognitive load
- repeated distress signal
- social withdrawal

### Output Classes
- `ROUTINE_SUPPORT`
- `MONITOR_CLOSELY`
- `ACTIVATE_INTERVENTION`
- `ESCALATE_TO_HUMAN_CLINICIAN`

## Why This Matters

Future long-duration missions and remote austere environments may require systems that can:

- recognize worsening distress early
- preserve human dignity and agency
- remain bounded and interpretable
- escalate uncertainty and risk to human experts

The design philosophy follows a **Do No Harm** principle and aligns with governance-constrained, human-in-the-loop AI safety.

## Machine Learning Pilot
This repository includes a preliminary multi-class machine learning simulation that predicts triage actions from structured scenario data.
The model is evaluated not only for overall performance, but for **safety-relevant behavior**, especially the need to avoid missing high-risk cases.
This pilot demonstrates how structured behavioral and cognitive features can be translated into bounded decision-support outputs within a governance-constrained AI system.

### Model Evaluation Results
![ISPS-VETA ML Pilot Results](images/isps_veta_ml_results.jpeg)
The Decision Tree model demonstrated stronger recall for escalation scenarios, indicating improved sensitivity to high-risk conditions. This aligns with safety-critical design goals, where minimizing missed escalation cases (false negatives) is prioritized over strict accuracy.
The system is explicitly designed to prioritize minimizing false negatives in high-risk escalation scenarios, reflecting safety-critical evaluation principles.

**ISPS-VETA ML Pilot Results.** Preliminary comparison of machine learning models for simulated clinical triage decisions. Evaluation emphasizes safety-relevant behavior, particularly recall for escalation to a human clinician. This pilot demonstrates how structured behavioral features can be translated into bounded decision-support outputs within a governance-constrained AI system.

### Safety Principle
In this system, it is more acceptable to over-monitor than to fail to escalate a serious concern.

## Current Status

- simulation-only prototype
- no real patient data
- no diagnostic claims
- early machine learning pilot for triage logic
- designed for future IRB-aligned testing

## Future Work

Planned next steps include:

- expansion of simulated scenario sets
- clinician-guided labeling of risk categories
- temporal modeling of accumulating distress
- integration with behavioral and physiological streams
- formal validation under clinician and IRB oversight
- future integration into the MAGSBHO QUARTET system

## Repository Files

- `isps_veta_ml_pilot.py` — pilot multi-class triage model
- `requirements.txt` — Python dependencies
- `images/quartet_architecture.jpg` — optional architecture image

## Run the Pilot

```bash
py isps_veta_ml_pilot.py

```
## Stage 2: Interpretable Clinical Triage Simulation

We extended the ISPS-VETA simulation to a Stage 2 machine learning framework using an expanded scenario dataset, additional temporal and frequency-related features, and a comparison of Decision Tree and Random Forest models.

New features included:
- stress trend
- distress frequency

The Stage 2 system predicts four triage actions:
- ROUTINE_SUPPORT
- MONITOR_CLOSELY
- ACTIVATE_INTERVENTION
- ESCALATE_TO_HUMAN_CLINICIAN

Because ISPS-VETA is designed for safety-critical behavioral health support, evaluation prioritizes minimizing false negatives in escalation scenarios.

### SHAP Interpretability
Stage 2 also incorporates **SHAP (Shapley Additive exPlanations)** to identify which behavioral and cognitive features most influenced triage outcomes. This improves model transparency and supports clinician review of escalation decisions within a governance-constrained, human-in-the-loop framework.

## Stage 2 Results: Interpretable Clinical Triage

The ISPS-VETA Stage 2 model demonstrates structured behavioral health triage across four bounded outcomes:

- ROUTINE_SUPPORT  
- MONITOR_CLOSELY  
- ACTIVATE_INTERVENTION  
- ESCALATE_TO_HUMAN_CLINICIAN  

### Scenario Validation

Example outputs from simulation:

- High-risk scenario → ESCALATE_TO_HUMAN_CLINICIAN  
- Moderate-risk scenario → ACTIVATE_INTERVENTION  
- Low-risk scenario → ROUTINE_SUPPORT  
- Intermediate scenario → MONITOR_CLOSELY  

This demonstrates appropriate risk stratification and escalation behavior in safety-critical contexts.

### Safety Objective

The system prioritizes:
- Minimizing false negatives in escalation scenarios  
- Maintaining bounded and interpretable outputs  
- Supporting human clinician oversight  

### SHAP Interpretability

We integrated SHAP (Shapley Additive exPlanations) to identify which behavioral features most influenced each triage decision.

This enables:
- Transparent model reasoning  
- Clinician review of escalation decisions  
- Alignment with governance-constrained AI systems  

### Outputs Generated

- SHAP Summary Plot (global feature importance)  
- SHAP Local Explanation (scenario-level reasoning)  
- Model comparison (Decision Tree vs Random Forest)

Validated in MMAARS virtual analog astronaut cohorts (N≈45), with in-person mission validation scheduled for 2026.

## Project Lead
**Dr. Susan Jewell, MD**  
Physician-scientist, AI safety researcher, analog astronautics leader  
GitHub: https://github.com/Drjewellmd  

## Related Project
Relationship to MAGSBHO
This model extends the governance-constrained AI approach developed in MAGSBHO into the clinical behavioral health domain.
**MAGSBHO AI Safety Prototype**  
Governance-constrained multi-agent AI system for behavioral health and operations in high-risk environments.
