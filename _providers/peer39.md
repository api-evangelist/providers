---
access_model:
  confidence: high
  label: Enterprise / Contact Sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://www.peer39.com/platform-demo
  - https://www.peer39.com/contact-us
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Peer39 External API manages Custom Categories — contextual targeting and brand-safety lists of keywords, URLs, mobile apps or CTV apps — and syncs them to a connected DSP partner. Nine operations '
  name: Peer39 External API
  slug: peer39-external-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peer39-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/peer39-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/peer39-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/peer39-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/peer39-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.peer39.com
- group: company
  title: ''
  type: Blog
  url: https://www.peer39.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.peer39.com/onboarding-guide
- group: start
  title: ''
  type: Login
  url: https://app.peer39.com/login
- group: start
  title: ''
  type: SignUp
  url: https://www.peer39.com/signup/
- group: operate
  title: ''
  type: Support
  url: https://www.peer39.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.peer39.com/service-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peer39.com/privacy-policy/
created: '2026-07-17'
description: 'Peer39 is a contextual advertising and intelligence company that provides pre-bid controls and post-buy analytics built on verified contextual data for programmatic media buyers. Its platform delivers contextual targeting, brand safety and suitability, and contextual analytics across web, mobile, and connected TV (CTV) and video environments, helping advertisers and platforms make privacy-forward, cookieless media decisions. Peer39 was surfaced as a portfolio company of Canaan Partners and added to the API Evangelist network. Peer39 does operate a real REST API — the Peer39 External API at https://app.peer39.com/api/external — for creating, updating and deleting Custom Categories (contextual targeting and brand-safety lists of keywords, URLs, mobile apps and CTV apps) and syncing them to connected DSPs such as The Trade Desk, Microsoft Advertising/Xandr, Basis, Yahoo and Amazon. That API is entirely undocumented in public: there is no developer portal, no API reference page,
  no OpenAPI specification and no published SDK. Credentials are provisioned by a Peer39 account or integration manager who grants the "External API" and "RTB Buyer" roles on a named account, and API documentation is distributed as PDFs rather than published on the web. A first-party-authored MCP server for the API exists in pre-release on a personal GitHub account and is the only public description of the surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peer39.png
layout: provider
mcp_servers:
- description: ''
  name: Peer39 Custom Category MCP Server
  slug: peer39-custom-category-mcp-server
modified: '2026-08-12'
name: Peer39
nav: Providers
network: true
overview: 'Peer39 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contextual Advertising, AdTech, Brand Safety, and Programmatic Advertising.


  Peer39''s developer surface includes engineering blog, getting-started guide, signup flow, support, and 9 more developer resources.'
plans:
- name: Peer39 Plans Pricing
  plan_count: 0
  slug: peer39-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Peer39 Rate Limits
  slug: peer39-rate-limits
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 21.2
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peer39/refs/heads/main/screenshots/peer39-2026-09-02T150936.png
security:
- kind: authentication
  name: Peer39 Authentication
  slug: peer39-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Peer39 Domain Security
  slug: peer39-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peer39
tags:
- Company
- Contextual Advertising
- AdTech
- Brand Safety
- Programmatic Advertising
- Contextual Targeting
- CTV
- MarTech
- Advertising
- Custom Categories
- DSP
website: https://www.peer39.com
---
