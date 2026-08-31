---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
  name: Osisoft Pi Agentic Access
  operation_count: 12
  slug: osisoft-pi-agentic-access
  summary_line: 12 operations · 1 acting
api_count: 1
apis:
- description: AVEVA CONNECT (formerly AVEVA Data Hub / OSIsoft Cloud Services) provides cloud-native REST APIs for industrial time-series data management, data views, event data, and secure cloud-based data sharing
  name: AVEVA CONNECT Data Services API
  slug: aveva-connect-api
- description: OSIsoft PI Asset Framework SDK (AF SDK) is a .NET client library for programmatic access to the PI System asset hierarchy, time-series data, and event frames from on-premises PI servers.
  name: OSIsoft PI AF SDK
  slug: pi-af-sdk
- description: Asset Framework server navigation
  name: osisoft-pi AssetServers API
  slug: osisoft-pi-assetservers-api
- description: AF attribute management
  name: osisoft-pi Attributes API
  slug: osisoft-pi-attributes-api
- description: Batch and parallel request execution
  name: osisoft-pi BatchRequests API
  slug: osisoft-pi-batchrequests-api
- description: PI Data Archive server management
  name: osisoft-pi DataServers API
  slug: osisoft-pi-dataservers-api
- description: AF element management
  name: osisoft-pi Elements API
  slug: osisoft-pi-elements-api
- description: Event frame query and management
  name: osisoft-pi EventFrames API
  slug: osisoft-pi-eventframes-api
- description: PI point (tag) management and data
  name: osisoft-pi PIPoints API
  slug: osisoft-pi-pipoints-api
- description: Time-series data streams
  name: osisoft-pi Streams API
  slug: osisoft-pi-streams-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OSIsoft PI Web AssetServers API
  slug: open-osisoft-pi-assetservers-api
- collection_type: open
  name: OSIsoft PI Web AssetServers Attributes API
  slug: open-osisoft-pi-attributes-api
- collection_type: open
  name: OSIsoft PI Web AssetServers BatchRequests API
  slug: open-osisoft-pi-batchrequests-api
- collection_type: open
  name: OSIsoft PI Web AssetServers DataServers API
  slug: open-osisoft-pi-dataservers-api
- collection_type: open
  name: OSIsoft PI Web AssetServers Elements API
  slug: open-osisoft-pi-elements-api
- collection_type: open
  name: OSIsoft PI Web AssetServers EventFrames API
  slug: open-osisoft-pi-eventframes-api
- collection_type: open
  name: OSIsoft PI Web AssetServers PIPoints API
  slug: open-osisoft-pi-pipoints-api
- collection_type: open
  name: OSIsoft PI Web AssetServers Streams API
  slug: open-osisoft-pi-streams-api
- collection_type: open
  name: OSIsoft PI Web API
  slug: open-osisoft-pi-web-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/osisoft-pi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/osisoft-pi-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/osisoft-pi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osisoft-pi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/osisoft-pi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/osisoft
- group: start
  title: ''
  type: Portal
  url: https://docs.aveva.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aveva.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aveva.com/bundle/pi-web-api-getting-started
- group: company
  title: ''
  type: Website
  url: https://www.aveva.com/
- group: operate
  title: ''
  type: Support
  url: https://softwaresupport.aveva.com/
- group: operate
  title: ''
  type: Support
  url: https://community.aveva.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learningacademy.aveva.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aveva
- group: build
  title: ''
  type: SDKs
  url: https://github.com/aveva
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/osisoft-pi-web-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/osisoft-pi-point-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/osisoft-pi-timed-value-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/osisoft-pi-context.jsonld
description: OSIsoft PI System is a real-time data management platform used by industrial organizations to capture, analyze, and visualize operational data from sensors, devices, and applications.
finops:
- name: Osisoft Pi Finops
  service_category: Industrial Software
  slug: osisoft-pi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/osisoft-pi.png
json_schemas:
- name: OSIsoft PI Point
  property_count: 22
  slug: osisoft-pi-point
- name: OSIsoft PI Timed Value
  property_count: 7
  slug: osisoft-pi-timed-value
jsonld:
- class_count: 0
  name: Osisoft Pi Context
  property_count: 23
  slug: osisoft-pi-context
layout: provider
modified: '2026-05-19'
name: OSIsoft PI System
nav: Providers
network: true
overview: 'OSIsoft PI System publishes 8 APIs on the [APIs.io](https://apis.io/) network, including osisoft-pi AssetServers API, osisoft-pi Attributes API, osisoft-pi BatchRequests API, and 5 more.


  The OSIsoft PI System catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OSIsoft PI System''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, and 14 more developer resources.'
plans:
- name: Osisoft Pi Plans Pricing
  plan_count: 1
  slug: osisoft-pi-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Osisoft Pi Rate Limits
  slug: osisoft-pi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OSIsoft PI System API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: osisoft-pi-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 69.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 9.8
    contract_quality: 57.5
    developer_ergonomics: 71.4
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/osisoft-pi/refs/heads/main/screenshots/osisoft-pi-2026-06-20T191219.png
security:
- kind: authentication
  name: Osisoft Pi Authentication
  slug: osisoft-pi-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Osisoft Pi Domain Security
  slug: osisoft-pi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Osisoft Pi Vulnerability Disclosure
  slug: osisoft-pi-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Osisoft Pi Trust Center
  slug: osisoft-pi-trust-center
  summary_line: trust center published
slug: osisoft-pi
website: https://www.aveva.com/
---
