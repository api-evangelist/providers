---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.omsignal.com'', ''status'': 301, ''note'': ''declared website redirects to https://hexoskin.com/collections/all?orig=omsignal — a different registrable domain (omsignal.com -> hexoskin.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omsignal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.omsignal.com
created: '2026-07-17'
description: 'OMsignal was a Montreal-based biometric smart-apparel startup, backed by Bessemer Venture Partners, that built compression shirts and the OMbra sports bra with embedded textile sensors streaming heart-rate, breathing, and activity data to a companion mobile app. The brand no longer operates independently: the omsignal.com domain now 301-redirects to hexoskin.com (Carre Technologies / Hexoskin), the biometric smart-clothing company that absorbed the product line. As of this enrichment pass OMsignal publishes no independent developer portal, API, or documentation of its own, and omsignal.com itself serves no API artifacts or well-known metadata.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/omsignal.png
layout: provider
modified: '2026-07-20'
name: OMsignal
nav: Providers
network: true
overview: OMsignal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Wearables, Biometrics, and Smart Clothing.
random_paper: 18
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omsignal/refs/heads/main/screenshots/omsignal-2026-08-07T190204.png
security:
- kind: domain-security
  name: Omsignal Domain Security
  slug: omsignal-domain-security
  summary_line: TLSv1.3
slug: omsignal
tags:
- Company
- Consumer
- Wearables
- Biometrics
- Smart Clothing
- Health
- Defunct
website: https://www.omsignal.com
---
