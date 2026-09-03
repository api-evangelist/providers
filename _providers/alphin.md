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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alphin-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alphin-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/alphin-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.alphin.com/
- group: company
  title: ''
  type: Blog
  url: https://www.alphin.com/en/blog-en
- group: start
  title: ''
  type: Login
  url: https://app.alphin.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alphin.com/en/gtc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alphin.com/en/utility-pages/data-protection
coverage:
  checked: '2026-08-12'
  detail: alphin ships only an end-user Business App — the Angular SPA at app.alphin.io talks to a private Express backend at api.alphin.io whose /v1 returns 401 and whose every documentation path (/openapi.json, /swagger.json, /api-docs, /docs, /graphql) returns "Cannot GET"; there is no developer portal, docs host (developer.alphin.com, docs.alphin.com and docs.alphin.io do not resolve), SDK on any package registry, or public GitHub organization.
  evidence:
  - status: 404
    url: https://api.alphin.io/openapi.json
  - status: 401
    url: https://api.alphin.io/v1
  - status: 404
    url: https://www.alphin.com/llms.txt
  - status: 404
    url: https://www.alphin.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: alphin is a Berlin-based marketing platform for local small businesses, giving restaurants, cafes, salons, and similar SMBs an all-in-one app to manage and automate their online presence. Its product suite spans review collection (alphin Reviews), Instagram and social management (alphin Socials), professional photography (alphin Photos), local influencer marketing (alphin Local Influencers), targeted Instagram advertising (alphin Local Ads), and multi-platform profile management across Google, TripAdvisor, and Yelp (alphin Portals), consolidated into one dashboard with daily reporting and analytics. Founded in 2016 (as Freachly GmbH), alphin serves 1,000+ local businesses across Germany, Austria, the UK, and Israel, and is backed by HV Capital, Partech, Scale Capital, and Wille Finance. alphin publishes no public API, developer portal, or SDKs; the product is delivered through its web and mobile Business App.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alphin.png
layout: provider
modified: '2026-08-12'
name: alphin
nav: Providers
network: true
overview: 'alphin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Local Marketing, Small Business, and Social-Media.


  alphin''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Alphin Plans Pricing
  plan_count: 0
  slug: alphin-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alphin/refs/heads/main/screenshots/alphin-2026-07-25T195801.png
security:
- kind: domain-security
  name: Alphin Domain Security
  slug: alphin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alphin
tags:
- Company
- Marketing
- Local Marketing
- Small Business
- Social-Media
- Reviews
- Advertising
- Software-as-a-Service
website: https://www.alphin.com/
---
