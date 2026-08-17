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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Blue Yonder Agentic Access
  operation_count: 7
  slug: blue-yonder-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 7
apis:
- description: The Blue Yonder Demand Planning API enables access to demand forecasting models, statistical baselines, and demand signals for retail and manufacturing supply chains. REST APIs support integration wit
  name: Blue Yonder Demand Planning API
  slug: blue-yonder-demand-planning-api
- description: 'The Blue Yonder Transportation Management API enables access to transportation planning, carrier management, load optimization, and freight audit capabilities. REST APIs support carrier connectivity, '
  name: Blue Yonder Transportation Management API
  slug: blue-yonder-transportation-management-api
- description: Blue Yonder Connect - API & Expansion Pack provides an advanced integration suite with pre-built MuleSoft connectors, enhanced API management tools, and higher throughput capacity. Supports REST, SOAP
  name: Blue Yonder Connect API & Expansion Pack
  slug: blue-yonder-connect-api
- description: Inventory positions and stock management
  name: blue-yonder Inventory API
  slug: blue-yonder-inventory-api
- description: Outbound order management and picking
  name: blue-yonder Orders API
  slug: blue-yonder-orders-api
- description: Inbound receiving and putaway
  name: blue-yonder Receipts API
  slug: blue-yonder-receipts-api
- description: Warehouse task management
  name: blue-yonder Tasks API
  slug: blue-yonder-tasks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blue Yonder Warehouse Management Inventory API
  slug: open-blue-yonder-inventory-api
- collection_type: open
  name: Blue Yonder Warehouse Management Inventory Orders API
  slug: open-blue-yonder-orders-api
- collection_type: open
  name: Blue Yonder Warehouse Management Inventory Receipts API
  slug: open-blue-yonder-receipts-api
- collection_type: open
  name: Blue Yonder Warehouse Management Inventory Tasks API
  slug: open-blue-yonder-tasks-api
- collection_type: open
  name: Blue Yonder Warehouse Management API
  slug: open-blue-yonder-warehouse-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blue-yonder-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blue-yonder-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blue-yonder-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/blue-yonder-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blue-yonder
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blueyonder
- group: company
  title: ''
  type: Website
  url: https://blueyonder.com
- group: start
  title: ''
  type: Portal
  url: https://blueyonder.com/solutions/blue-yonder-platform
- group: docs
  title: ''
  type: Documentation
  url: https://blueyonder.com/solutions/blue-yonder-platform
- group: start
  title: ''
  type: GettingStarted
  url: https://info.blueyonder.com/blue-yonder-platform/what-is-blue-yonder-connect-api-expansion-pack
- group: company
  title: ''
  type: Blog
  url: https://blog.blueyonder.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/openapi/blue-yonder-warehouse-management-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/json-schema/blue-yonder-inventory-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/json-ld/blue-yonder-context.jsonld
description: Transforming supply chains through an end-to-end platform for planning, execution, commerce and returns.
finops:
- name: Blue Yonder Finops
  service_category: Supply Chain SaaS
  slug: blue-yonder-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blue-yonder.png
json_schemas:
- name: Blue Yonder Inventory Position
  property_count: 15
  slug: blue-yonder-inventory
jsonld:
- class_count: 0
  name: Blue Yonder Context
  property_count: 4
  slug: blue-yonder-context
layout: provider
modified: '2026-05-19'
name: blue-yonder
nav: Providers
network: true
overview: 'blue-yonder publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Inventory API, Orders API, Receipts API, and 1 more.


  The blue-yonder catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  blue-yonder''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 9 more developer resources.'
plans:
- name: Blue Yonder Plans Pricing
  plan_count: 1
  slug: blue-yonder-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 1
  name: Blue Yonder Rate Limits
  slug: blue-yonder-rate-limits
rules:
- name: blue-yonder API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: blue-yonder-jsonschema-spectral-rules
scopes:
- name: Blue Yonder Scopes
  scope_count: 2
  slug: blue-yonder-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 60.4
    developer_ergonomics: 41.3
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/screenshots/blue-yonder-2026-06-20T173532.png
security:
- kind: authentication
  name: Blue Yonder Authentication
  slug: blue-yonder-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Blue Yonder Domain Security
  slug: blue-yonder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blue-yonder
website: https://blueyonder.com
---
