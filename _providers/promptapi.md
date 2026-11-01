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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/promptapi/llms/promptapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/promptapi-llms.txt
- group: other
  href: https://artifacts.apis.io/promptapi/hosts/promptapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptapi/vendors/promptapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptapi-vendors.yml
- group: auth
  href: https://artifacts.apis.io/promptapi/security/promptapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apilayer.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apilayer.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/
- group: operate
  title: ''
  type: Support
  url: https://apilayer.com/contact-us
created: '2026-10-21'
description: Prompt API is a product suite offered by APILayer, providing a collection of ready-to-use AI prompt generation APIs. It enables developers to integrate prompt-based AI capabilities such as text generation, classification, and transformation into applications with simple REST endpoints. The service includes extensive documentation, SDKs, and a unified API key for access, targeting use cases in content creation, chatbots, and automation across various industries.
image: https://apilayer.com/wp-content/uploads/2026/03/logo.png
layout: provider
modified: '2026-10-21'
name: Prompt API
nav: Providers
network: true
overview: 'Prompt API is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Prompt, API, Platform, and APILayer.


  Prompt API''s developer surface includes documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Promptapi Domain Security
  slug: promptapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: promptapi
tags:
- AI
- Prompt
- API
- Platform
- APILayer
website: https://promptapi.com/
---
