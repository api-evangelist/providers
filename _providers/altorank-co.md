---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AltoRank MCP Server provides a REST API for AI agents to interact with AltoRank services. Documentation at the API reference page.
  name: MCP Server API
  slug: mcp-server-api
artifact_total: 4
asyncapis:
- description: ''
  name: Altorank Co Webhooks
  slug: altorank-co-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/altorank-co/plans/altorank-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/altorank-co-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/altorank-co/asyncapi/altorank-co-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/altorank-co-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/altorank-co/llms/altorank-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/altorank-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/altorank-co/well-known/altorank-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altorank-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/altorank-co/hosts/altorank-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altorank-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/altorank-co/vendors/altorank-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altorank-co-vendors.yml
- group: auth
  href: https://artifacts.apis.io/altorank-co/security/altorank-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altorank-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altorank.co/
- group: docs
  title: ''
  type: Documentation
  url: https://altorank.co/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://altorank.co/docs/mcp/
- group: commercial
  title: ''
  type: Pricing
  url: https://altorank.co/pricing/
- group: company
  title: ''
  type: Blog
  url: https://altorank.co/blog/
- group: operate
  title: ''
  type: Support
  url: https://altorank.co/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altorank.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altorank.co/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://altorank.co/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://altorank.co/docs/mcp/
coverage:
  checked: '2026-11-01'
  detail: Docs are rendered via JavaScript and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://altorank.co/docs/mcp/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AltoRank provides AI‑powered SEO content generation and optimization tools. It helps businesses turn search queries into high‑quality articles, offering keyword research, AI writing, editorial review, and integration with popular platforms like WordPress and Shopify. The service includes a free tier, paid growth plans, and open‑source components, aiming to improve website visibility and ranking on Google.
image: https://altorank.co/og-default.png
layout: provider
modified: '2026-11-01'
name: AltoRank
nav: Providers
network: true
overview: 'AltoRank is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, Artificial Intelligence, Content Generation, Marketing, and Software-as-a-Service.


  The AltoRank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AltoRank''s developer surface includes documentation, API reference, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Altorank Co Plans Pricing
  plan_count: 3
  slug: altorank-co-plans-pricing
random_paper: 11
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 34.4
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Altorank Co Domain Security
  slug: altorank-co-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: altorank-co
tags:
- SEO
- Artificial Intelligence
- Content Generation
- Marketing
- Software-as-a-Service
- Automation
website: https://altorank.co/
---
