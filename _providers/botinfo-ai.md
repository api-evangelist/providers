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
- description: Robotics lead intelligence API providing robot market data.
  name: BotInfo AI API
  slug: botinfo-ai-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/botinfo-ai/llms/botinfo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botinfo-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/botinfo-ai/vendors/botinfo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botinfo-ai-vendors.yml
- group: other
  href: https://artifacts.apis.io/botinfo-ai/hosts/botinfo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botinfo-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botinfo.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botinfo.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://botinfo.ai/
- group: auth
  href: https://artifacts.apis.io/botinfo-ai/security/botinfo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botinfo-ai-domain-security.yml
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://botinfo.ai/openapi.json
  - status: 404
    url: https://api.botinfo.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BotInfo AI provides dated, checkout‑verified US prices, availability and legal status for humanoid robots and robot dogs. The site publishes detailed pricing data for Unitree humanoids and the programmable Go2 EDU, with licensing required for commercial use of the data. It serves as a data source for developers and analysts interested in robotics market information.
image: https://cdn.prod.website-files.com/663e2d5c1f3e68f94da70063/67052f443299df6feb4316ba_Frame%202(1).png
layout: provider
modified: '2026-11-02'
name: BotInfo AI
nav: Providers
network: true
overview: BotInfo AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Lead Intelligence, Market Intelligence, and Referral Service.
random_paper: 16
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
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
  name: Botinfo Ai Domain Security
  slug: botinfo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: botinfo-ai
tags:
- Lead Intelligence
- Market Intelligence
- Referral Service
website: https://botinfo.ai/
---
