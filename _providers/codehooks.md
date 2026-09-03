---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Codehooks Agentic Access
  operation_count: 15
  slug: codehooks-agentic-access
  summary_line: 15 operations · 11 acting
api_count: 1
apis:
- description: 'Asynchronous CRUD lifecycle hooks (onBeforeCreate, onAfterCreate, onBeforeRead, onAfterRead, onBeforeUpdate, onAfterUpdate, onBeforeDelete, onAfterDelete) and queue worker processing (onQueueJob) for '
  name: Codehooks Events (AsyncAPI)
  slug: codehooks-events
- baseURL: https://{projectId}.api.codehooks.io/{space}
  baseurl_source: declared
  description: CRUD operations on NoSQL collection documents
  name: Codehooks Documents API
  slug: codehooks-documents-api
- baseURL: https://{projectId}.api.codehooks.io/{space}
  baseurl_source: declared
  description: Fast key-value storage with optional TTL for caching and lookups
  name: Codehooks Key-Value Store API
  slug: codehooks-key-value-store-api
- baseURL: https://{projectId}.api.codehooks.io/{space}
  baseurl_source: declared
  description: Asynchronous job queue for worker processing
  name: Codehooks Queue API
  slug: codehooks-queue-api
artifact_total: 23
asyncapis:
- description: Asynchronous event API for Codehooks serverless backend hooks and queue workers. Covers CRUD lifecycle hooks triggered on collection document operations and asynchronous queue worker processing for na
  name: Codehooks Events API
  slug: codehooks-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Codehooks Database REST API
  slug: open-codehooks-database-rest-api
- collection_type: open
  name: Codehooks Database REST Documents API
  slug: open-codehooks-documents-api
- collection_type: open
  name: Codehooks Database REST Documents Key-Value Store API
  slug: open-codehooks-key-value-store-api
- collection_type: open
  name: Codehooks Database REST Documents Queue API
  slug: open-codehooks-queue-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codehooks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codehooks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codehooks-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codehooks-io
- group: company
  title: ''
  type: Website
  url: https://codehooks.io/
- group: docs
  title: ''
  type: Documentation
  url: https://codehooks.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://codehooks.io/docs/quickstart-cli
- group: company
  title: ''
  type: Blog
  url: https://codehooks.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://codehooks.io/#pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/RestDB
- group: build
  title: ''
  type: NPMPackage
  url: https://www.npmjs.com/package/codehooks-js
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codehooks.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codehooks.io/privacy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/codehooks-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/codehooks-document-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/codehooks-key-value-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/codehooks-queue-job-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/codehooks-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://codehooks.io/llms.txt
created: '2025-02-08'
description: Codehooks is a JavaScript-native serverless backend platform that bundles a NoSQL document database, key-value store, persistent queues with workers, CRON jobs, blob storage, frontend hosting, and an automatic CRUD REST API in a single CLI-deployable runtime. Developers write small Node.js handler files and Codehooks generates a secure REST API, OpenAPI documentation, and event hooks (onBefore/onAfter Create/Read/Update/Delete) without managing servers. The platform targets agent-native and AI backend use cases where simple, fast, MongoDB-style data access and event-driven automation matter.
finops:
- name: Codehooks Finops
  service_category: API
  slug: codehooks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codehooks.png
json_schemas:
- name: Codehooks Document
  property_count: 3
  slug: codehooks-document
- name: Codehooks Key-Value Entry
  property_count: 3
  slug: codehooks-key-value
- name: Codehooks Queue Job
  property_count: 6
  slug: codehooks-queue-job
jsonld:
- class_count: 3
  name: Codehooks Context
  property_count: 12
  slug: codehooks-context
layout: provider
modified: '2026-05-19'
name: Codehooks
nav: Providers
network: true
overview: 'Codehooks publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Events (AsyncAPI), Documents API, Key-Value Store API, and 1 more. Tagged areas include Backend, Database, Event, Hooks, and JavaScript.


  The Codehooks catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Codehooks'' developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, GitHub presence, and 13 more developer resources.'
plans:
- name: Codehooks Plans Pricing
  plan_count: 3
  slug: codehooks-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Codehooks Rate Limits
  slug: codehooks-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Codehooks API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: codehooks-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Codehooks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: codehooks-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Codehooks API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 3
  slug: codehooks-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 61.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 67.3
    developer_ergonomics: 35.7
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codehooks/refs/heads/main/screenshots/codehooks-2026-06-20T174700.png
security:
- kind: authentication
  name: Codehooks Authentication
  slug: codehooks-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Codehooks Domain Security
  slug: codehooks-domain-security
  summary_line: TLSv1.3 · DMARC
slug: codehooks
tags:
- Backend
- Database
- Event
- Hooks
- JavaScript
- NoSQL
- Queues
- Serverless
- Webhook
- Workers
- Workflows
website: https://codehooks.io/
---
