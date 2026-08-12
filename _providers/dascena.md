---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-11'
  detail: dascena.com still holds a live GoDaddy registration delegating to four Route 53 nameservers, but the hosted zone behind them is gone, so every public resolver returns SERVFAIL and no HTTP request to any Dascena host can complete; the laboratory business was acquired by CirrusDx in August 2022 and the successor host serves no developer surface either.
  evidence:
  - status: 0
    url: https://dascena.com/
  - status: 0
    url: https://dascena.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/dascena
  - status: 404
    url: https://cirrusdx.com/openapi.json
  - status: 200
    url: https://cirrusdx.com/
  reason: defunct
  state: none
created: '2026-08-11'
description: Dascena was an Oakland, California health-technology company that built machine-learning diagnostic and clinical decision support algorithms for hospitals, most notably InSight, a sepsis prediction model that scored electronic health record vitals and labs in real time to flag patients at risk hours before onset, plus FDA breakthrough-designated models for acute kidney injury and gastrointestinal bleeding. The algorithms were delivered as an embedded integration inside a customer hospital's EHR under a services and laboratory agreement rather than as a public developer API, so the company never operated a developer portal, published a machine-readable contract, or shipped client SDKs. CirrusDx acquired the Dascena Labs laboratory business effective 5 August 2022 and the company identity now trades as DBA CirrusDx; the dascena.com domain no longer resolves.
layout: provider
modified: '2026-08-11'
name: Dascena
nav: Providers
network: true
random_paper: 23
slug: dascena
tags:
- Company
- Health Care
- Artificial Intelligence
- Machine Learning
- Diagnostics
- Clinical Decision Support
- Sepsis
- Acquired
---
