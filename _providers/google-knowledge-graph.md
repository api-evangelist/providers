---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Knowledge Graph Agentic Access
  operation_count: 1
  slug: google-knowledge-graph-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://kgsearch.googleapis.com/v1
  baseurl_source: declared
  description: The Entities:search API from Google Knowledge Graph Search — 1 operation(s) for entities:search.
  name: Google Knowledge Graph Search Entities:search API
  slug: google-knowledge-graph-entities-search-api
artifact_total: 16
collections:
- collection_type: postman
  name: Google Knowledge Graph Search Entities:search API
  slug: postman-google-knowledge-graph-entities-search-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Knowledge Graph Search Entities:search API
  slug: open-google-knowledge-graph-entities-search-api
- collection_type: open
  name: Google Knowledge Graph Search API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-knowledge-graph-search/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-knowledge-graph-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-knowledge-graph-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-knowledge-graph-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-knowledge-graph-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/knowledge-graph
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/knowledge-graph/how-tos/search-widget
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/knowledge-graph
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/knowledge-graph/how-tos/authorizing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/knowledge-graph/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google Knowledge Graph Search API allows developers to search for entities (people, places, things) in the Google Knowledge Graph and retrieve structured data about them in JSON-LD format conforming to schema.org standards. Results include names, descriptions, images, and detailed descriptions with relevance scoring.
finops:
- name: Google Knowledge Graph Finops
  service_category: API
  slug: google-knowledge-graph-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-knowledge-graph.png
json_schemas:
- name: Google Knowledge Graph Entity
  property_count: 7
  slug: Entity
jsonld:
- class_count: 14
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Knowledge Graph Search
nav: Providers
network: true
overview: 'Google Knowledge Graph Search publishes 1 API on the [APIs.io](https://apis.io/) network: Entities:search API. Tagged areas include Entities, Google, Knowledge Graph, Linked Data, and Schema.org.


  The Google Knowledge Graph Search catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Knowledge Graph Search''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, and 9 more developer resources.'
plans:
- name: Google Knowledge Graph Plans Pricing
  plan_count: 3
  slug: google-knowledge-graph-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Google Knowledge Graph Rate Limits
  slug: google-knowledge-graph-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Knowledge Graph Search API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-knowledge-graph-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Google Knowledge Graph Search API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 5
  slug: google-knowledge-graph-spectral-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 61.9
    developer_ergonomics: 44.0
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 23.7
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-knowledge-graph/refs/heads/main/screenshots/google-knowledge-graph-2026-06-20T182208.png
security:
- kind: authentication
  name: Google Knowledge Graph Authentication
  slug: google-knowledge-graph-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Google Knowledge Graph Domain Security
  slug: google-knowledge-graph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Knowledge Graph Vulnerability Disclosure
  slug: google-knowledge-graph-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-knowledge-graph
tags:
- Entities
- Google
- Knowledge Graph
- Linked Data
- Schema.org
- Semantic Search
website: https://developers.google.com/knowledge-graph
---
