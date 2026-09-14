---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://orphai-therapeutics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AI-Therapeutics
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ai-therapeutics-domain-security.yml
coverage:
  checked: '2026-09-13'
  detail: AI Therapeutics is a clinical-stage biopharmaceutical company (now Orphai Therapeutics, a Quince Therapeutics subsidiary) whose product is an inhaled rapamycin drug candidate, not software — its only live host, orphai-therapeutics.com, is a one-page WordPress corporate site that 404s every /.well-known/, OpenAPI and llms.txt path, and its GitHub organization has zero public repositories.
  evidence:
  - status: 404
    url: https://orphai-therapeutics.com/.well-known/agent-card.json
  - status: 404
    url: https://orphai-therapeutics.com/openapi.json
  - status: 404
    url: https://orphai-therapeutics.com/llms.txt
  - status: 200
    url: https://api.github.com/users/AI-Therapeutics/repos
  reason: not-a-software-company
  state: none
created: '2026-09-13'
description: 'AI Therapeutics (now Orphai Therapeutics) is a clinical-stage biopharmaceutical company founded in Guilford, Connecticut by Jonathan Rothberg as LAM Therapeutics, renamed AI Therapeutics, and renamed again to OrphAI Therapeutics in September 2023. It built an internal deep-learning platform that synthesized public and proprietary drug and disease data to match existing chemical entities to new indications, and used it to advance a rare-disease and pulmonary pipeline — LAM-001, an inhaled formulation of sirolimus (rapamycin) targeting mTOR-driven pulmonary disease, plus the earlier PIKfyve inhibitor programs LAM-002 and LAM-003. Quince Therapeutics (Nasdaq: QNCX) acquired Orphai in May 2026 and now runs it as a subsidiary. The AI platform is an internal drug-discovery tool, not a product: the company operates no developer program, publishes no API, SDK or machine-readable contract, and its public web presence is a single-page corporate site.'
image: https://orphai-therapeutics.com/wp-content/uploads/2026/07/orphai-logo-new.png
layout: provider
modified: '2026-09-13'
name: AI Therapeutics
nav: Providers
network: true
overview: AI Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Drug Discovery.
random_paper: 11
security:
- kind: domain-security
  name: Ai Therapeutics Domain Security
  slug: ai-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ai-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Drug Discovery
- Artificial Intelligence
- Clinical Trials
- Rare Disease
website: https://orphai-therapeutics.com/
---
