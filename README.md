# CROCODILE

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Crocodile) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Intended uses](#intended-uses)
- [Core path](#core-path)
- [Flat-stack repository](#flat-stack-repository)
- [Scientific hypothesis](#scientific-hypothesis)
- [Supported evaluation concepts](#supported-evaluation-concepts)
- [Primary endpoint](#primary-endpoint)
- [Causal discipline](#causal-discipline)
- [Installation](#installation)
- [Run](#run)
- [Tests](#tests)
- [Freeze discipline](#freeze-discipline)
- [Negative results](#negative-results)
- [Status](#status)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Dragon](https://github.com/enuminous/Dragon) · [Hedgehog](https://github.com/enuminous/Hedgehog) · [Turtle](https://github.com/enuminous/Turtle) · [Bat](https://github.com/enuminous/Bat)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


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
