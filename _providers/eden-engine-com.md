---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  score: 5.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/eden-engine-com/plans/eden-engine-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eden-engine-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/eden-engine-com/security/eden-engine-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/eden-engine-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/eden-engine-com/authentication/eden-engine-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eden-engine-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/eden-engine-com/llms/eden-engine-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eden-engine-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/eden-engine-com/well-known/eden-engine-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/eden-engine-com-security.txt
- group: auth
  href: https://artifacts.apis.io/eden-engine-com/well-known/eden-engine-com-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/eden-engine-com-mcp-security.txt
- group: agent
  href: https://artifacts.apis.io/eden-engine-com/well-known/eden-engine-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eden-engine-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/eden-engine-com/hosts/eden-engine-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eden-engine-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/eden-engine-com/vendors/eden-engine-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eden-engine-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eden-engine.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://eden-engine.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eden-engine.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://eden-engine.com/pricing
- group: start
  title: ''
  type: Login
  url: https://eden-engine.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://eden-engine.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://eden-engine.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://eden-engine.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/eden-engine-com/security/eden-engine-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/eden-engine-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/eden-engine-com/security/eden-engine-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eden-engine-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eden-engine.com/
coverage:
  checked: '2026-11-06'
  detail: Developer portal pages are JavaScript-rendered single-page apps, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://eden-engine.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: Eden Engine lets your AI assistant research, look things up and pull data for you. One balance, no subscription, and you pay only when it runs. It provides a simple interface for AI tools to perform real‑world tasks, turning language model output into actionable results without hidden fees.
image: https://eden-engine.com/brand/og.png
layout: provider
modified: '2026-11-06'
name: Eden Engine
nav: Providers
network: true
overview: 'Eden Engine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Assistant, Productivity, Software-as-a-Service, and Company.


  Eden Engine''s developer surface includes authentication, pricing, documentation, API reference, and 16 more developer resources.'
plans:
- name: Eden Engine Com Plans Pricing
  plan_count: 8
  slug: eden-engine-com-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Eden Engine Com Authentication
  slug: eden-engine-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Eden Engine Com Domain Security
  slug: eden-engine-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eden Engine Com Vulnerability Disclosure
  slug: eden-engine-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: eden-engine-com
tags:
- Artificial Intelligence
- Assistant
- Productivity
- Software-as-a-Service
- Company
website: https://eden-engine.com/
---
