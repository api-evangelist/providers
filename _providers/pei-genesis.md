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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pei-genesis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pei-genesis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.peigenesis.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pei-genesis
created: '2026-05-23'
description: PEI-Genesis is a privately held, Philadelphia-headquartered global authorized distributor and value-added assembler of interconnect components (cable and circular connectors), founded in 1946. The company self-describes on LinkedIn as providing "Engineered Solutions for Connectors and Cables" in the Appliances, Electrical, and Electronics Manufacturing industry, with 501-1,000 employees. The public-facing peigenesis.com web property is a product catalog and quote-request portal protected by an interstitial JavaScript challenge; no public REST API, OpenAPI specification, developer portal, EDI integration documentation, PunchOut catalog, or GitHub organization could be located. Public API documentation has not yet been catalogued in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pei-genesis.png
layout: provider
modified: '2026-05-23'
name: PEI-Genesis
nav: Providers
network: true
overview: PEI-Genesis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Distribution, Electronics, Connectors, Cable Assembly, and Manufacturing.
random_paper: 47
score:
  band: minimal
  composite: 4.4
  delta: -1.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pei-genesis/refs/heads/main/screenshots/pei-genesis-2026-06-20T191533.png
security:
- kind: domain-security
  name: Pei Genesis Domain Security
  slug: pei-genesis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pei Genesis Vulnerability Disclosure
  slug: pei-genesis-vulnerability-disclosure
  summary_line: disclosure policy published
slug: pei-genesis
tags:
- Distribution
- Electronics
- Connectors
- Cable Assembly
- Manufacturing
website: https://www.peigenesis.com/
---
