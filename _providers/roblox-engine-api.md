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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Roblox Engine Api Agentic Access
  operation_count: 21
  slug: roblox-engine-api-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 8
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
artifact_total: 31
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
random_paper: 2
rate_limits:
- limit_count: 5
  name: Roblox Engine Api Rate Limits
  slug: roblox-engine-api-rate-limits
rules:
- name: Roblox Engine API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: roblox-engine-api-jsonschema-spectral-rules
- name: Roblox Engine API API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 4
    warn: 5
  slug: roblox-open-cloud-rules
score:
  band: strong
  composite: 57.4
  delta: -3.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 75.4
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
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
