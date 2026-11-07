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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Croxy Residential Proxy API provides endpoints for managing and using residential, static, and ISP proxies.
  name: Residential Proxy API
  slug: residential-proxy-api
artifact_total: 2
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://croxy.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://croxy.com/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://croxy.com/privacy-policy/
- group: agent
  href: https://artifacts.apis.io/croxy/llms/croxy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/croxy-llms.txt
- group: other
  href: https://artifacts.apis.io/croxy/hosts/croxy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/croxy-hosts.yml
- group: other
  href: https://artifacts.apis.io/croxy/vendors/croxy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/croxy-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://croxy.com/login/
- group: company
  title: ''
  type: Blog
  url: https://croxy.com/blog/
- group: auth
  href: https://artifacts.apis.io/croxy/security/croxy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/croxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://croxy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://croxy.com/user-guide/residential-proxy-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://croxy.com/buy/residential/
coverage:
  checked: '2026-11-02'
  detail: Documentation is HTML without a published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://croxy.com/user-guide/residential-proxy-api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Croxy provides premium residential, static, and ISP proxy solutions, offering a large pool of IP addresses for web scraping, data access, and anonymity. Their platform features fast, secure, unlimited traffic proxies, a user-friendly dashboard, and flexible pricing plans for developers and enterprises.
image: https://croxy.com/favicon.ico
layout: provider
modified: '2026-11-02'
name: Croxy
nav: Providers
network: true
overview: 'Croxy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Proxy, Residential Proxy, Web Scraping, and Developer Tools.


  Croxy''s developer surface includes support, engineering blog, documentation, pricing, and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Croxy Domain Security
  slug: croxy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: croxy
tags:
- Proxy
- Residential Proxy
- Web Scraping
- Developer Tools
website: https://croxy.com/
---
