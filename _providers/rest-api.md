---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rest-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://restfulapi.net
- group: docs
  title: ''
  type: Reference
  url: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
- group: docs
  title: ''
  type: Guide
  url: https://www.freecodecamp.org/news/build-consume-and-document-a-rest-api/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rest-api/refs/heads/main/vocabulary/rest-api-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rest-api/refs/heads/main/json-ld/rest-api-context.jsonld
created: '2025-01-01'
description: Representational State Transfer (REST) is an architectural style for designing networked applications using standard HTTP methods and stateless communication between client and server. REST APIs define how client and server applications communicate over the web using GET, POST, PUT, DELETE, and PATCH methods against resource-oriented URLs. REST is the dominant API paradigm, used by 89% of organisations as their primary API format. This index covers the REST API landscape including specifications, tools, frameworks, best practices, and educational resources.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rest-api.png
jsonld:
- class_count: 5
  name: Rest Api Context
  property_count: 13
  slug: rest-api-context
layout: provider
modified: '2026-05-02'
name: REST API
nav: Providers
network: true
overview: 'REST API is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, HTTP, Web Services, REST, and API Design.


  The REST API catalog on APIs.io includes 1 JSON-LD context.'
random_paper: 7
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 15.2
    contract_quality: 14.7
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 15.2
    operational_transparency: 0.0
  previous_composite: 11.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rest-api/refs/heads/main/screenshots/rest-api-2026-06-20T192956.png
security:
- kind: domain-security
  name: Rest Api Domain Security
  slug: rest-api-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rest-api
tags:
- Architecture
- HTTP
- Web Services
- REST
- API Design
website: https://restfulapi.net
---
