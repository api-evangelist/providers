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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/goat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goat-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.goat.com/security/responsible-disclosure
- group: company
  title: ''
  type: Website
  url: https://www.goat.com
created: '2026-07-17'
description: GOAT (operated by GOAT Group) is a global online marketplace for authentic sneakers, apparel, and accessories, launched in 2015 and headquartered in the Los Angeles area. The platform pairs a consumer buying-and-selling experience with in-house authentication that verifies new and used footwear and streetwear from thousands of brands, and GOAT Group also operates the Flight Club consignment stores and the alias seller platform. GOAT was surfaced as a portfolio company of a16z, accel, index-ventures, initialized-capital, matrix-partners, and sv-angel and added to the API Evangelist network as a venture-backed company profile. It runs a consumer commerce platform rather than a public developer API, so this enriched profile focuses on verified company identity and the security surface probed from its public domain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goat.png
layout: provider
modified: '2026-07-19'
name: GOAT
nav: Providers
network: true
overview: GOAT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Marketplace, Retail, and Fashion.
random_paper: 67
score:
  band: minimal
  composite: 6.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 6.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Goat Domain Security
  slug: goat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Goat Vulnerability Disclosure
  slug: goat-vulnerability-disclosure
  summary_line: disclosure policy published
slug: goat
tags:
- Company
- Commerce
- Marketplace
- Retail
- Fashion
- Sneakers
- Apparel
website: https://www.goat.com
---
