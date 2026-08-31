---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/human-dx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://humandx.org
created: '2026-07-17'
description: The Human Diagnosis Project (Human Dx) is a nonprofit initiative building an open, global medical intelligence system that combines the collective insight of physicians with machine learning to help make high-quality, affordable healthcare accessible to everyone. Its programs pair clinical microlearning and training tools for medical trainees with a specialist eConsult network that connects safety-net and underserved patients and their primary-care providers to volunteer specialists. The organization operates under the tagline "Rise together." Surfaced in the API Evangelist network as a portfolio-lead stub; no public API, developer portal, or machine-readable API surface was found during enrichment.
image: https://resources.humandx.org/static/img/symbol_v3_og_image.jpg
layout: provider
modified: '2026-07-19'
name: Human DX
nav: Providers
network: true
overview: Human DX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Medical, and Diagnosis.
random_paper: 4
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/human-dx/refs/heads/main/screenshots/human-dx-2026-07-25T221647.png
security:
- kind: domain-security
  name: Human Dx Domain Security
  slug: human-dx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: human-dx
tags:
- Company
- Health
- Healthcare
- Medical
- Diagnosis
- Machine-Learning
- Non-Profit
- Clinical Decision Support
website: https://humandx.org
---
