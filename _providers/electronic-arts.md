---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Public-facing presence of Electronic Arts. Covers EA''s corporate site, consumer game services, EA app, EA Play subscription, and EA Help support surfaces. EA does not publicly publish a developer API '
  name: Electronic Arts
  slug: electronic-arts
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/electronic-arts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electronic-arts-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electronic-arts
- group: company
  title: ''
  type: Website
  url: https://www.ea.com
- group: operate
  title: ''
  type: Support
  url: https://help.ea.com
- group: other
  title: ''
  type: Subscription
  url: https://www.ea.com/ea-play
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.ea.com
- group: company
  title: ''
  type: Careers
  url: https://www.ea.com/careers
- group: build
  title: ''
  type: GitHub
  url: https://github.com/electronicarts
- group: company
  title: ''
  type: Blog
  url: https://www.ea.com/news
created: '2026-03-21'
description: Electronic Arts (EA) is a global leader in digital interactive entertainment, developing and delivering games, content, and online services for internet-connected consoles, mobile devices, and personal computers. EA's portfolio includes franchises such as EA SPORTS FC, Madden NFL, Battlefield, The Sims, Apex Legends, and Need for Speed, supported by online services like EA app, EA Play, and Origin. EA does not currently publish a public developer API portal; integrations and data exchanges are handled through partner programs and the EA Help support and account surfaces.
finops:
- name: Electronic Arts Finops
  service_category: Entertainment
  slug: electronic-arts-finops
graphqls:
- description: 'This is a conceptual GraphQL schema for Electronic Arts (EA) gaming and player services. Electronic Arts does not currently publish a public developer API portal; this schema is derived from known EA '
  name: Electronic Arts GraphQL Schema
  slug: electronic-arts-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/electronic-arts.png
layout: provider
modified: '2026-04-28'
name: Electronic Arts
nav: Providers
network: true
overview: 'Electronic Arts publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Video Games, Entertainment, Consumer, and Player Services.


  Electronic Arts'' developer surface includes support, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Electronic Arts Plans Pricing
  plan_count: 2
  slug: electronic-arts-plans-pricing
press:
- date: '2026-05-25'
  title: Sent Via email October 28, 2025 Scott Bessent Secretary of ...
  url: https://cwa-union.org/sites/default/files/2025-10/20251028_cwa_letter_to_secretary_bessent.pdf
- date: '2026-05-25'
  title: Stability AI Partners with Electronic Arts on Customizable AI
  url: https://www.linkedin.com/posts/prem-akkaraju-7b10a265_inside-video-game-giant-electronic-arts-activity-7424598337934442497-I3Ck
- date: '2026-05-25'
  title: Mr. Andrew Wilson Chief Executive Officer Electronic Arts, Inc.
  url: https://www.hsgac.senate.gov/wp-content/uploads/2025-10-14-Letter-from-Blumenthal-and-Warren-to-Electronic-Arts-CEO-Andrew-Wilson.pdf
- date: '2026-05-25'
  title: Inside the AI divide roiling video game giant Electronic Arts
  url: https://www.businessinsider.com/inside-ai-divide-roiling-video-game-giant-electronic-arts-2025-10
- date: '2026-05-25'
  title: EA and Stability AI partner to empower artists, designers, ...
  url: https://www.ea.com/news/ea-partners-with-stability-ai
random_paper: 18
rate_limits:
- limit_count: 1
  name: Electronic Arts Rate Limits
  slug: electronic-arts-rate-limits
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 4.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 21.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/electronic-arts/refs/heads/main/screenshots/electronic-arts-2026-06-20T180553.png
security:
- kind: domain-security
  name: Electronic Arts Domain Security
  slug: electronic-arts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Electronic Arts Vulnerability Disclosure
  slug: electronic-arts-vulnerability-disclosure
  summary_line: disclosure policy published
slug: electronic-arts
tags:
- Gaming
- Video Games
- Entertainment
- Consumer
- Player Services
- Fortune 1000
website: https://www.ea.com
---
