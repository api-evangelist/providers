---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://grandet.ai
  baseurl_source: declared
  description: Public listed declarations, independent currencies, original observations.
  name: Grandet Anonymous Price Discovery API
  slug: grandet-anonymous-price-discovery-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/grandet-ai/conformance/grandet-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/grandet-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/grandet-ai/llms/grandet-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grandet-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/grandet-ai/hosts/grandet-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/grandet-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/grandet-ai/vendors/grandet-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/grandet-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://grandet.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grandet.ai/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://grandet.ai/docs/quick-start/
- group: docs
  title: ''
  type: APIReference
  url: https://grandet.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/grandet-ai/security/grandet-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grandet-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grandet.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://grandet.ai/wiki/
- group: operate
  title: ''
  type: Support
  url: https://grandet.ai/community/
- group: commercial
  title: ''
  type: Pricing
  url: https://grandet.ai/price-finder.md
created: '2026-10-30'
description: Grandet AI provides a comprehensive ranking and pricing comparison platform for large language model (LLM) APIs. It aggregates public pricing data from thousands of providers, offers free token information, and supplies a skill for AI assistants to query model costs directly. The site includes a product wiki, model leaderboard, and downloadable skill, serving developers and businesses looking to optimize LLM usage and costs.
image: https://grandet.ai/images/grandet-ranking-card.png
layout: provider
modified: '2026-10-30'
name: grandet-ai
nav: Providers
network: true
overview: 'grandet-ai is listed with 1 API on the [APIs.io](https://apis.io/) network: Grandet Anonymous Price Discovery API. Tagged areas include Company, AI, LLM, Pricing, and Data.


  grandet-ai''s developer surface includes getting-started guide, API reference, documentation, support, pricing, and 8 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 16.4
    contract_quality: 30.5
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Grandet Ai Domain Security
  slug: grandet-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: grandet-ai
tags:
- Company
- AI
- LLM
- Pricing
- Data
website: https://grandet.ai/
---
