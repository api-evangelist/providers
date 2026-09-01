---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    delegated_identity: documented
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
  score: 23.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ptc Thingworx Agentic Access
  operation_count: 11
  slug: ptc-thingworx-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- description: PTC ThingWorx AlwaysOn WebSocket API enables persistent bidirectional connections for industrial edge devices and remote assets, supporting real-time telemetry streaming, command and control, and devi
  name: PTC ThingWorx WebSocket/AlwaysOn API
  slug: thingworx-websocket-api
- description: PTC Windchill REST API provides product lifecycle management and PDM access for CAD data management, bill of materials, change management, workflow automation, and product lifecycle workflows in manuf
  name: PTC Windchill REST API
  slug: windchill-rest-api
- description: Data shape definitions
  name: ptc-thingworx DataShapes API
  slug: ptc-thingworx-datashapes-api
- description: Event management and subscription
  name: ptc-thingworx Events API
  slug: ptc-thingworx-events-api
- description: Thing property read/write
  name: ptc-thingworx Properties API
  slug: ptc-thingworx-properties-api
- description: Thing (digital twin) management
  name: ptc-thingworx Things API
  slug: ptc-thingworx-things-api
- description: Thing template management
  name: ptc-thingworx ThingTemplates API
  slug: ptc-thingworx-thingtemplates-api
- description: Time-series property streams
  name: ptc-thingworx ValueStreams API
  slug: ptc-thingworx-valuestreams-api
artifact_total: 28
asyncapis:
- description: PTC ThingWorx AlwaysOn WebSocket API enables persistent bidirectional connections for industrial edge devices and remote assets. Supports real-time telemetry streaming, command and control, event noti
  name: PTC ThingWorx AlwaysOn WebSocket API
  slug: ptc-thingworx-websocket-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PTC ThingWorx REST DataShapes API
  slug: open-ptc-thingworx-datashapes-api
- collection_type: open
  name: PTC ThingWorx REST DataShapes Events API
  slug: open-ptc-thingworx-events-api
- collection_type: open
  name: PTC ThingWorx REST DataShapes Properties API
  slug: open-ptc-thingworx-properties-api
- collection_type: open
  name: PTC ThingWorx REST API
  slug: open-ptc-thingworx-rest
- collection_type: open
  name: PTC ThingWorx REST DataShapes Things API
  slug: open-ptc-thingworx-things-api
- collection_type: open
  name: PTC ThingWorx REST DataShapes ThingTemplates API
  slug: open-ptc-thingworx-thingtemplates-api
- collection_type: open
  name: PTC ThingWorx REST DataShapes ValueStreams API
  slug: open-ptc-thingworx-valuestreams-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ptc-thingworx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ptc-thingworx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ptc-thingworx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ptc-thingworx-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ptc-thingworx
- group: start
  title: ''
  type: Portal
  url: https://docs.ptc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ptc.com/
- group: company
  title: ''
  type: Website
  url: https://www.ptc.com/en/technologies/iiot/thingworx-platform
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ptc.com/en/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ptc-iot-sharing
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/ptc-thingworx-rest-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/ptc-thingworx-websocket-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ptc-thingworx-thing-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/ptc-thingworx-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.ptc.com/en/blogs
description: PTC ThingWorx is an industrial Internet of Things platform that enables companies to rapidly develop and deploy smart, connected solutions for industrial environments.
finops:
- name: Ptc Thingworx Finops
  service_category: Industrial IoT Platform
  slug: ptc-thingworx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ptc-thingworx.png
json_schemas:
- name: PTC ThingWorx Thing
  property_count: 10
  slug: ptc-thingworx-thing
jsonld:
- class_count: 0
  name: Ptc Thingworx Context
  property_count: 27
  slug: ptc-thingworx-context
layout: provider
modified: '2026-05-19'
name: PTC ThingWorx
nav: Providers
network: true
overview: 'PTC ThingWorx publishes 7 APIs on the [APIs.io](https://apis.io/) network, including WebSocket/AlwaysOn API, ptc-thingworx DataShapes API, ptc-thingworx Events API, and 4 more.


  The PTC ThingWorx catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  PTC ThingWorx''s developer surface includes authentication, developer portal, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Ptc Thingworx Plans Pricing
  plan_count: 1
  slug: ptc-thingworx-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Ptc Thingworx Rate Limits
  slug: ptc-thingworx-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: PTC ThingWorx API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: ptc-thingworx-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: PTC ThingWorx API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ptc-thingworx-jsonschema-spectral-rules
scopes:
- name: Ptc Thingworx Scopes
  scope_count: 1
  slug: ptc-thingworx-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 68.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 65.7
    developer_ergonomics: 35.7
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Ptc Thingworx Authentication
  slug: ptc-thingworx-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Ptc Thingworx Domain Security
  slug: ptc-thingworx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ptc-thingworx
website: https://www.ptc.com/en/technologies/iiot/thingworx-platform
---
