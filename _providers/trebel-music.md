---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trebel-music-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trebel-music-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/trebel-music-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trebel-music-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trebel-music-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://home.trebel.io/
- group: operate
  title: ''
  type: Support
  url: https://home.trebel.io/get-in-touch
- group: commercial
  title: ''
  type: TermsOfService
  url: https://home.trebel.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://home.trebel.io/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://home.trebel.io/bug-program
- group: company
  title: ''
  type: X (Twitter)
  url: https://twitter.com/trebelmusic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trebelmusic/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCPy1kySujznHGx2wHXwUWTg
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/trebelapp
coverage:
  checked: '2026-08-30'
  detail: TREBEL is a consumer music app with no developer program at all — its sitemap lists 45 pages and not one is a developer portal, API reference or spec, and api.trebel.io is a private nginx backend for the mobile apps that returns 404 on its root and on every OpenAPI/GraphQL/MCP/agent-card path probed.
  evidence:
  - status: 404
    url: https://api.trebel.io/openapi.json
  - status: 404
    url: https://api.trebel.io/
  - status: 200
    url: https://home.trebel.io/sitemap.xml
  - status: 404
    url: https://home.trebel.io/docs
  - status: 404
    url: https://api.trebel.io/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-30'
description: TREBEL Music (operated by M&M Media, Inc.) is an advertising-sponsored, legally licensed music download and streaming service that lets people download and listen to music offline at no cost. Founded in 2014 by Gary Mekikian, Corey Jones and Luis Soto Durazo and headquartered in Stamford, Connecticut with offices in Mexico City, Jakarta, Bogota, Los Angeles and Miami, TREBEL licenses catalog from Universal Music Group, Sony Music Entertainment, Warner Music Group and independent labels, and monetizes through digital advertising, branded experiences, virtual goods and a TREBEL Max tier rather than a conventional paid subscription. TREBEL is a consumer mobile product distributed through the Apple App Store, Google Play and Huawei AppGallery; it publishes no public developer program, API reference, SDK or machine-readable contract.
image: https://home.trebel.io/TREBEL_favicon.png
layout: provider
modified: '2026-08-30'
name: TREBEL Music
nav: Providers
network: true
overview: 'TREBEL Music is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Music Streaming, Media, and Entertainment.


  TREBEL Music''s developer surface includes support, YouTube channel, and 12 more developer resources.'
plans:
- name: Trebel Music Plans Pricing
  plan_count: 0
  slug: trebel-music-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Trebel Music Rate Limits
  slug: trebel-music-rate-limits
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trebel-music/refs/heads/main/screenshots/trebel-music-2026-09-02T164157.png
security:
- kind: domain-security
  name: Trebel Music Domain Security
  slug: trebel-music-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trebel Music Vulnerability Disclosure
  slug: trebel-music-vulnerability-disclosure
  summary_line: Hackerone
slug: trebel-music
tags:
- Company
- Music
- Music Streaming
- Media
- Entertainment
- Mobile Apps
- Advertising
- Consumer
website: https://home.trebel.io/
---
