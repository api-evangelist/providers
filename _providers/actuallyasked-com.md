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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: docs
  title: ''
  type: Documentation
  url: https://actuallyasked.com/guides
- group: commercial
  href: https://artifacts.apis.io/actuallyasked-com/plans/actuallyasked-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/actuallyasked-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/actuallyasked-com/llms/actuallyasked-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/actuallyasked-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/actuallyasked-com/well-known/actuallyasked-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/actuallyasked-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/actuallyasked-com/hosts/actuallyasked-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actuallyasked-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/actuallyasked-com/security/actuallyasked-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actuallyasked-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actuallyasked.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://actuallyasked.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://actuallyasked.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://actuallyasked.com/privacy
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.actuallyasked.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Actually Asked provides an AI-powered FAQ solution for websites and Shopify stores, enabling inline FAQs, highlighted text queries, self‑improving knowledge bases, weekly gap reports, lead capture, and a suite of free tools such as FAQ gap finder and llms.txt generator. The platform integrates with major site builders like Shopify, WordPress, Webflow, Framer, Squarespace, and supports AI assistants including Claude, ChatGPT, Cursor, and Codex. It offers a free tier with up to 50 AI answers per month and paid plans for higher usage.
image: https://actuallyasked.com/assets/share/home-8f358d0d.png
layout: provider
modified: '2026-10-31'
name: Actually Asked
nav: Providers
network: true
overview: 'Actually Asked is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, FAQ, Shopify, Integration, and Software-as-a-Service.


  Actually Asked''s developer surface includes documentation, pricing, and 8 more developer resources.'
plans:
- name: Actuallyasked Com Plans Pricing
  plan_count: 4
  slug: actuallyasked-com-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Actuallyasked Com Rate Limits
  slug: actuallyasked-com-rate-limits
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 19.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Actuallyasked Com Domain Security
  slug: actuallyasked-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: actuallyasked-com
tags:
- Artificial Intelligence
- FAQ
- Shopify
- Integration
- Software-as-a-Service
- Company
website: https://actuallyasked.com/
---
