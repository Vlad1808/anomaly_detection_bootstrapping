# Anomaly Detection with Bootstrapping

*A regulatory‑grade framework for surfacing atypical behaviour in high‑volume data streams*

---

## 1  Overview

This repository contains a **self‑contained Jupyter Notebook** that demonstrates how bootstrapped statistical resampling can be combined with classic and machine‑learning‑based anomaly detectors to uncover hidden irregularities in large, messy datasets.

The workflow grew out of my production work in Tier‑1 banking, where early detection of suspicious transactions is critical for complying with U.S. regulations such as **SEC Rule 17a‑3**, **FINRA 2200/2400**, and the **Bank Secrecy Act (BSA)**.  By open‑sourcing the approach, the project enables smaller financial institutions, reg‑tech vendors, and research groups to adopt best‑in‑class monitoring without prohibitive R\&D cost—advancing the U.S. national interest in resilient capital markets and fraud‑free commerce.

## 2  Key Capabilities

| Capability                    | Description                                                                                              | Typical Domain                          |
| ----------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **Data‑quality audit**        | Flags measurement errors, rounding artefacts, and mis‑keyed values via bootstrapped confidence intervals | Any tabular dataset                     |
| **Noise/outlier detection**   | Isolation Forest & autoencoder score events that deviate from expected multivariate behaviour            | Credit‑card fraud, AML, insider trading |
| **Out‑of‑distribution check** | K‑NN distance test to detect records belonging to "foreign" populations                                  | Network intrusion, sensor malfunction   |
| **Explainable ranking**       | SHAP values & rule‑based tags to help analysts understand *why* an alert fired                           | Regulatory compliance reviews           |

## 3  Repository Layout

```
├── notebooks/
│   └── 01_regulatory_anomaly_detection.ipynb  # end‑to‑end tutorial
├── data/
│   └── synthetic_ach_sample.parquet           # no customer PII
├── environment.yml                            # conda spec
└── LICENSE
```

## 4  Quick Start

```bash
# clone
$ git clone https://github.com/<your‑fork>/anomaly‑bootstrapping.git
$ cd anomaly‑bootstrapping

# create environment
$ conda env create -f environment.yml
$ conda activate anomaly‑detect

# launch demo
$ jupyter lab notebooks/01_regulatory_anomaly_detection.ipynb
```

The notebook loads a 1 million‑row synthetic ACH feed, trains an Isolation Forest using bootstrapped thresholds, and visualises alerts with SHAP plots.  End‑to‑end runtime ≈ 7 minutes on a laptop CPU.

## 5  Why Bootstrapping?

Traditional detectors often assume clean training data and stable distributions—rare in live banking feeds.  By repeatedly resampling the data we:

1. Build **robust baselines** that tolerate minor noise.
2. Obtain **confidence intervals** for anomaly scores, reducing false positives.
3. Create a **data‑agnostic wrapper** that works across domains—from finance and cybersecurity to healthcare and seismology.

## 6  Use‑Case Highlights
* **Sensor network**: early detection of valve failures in an oil‑pipeline IoT rollout (industry PoC, 2025).

## 7  Contributing

Pull requests are welcome!  Please open an issue to discuss major changes first.

## 8  License

Released under the MIT License—see `LICENSE`.

## 9  Author

**Vladislav Lukonin**  |  Senior Data Scientist
