---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Eventuate Agentic Access
  operation_count: 10
  slug: eventuate-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The Entities API from Eventuate — 2 operation(s) for entities.
  name: Eventuate Entities API
  slug: eventuate-entities-api
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The Events API from Eventuate — 1 operation(s) for events.
  name: Eventuate Events API
  slug: eventuate-events-api
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The Subscriptions API from Eventuate — 4 operation(s) for subscriptions.
  name: Eventuate Subscriptions API
  slug: eventuate-subscriptions-api
- baseURL_template: '{baseUrl}'
  baseurl_source: spec_template
  description: The System API from Eventuate — 1 operation(s) for system.
  name: Eventuate System API
  slug: eventuate-system-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Eventuate REST API
  slug: open-eventuate-api
- collection_type: open
  name: Eventuate REST Entities API
  slug: open-eventuate-entities-api
- collection_type: open
  name: Eventuate REST Entities Events API
  slug: open-eventuate-events-api
- collection_type: open
  name: Eventuate REST Entities Subscriptions API
  slug: open-eventuate-subscriptions-api
- collection_type: open
  name: Eventuate REST Entities System API
  slug: open-eventuate-system-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eventuate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eventuate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eventuate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://eventuate.io/docs/general/getting-started.html
- group: start
  title: ''
  type: GettingStarted
  url: https://eventuate.io/exampleapps.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/eventuate-tram
- group: company
  title: ''
  type: Blog
  url: https://eventuate.io/news.html
created: '2026-03-26'
description: Eventuate is a platform for developing transactional microservices using event sourcing and CQRS patterns, providing frameworks for managing distributed data consistency across services without two-phase commit.
finops:
- name: Eventuate Finops
  service_category: API
  slug: eventuate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eventuate.png
layout: provider
modified: '2026-05-19'
name: Eventuate
nav: Providers
network: true
overview: 'Eventuate publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Entities API, Events API, Subscriptions API, and 1 more. Tagged areas include CQRS, Distributed Data, Event Sourcing, Event-Driven, and Microservices.


  Eventuate''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, and 3 more developer resources.'
plans:
- name: Eventuate Plans Pricing
  plan_count: 3
  slug: eventuate-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Eventuate Rate Limits
  slug: eventuate-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 46.8
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eventuate/refs/heads/main/screenshots/eventuate-2026-06-20T180901.png
security:
- kind: domain-security
  name: Eventuate Domain Security
  slug: eventuate-domain-security
  summary_line: TLSv1.3
slug: eventuate
tags:
- CQRS
- Distributed Data
- Event Sourcing
- Event-Driven
- Microservices
- Sagas
website: https://eventuate.io/
---
