---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: true
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
    delegated_identity: false
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Ad specs, campaign objectives and optimization goals, platform differences, glossary, and frequently asked questions.
  name: Adsap API
  slug: adsap-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/adsap-ai/plans/adsap-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adsap-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adsap-ai/llms/adsap-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adsap-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/adsap-ai/well-known/adsap-ai-calendly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adsap-ai-calendly-security.txt
- group: agent
  href: https://artifacts.apis.io/adsap-ai/well-known/adsap-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adsap-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adsap-ai/hosts/adsap-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adsap-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adsap-ai/vendors/adsap-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adsap-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adsap-ai/security/adsap-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adsap-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adsap.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://adsap.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://adsap.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://adsap.ai/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://adsap.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://adsap.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.adsap.ai/auth?tab=signup
- group: start
  title: ''
  type: Login
  url: https://app.adsap.ai/auth?tab=signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adsap.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adsap.ai/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.adsap.ai/
coverage:
  checked: '2026-11-01'
  detail: Public documentation exists but no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other spec is published.
  evidence:
  - status: 200
    url: https://adsap.ai/docs/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Adsap provides a platform to launch and manage Meta (Facebook) and Google advertising campaigns at scale. Users can create bulk ads via a web dashboard or an AI copilot integrated with Claude, ChatGPT, or Perplexity, leveraging about 100 built‑in tools. All changes require user approval, ensuring control while automating repetitive tasks for e‑commerce brands and agencies.
image: https://adsap.ai/opengraph-image?e7a2f4b915cb0007
layout: provider
modified: '2026-10-31'
name: Adsap
nav: Providers
network: true
overview: 'Adsap is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Automation, Artificial Intelligence, Software-as-a-Service, and Marketing.


  Adsap''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Adsap Ai Plans Pricing
  plan_count: 2
  slug: adsap-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Adsap Ai Rate Limits
  slug: adsap-ai-rate-limits
scopes:
- name: Adsap Ai Scopes
  scope_count: 0
  slug: adsap-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 30.2
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
  name: Adsap Ai Authentication
  slug: adsap-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adsap Ai Domain Security
  slug: adsap-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adsap-ai
tags:
- Advertising
- Automation
- Artificial Intelligence
- Software-as-a-Service
- Marketing
website: https://adsap.ai/
---
