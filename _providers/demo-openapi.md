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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://search-api.apis.io/
  baseurl_source: declared
  description: Index of HTTP application programming interfaces.
  name: Manage OpenAPI via GitHub Demo APIs API
  slug: demo-openapi-apis-api
- baseURL: https://search-api.apis.io/
  baseurl_source: declared
  description: Search using a cloud search engine.
  name: Manage OpenAPI via GitHub Demo Search API
  slug: demo-openapi-search-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Technical Contract for the .io Search APIs API
  slug: open-demo-openapi-apis-api
- collection_type: open
  name: Technical Contract for the APIs.io Search API
  slug: open-demo-openapi-search-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demo-openapi-domain-security.yml
- group: company
  title: ''
  type: BlogPost
  url: https://github.com/api-evangelist/demo-openapi
- group: other
  title: ''
  type: CanonicalRepo
  url: https://github.com/api-evangelist/search-api
- group: other
  title: ''
  type: APIsIo
  url: https://apis.io
- group: other
  title: ''
  type: Developer
  url: https://developer.apis.io
- group: operate
  title: ''
  type: SupportEmail
  url: mailto:kin@apievangelist.com
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/demo-openapi-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/demo-openapi-context.jsonld
created: '2024-10-31'
description: This is a demo repository showing how GitHub can be used to manage an API contract using an APIs.json index plus an OpenAPI definition and supporting artifacts. The API used in the demo is the APIs.io Search API, which exposes search and submission endpoints over the APIs.io index. The repository is referenced by an API Evangelist blog post on managing OpenAPI in GitHub.
finops:
- name: Demo Openapi Finops
  service_category: API
  slug: demo-openapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/demo-openapi.png
jsonld:
- class_count: 2
  name: Demo Openapi Context
  property_count: 7
  slug: demo-openapi-context
layout: provider
modified: '2026-04-28'
name: Manage OpenAPI via GitHub Demo
nav: Providers
network: true
overview: 'Manage OpenAPI via GitHub Demo publishes 2 APIs on the [APIs.io](https://apis.io/) network: APIs API and Search API. Tagged areas include APIs.json, Demo, GitHub, OpenAPI, and Reference.


  The Manage OpenAPI via GitHub Demo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Demo Openapi Plans Pricing
  plan_count: 3
  slug: demo-openapi-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Demo Openapi Rate Limits
  slug: demo-openapi-rate-limits
rules:
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Manage OpenAPI via GitHub Demo API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: apis-io-search-api-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 71.0
    catalog_earned_first_party: 0.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 60.6
    contract_quality: 59.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 60.6
    operational_transparency: 7.9
  previous_composite: 33.3
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demo-openapi/refs/heads/main/screenshots/demo-openapi-2026-06-20T175908.png
security:
- kind: domain-security
  name: Demo Openapi Domain Security
  slug: demo-openapi-domain-security
  summary_line: TLSv1.3
slug: demo-openapi
tags:
- APIs.json
- Demo
- GitHub
- OpenAPI
- Reference
- Search
website: https://developer.apis.io
---
