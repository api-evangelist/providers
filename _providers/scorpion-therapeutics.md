---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scorpion-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scorpiontx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scorpiontx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scorpiontherapeutics
- group: company
  title: ''
  type: Press
  url: https://investor.lilly.com/news-releases/news-release-details/lilly-acquire-scorpion-therapeutics-mutant-selective-pi3ka
coverage:
  checked: '2026-08-05'
  detail: Scorpion's own site no longer serves the company — https://www.scorpiontx.com/ 302-redirects every request to Eli Lilly's January 2025 acquisition press release, and the only first-party technical surface left is a four-repo GitHub org of computational-chemistry forks and an STX-721 molecular-dynamics data-availability README, with no API, SDK or spec anywhere.
  evidence:
  - status: 302
    url: https://www.scorpiontx.com/
  - status: 404
    url: https://www.scorpiontx.com/openapi.json
  - status: 404
    url: https://www.scorpiontx.com/llms.txt
  - status: 403
    url: https://www.scorpiontx.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/scorpiontx
  reason: defunct
  state: none
created: '2026-08-05'
description: 'Scorpion Therapeutics is a clinical-stage precision oncology biotechnology company founded in 2020 and headquartered in Boston, Massachusetts. It pursued what it called Precision Oncology 2.0 — integrating target discovery, medicinal chemistry and translational medicine to produce mutant-selective small-molecule cancer drugs — led by STX-478, an oral mutant-selective PI3K-alpha inhibitor in Phase 1/2 trials for breast cancer and other advanced solid tumors, and STX-721, a covalent EGFR/HER2 exon 20 inhibitor. In January 2025 Eli Lilly agreed to acquire Scorpion and its PI3K-alpha program in a transaction valued at up to $2.5 billion, with the non-PI3K-alpha pipeline and staff spun into a separate independent company. Scorpion is a drug developer, not a software vendor: it publishes no API, SDK, developer portal or machine-readable specification, and its own domain now redirects to the acquirer''s announcement.'
image: https://avatars.githubusercontent.com/u/73207155?v=4
layout: provider
modified: '2026-08-05'
name: Scorpion Therapeutics
nav: Providers
network: true
overview: Scorpion Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Precision Medicine.
random_paper: 133
score:
  band: minimal
  composite: 6.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Scorpion Therapeutics Domain Security
  slug: scorpion-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: scorpion-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Precision Medicine
- Drug Discovery
- Life Sciences
- Clinical Research
website: https://www.scorpiontx.com/
---
