---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iolyx-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iolyx.com/
coverage:
  checked: '2026-08-23'
  detail: Iolyx is a clinical-stage drug developer whose entire web presence is a six-page WordPress marketing site (Home, Pipeline, Team, News, Media, Contact) with zero blog posts, no developer or API section, no GitHub organization, and no package on any public registry — the only machine-readable thing on iolyx.com is the stock WordPress /wp-json/ discovery document the hosting stack serves by default, which is not a product API.
  evidence:
  - status: 200
    url: https://iolyx.com/
  - status: 404
    url: https://iolyx.com/openapi.json
  - status: 404
    url: https://iolyx.com/llms.txt
  - status: 404
    url: https://iolyx.com/.well-known/agent-card.json
  - status: 200
    url: https://iolyx.com/wp-json/
  - status: 404
    url: https://api.github.com/orgs/iolyx-therapeutics
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Iolyx Therapeutics, Inc. is a privately held, clinical-stage biopharmaceutical company headquartered in Burlingame, California, working at what it calls the intersection of immunology and ophthalmology — "immuno-ophthalmology". The company develops immunomodulatory therapeutics that target ocular inflammation at its source, using what it describes as innovative pathways and tailored formulations for precise delivery to the relevant ocular tissues, positioned as an alternative to conventional steroids and broad immunosuppressants. Its lead asset, ILYX-002, is in trials for autoimmune-associated dry eye disease; the company announced Phase 2 results in May 2025 and, in December 2025, a strategic agreement with Laboratoires Théa to develop and commercialize ILYX-002 alongside Series B funding for its retinal pipeline. The stated pipeline spans front-of-eye indications (dry eye, ocular allergy, rosacea, uveitis) and back-of-eye indications (age-related macular degeneration, diabetic
  retinopathy, posterior uveitis). Iolyx is a drug developer rather than a software vendor: it operates a six-page WordPress marketing site at iolyx.com and publishes no public API, developer portal, SDK, or machine-readable specification.'
image: https://iolyx.com/wp-content/uploads/2023/10/iolyx-logo.png
layout: provider
modified: '2026-08-23'
name: Iolyx Therapeutics
nav: Providers
network: true
overview: Iolyx Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Biotechnology, Pharmaceuticals, and Life Sciences.
random_paper: 17
score:
  band: minimal
  composite: 3.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Iolyx Therapeutics Domain Security
  slug: iolyx-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iolyx-therapeutics
tags:
- Company
- Healthcare
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Ophthalmology
- Immunology
- Clinical Trials
website: https://iolyx.com/
---
