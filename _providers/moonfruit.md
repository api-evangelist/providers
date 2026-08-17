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
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moonfruit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moonfruit.com
- group: company
  title: ''
  type: Blog
  url: https://moonfruit.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://moonfruit.com/faq
- group: start
  title: ''
  type: SignUp
  url: https://moonfruit.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moonfruit.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moonfruit.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://moonfruit.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moonfruitsocial/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moonfruit-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/moonfruit-plans-pricing.yml
coverage:
  checked: '2026-08-13'
  detail: 'MoonFruit is a WordPress-hosted directory of digital marketing agencies with no developer program of any kind: api., developer. and docs.moonfruit.com are wildcard DNS records that return the 236KB marketing homepage with HTTP 200, every /.well-known/ path 404s, and the only machine-readable surface on the domain is the stock WordPress REST API at /wp-json/ (WordPress core and third-party plugin namespaces only, no first-party MoonFruit namespace, with the bundled MCP Adapter endpoint returning rest_forbidden 401).'
  evidence:
  - status: 200
    url: https://api.moonfruit.com/openapi.json
  - status: 404
    url: https://moonfruit.com/openapi.json
  - status: 404
    url: https://moonfruit.com/.well-known/agent-card.json
  - status: 200
    url: https://moonfruit.com/wp-json/
  - status: 401
    url: https://moonfruit.com/wp-json/mcp/mcp-adapter-default-server
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: MoonFruit is a directory platform that connects businesses with vetted digital marketing agencies worldwide, letting users search and filter agencies by service specialization (SEO, PPC, content marketing, web design, branding, video production and more) and by geographic location across major US cities and international markets such as London and Dubai. Each listing surfaces agency details including location, budget ranges and service descriptions, and agencies can submit or claim their own profiles. The company was surfaced as a portfolio company of 500 Global and added to the API Evangelist network for enrichment; as of this pass the live site publishes no public API, developer portal, or programmatic surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moonfruit.png
layout: provider
modified: '2026-08-13'
name: MoonFruit
nav: Providers
network: true
overview: 'MoonFruit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Directory, Marketing Agencies, Digital Marketing, and Marketplace.


  MoonFruit''s developer surface includes engineering blog, signup flow, support, and 8 more developer resources.'
plans:
- name: Moonfruit Plans Pricing
  plan_count: 0
  slug: moonfruit-plans-pricing
random_paper: 101
score:
  band: emerging
  composite: 13.9
  delta: 0.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moonfruit/refs/heads/main/screenshots/moonfruit-2026-08-07T184243.png
security:
- kind: domain-security
  name: Moonfruit Domain Security
  slug: moonfruit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: moonfruit
tags:
- Company
- Directory
- Marketing Agencies
- Digital Marketing
- Marketplace
- Website
website: https://moonfruit.com
---
