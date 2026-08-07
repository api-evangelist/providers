---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-07'
  detail: Bionaut Labs builds a magnetically steered micro-robot drug-delivery device regulated as a medical device, and its entire website now serves the same 790-byte logo placeholder for every path — /newsroom, /team/*, /.well-known/* and /openapi.json all return byte-identical HTML to a nonsense control path — so there is no developer surface, and no documentation surface at all, to read.
  evidence:
  - status: 200
    url: https://www.bionautlabs.com/
  - status: 200
    url: https://bionautlabs.com/.well-known/agent-card.json
  - status: 200
    url: https://bionautlabs.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/bionaut-labs/repos
  - status: 0
    url: https://api.bionautlabs.com/
  reason: not-a-software-company
  state: none
created: '2026-08-07'
description: 'Bionaut Labs is a clinical-stage medical robotics company headquartered in Los Angeles, California, developing "Bionauts" — remote-controlled, magnetically steered microscale robots roughly the size of a grain of rice that travel through tissue to deliver drugs, biologics and nucleic acids directly to targets deep in the brain and central nervous system. Founded in 2016 by CEO Michael Shpigelmacher, the company is pursuing treatments for malignant glioma, Dandy-Walker syndrome, Parkinson''s disease and Huntington''s disease, and has raised more than $80 million from investors including Khosla Ventures. Its product is a therapeutic device and navigation platform regulated as a medical device, not software sold to developers: Bionaut Labs operates no public API, developer portal, SDK or machine-readable contract of any kind.'
image: https://www.bionautlabs.com/images/bionaut-logo.svg
layout: provider
modified: '2026-08-07'
name: Bionaut Labs
nav: Providers
network: true
random_paper: 87
slug: bionaut-labs
tags:
- Company
- Medical Devices
- Robotics
- Healthcare
- Biotechnology
- Drug Delivery
- Neurology
- Micro-Robotics
- Life Sciences
---
