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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for DripRaven messaging platform, enabling programmatic access to campaigns, contacts and messaging channels.
  name: DripRaven API
  slug: dripraven-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dripraven-com/llms/dripraven-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dripraven-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dripraven-com/well-known/dripraven-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dripraven-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dripraven-com/hosts/dripraven-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dripraven-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/dripraven-com/packages/dripraven-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dripraven-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dripraven-com/packages/dripraven-com-packages.yml
  title: ''
  type: Packages
  url: packages/dripraven-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dripraven.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dripraven.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://dripraven.com/blog
- group: auth
  href: https://artifacts.apis.io/dripraven-com/security/dripraven-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dripraven-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dripraven.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.dripraven.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://app.dripraven.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dripraven.com/#pricing
coverage:
  checked: '2026-11-06'
  detail: API endpoints require authentication, preventing public contract discovery.
  evidence:
  - status: 0
    url: https://api.dripraven.com/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-05'
description: DripRaven provides AI‑powered messaging campaign tools, enabling WhatsApp, SMS and future channels directly from AI assistants like ChatGPT and Claude. Users can import contacts, build segments, and launch campaigns via chat, with a focus on seamless integration and automation.
image: https://dripraven.com/opengraph-image?1b41765b58d8e584
layout: provider
modified: '2026-11-05'
name: DripRaven
nav: Providers
network: true
overview: 'DripRaven is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, Artificial Intelligence, Automation, WhatsApp, and ChatGPT.


  DripRaven''s developer surface includes engineering blog, getting-started guide, pricing, and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dripraven Com Domain Security
  slug: dripraven-com-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: dripraven-com
tags:
- Messaging
- Artificial Intelligence
- Automation
- WhatsApp
- ChatGPT
website: https://dripraven.com/
---
