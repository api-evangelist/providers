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
    auth_clarity: false
    consent_identity: true
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
  score: 2.7
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autolus-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/autolus-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/autolus-security.txt
- group: company
  title: ''
  type: Website
  url: https://www.autolus.com
created: '2026-07-17'
description: 'Autolus is a life-sciences (biopharmaceutical) company operating in the cell-therapy space, developing programmed / engineered T cell (CAR-T) therapies for cancer and other serious diseases. It was surfaced as a portfolio company of GV and added to the API Evangelist network for enrichment. As a clinical/commercial-stage biopharma, its public web presence (autolus.com) is a corporate marketing and investor-relations site rather than a developer platform: no public API, developer portal, API documentation, or OpenAPI surface was found during enrichment. The only machine-discoverable artifact is a minimal RFC 9116 security.txt.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autolus.png
layout: provider
modified: '2026-07-18'
name: Autolus *
nav: Providers
network: true
overview: Autolus * is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Biopharmaceutical, Biotechnology, and Cell Therapy.
random_paper: 85
score:
  band: minimal
  composite: 5.4
  delta: -0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autolus/refs/heads/main/screenshots/autolus-2026-07-25T201826.png
security:
- kind: domain-security
  name: Autolus Domain Security
  slug: autolus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: autolus
tags:
- Company
- Life Sciences
- Biopharmaceutical
- Biotechnology
- Cell Therapy
- Immunotherapy
- Oncology
- CAR-T
website: https://www.autolus.com
---
