---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The API host point.me operates behind its consumer search product and its Gateway embedded platform. https://api.point.me/ returns HTTP 200 text/plain "Flight Search APIs"; every other path probed (/o
  name: point.me Flight Search API
  slug: point-me-flight-search-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/point-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.point.me/
- group: company
  title: ''
  type: About
  url: https://www.point.me/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.point.me/our-services
- group: commercial
  title: ''
  type: Plans
  url: plans/point-me-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://point.me/signup/basic
- group: operate
  title: ''
  type: Support
  url: https://connect.point.me/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://connect.point.me/faq
- group: company
  title: ''
  type: Blog
  url: https://www.point.me/insights/
- group: company
  title: ''
  type: Press
  url: https://www.point.me/press/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.point.me/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.point.me/privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.point.me/accessibility
- group: company
  title: ''
  type: Partners
  url: https://www.point.me/partnerships/
- group: company
  title: ''
  type: Jobs
  url: https://connect.point.me/jobs
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/point-me-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/point-me-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/point-me-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/point-me-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/point-me-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/point-me-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/point-me-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/point-me-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/point-me-mcp.yml
created: '2026-08-26'
description: 'point.me is an award-travel company that operates a real-time award flight search engine for consumers and, through point.me Gateway, an API-first embedded loyalty-travel platform that banks and loyalty programs run inside their own branded apps. The consumer product searches award availability across 150+ airline and hotel loyalty programs on Basic/Standard/Premium annual subscriptions, and adds paid concierge booking. Gateway sells award search, point transfers and booking as an embedded integration to financial institutions (Amex among its named partners) and to loyalty programs. The API host api.point.me is live and identifies itself as "Flight Search APIs", but every path on it answers 401 with WWW-Authenticate: Bearer, and Gateway is sold through a demo form rather than a public developer portal, so no machine-readable contract is published.'
image: https://d27oqxoyguxgs9.cloudfront.net/jm-web-images-21082401/site-thumbnail.jpg
layout: provider
mcp_servers:
- description: point.me ships no Model Context Protocol server — neither a remote endpoint nor a local stdio package. No candidate tool list is derived either, because point.me publishes no OpenAPI to derive one fro
  name: POINT.ME MCP Server
  slug: pointme-mcp-server
modified: '2026-08-26'
name: POINT.ME
nav: Providers
network: true
overview: 'POINT.ME publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Award Travel, Loyalty, Points and Miles, and Flights.


  POINT.ME''s developer surface includes pricing, signup flow, support, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Point Me Plans Pricing
  plan_count: 3
  slug: point-me-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Point Me Rate Limits
  slug: point-me-rate-limits
scopes:
- name: Point Me Scopes
  scope_count: 0
  slug: point-me-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 34.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/point-me/refs/heads/main/screenshots/point-me-2026-09-02T151619.png
security:
- kind: authentication
  name: Point Me Authentication
  slug: point-me-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Point Me Domain Security
  slug: point-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: point-me
tags:
- Travel
- Award Travel
- Loyalty
- Points and Miles
- Flights
- Rewards
- Embedded Finance
- Banking
- Search
- Company
website: https://www.point.me/
---
