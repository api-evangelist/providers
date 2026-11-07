---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AgentCDN account and public APIs for video management and AI access
  name: AgentCDN API
  slug: agentcdn-api
artifact_total: 6
asyncapis:
- description: ''
  name: Agentcdn Com Webhooks
  slug: agentcdn-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/agentcdn-com/plans/agentcdn-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentcdn-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentcdn-com/asyncapi/agentcdn-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agentcdn-com-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/agentcdn-com/security/agentcdn-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentcdn-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentcdn-com/authentication/agentcdn-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentcdn-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentcdn-com/conformance/agentcdn-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentcdn-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentcdn-com/llms/agentcdn-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentcdn-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agentcdn-com/a2a/agentcdn-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentcdn-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentcdn-com/well-known/agentcdn-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentcdn-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentcdn-com/hosts/agentcdn-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentcdn-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentcdn-com/vendors/agentcdn-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentcdn-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://agentcdn.com/media
- group: start
  title: ''
  type: Login
  url: https://app.agentcdn.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.agentcdn.com`
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentcdn.com/api-reference/overview
- group: auth
  href: https://artifacts.apis.io/agentcdn-com/security/agentcdn-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentcdn-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentcdn-com/security/agentcdn-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentcdn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentcdn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentcdn.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentcdn.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentcdn.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://agentcdn.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentcdn.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentcdn.com/terms
created: '2026-10-31'
description: AgentCDN provides a platform that makes video libraries usable by AI assistants. Their solution enables AI applications like ChatGPT or Claude to retrieve and play specific video segments in response to user queries, enhancing content accessibility and interaction. The service offers tools for video understanding, geo-targeting, SEO, and integration via APIs, targeting creators, brands, and developers looking to embed video intelligence into their products.
image: https://agentcdn.com/og/home.png
layout: provider
modified: '2026-10-31'
name: AgentCDN
nav: Providers
network: true
overview: 'AgentCDN is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Artificial Intelligence, Platform, Media, and Integration.


  The AgentCDN catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AgentCDN''s developer surface includes authentication, API reference, documentation, pricing, getting-started guide, support, and 17 more developer resources.'
plans:
- name: Agentcdn Com Plans Pricing
  plan_count: 3
  slug: agentcdn-com-plans-pricing
random_paper: 0
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 33.3
    discoverability: 67.0
    operational_transparency: 18.4
  previous_composite: 47.7
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentcdn Com Authentication
  slug: agentcdn-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentcdn Com Domain Security
  slug: agentcdn-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentcdn Com Vulnerability Disclosure
  slug: agentcdn-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: agentcdn-com
tags:
- Video
- Artificial Intelligence
- Platform
- Media
- Integration
- Company
website: https://agentcdn.com/
---
