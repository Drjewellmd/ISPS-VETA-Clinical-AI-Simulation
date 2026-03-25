# ISPS-VETA Clinical AI Simulation

**ISPS-VETA (Integrated Space Psychiatry System – Virtual Embodiment TeleAvatar)** is a simulation-based clinical AI decision-support prototype designed to support behavioral health triage in isolated, confined, and extreme (I.C.E.) environments.

This repository presents an early-stage **pilot simulation model** for a future clinically supervised support agent within the broader **MAGSBHO QUARTET architecture**.

---

## Purpose

The purpose of this project is to explore how a bounded, explainable, simulation-based AI system could support:

- early detection of behavioral or cognitive distress  
- triage of support needs  
- escalation to human clinicians in higher-risk situations  

This repository is intentionally structured as a **simulation pilot only**.

---

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

---

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

---

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

---

## Why This Matters

Future long-duration missions and remote austere environments may require systems that can:

- recognize worsening distress early  
- preserve human dignity and agency  
- remain bounded and interpretable  
- escalate uncertainty and risk to human experts  

The design philosophy follows a **Do No Harm** principle and aligns with governance-constrained, human-in-the-loop AI safety.

---

## Machine Learning Pilot

This repository includes a preliminary multi-class machine learning simulation that predicts triage actions from structured scenario data.

The model is evaluated not only for overall performance, but for **safety-relevant behavior**, especially the need to avoid missing high-risk cases.

This pilot demonstrates how structured behavioral and cognitive features can be translated into bounded decision-support outputs within a governance-constrained AI system.

### Model Evaluation Results

![ISPS-VETA ML Pilot Results](images/isps_veta_ml_results.jpeg)

**ISPS-VETA ML Pilot Results.** Preliminary comparison of machine learning models for simulated clinical triage decisions. Evaluation emphasizes safety-relevant behavior, particularly recall for escalation to a human clinician.

The system is explicitly designed to prioritize minimizing false negatives in high-risk escalation scenarios, reflecting safety-critical evaluation principles.

### Safety Principle

In this system, it is more acceptable to over-monitor than to fail to escalate a serious concern.

---

## Stage 2: Interpretable Clinical Triage Simulation (ISPS-VETA)

This Stage 2 extension builds upon the initial pilot model by introducing an expanded structured dataset (~60 simulated scenarios), additional temporal and frequency-based features, model comparison, and interpretable machine learning techniques.

### Features
- stress  
- mood  
- sleep quality  
- cognitive load  
- repeated distress  
- social withdrawal  
- stress trend  
- distress frequency  

### Output Classes
- ROUTINE_SUPPORT  
- MONITOR_CLOSELY  
- ACTIVATE_INTERVENTION  
- ESCALATE_TO_HUMAN_CLINICIAN  

### Performance

The model achieved ~90% accuracy with high recall in escalation scenarios, prioritizing minimization of false negatives in high-risk conditions.

### Model Comparison

We compared Decision Tree and Random Forest models.

The Random Forest model demonstrated improved recall for escalation scenarios, supporting safer deployment in safety-critical environments.

### Scenario Validation

Example outputs from simulation:

- High-risk scenario → ESCALATE_TO_HUMAN_CLINICIAN  
- Moderate-risk scenario → ACTIVATE_INTERVENTION  
- Low-risk scenario → ROUTINE_SUPPORT  
- Intermediate scenario → MONITOR_CLOSELY  

This demonstrates appropriate risk stratification and bounded decision-making.

### SHAP Interpretability

We integrated SHAP (Shapley Additive exPlanations) to identify which behavioral and cognitive features most influenced each triage decision.

This enables:
- Transparent model reasoning  
- Clinician review of escalation decisions  
- Alignment with human-in-the-loop governance  

### SHAP Outputs

![ISPS-VETA SHAP Summary](images/isps_veta_shap_summary.png)

**Figure.** Global feature importance showing which inputs most influence escalation decisions.

![ISPS-VETA SHAP Local Explanation](images/isps_veta_shap_local.png)

**Figure.** Scenario-level explanation showing feature contributions to escalation outcomes.

### Safety Framework

The ML system operates as a bounded decision-support layer and does not perform autonomous clinical decision-making.

The system incorporates:
- Human-in-the-loop escalation  
- Governance-constrained outputs  
- Explainable AI via SHAP  

Aligned with:
- **EarthStar “Do No Harm” Safety Protocol**  
- **MMAARSstar Non-Tokenized Data Training Protocol**  

### Limitations & Mitigation

Limitations:
- Trained on simulated data; real-world variability may differ  
- Edge cases with conflicting inputs require human judgment  
- Not designed for autonomous medical decision-making  

Mitigation:
- Human oversight required for escalation  
- Governance constraints enforce bounded outputs  
- SHAP interpretability supports review and transparency  

### Real-World Validation

Validated in MMAARS virtual analog astronaut cohorts (N≈45), with in-person mission validation scheduled for 2026.

---

## Current Status

- simulation-only prototype  
- no real patient data  
- no diagnostic claims  
- early machine learning pilot for triage logic  
- designed for future IRB-aligned testing  

---

## Future Work

Planned next steps include:

- expansion of simulated scenario sets  
- clinician-guided labeling of risk categories  
- temporal modeling of accumulating distress  
- integration with behavioral and physiological streams  
- formal validation under clinician and IRB oversight  
- future integration into the MAGSBHO QUARTET system  

---

## Repository Files

- `isps_veta_ml_pilot.py` — pilot multi-class triage model  
- `requirements.txt` — Python dependencies  
- `images/quartet_architecture.jpg` — optional architecture image  

---

## Run the Pilot

```bash
py isps_veta_ml_pilot.py
