---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/ask-recipes/plans/ask-recipes-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ask-recipes-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/ask-recipes/llms/ask-recipes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ask-recipes-llms.txt
- group: agent
  href: https://artifacts.apis.io/ask-recipes/well-known/ask-recipes-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ask-recipes-well-known.yml
- group: other
  href: https://artifacts.apis.io/ask-recipes/hosts/ask-recipes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ask-recipes-hosts.yml
- group: other
  href: https://artifacts.apis.io/ask-recipes/vendors/ask-recipes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ask-recipes-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ask-recipes/security/ask-recipes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ask-recipes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ask.recipes/
- group: docs
  title: ''
  type: Documentation
  url: https://ask.recipes/docs
- group: docs
  title: ''
  type: Guides
  url: https://ask.recipes/guides
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ask.recipes/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ask.recipes/terms
coverage:
  checked: '2026-11-01'
  detail: Documentation pages exist but no machine-readable API contract was found.
  evidence:
  - status: 200
    url: https://ask.recipes/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: 'ask-recipes is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://ask.recipes/icon-512.png
layout: provider
modified: '2026-11-01'
name: Ask Recipes
nav: Providers
network: true
overview: 'Ask Recipes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI cooking assistant and Recipe Search.


  Ask Recipes'' developer surface includes documentation and 10 more developer resources.'
plans:
- name: Ask Recipes Plans Pricing
  plan_count: 1
  slug: ask-recipes-plans-pricing
random_paper: 7
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 8.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 30.4
    operational_transparency: 0.0
  previous_composite: 14.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ask Recipes Domain Security
  slug: ask-recipes-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ask-recipes
tags:
- AI cooking assistant
- Recipe Search
website: https://ask.recipes/
---
