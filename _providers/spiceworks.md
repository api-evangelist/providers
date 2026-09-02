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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Spiceworks Agentic Access
  operation_count: 10
  slug: spiceworks-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- description: Ticket comment operations for adding and retrieving comments on Help Desk support tickets
  name: Spiceworks Comments API
  slug: spiceworks-comments-api
- description: Device inventory operations for accessing information about managed IT devices including computers, servers, and network equipment
  name: Spiceworks Devices API
  slug: spiceworks-devices-api
- description: Help Desk ticket management operations for creating, reading, updating, and listing support tickets within the Spiceworks IT management platform
  name: Spiceworks Tickets API
  slug: spiceworks-tickets-api
- description: User management operations for accessing Spiceworks user and technician profiles
  name: Spiceworks Users API
  slug: spiceworks-users-api
artifact_total: 29
collections:
- collection_type: postman
  name: Spiceworks Cloud Apps Comments API
  slug: postman-spiceworks-comments-api
- collection_type: postman
  name: Spiceworks Cloud Apps Comments Devices API
  slug: postman-spiceworks-devices-api
- collection_type: postman
  name: Spiceworks Cloud Apps Comments Tickets API
  slug: postman-spiceworks-tickets-api
- collection_type: postman
  name: Spiceworks Cloud Apps Comments Users API
  slug: postman-spiceworks-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spiceworks Cloud Apps API
  slug: open-spiceworks-cloud-apps
- collection_type: open
  name: Spiceworks Cloud Apps Comments API
  slug: open-spiceworks-comments-api
- collection_type: open
  name: Spiceworks Cloud Apps Comments Devices API
  slug: open-spiceworks-devices-api
- collection_type: open
  name: Spiceworks Cloud Apps Comments Tickets API
  slug: open-spiceworks-tickets-api
- collection_type: open
  name: Spiceworks Cloud Apps Comments Users API
  slug: open-spiceworks-users-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/spiceworks/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spiceworks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spiceworks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spiceworks-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spiceworks-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://community.spiceworks.com/
- group: start
  title: ''
  type: Signup
  url: https://community.spiceworks.com/register
- group: start
  title: ''
  type: Login
  url: https://community.spiceworks.com/login
- group: start
  title: ''
  type: Portal
  url: https://spiceworks.github.io/developers.spiceworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://spiceworks.github.io/developers.spiceworks.com/documentation/cloud-apps/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/spiceworks/spiceworks-js-sdk
- group: operate
  title: ''
  type: Support
  url: https://community.spiceworks.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.spiceworks.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://community.spiceworks.com/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://community.spiceworks.com/blog
- group: other
  title: ''
  type: X
  url: https://twitter.com/spiceworks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spiceworks
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Spiceworks
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/spiceworks
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spiceworks
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/spiceworks-cloud-apps-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/spiceworks-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spiceworks-vocabulary.yml
created: '2024-01-01'
description: Spiceworks is an online community and marketplace where IT professionals can find advice, manage their networks, and discover and purchase IT products and services. The Spiceworks Cloud Apps API enables developers to build integrated applications within the Spiceworks platform, accessing Help Desk ticketing, device inventory, and user management data through a JavaScript SDK with OAuth-based authentication.
examples:
- key_count: 2
  name: Spiceworks Get Device Example
  slug: spiceworks-get-device-example
- key_count: 2
  name: Spiceworks List Tickets Example
  slug: spiceworks-list-tickets-example
finops:
- name: Spiceworks Finops
  service_category: API
  slug: spiceworks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spiceworks.png
json_schemas:
- name: Spiceworks Inventory Device
  property_count: 16
  slug: spiceworks-device
- name: Spiceworks Help Desk Ticket
  property_count: 12
  slug: spiceworks-ticket
json_structures:
- name: Spiceworks Ticket Structure
  property_count: 0
  slug: spiceworks-ticket-structure
jsonld:
- class_count: 5
  name: Spiceworks Context
  property_count: 29
  slug: spiceworks-context
layout: provider
modified: '2026-05-19'
name: Spiceworks
nav: Providers
network: true
overview: 'Spiceworks publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Devices API, Tickets API, and 1 more. Tagged areas include Community, Enterprise IT, and IT Management.


  The Spiceworks catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spiceworks'' developer surface includes authentication, signup flow, developer portal, documentation, support, engineering blog, YouTube channel, and 16 more developer resources.'
plans:
- name: Spiceworks Plans Pricing
  plan_count: 3
  slug: spiceworks-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Spiceworks Rate Limits
  slug: spiceworks-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spiceworks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spiceworks-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Spiceworks API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: spiceworks-rules
scopes:
- name: Spiceworks Scopes
  scope_count: 3
  slug: spiceworks-scopes
  summary_line: 3 scopes · implicit
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 28.8
    contract_quality: 65.8
    developer_ergonomics: 40.5
    discoverability: 50.0
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spiceworks/refs/heads/main/screenshots/spiceworks-2026-06-20T194312.png
security:
- kind: authentication
  name: Spiceworks Authentication
  slug: spiceworks-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Spiceworks Domain Security
  slug: spiceworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spiceworks
tags:
- Community
- Enterprise IT
- IT Management
website: https://community.spiceworks.com/
---
