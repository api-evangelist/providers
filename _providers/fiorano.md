---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/fiorano/authentication/fiorano-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fiorano-authentication.yml
- group: agent
  href: https://artifacts.apis.io/fiorano/llms/fiorano-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fiorano-llms.txt
- group: other
  href: https://artifacts.apis.io/fiorano/hosts/fiorano-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fiorano-hosts.yml
- group: auth
  href: https://artifacts.apis.io/fiorano/security/fiorano-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fiorano-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fiorano.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fiorano.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.fiorano.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.fiorano.com/developers
- group: operate
  title: ''
  type: Support
  url: https://support.fiorano.com
- group: company
  title: ''
  type: Blog
  url: https://www.fiorano.com/blogs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fiorano.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fiorano.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fiorano.com/privacy
coverage:
  checked: '2026-10-20'
  detail: Developer pages return HTML only with no OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.fiorano.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Fiorano Software provides a hybrid integration platform and API management solutions for enterprises. Their suite includes Fiorano Integration Platform, API Management, FioranoMQ, and B2B integration, enabling real‑time data flow, microservices orchestration, and secure messaging across on‑premise and cloud environments. The company serves industries such as banking, healthcare, logistics, and energy, offering robust tools for digital transformation and enterprise connectivity.
image: https://www.fiorano.com/assets/images/common/Fiorano-logo-share.jpg
layout: provider
modified: '2026-10-20'
name: Fiorano Software
nav: Providers
network: true
overview: 'Fiorano Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, API Management, Enterprise, and Messaging.


  Fiorano Software''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 6 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Fiorano Authentication
  slug: fiorano-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Fiorano Domain Security
  slug: fiorano-domain-security
  summary_line: TLSv1.2 · DMARC
slug: fiorano
tags:
- Company
- Integration
- API Management
- Enterprise
- Messaging
website: https://fiorano.com/
---
