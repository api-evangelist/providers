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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Osmapi Agentic Access
  operation_count: 4
  slug: osmapi-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 4
apis:
- description: The Chat API from osmAPI — 1 operation(s) for chat.
  name: osmAPI Chat API
  slug: osmapi-chat-api
- description: The Messages API from osmAPI — 1 operation(s) for messages.
  name: osmAPI Messages API
  slug: osmapi-messages-api
- description: The Models API from osmAPI — 1 operation(s) for models.
  name: osmAPI Models API
  slug: osmapi-models-api
- description: The OsmAPI Health API API from osmAPI — 1 operation(s) for osmapi health api.
  name: osmAPI OsmAPI Health API API
  slug: osmapi-osmapi-health-api-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: osmAPI Anthropic Messages API
  slug: open-osmapi-anthropic-messages
- collection_type: open
  name: osmAPI Anthropic Messages Chat API
  slug: open-osmapi-chat-api
- collection_type: open
  name: osmAPI Chat Completions API
  slug: open-osmapi-chat-completions
- collection_type: open
  name: osmAPI Health API
  slug: open-osmapi-health
- collection_type: open
  name: osmAPI Anthropic Chat Messages API
  slug: open-osmapi-messages-api
- collection_type: open
  name: osmAPI Anthropic Messages Chat Models API
  slug: open-osmapi-models-api
- collection_type: open
  name: osmAPI Models API
  slug: open-osmapi-models
- collection_type: open
  name: osmAPI Anthropic Messages Chat OsmAPI Health API API
  slug: open-osmapi-osmapi-health-api-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/osmapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osmapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/osmapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openstreetmap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/osm-api
- group: start
  title: ''
  type: Portal
  url: https://www.osmapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.osmapi.com/
- group: other
  title: ''
  type: Dashboard
  url: https://app.osmapi.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.osmapi.com/features/api-keys
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.osmapi.com/resources/rate-limits
- group: other
  title: ''
  type: Routing
  url: https://docs.osmapi.com/features/routing
- group: other
  title: ''
  type: Caching
  url: https://docs.osmapi.com/features/caching
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.osmapi.com/features/cost-breakdown
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/osmapi-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/osmapi-chat-completion-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/osmapi-model-schema.json
created: '2026-03-21'
description: osmAPI is a unified AI gateway that routes requests to OpenAI, Anthropic, Google, and 14+ LLM providers through a single API. Drop-in compatible with the OpenAI SDK, it provides smart routing, streaming, function calling, web search, response healing, embeddings, audio, and realtime endpoints.
finops:
- name: Osmapi Finops
  service_category: AI Infrastructure
  slug: osmapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/osmapi.png
json_schemas:
- name: osmAPI Chat Completion Response
  property_count: 7
  slug: osmapi-chat-completion
- name: osmAPI Model
  property_count: 19
  slug: osmapi-model
jsonld:
- class_count: 4
  name: Osmapi Context
  property_count: 6
  slug: osmapi-context
layout: provider
modified: '2026-05-19'
name: osmAPI
nav: Providers
network: true
overview: 'osmAPI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Messages API, Models API, and 1 more. Tagged areas include Artificial Intelligence, Anthropic, Gateway, LLM, and OpenAI.


  The osmAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  osmAPI''s developer surface includes authentication, developer portal, documentation, pricing, and 12 more developer resources.'
plans:
- name: Osmapi Plans Pricing
  plan_count: 3
  slug: osmapi-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Osmapi Rate Limits
  slug: osmapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: osmAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: osmapi-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 57.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 9.8
    contract_quality: 59.7
    developer_ergonomics: 20.2
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/osmapi/refs/heads/main/screenshots/osmapi-2026-06-20T191217.png
security:
- kind: authentication
  name: Osmapi Authentication
  slug: osmapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Osmapi Domain Security
  slug: osmapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: osmapi
tags:
- Artificial Intelligence
- Anthropic
- Gateway
- LLM
- OpenAI
- Routing
website: https://www.osmapi.com/
---
