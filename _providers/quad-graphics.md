---
access_model:
  confidence: medium
  label: Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.quad.com/solutions/technology/at-home-connect
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quad-graphics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quad.com
- group: agent
  title: ''
  type: LlmsText
  url: https://quad.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.quad.com/feed
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quad-graphics-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/quad-graphics-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/quad-graphics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quad-graphics-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://www.quad.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quad.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quad.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QuadGraphics
- group: start
  title: ''
  type: Login
  url: https://athomeconnect.quad.com/
coverage:
  checked: '2026-08-13'
  detail: Quad markets an At-Home Connect API for triggering direct mail from CRM and marketing automation platforms but publishes no reference for it — the product page's only next step is a contact form to "see if you qualify for early access", and the one reachable Quad API host, api.postal.quad.com, answers 403 to anonymous requests with no WWW-Authenticate challenge and real 404s on every spec path.
  evidence:
  - status: 200
    url: https://www.quad.com/solutions/technology/at-home-connect
  - status: 403
    url: https://api.postal.quad.com/
  - status: 404
    url: https://api.postal.quad.com/openapi.json
  - status: 401
    url: https://connect.qg.com/swagger.json
  reason: sales-gate
  state: gated
created: '2026-03-24'
description: 'Quad (NYSE: QUAD), formerly Quad/Graphics, is a Sussex, Wisconsin marketing experience company that pairs one of North America''s largest commercial printing platforms with data, creative, media and marketing-technology services. Its offer spans audience targeting and consumer analytics, creative and content production through its Betty agency, omnichannel media planning and placement through its Rise agency, catalog, magazine, direct mail and packaging production, in-store retail media displays, postal optimization and logistics, and the QuadMed employee health business. Quad markets three named marketing-technology platforms — At-Home Connect for automated triggered direct mail, Local Connect for multi-location marketing, and In-Store Connect for retail media — and advertises API integration with CRM and marketing-automation platforms for At-Home Connect, but publishes no developer portal, API reference or machine-readable specification for any of them.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quad-graphics.png
layout: provider
modified: '2026-08-13'
name: Quad/Graphics
nav: Providers
network: true
overview: 'Quad/Graphics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Print, Media, Advertising, and Direct Mail.


  Quad/Graphics'' developer surface includes engineering blog, authentication, support, and 10 more developer resources.'
plans:
- name: Quad Graphics Plans Pricing
  plan_count: 0
  slug: quad-graphics-plans-pricing
press:
- date: '2026-05-25'
  title: Quad Announces Participation in the Rosenblatt Virtual ...
  url: https://www.prnewswire.com/news-releases/quad-announces-participation-in-the-rosenblatt-virtual-technology-summit-the-age-of-ai-302776617.html
- date: '2026-05-25'
  title: Quad names Dave Honan President alongside COO role
  url: https://www.stocktitan.net/sec-filings/QUAD/8-k-quad-graphics-inc-reports-material-event-363415c2f882.html
- date: '2026-05-25'
  title: '99.1'
  url: https://www.sec.gov/Archives/edgar/data/1481792/000148179226000088/pressreleaseex991q12026.htm
- date: '2026-05-25'
  title: Quad & Google Cloud to launch AI-powered marketing ...
  url: https://www.quad.com/newsroom/quad-and-google-cloud-to-launch-next-generation-ai-powered-marketing-solutions
- date: '2026-05-25'
  title: Quad makes audience creation easier, faster and more ...
  url: https://www.prnewswire.com/news-releases/quad-makes-audience-creation-easier-faster-and-more-precise-with-natural-language-ai-prompts-powered-by-snowflake-302578665.html
random_paper: 19
rate_limits:
- limit_count: 0
  name: Quad Graphics Rate Limits
  slug: quad-graphics-rate-limits
score:
  band: emerging
  composite: 15.4
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quad-graphics/refs/heads/main/screenshots/quad-graphics-2026-06-20T192354.png
security:
- kind: authentication
  name: Quad Graphics Authentication
  slug: quad-graphics-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Quad Graphics Domain Security
  slug: quad-graphics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quad-graphics
tags:
- Marketing
- Print
- Media
- Advertising
- Direct Mail
- Marketing Technology
- Retail Media
- Packaging
- Data
website: https://www.quad.com
---
