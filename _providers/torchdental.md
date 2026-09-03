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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://torchdental.com
- group: start
  title: ''
  type: Login
  url: https://app.torchdental.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/torchdental-domain-security.yml
created: '2026-07-17'
description: 'Torchdental (Torch Dental) is a B2B dental-supply procurement platform for independent dental practices and dental groups. It runs a web application at app.torchdental.com that lets practices order dental supplies and equipment from multiple vendors in one place, compare prices, manage recurring ordering and budgets, and streamline back-office purchasing. The company is venture backed and was surfaced as a portfolio company of Felicis. As of this enrichment pass Torchdental exposes no public developer/API surface: no api/docs/developer subdomains resolve, and the application host publishes no /.well-known/ discovery documents. This profile therefore captures company identity and probed domain-security posture only.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/torchdental.png
layout: provider
modified: '2026-07-21'
name: Torchdental
nav: Providers
network: true
overview: Torchdental is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Dental, Healthcare, Procurement, and E-Commerce.
random_paper: 0
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/torchdental/refs/heads/main/screenshots/torchdental-2026-09-02T163933.png
security:
- kind: domain-security
  name: Torchdental Domain Security
  slug: torchdental-domain-security
  summary_line: TLSv1.3 · DMARC
slug: torchdental
tags:
- Company
- Dental
- Healthcare
- Procurement
- E-Commerce
- Supply Chain
- B2B
- Software-as-a-Service
website: https://torchdental.com
---
