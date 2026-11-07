---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 24.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Chrysai API provides AI‑powered database operations via the MCP protocol. Documentation is at the Getting Started page.
  name: Chrysai API
  slug: chrysai-api
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/chrysai-com/rate-limits/chrysai-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chrysai-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chrysai-com/plans/chrysai-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chrysai-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/chrysai-com/llms/chrysai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chrysai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/chrysai-com/well-known/chrysai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chrysai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/chrysai-com/hosts/chrysai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chrysai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chrysai-com/vendors/chrysai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chrysai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chrysai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chrysai.com/privacy
- group: auth
  href: https://artifacts.apis.io/chrysai-com/security/chrysai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chrysai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chrysai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.chrysai.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chrysai.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chrysai.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.chrysai.com/register
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://www.chrysai.com/api/mcp
  - status: 200
    url: https://chrysai.com/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Chrysai provides an AI‑powered platform that lets developers describe data models in natural language and automatically creates, manages, and queries databases via the MCP protocol. The service offers instant schema generation, CRUD operations, and a low‑code interface for building real data applications, positioning itself at the intersection of AI, databases, and low‑code development.
image: https://www.chrysai.com/og-image.png
layout: provider
modified: '2026-11-03'
name: Chrysai
nav: Providers
network: true
overview: 'Chrysai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Database, MCP, Low-Code, and Data.


  Chrysai''s developer surface includes documentation, pricing, getting-started guide, signup flow, and 10 more developer resources.'
plans:
- name: Chrysai Com Plans Pricing
  plan_count: 3
  slug: chrysai-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 6
  name: Chrysai Com Rate Limits
  slug: chrysai-com-rate-limits
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chrysai Com Domain Security
  slug: chrysai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chrysai-com
tags:
- Artificial Intelligence
- Database
- MCP
- Low-Code
- Data
website: https://chrysai.com/
---
