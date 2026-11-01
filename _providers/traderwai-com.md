---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for TraderWAI platform connecting AI models to brokerage accounts, documented at the developer portal.
  name: TraderWAI API
  slug: traderwai-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/traderwai-com/llms/traderwai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/traderwai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/traderwai-com/hosts/traderwai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/traderwai-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://traderwai.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://traderwai.com/en/privacy
- group: start
  title: ''
  type: Login
  url: https://traderwai.com/en/login
- group: auth
  href: https://artifacts.apis.io/traderwai-com/security/traderwai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/traderwai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://traderwai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://traderwai.com/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://traderwai.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://traderwai.com/en/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://traderwai.com/en/status
- group: start
  title: ''
  type: DeveloperPortal
  url: https://traderwai.com/en
coverage:
  checked: '2026-10-30'
  detail: Documentation is a JavaScript-rendered site with no accessible OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://traderwai.com/en/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: TraderWAI provides a platform that connects large language model AIs such as Claude, ChatGPT, Gemini, and others directly to users' brokerage accounts, enabling AI-driven analysis, order suggestions, and automated execution with user-defined risk controls. The service offers a free forever plan, no credit-card required, and supports multiple brokers. It includes documentation, pricing details, a blog, investor information, and a status page, all accessible via its website.
layout: provider
modified: '2026-10-30'
name: traderwai-com
nav: Providers
network: true
overview: 'traderwai-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Trading, Brokerage, Automation, and Platform.


  traderwai-com''s developer surface includes documentation, pricing, engineering blog, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 12.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Traderwai Com Domain Security
  slug: traderwai-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: traderwai-com
tags:
- AI
- Trading
- Brokerage
- Automation
- Platform
website: https://traderwai.com/
---
