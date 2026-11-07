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
    agent_card: conformant
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only API exposing published homes and travel‑related data.
  name: Chucho public property discovery
  slug: chucho-public-property-discovery
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/chucho-ai/plans/chucho-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chucho-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chucho-ai/conformance/chucho-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chucho-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chucho-ai/llms/chucho-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chucho-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/chucho-ai/a2a/chucho-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chucho-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/chucho-ai/well-known/chucho-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chucho-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/chucho-ai/hosts/chucho-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chucho-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/chucho-ai/vendors/chucho-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chucho-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chucho.ai/muse/terms/
- group: operate
  title: ''
  type: Support
  url: https://chucho.ai/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chucho.ai/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://chucho.ai/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://chucho.ai/guides/
- group: company
  title: ''
  type: Blog
  url: https://chucho.ai/blog/en
- group: docs
  title: ''
  type: APIReference
  url: https://chucho.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/chucho-ai/security/chucho-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chucho-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chucho.ai/
created: '2026-11-03'
description: Chucho provides digital guest guides for vacation rentals, enabling hosts to offer multilingual, AI‑enhanced information to their guests. The platform lets property owners create free public listings, customize guide content, and compare plans for their properties, improving guest experience and operational efficiency.
image: https://chucho.ai/assets/og-card.jpg?v=9
layout: provider
modified: '2026-11-03'
name: Chucho
nav: Providers
network: true
overview: 'Chucho is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vacation Rentals, Guest Guides, Hospitality, and Artificial Intelligence.


  Chucho''s developer surface includes support, pricing, documentation, engineering blog, API reference, and 11 more developer resources.'
plans:
- name: Chucho Ai Plans Pricing
  plan_count: 3
  slug: chucho-ai-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chucho Ai Domain Security
  slug: chucho-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chucho-ai
tags:
- Company
- Vacation Rentals
- Guest Guides
- Hospitality
- Artificial Intelligence
website: https://chucho.ai/
---
