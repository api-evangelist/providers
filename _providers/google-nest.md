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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Nest Agentic Access
  operation_count: 5
  slug: google-nest-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: Manage and control Nest devices
  name: Google Nest Smart Device Management Devices API
  slug: google-nest-devices-api
- description: Manage rooms within structures
  name: Google Nest Smart Device Management Rooms API
  slug: google-nest-rooms-api
- description: Manage structures (homes)
  name: Google Nest Smart Device Management Structures API
  slug: google-nest-structures-api
artifact_total: 22
collections:
- collection_type: postman
  name: Google Nest Smart Device Management Devices API
  slug: postman-google-nest-devices-api
- collection_type: postman
  name: Google Nest Smart Device Management Devices Rooms API
  slug: postman-google-nest-rooms-api
- collection_type: postman
  name: Google Nest Smart Device Management Devices Structures API
  slug: postman-google-nest-structures-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Nest Smart Device Management Devices API
  slug: open-google-nest-devices-api
- collection_type: open
  name: Google Nest Smart Device Management Devices Rooms API
  slug: open-google-nest-rooms-api
- collection_type: open
  name: Google Nest Smart Device Management Devices Structures API
  slug: open-google-nest-structures-api
- collection_type: open
  name: Google Nest Smart Device Management API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-nest-smart-device-management/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-nest-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-nest-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-nest-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-nest
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/nest/device-access
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/nest/device-access/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/nest/device-access
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/nest/device-access/authorization
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
  url: https://developers.google.com/nest/device-access/support
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/google-nest/refs/heads/main/json-ld/google-nest.jsonld
- group: company
  title: ''
  type: Blog
  url: https://blog.google/products/google-nest/rss/
created: '2026-03-13'
description: The Smart Device Management (SDM) API is a REST API that allows developers to manage Google Nest devices including thermostats, cameras, doorbells, and displays. It provides access to device traits and commands using a trait-based model, enabling applications to read device state, execute commands to control devices, and manage structures and rooms within a home.
finops:
- name: Google Nest Finops
  service_category: API
  slug: google-nest-finops
graphqls:
- description: 'This GraphQL schema models the Google Nest Smart Device Management (SDM) API, which provides access to Nest thermostats, cameras, doorbells, displays, and the structures and rooms they belong to. The '
  name: Google Nest / Smart Device GraphQL Schema
  slug: google-nest-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-nest.png
json_schemas:
- name: Google Nest Smart Device Management API Schema
  property_count: 0
  slug: google-nest
jsonld:
- class_count: 0
  name: Google Nest Context
  property_count: 9
  slug: google-nest
layout: provider
modified: '2026-05-19'
name: Google Nest Smart Device Management
nav: Providers
network: true
overview: 'Google Nest Smart Device Management publishes 3 APIs on the [APIs.io](https://apis.io/) network: Devices API, Rooms API, and Structures API. Tagged areas include Camera, Device Management, Doorbell, Google Nest, and IoT.


  The Google Nest Smart Device Management catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Nest Smart Device Management''s developer surface includes developer portal, getting-started guide, documentation, authentication, support, engineering blog, and 10 more developer resources.'
plans:
- name: Google Nest Plans Pricing
  plan_count: 3
  slug: google-nest-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Google Nest Rate Limits
  slug: google-nest-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Nest Smart Device Management API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-nest-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Google Nest Smart Device Management API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 4
  slug: google-nest-spectral-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 60.2
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-nest/refs/heads/main/screenshots/google-nest-2026-06-20T182217.png
security:
- kind: domain-security
  name: Google Nest Domain Security
  slug: google-nest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Nest Vulnerability Disclosure
  slug: google-nest-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-nest
tags:
- Camera
- Device Management
- Doorbell
- Google Nest
- IoT
- Smart Home
- Thermostat
website: https://developers.google.com/nest/device-access
---
