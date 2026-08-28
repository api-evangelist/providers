---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dead Drop Agentic Access
  operation_count: 11
  slug: dead-drop-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 4
apis:
- description: The Documentation API from Dead Drop — 2 operation(s) for documentation.
  name: Dead Drop Documentation API
  slug: dead-drop-documentation-api
- description: Drop CRUD operations
  name: Dead Drop Drops API
  slug: dead-drop-drops-api
- description: Health check endpoints
  name: Dead Drop Health API
  slug: dead-drop-health-api
- description: Drop version history
  name: Dead Drop History API
  slug: dead-drop-history-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: dead-drop API v1 Documentation API
  slug: open-dead-drop-documentation-api
- collection_type: open
  name: dead-drop API v1 Documentation Drops API
  slug: open-dead-drop-drops-api
- collection_type: open
  name: dead-drop API v1 Documentation Health API
  slug: open-dead-drop-health-api
- collection_type: open
  name: dead-drop API v1 Documentation History API
  slug: open-dead-drop-history-api
- collection_type: open
  name: dead-drop API v1
  slug: open-dead-drop
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/davorinrusevljan/dead-drop/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dead-drop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dead-drop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dead-drop.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://davorinrusevljan.github.io/dead-drop/
- group: docs
  title: ''
  type: APIReference
  url: https://davorinrusevljan.github.io/dead-drop/latest/
- group: other
  title: ''
  type: APIsJSON
  url: https://davorinrusevljan.github.io/dead-drop/latest/openapi.json
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/davorinrusevljan/dead-drop
- group: commercial
  title: ''
  type: Legal
  url: https://github.com/davorinrusevljan/dead-drop/blob/main/LICENSE
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dead-drop.xyz/terms
created: '2026-05-16'
description: Privacy-focused, ephemeral data-sharing API with zero-knowledge encryption. Open source under MIT, built on Cloudflare Workers, Hono, and D1.
examples:
- key_count: 2
  name: Dead Drop Check Name Example
  slug: dead-drop-check-name-example
- key_count: 2
  name: Dead Drop Create Drop Example
  slug: dead-drop-create-drop-example
- key_count: 2
  name: Dead Drop Delete Drop Example
  slug: dead-drop-delete-drop-example
- key_count: 2
  name: Dead Drop Generate Name Example
  slug: dead-drop-generate-name-example
- key_count: 2
  name: Dead Drop Health Example
  slug: dead-drop-health-example
- key_count: 2
  name: Dead Drop List History Example
  slug: dead-drop-list-history-example
- key_count: 2
  name: Dead Drop Retrieve Drop Example
  slug: dead-drop-retrieve-drop-example
- key_count: 2
  name: Dead Drop Update Drop Example
  slug: dead-drop-update-drop-example
finops:
- name: Dead Drop Finops
  service_category: API
  slug: dead-drop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dead-drop.png
json_schemas:
- name: Drop
  property_count: 13
  slug: dead-drop-drop
- name: Error
  property_count: 1
  slug: dead-drop-error
- name: Drop Version
  property_count: 4
  slug: dead-drop-version
json_structures:
- name: Dead Drop Drop Structure
  property_count: 13
  slug: dead-drop-drop-structure
jsonld:
- class_count: 18
  name: Dead Drop Context
  property_count: 2
  slug: dead-drop-context
layout: provider
modified: '2026-05-19'
name: Dead Drop
nav: Providers
network: true
overview: 'Dead Drop publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Documentation API, Drops API, Health API, and 1 more. Tagged areas include Messaging, Privacy, Anonymous, and Open-Source.


  The Dead Drop catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dead Drop''s developer surface includes documentation, API reference, legal docs, and 7 more developer resources.'
plans:
- name: Dead Drop Plans Pricing
  plan_count: 1
  slug: dead-drop-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Dead Drop Rate Limits
  slug: dead-drop-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Dead Drop API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dead-drop-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Dead Drop API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: dead-drop-rules
score:
  band: thin
  composite: 35.4
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 56.5
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dead-drop/refs/heads/main/screenshots/dead-drop-2026-06-20T175740.png
security:
- kind: domain-security
  name: Dead Drop Domain Security
  slug: dead-drop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dead-drop
tags:
- Messaging
- Privacy
- Anonymous
- Open-Source
website: https://dead-drop.xyz
---
