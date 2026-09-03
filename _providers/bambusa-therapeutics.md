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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bambusa-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bambusatx.com/
- group: company
  title: ''
  type: About
  url: https://bambusatx.com/about/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bambusa-therapeutics_stock/
coverage:
  checked: '2026-08-06'
  detail: Bambusa is a 2024-founded clinical-stage antibody developer whose only web property, bambusatx.com, is a marketing site sitting entirely behind a SiteGround captcha (every path, including /, answers 202 with an sgcaptcha redirect), while DNS resolves no api./docs./developers./portal. host and no company GitHub organization exists — the product is a bispecific-antibody pipeline, not software, so there is no API to publish.
  evidence:
  - status: 202
    url: https://bambusatx.com/openapi.json
  - status: 202
    url: https://bambusatx.com/.well-known/agent-card.json
  - status: 202
    url: https://bambusatx.com/.well-known/security.txt
  - status: 202
    url: https://bambusatx.com/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: Bambusa Therapeutics, Inc. is a clinical-stage biotechnology company headquartered in the Boston Seaport, founded in 2024 by Shanshan Xu and Helmut Jeggle to develop next-generation bispecific antibodies for immunological and inflammatory (I&I) diseases. Its antibody-engineering platform combines half-life extension with high-concentration subcutaneous delivery, and its pipeline spans dermatology, respiratory, gastroenterology and rheumatology — led by BBT-001 (IL-31 x IL-4Ralpha, in a Phase 1b/2a atopic dermatitis trial) and BBT-002 for COPD. The company raised a Series Seed in 2024, an approximately $90M Series A led by RA Capital Management in February 2025, and an oversubscribed Series A-2 in November 2025. It is a therapeutics developer, not a software vendor, and publishes no public API, SDK or developer program.
layout: provider
modified: '2026-08-06'
name: Bambusa Therapeutics
nav: Providers
network: true
overview: Bambusa Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Immunology.
random_paper: 15
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bambusa-therapeutics/refs/heads/main/screenshots/bambusa-therapeutics-2026-08-07T162119.png
security:
- kind: domain-security
  name: Bambusa Therapeutics Domain Security
  slug: bambusa-therapeutics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bambusa-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Immunology
- Clinical Trials
- Drug Development
- Antibodies
website: https://bambusatx.com/
---
