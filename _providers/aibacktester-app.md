---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Guides: backtesting trading strategies honestly — AI Backtester'
  name: AI Backtester API
  slug: ai-backtester-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/aibacktester-app/plans/aibacktester-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aibacktester-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aibacktester-app/well-known/aibacktester-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aibacktester-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/aibacktester-app/hosts/aibacktester-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aibacktester-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aibacktester-app/vendors/aibacktester-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aibacktester-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aibacktester-app/security/aibacktester-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aibacktester-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aibacktester.app/
- group: docs
  title: ''
  type: Documentation
  url: https://aibacktester.app/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://aibacktester.app/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://aibacktester.app/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://aibacktester.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://aibacktester.app/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aibacktester.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aibacktester.app/privacy
coverage:
  checked: '2026-11-01'
  detail: MCP endpoint /mcp returns 401 Unauthorized, indicating the API is gated behind authentication.
  evidence:
  - status: 401
    url: https://aibacktester.app/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: AI Backtester provides free AI-powered backtesting for crypto trading strategies, allowing users to describe strategies in plain English and receive detailed performance reports instantly.
image: https://aibacktester.app/opengraph-image?8f39ac4e81534478
layout: provider
modified: '2026-11-01'
name: AI Backtester
nav: Providers
network: true
overview: 'AI Backtester is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Cryptocurrency, Backtesting, Finance, and Automation.


  AI Backtester''s developer surface includes documentation, getting-started guide, support, pricing, signup flow, and 8 more developer resources.'
plans:
- name: Aibacktester App Plans Pricing
  plan_count: 2
  slug: aibacktester-app-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Aibacktester App Rate Limits
  slug: aibacktester-app-rate-limits
scopes:
- name: Aibacktester App Scopes
  scope_count: 0
  slug: aibacktester-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 25.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aibacktester App Authentication
  slug: aibacktester-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aibacktester App Domain Security
  slug: aibacktester-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aibacktester-app
tags:
- Artificial Intelligence
- Cryptocurrency
- Backtesting
- Finance
- Automation
website: https://aibacktester.app/
---
