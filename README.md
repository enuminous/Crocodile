# CROCODILE

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Crocodile) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

**Causal Recursive Observation of Coupling, Outcomes, Drift, Intervention, Latency and Effects**

CROCODILE is the EFMW animal for **causal intervention**.

Its narrow question is:

> If we perturb a component, what changes downstream, when does it change, and does the observed coupling survive a causal test?

CROCODILE is explicitly designed to distinguish correlation from intervention-sensitive effects.

## Intended uses

- controlled experiments
- A/B tests
- system perturbation studies
- industrial process experiments
- agent interventions
- causal reliability studies
- network intervention analysis
- policy simulation with measured interventions
- controlled maintenance experiments

## Core path

```text
system state
→ frozen intervention
→ treatment / control
→ observed response
→ lagged downstream response
→ drift adjustment
→ effect estimate
→ latency profile
→ heterogeneity
→ recursive downstream effects
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
crocodile.py
features.py
models.py
metrics.py
freeze.py
intervention_schema.json
example_config.yaml
example_data.csv
example_run.py
test_crocodile.py
MANIFEST.sha256
```

## Scientific hypothesis

> Some apparent system relationships are merely correlational; a valid causal mechanism should produce predictable downstream changes under controlled perturbation.

CROCODILE does not assume that every observed coupling is causal.

## Supported evaluation concepts

- treatment vs. control
- average treatment effect
- difference-in-differences style drift adjustment
- lagged treatment effects
- effect decay
- downstream propagation
- heterogeneous effects
- placebo intervention timing
- pre-trend checks

## Primary endpoint

Default:

`ATE = mean(outcome | treated) - mean(outcome | control)`

For drifting systems, CROCODILE also reports a simple pre/post difference-in-differences estimate.

For sequential systems, it reports a frozen lag profile.

## Causal discipline

A positive association is not enough.

Serious causal claims require design assumptions such as:

- randomized treatment
- valid natural experiment
- justified ignorability
- stable unit treatment assumptions
- no hidden post-treatment leakage
- clearly defined intervention timing

This package can calculate estimates; it cannot manufacture causal identification where the design does not support it.

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Freeze discipline

Before outcomes are inspected, freeze:

- intervention definition
- treatment assignment
- control group
- intervention time
- pre-period
- post-period
- outcome variables
- downstream variables
- lag set
- exclusion rules
- estimator
- placebo timing
- heterogeneity groups
- seeds

Then:

```bash
python freeze.py
```

## Negative results

If the intervention produces no reproducible downstream change, CROCODILE should report a null effect.

If placebo timing produces similar effects, the causal interpretation is weakened.

## Status

Research software. Experimental.
