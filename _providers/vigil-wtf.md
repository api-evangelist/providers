---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.vigil.wtf
  baseurl_source: declared
  description: A pass-through proxy for AI provider APIs. Requests to https://api.vigil.wtf/{user_id}/{provider}/{path} are forwarded to the named provider and the provider's response is returned, with Vigil's reque
  name: Vigil Proxy
  slug: vigil-wtf-vigil-proxy-api
- baseURL: https://api.vigil.wtf
  baseurl_source: declared
  description: Send a score from 1 to 5 for one of your proxied calls, keyed by Vigil's request id (POST /v1/feedback); a later score for the same request replaces the earlier one.
  name: Vigil Feedback API
  slug: vigil-wtf-feedback-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/vigil-wtf/plans/vigil-wtf-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vigil-wtf-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/vigil-wtf/authentication/vigil-wtf-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vigil-wtf-authentication.yml
- group: other
  href: https://artifacts.apis.io/vigil-wtf/hosts/vigil-wtf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vigil-wtf-hosts.yml
- group: other
  href: https://artifacts.apis.io/vigil-wtf/vendors/vigil-wtf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vigil-wtf-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vigil.wtf/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vigil.wtf/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vigil.wtf/pricing
- group: start
  title: ''
  type: Login
  url: https://www.vigil.wtf/auth/login
- group: company
  title: ''
  type: Blog
  url: https://www.vigil.wtf/blog
- group: auth
  href: https://artifacts.apis.io/vigil-wtf/security/vigil-wtf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vigil-wtf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vigil.wtf
- group: docs
  title: ''
  type: Documentation
  url: https://www.vigil.wtf/docs
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.vigil.wtf/llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.vigil.wtf/changelog
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.vigil.wtf/.well-known/security.txt
coverage:
  checked: '2026-10-02'
  detail: API root returns 400 errors and no OpenAPI or docs are available.
  evidence:
  - status: 400
    url: https://api.vigil.wtf
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Vigil offers a token‑optimisation and cost‑monitoring proxy for large‑language‑model APIs. It aggregates calls to frontier models, providing per‑call latency, error tracking, and token‑usage analytics, enabling developers to manage expenses and performance across multiple providers.
image: https://www.vigil.wtf/opengraph-image
layout: provider
modified: '2026-10-05'
name: Vigil
nav: Providers
network: true
overview: 'Vigil publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Proxy and Feedback API. Tagged areas include Monitoring, AI Middleware, Security, and Analytics.


  The Vigil catalog on APIs.io includes 1 Spectral governance ruleset.


  Vigil''s developer surface includes authentication, pricing, engineering blog, documentation, changelog, and 10 more developer resources.'
plans:
- name: Vigil Wtf Plans Pricing
  plan_count: 1
  slug: vigil-wtf-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Vigil API Rules
  rule_count: 46
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 2
  slug: vigil-wtf-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 44.5
    catalog_earned_first_party: 8.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 43.4
    contract_governance: 13.6
    contract_quality: 49.3
    developer_ergonomics: 17.9
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 41.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vigil-wtf/vigil-wtf-2026-10-11T133003.png
security:
- kind: authentication
  name: Vigil Wtf Authentication
  slug: vigil-wtf-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Vigil Wtf Domain Security
  slug: vigil-wtf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vigil-wtf
tags:
- Monitoring
- AI Middleware
- Security
- Analytics
website: https://www.vigil.wtf
---
