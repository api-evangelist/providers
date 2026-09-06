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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Thunder Client is the flagship VS Code REST API client extension offering a lightweight GUI for sending HTTP requests, managing collections with environment variables, and running scriptless tests. Fe
  name: Thunder Client
  slug: thunder-client
- description: The Thunder Client CLI (@thunderclient/cli) is a Node.js command-line tool for running Thunder Client requests, collections, and cURL commands from the terminal. It supports CI/CD integration, paralle
  name: Thunder Client CLI
  slug: thunder-client-cli
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thunder-client-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thunderclient
- group: company
  title: ''
  type: Website
  url: https://www.thunderclient.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thunderclient.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/thunderclient/thunder-client-support
- group: build
  title: ''
  type: VS Code Marketplace
  url: https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thunderclient.com/pricing
- group: build
  title: ''
  type: npm
  url: https://www.npmjs.com/package/@thunderclient/cli
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/thunderclient/thunder-client-support/releases
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/json-schema/thunder-client-collection-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/json-schema/thunder-client-environment-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/json-structure/thunder-client-collection-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/json-ld/thunder-client-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/vocabulary/thunder-client-vocabulary.yml
created: '2026-03-16'
description: Thunder Client is a lightweight REST API client extension for Visual Studio Code created by Ranga Vadhineni, providing a clean interface for sending HTTP requests, managing collections, and testing APIs without leaving the editor. With nearly 7 million installs, it pioneered GUI-based API testing in VS Code with 100% local storage, scriptless testing, Git Sync for team collaboration, GraphQL support, and an advanced CLI for CI/CD integration. Thunder Client supports importing collections from Postman, Insomnia, Hoppscotch, and OpenAPI 3.0, and offers pre/post-request scripting and environment variables.
examples:
- key_count: 7
  name: Thunder Client Collection Example
  slug: thunder-client-collection-example
- key_count: 5
  name: Thunder Client Environment Example
  slug: thunder-client-environment-example
finops:
- name: Thunder Client Finops
  service_category: API
  slug: thunder-client-finops
graphqls:
- description: Thunder Client is the flagship VS Code REST API client extension offering a lightweight GUI for sending HTTP requests, managing collections with environment variables, and running scriptless tests. Fe
  name: Thunder Client GraphQL API
  slug: thunder-client-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thunder-client.png
json_schemas:
- name: Thunder Client Collection
  property_count: 7
  slug: thunder-client-collection
- name: Thunder Client Environment
  property_count: 5
  slug: thunder-client-environment
json_structures:
- name: Thunder Client Collection Structure
  property_count: 0
  slug: thunder-client-collection-structure
jsonld:
- class_count: 14
  name: Thunder Client Context
  property_count: 27
  slug: thunder-client-context
layout: provider
modified: '2026-05-03'
name: Thunder Client
nav: Providers
network: true
overview: 'Thunder Client publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Client, API Testing, CI/CD, CLI, and Collection.


  The Thunder Client catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Thunder Client''s developer surface includes documentation, GitHub presence, pricing, changelog, and 10 more developer resources.'
plans:
- name: Thunder Client Plans Pricing
  plan_count: 3
  slug: thunder-client-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Thunder Client Rate Limits
  slug: thunder-client-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Thunder Client API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: thunder-client-jsonschema-spectral-rules
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 65.3
    catalog_earned_first_party: 0.0
    catalog_gap: 49.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 14.7
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 28.9
  previous_composite: 26.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thunder-client/refs/heads/main/screenshots/thunder-client-2026-06-20T195320.png
security:
- kind: domain-security
  name: Thunder Client Domain Security
  slug: thunder-client-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thunder-client
tags:
- API Client
- API Testing
- CI/CD
- CLI
- Collection
- GraphQL
- REST Client
- VS Code
website: https://www.thunderclient.com
---
