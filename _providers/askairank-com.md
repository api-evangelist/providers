---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AskAiRank platform, providing endpoints for AI visibility tracking and analytics.
  name: AskAiRank API
  slug: askairank-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/askairank-com/plans/askairank-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askairank-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/askairank-com/llms/askairank-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askairank-com-llms.txt
- group: other
  href: https://artifacts.apis.io/askairank-com/hosts/askairank-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askairank-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/askairank-com/vendors/askairank-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askairank-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askairank.com/terms
- group: start
  title: ''
  type: Sandbox
  url: https://help.askairank.com/articles/playground/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askairank.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://askairank.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.askairank.com/auth/login
- group: company
  title: ''
  type: Blog
  url: https://askairank.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.askairank.com/articles/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://help.askairank.com/
- group: auth
  href: https://artifacts.apis.io/askairank-com/security/askairank-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askairank-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askairank.com/
coverage:
  checked: '2026-11-03'
  detail: Documentation is public HTML but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 0
    url: https://api.askairank.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AskAiRank provides an AI Visibility Tracker platform for SaaS founders and marketers, enabling them to monitor how their brand appears across AI-powered search and chat interfaces such as ChatGPT, Google AI, and other large language model platforms. The service offers product features like AI visibility tracking, brand monitoring, citation tracking, competitor analysis, and website scanning, with a free 3‑day trial followed by paid plans starting at $19 per month. The platform aims to help companies understand and improve their AI-driven discoverability and reputation.
image: https://askairank.com/og/default.png
layout: provider
modified: '2026-11-01'
name: AskAiRank
nav: Providers
network: true
overview: 'AskAiRank is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Software-as-a-Service, Marketing, Visibility, and Analytics.


  AskAiRank''s developer surface includes sandbox, pricing, engineering blog, getting-started guide, documentation, and 9 more developer resources.'
plans:
- name: Askairank Com Plans Pricing
  plan_count: 4
  slug: askairank-com-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 26.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askairank Com Domain Security
  slug: askairank-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askairank-com
tags:
- Artificial Intelligence
- Software-as-a-Service
- Marketing
- Visibility
- Analytics
- Company
website: https://askairank.com/
---
