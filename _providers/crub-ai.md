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
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/crub-ai/plans/crub-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crub-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/crub-ai/llms/crub-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crub-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/crub-ai/well-known/crub-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crub-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/crub-ai/hosts/crub-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crub-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/crub-ai/vendors/crub-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crub-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crub.ai/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://crub.ai/help
- group: auth
  title: ''
  type: Security
  url: https://crub.ai/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crub.ai/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://crub.ai/pricing
- group: auth
  href: https://artifacts.apis.io/crub-ai/security/crub-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crub-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crub-ai/security/crub-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crub-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crub.ai/
created: '2026-11-04'
description: Crub provides an AI-powered plant, mushroom, and insect identification service, offering confidence-matched results from a curated library of over 150,000 species. Users can map their gardens, receive care recommendations, and integrate the service via its Model Context Protocol. The platform combines computer vision with extensive botanical data to help gardeners, researchers, and hobbyists accurately identify flora and fauna.
image: https://crub.ai/opengraph-image?44824a1bfedb81cb
layout: provider
modified: '2026-11-04'
name: Crub
nav: Providers
network: true
overview: 'Crub is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Plant Identification, Gardening, Computer Vision, and Botany.


  Crub''s developer surface includes support, pricing, and 11 more developer resources.'
plans:
- name: Crub Ai Plans Pricing
  plan_count: 3
  slug: crub-ai-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Crub Ai Domain Security
  slug: crub-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Crub Ai Vulnerability Disclosure
  slug: crub-ai-vulnerability-disclosure
  summary_line: no policy recorded
slug: crub-ai
tags:
- Artificial Intelligence
- Plant Identification
- Gardening
- Computer Vision
- Botany
- Company
website: https://crub.ai/
---
