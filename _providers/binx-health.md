---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-07'
  detail: binx health sells a physical point-of-care instrument through medical distributors and runs no developer program at all — /api, /developers, /docs and /integrations are honest 404s on mybinxhealth.com, no api.* or developer.* host resolves, and the only machine-readable endpoints on the host are its WordPress CMS REST API and an auth-gated WordPress MCP adapter plugin (401), neither of which is a product API.
  evidence:
  - status: 404
    url: https://mybinxhealth.com/developers
  - status: 404
    url: https://mybinxhealth.com/api-docs
  - status: 404
    url: https://mybinxhealth.com/openapi.json
  - status: 404
    url: https://mybinxhealth.com/.well-known/agent-card.json
  - status: 401
    url: https://mybinxhealth.com/wp-json/mcp/mcp-adapter-default-server
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: binx health, inc. is a Boston, Massachusetts point-of-care diagnostics company whose binx io platform is the first FDA-cleared, CLIA-waived molecular point-of-care test for chlamydia (Chlamydia trachomatis) and gonorrhea (Neisseria gonorrhoeae), returning central-lab-equivalent results in roughly thirty minutes from female vaginal swabs or male urine so a patient can be tested, diagnosed and treated in a single visit. The instrument pairs ultra-rapid PCR amplification with the company's proprietary electrochemical detection and needs no calibration, preventative maintenance or result interpretation, so it can be run by staff with no laboratory training. binx sells into urgent care, OB/GYN, pediatrics, student health, government health and other specialty settings through distributors including Cardinal Health, McKesson, Medline and Fisher Healthcare. The company divested its at-home consumer testing business to imaware in December 2023 and retained the point-of-care molecular
  diagnostics business. binx health publishes no public developer program, API reference or machine-readable specification.
image: https://mybinxhealth.com/wp-content/uploads/2025/04/cropped-binx_logo-1.webp
layout: provider
modified: '2026-08-07'
name: Binx Health
nav: Providers
network: true
random_paper: 91
slug: binx-health
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Molecular Diagnostics
- Point of Care Testing
- Medical Devices
- Sexual Health
- Laboratory
---
