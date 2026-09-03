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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/religion-of-sports-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.religionofsports.com/
- group: company
  title: ''
  type: About
  url: https://www.religionofsports.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.religionofsports.com/news
- group: operate
  title: ''
  type: Contact
  url: https://www.religionofsports.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.religionofsports.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.religionofsports.com/california-privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/religion-of-sports
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/religion-of-sports-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Religion of Sports is a documentary film and sports-media production studio whose entire public surface is a six-page Webflow marketing and press site — there is no developer portal, no product to integrate with, and api.religionofsports.com does not resolve in DNS.
  evidence:
  - status: 404
    url: https://www.religionofsports.com/openapi.json
  - status: 404
    url: https://www.religionofsports.com/.well-known/agent-card.json
  - status: 404
    url: https://www.religionofsports.com/.well-known/api-catalog
  - status: 404
    url: https://www.religionofsports.com/llms.txt
  - status: 0
    url: https://api.religionofsports.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Religion of Sports is an Emmy Award-winning sports media and entertainment production studio founded in 2017 by Tom Brady, Michael Strahan and Gotham Chopra, headquartered in Santa Monica, California and operating as The Religion of Sports Media, Inc. The company produces premium non-fiction film, documentary series and branded content that examine why sports matter, distributed through Netflix, HBO, Paramount+, ESPN, Apple TV+, Showtime, Fox Sports and NBC Sports, with titles including Simone Biles Rising, In the Arena: Serena Williams, Made for March, 5-Star and Alex vs. ARod. It raised a $50M Series B led by Shamrock Capital in June 2022 to build a non-fiction studio arm and expand into new formats and non-sports categories. Its public surface is a marketing and press site; the company operates no developer program, publishes no API documentation, and exposes no machine-readable contract.'
image: https://cdn.prod.website-files.com/66b0c0227ef11307efb1cf8c/66bcfa9e74b41c90f32de3c2_Religion%20of%20Sports%20webclip.jpg
layout: provider
modified: '2026-08-26'
name: Religion of Sports
nav: Providers
network: true
overview: 'Religion of Sports is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Entertainment, Sports, and Video.


  Religion of Sports'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/religion-of-sports/refs/heads/main/screenshots/religion-of-sports-2026-09-02T153318.png
security:
- kind: domain-security
  name: Religion Of Sports Domain Security
  slug: religion-of-sports-domain-security
  summary_line: TLSv1.3 · HSTS
slug: religion-of-sports
tags:
- Company
- Media
- Entertainment
- Sports
- Video
- Documentary
- Content Production
- Streaming
website: https://www.religionofsports.com/
---
