---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cat Facts Catfact Agentic Access
  operation_count: 3
  slug: cat-facts-catfact-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: Catalog of cat breeds with country, origin, coat, and pattern.
  name: Cat Facts (catfact.ninja) Breeds API
  slug: cat-facts-catfact-breeds-api
- description: Random cat trivia, individually or in paginated lists.
  name: Cat Facts (catfact.ninja) Facts API
  slug: cat-facts-catfact-facts-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cat Facts Breeds API
  slug: open-cat-facts-catfact-breeds-api
- collection_type: open
  name: Cat Breeds Facts API
  slug: open-cat-facts-catfact-facts-api
- collection_type: open
  name: Cat Facts API
  slug: open-cat-facts-catfact
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cat-facts-catfact-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cat-facts-catfact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catfact.ninja/
- group: docs
  title: ''
  type: SwaggerUI
  url: https://catfact.ninja/
- group: docs
  title: ''
  type: OpenAPI
  url: https://catfact.ninja/docs?api-docs.json
- group: operate
  title: ''
  type: ContactEmail
  url: mailto:contact@catfact.ninja
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: auth
  title: No Authentication Required
  type: Authentication
  url: https://catfact.ninja/
- group: build
  title: MCP Server (Community — cursethevulgar)
  type: Tools
  url: https://github.com/cursethevulgar/catfact-mcp-server
- group: build
  title: MCP Server (Community — mtrmarko)
  type: Tools
  url: https://github.com/mtrmarko/cat-facts-mcp
- group: build
  title: MCP Server (Community — Volspan)
  type: Tools
  url: https://github.com/volspan-deployments/cat-facts-mcp
- group: design
  title: ''
  type: SpectralRules
  url: rules/cat-facts-catfact-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cat-facts-catfact-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cat-facts-catfact-context.jsonld
created: '2026-05-28'
description: Cat Facts is a free, no-authentication community REST API at catfact.ninja that serves random cat trivia and a catalog of cat breeds. It exposes three documented endpoints — a single random fact, a paginated list of facts, and a paginated list of breeds — and ships a Swagger UI based OpenAPI 3.0 document at /docs. The service is widely used in API onboarding tutorials, demos, and sample apps because it requires no API key and returns small, predictable JSON payloads.
examples:
- key_count: 5
  name: Cat Facts Catfact Breed Example
  slug: cat-facts-catfact-breed-example
- key_count: 13
  name: Cat Facts Catfact Breed List Example
  slug: cat-facts-catfact-breed-list-example
- key_count: 2
  name: Cat Facts Catfact Cat Fact Example
  slug: cat-facts-catfact-cat-fact-example
- key_count: 13
  name: Cat Facts Catfact Cat Fact List Example
  slug: cat-facts-catfact-cat-fact-list-example
- key_count: 3
  name: Cat Facts Catfact Pagination Link Example
  slug: cat-facts-catfact-pagination-link-example
image: https://catfact.ninja/docs/asset/favicon-32x32.png
json_schemas:
- name: BreedList
  property_count: 13
  slug: cat-facts-catfact-breed-list
- name: Breed
  property_count: 5
  slug: cat-facts-catfact-breed
- name: CatFactList
  property_count: 13
  slug: cat-facts-catfact-cat-fact-list
- name: CatFact
  property_count: 2
  slug: cat-facts-catfact-cat-fact
- name: PaginationLink
  property_count: 3
  slug: cat-facts-catfact-pagination-link
json_structures:
- name: Cat Facts Catfact Breed List Structure
  property_count: 13
  slug: cat-facts-catfact-breed-list-structure
- name: Cat Facts Catfact Breed Structure
  property_count: 5
  slug: cat-facts-catfact-breed-structure
- name: Cat Facts Catfact Cat Fact List Structure
  property_count: 13
  slug: cat-facts-catfact-cat-fact-list-structure
- name: Cat Facts Catfact Cat Fact Structure
  property_count: 2
  slug: cat-facts-catfact-cat-fact-structure
- name: Cat Facts Catfact Pagination Link Structure
  property_count: 3
  slug: cat-facts-catfact-pagination-link-structure
jsonld:
- class_count: 9
  name: Cat Facts Catfact Context
  property_count: 22
  slug: cat-facts-catfact-context
layout: provider
modified: '2026-05-30'
name: Cat Facts (catfact.ninja)
nav: Providers
network: true
overview: 'Cat Facts (catfact.ninja) publishes 2 APIs on the [APIs.io](https://apis.io/) network: Breeds API and Facts API. Tagged areas include Animals, Cats, Trivia, Public APIs, and Community.


  The Cat Facts (catfact.ninja) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cat Facts (catfact.ninja)''s developer surface includes authentication, tooling, and 12 more developer resources.'
random_paper: 19
rules:
- effective_rule_count: 5
  extends: []
  name: Cat Facts (catfact.ninja) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cat-facts-catfact-jsonschema-spectral-rules
- effective_rule_count: 78
  extends:
  - spectral:oas
  name: Cat Facts (catfact.ninja) API Rules
  rule_count: 37
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 25
  slug: cat-facts-catfact-rules
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 42.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 20.9
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 0.0
  previous_composite: 20.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cat-facts-catfact/refs/heads/main/screenshots/cat-facts-catfact-2026-06-20T174040.png
security:
- kind: domain-security
  name: Cat Facts Catfact Domain Security
  slug: cat-facts-catfact-domain-security
  summary_line: TLSv1.3
slug: cat-facts-catfact
tags:
- Animals
- Cats
- Trivia
- Public APIs
- Community
- No Authentication
- REST
website: https://catfact.ninja/
---
