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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chroniclebio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chroniclebio.com/
created: '2026-07-17'
description: 'ChronicleBio is a biotechnology company working at the intersection of human data and drug discovery, with the stated mission of translating human data into disease-defining medicines. It operates in the healthcare and life-sciences sector and was surfaced through the electric-capital portfolio. As of this profile, ChronicleBio publishes a corporate marketing website but no public developer surface: enrichment found no API documentation, developer portal, OpenAPI specification, SDKs, MCP server, or changelog. Domain security was probed live (TLS 1.3, HSTS, SPF, and a DMARC quarantine policy present; DNSSEC and CAA absent).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chroniclebio.png
layout: provider
modified: '2026-07-18'
name: ChronicleBio
nav: Providers
network: true
overview: ChronicleBio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Biotechnology, Life Sciences, and Drug Discovery.
random_paper: 30
score:
  band: minimal
  composite: 5.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chroniclebio/refs/heads/main/screenshots/chroniclebio-2026-07-25T205305.png
security:
- kind: domain-security
  name: Chroniclebio Domain Security
  slug: chroniclebio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chroniclebio
tags:
- Company
- Healthcare
- Biotechnology
- Life Sciences
- Drug Discovery
- Therapeutics
- Pharmaceuticals
- Human Data
website: https://chroniclebio.com/
---
