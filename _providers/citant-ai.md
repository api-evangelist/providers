---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    dynamic_client_registration: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/citant-ai/plans/citant-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/citant-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/citant-ai/llms/citant-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citant-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/citant-ai/well-known/citant-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citant-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/citant-ai/hosts/citant-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citant-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/citant-ai/vendors/citant-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citant-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/citant-ai/security/citant-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citant-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citant.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://citant.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://citant.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citant.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citant.ai/privacy/
- group: operate
  title: ''
  type: Contact
  url: https://citant.ai/contact/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://citant.ai/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Citant.ai is a Generative Engine Optimization (GEO) agency focused on boosting B2B SaaS visibility in large language model (LLM) search results. They offer a 9‑week citation guarantee, promising to place your SaaS product in AI‑generated answers or refund the pilot payment. Services include AI‑driven SEO, citation management, and strategic content creation to improve AI citation rankings, targeting enterprises seeking AI‑enhanced discoverability.
image: https://citant.ai/wp-content/uploads/2026/10/citant-homepage-og-1200x630-1.png
layout: provider
modified: '2026-11-03'
name: Citant.ai
nav: Providers
network: true
overview: 'Citant.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Geo, SEO, B2B, and Software-as-a-Service.


  Citant.ai''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Citant Ai Plans Pricing
  plan_count: 3
  slug: citant-ai-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Citant Ai Domain Security
  slug: citant-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: citant-ai
tags:
- Artificial Intelligence
- Geo
- SEO
- B2B
- Software-as-a-Service
website: https://citant.ai/
---
