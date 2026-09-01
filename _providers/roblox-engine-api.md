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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Roblox Engine Api Agentic Access
  operation_count: 21
  slug: roblox-engine-api-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 1
apis:
- description: The Roblox Engine API documents all classes, data types, enumerations, global functions, variables, and libraries available when scripting Roblox experiences in Luau. This is the primary reference for
  name: Roblox Engine API
  slug: roblox-engine-api
- description: Asset management and operations
  name: Roblox Engine API Assets API
  slug: roblox-engine-api-assets-api
- description: Persistent data storage for experiences
  name: Roblox Engine API Data Stores API
  slug: roblox-engine-api-data-stores-api
- description: Roblox group management
  name: Roblox Engine API Groups API
  slug: roblox-engine-api-groups-api
- description: Cross-server messaging service
  name: Roblox Engine API Messaging API
  slug: roblox-engine-api-messaging-api
- description: Place publishing and management
  name: Roblox Engine API Places API
  slug: roblox-engine-api-places-api
- description: Experience (universe) management
  name: Roblox Engine API Universes API
  slug: roblox-engine-api-universes-api
- description: Roblox user information
  name: Roblox Engine API Users API
  slug: roblox-engine-api-users-api
artifact_total: 39
collections:
- collection_type: postman
  name: Roblox Open Cloud Assets API
  slug: postman-roblox-engine-api-assets-api
- collection_type: postman
  name: Roblox Open Cloud Assets Data Stores API
  slug: postman-roblox-engine-api-data-stores-api
- collection_type: postman
  name: Roblox Open Cloud Assets Groups API
  slug: postman-roblox-engine-api-groups-api
- collection_type: postman
  name: Roblox Open Cloud Assets Messaging API
  slug: postman-roblox-engine-api-messaging-api
- collection_type: postman
  name: Roblox Open Cloud Assets Places API
  slug: postman-roblox-engine-api-places-api
- collection_type: postman
  name: Roblox Open Cloud Assets Universes API
  slug: postman-roblox-engine-api-universes-api
- collection_type: postman
  name: Roblox Open Cloud Assets Users API
  slug: postman-roblox-engine-api-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Roblox Open Cloud Assets API
  slug: open-roblox-engine-api-assets-api
- collection_type: open
  name: Roblox Open Cloud Assets Data Stores API
  slug: open-roblox-engine-api-data-stores-api
- collection_type: open
  name: Roblox Open Cloud Assets Groups API
  slug: open-roblox-engine-api-groups-api
- collection_type: open
  name: Roblox Open Cloud Assets Messaging API
  slug: open-roblox-engine-api-messaging-api
- collection_type: open
  name: Roblox Open Cloud Assets Places API
  slug: open-roblox-engine-api-places-api
- collection_type: open
  name: Roblox Open Cloud Assets Universes API
  slug: open-roblox-engine-api-universes-api
- collection_type: open
  name: Roblox Open Cloud Assets Users API
  slug: open-roblox-engine-api-users-api
- collection_type: open
  name: Roblox Open Cloud API
  slug: open-roblox-open-cloud
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/roblox-engine-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/roblox-engine-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/roblox-engine-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roblox-engine-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/roblox-engine-api-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/roblox
- group: company
  title: ''
  type: Website
  url: https://www.roblox.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://create.roblox.com
- group: docs
  title: ''
  type: Documentation
  url: https://create.roblox.com/docs
- group: operate
  title: ''
  type: DevForum
  url: https://devforum.roblox.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Roblox
- group: company
  title: ''
  type: Blog
  url: https://blog.roblox.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.roblox.com/info/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://en.help.roblox.com/hc/en-us/articles/115004647846
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/json-ld/roblox-engine-api-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/vocabulary/roblox-engine-api-vocabulary.yml
created: '2024-11-07'
description: Roblox provides a suite of developer APIs for building experiences on the Roblox platform. The Engine API documents all classes, data types, enumerations, functions, events, callbacks, and properties for in-experience scripting in Luau. The Open Cloud REST API provides external programmatic access to Roblox platform resources including experiences, places, data stores, users, groups, assets, messaging, and more. In March 2026 Roblox launched new unified Open Cloud reference documentation.
examples:
- key_count: 2
  name: Roblox Get Universe Example
  slug: roblox-get-universe-example
- key_count: 2
  name: Roblox Set Datastore Entry Example
  slug: roblox-set-datastore-entry-example
finops:
- name: Roblox Engine Api Finops
  service_category: API
  slug: roblox-engine-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roblox-engine-api.png
json_schemas:
- name: Roblox Universe
  property_count: 7
  slug: roblox-universe
- name: Roblox User
  property_count: 9
  slug: roblox-user
json_structures:
- name: Roblox Universe Structure
  property_count: 0
  slug: roblox-universe-structure
jsonld:
- class_count: 30
  name: Roblox Engine Api Context
  property_count: 0
  slug: roblox-engine-api-context
layout: provider
modified: '2026-05-19'
name: Roblox Engine API
nav: Providers
network: true
overview: 'Roblox Engine API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Data Stores API, Groups API, and 4 more. Tagged areas include Gaming, Game Development, Metaverse, Roblox, and Open Cloud.


  The Roblox Engine API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Roblox Engine API''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: Roblox Engine Api Plans Pricing
  plan_count: 3
  slug: roblox-engine-api-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Roblox Engine Api Rate Limits
  slug: roblox-engine-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Roblox Engine API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: roblox-engine-api-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Roblox Engine API API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 4
    warn: 5
  slug: roblox-open-cloud-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 68.9
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/screenshots/roblox-engine-api-2026-06-20T193143.png
security:
- kind: authentication
  name: Roblox Engine Api Authentication
  slug: roblox-engine-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Roblox Engine Api Domain Security
  slug: roblox-engine-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Roblox Engine Api Vulnerability Disclosure
  slug: roblox-engine-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: roblox-engine-api
tags:
- Gaming
- Game Development
- Metaverse
- Roblox
- Open Cloud
website: https://www.roblox.com
---
