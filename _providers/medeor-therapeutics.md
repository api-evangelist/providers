---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://medeortx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medeortx.com/privacy-policy.php
- group: company
  title: ''
  type: News
  url: https://medeortx.com/news.php
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medeor-therapeutics/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/medeor-therapeutics_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medeor-therapeutics-domain-security.yml
coverage:
  checked: '2026-08-25'
  detail: medeortx.com serves a live homepage whose lead paragraph states Medeor has suspended operations and is seeking an acquirer to complete the BLA filing, leaving a clinical-trial archive site with no developer, API, or data surface of any kind.
  evidence:
  - status: 200
    url: https://medeortx.com/
  - status: 404
    url: https://medeortx.com/openapi.json
  - status: 404
    url: https://medeortx.com/llms.txt
  - status: 404
    url: https://medeortx.com/.well-known/api-catalog
  - status: 404
    url: https://github.com/medeortx
  reason: defunct
  state: none
created: '2026-08-25'
description: 'Medeor Therapeutics is a clinical-stage cellular immunotherapy company in San Mateo, California, developing MDR-101, a one-time cell therapy manufactured from a living kidney donor''s blood that induces mixed chimerism so HLA-matched transplant recipients can withdraw from lifelong immunosuppression while preserving graft function. The platform originated in roughly two decades of research at Stanford University led by Dr. Samuel Strober. The company completed a Phase 3 registration trial that exceeded its target success rate, and has since suspended operations and is seeking an acquirer to complete the BLA filing. Medeor is a therapeutics developer, not a software company: it publishes no developer portal, API, SDK, or machine-readable specification.'
layout: provider
modified: '2026-08-25'
name: Medeor Therapeutics
nav: Providers
network: true
overview: 'Medeor Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Cell Therapy, and Immunotherapy.


  Medeor Therapeutics'' developer surface includes product news and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medeor-therapeutics/refs/heads/main/screenshots/medeor-therapeutics-2026-09-02T150451.png
security:
- kind: domain-security
  name: Medeor Therapeutics Domain Security
  slug: medeor-therapeutics-domain-security
  summary_line: TLSv1.2
slug: medeor-therapeutics
tags:
- Company
- Biotechnology
- Life Sciences
- Cell Therapy
- Immunotherapy
- Organ Transplant
- Healthcare
- Clinical Trials
- Pharmaceuticals
website: https://medeortx.com/
---
