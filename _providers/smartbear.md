---
access_model:
  confidence: high
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Smartbear Agentic Access
  operation_count: 29
  slug: smartbear-agentic-access
  summary_line: 29 operations · 16 acting
api_count: 1
apis:
- description: ReadyAPI is SmartBear's API quality platform for functional, security, and performance testing. It supports RESTful, GraphQL, and other API standards, and is used by more than 250,000 users running mo
  name: ReadyAPI
  slug: readyapi
- description: PactFlow is SmartBear's contract testing platform that ensures API changes do not break consumer applications. It integrates with SwaggerHub for bi-directional contract testing and uses REST principle
  name: PactFlow
  slug: pactflow
- baseURL: https://api.swaggerhub.com
  baseurl_source: spec
  description: Manage API definitions and versions
  name: SmartBear APIs API
  slug: smartbear-apis-api
- baseURL: https://api.swaggerhub.com
  baseurl_source: spec
  description: Manage reusable domain definitions
  name: SmartBear Domains API
  slug: smartbear-domains-api
- baseURL: https://api.swaggerhub.com
  baseurl_source: spec
  description: Manage API integrations with third-party services
  name: SmartBear Integrations API
  slug: smartbear-integrations-api
- baseURL: https://api.swaggerhub.com
  baseurl_source: spec
  description: Manage organizations and members
  name: SmartBear Organizations API
  slug: smartbear-organizations-api
- baseURL: https://api.swaggerhub.com
  baseurl_source: spec
  description: Manage SwaggerHub projects
  name: SmartBear Projects API
  slug: smartbear-projects-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SmartBear SwaggerHub APIs API
  slug: open-smartbear-apis-api
- collection_type: open
  name: SmartBear SwaggerHub APIs Domains API
  slug: open-smartbear-domains-api
- collection_type: open
  name: SmartBear SwaggerHub APIs Integrations API
  slug: open-smartbear-integrations-api
- collection_type: open
  name: SmartBear SwaggerHub APIs Organizations API
  slug: open-smartbear-organizations-api
- collection_type: open
  name: SmartBear SwaggerHub APIs Projects API
  slug: open-smartbear-projects-api
- collection_type: open
  name: SmartBear SwaggerHub API
  slug: open-smartbear-swaggerhub
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/SmartBear/swaggerhub-cli/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/SmartBear/swaggerhub-cli/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/SmartBear/swaggerhub-cli/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/SmartBear/swaggerhub-cli/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartbear-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/smartbear-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartbear-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartbear-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smartbear
- group: company
  title: ''
  type: Website
  url: https://smartbear.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.smartbear.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.smartbear.com/documentation/
- group: operate
  title: ''
  type: Community
  url: https://community.smartbear.com/
- group: company
  title: ''
  type: Blog
  url: https://smartbear.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SmartBear
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SmartBear-DevRel
- group: commercial
  title: ''
  type: Pricing
  url: https://swagger.io/product/pricing/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/smartbear-swaggerhub-openapi.yml
- group: design
  title: ''
  type: Spectral
  url: rules/smartbear-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/smartbear-api-entry-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/smartbear-integration-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/smartbear-swaggerhub-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/smartbear-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/smartbear-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/SmartBear/smartbear-mcp
created: '2025-01-08'
description: SmartBear is a software company that provides AI-powered tools for API lifecycle management including design, testing, documentation, and governance. Their product portfolio includes SwaggerHub for API design and documentation, ReadyAPI for API testing, PactFlow for contract testing, and other tools for software quality and performance. SmartBear's developer API enables programmatic access to manage API definitions, automate lifecycle workflows, and integrate SwaggerHub with CI/CD pipelines and third-party services.
examples:
- key_count: 2
  name: Smartbear Create Integration Example
  slug: smartbear-create-integration-example
- key_count: 2
  name: Smartbear Get Owner Apis Example
  slug: smartbear-get-owner-apis-example
finops:
- name: Smartbear Finops
  service_category: API Design / Testing / Observability
  slug: smartbear-finops
graphqls:
- description: ''
  name: SmartBear GraphQL API
  slug: smartbear-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartbear.png
json_schemas:
- name: SmartBear API Entry
  property_count: 10
  slug: smartbear-api-entry
- name: SmartBear Integration
  property_count: 5
  slug: smartbear-integration
json_structures:
- name: Smartbear Swaggerhub Structure
  property_count: 0
  slug: smartbear-swaggerhub-structure
jsonld:
- class_count: 15
  name: Smartbear Context
  property_count: 7
  slug: smartbear-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: SmartBear
nav: Providers
network: true
overview: 'SmartBear publishes 5 APIs on the [APIs.io](https://apis.io/) network, including APIs API, Domains API, Integrations API, and 2 more. Tagged areas include API Design, API Documentation, API Testing, Contract Testing, and Governance.


  The SmartBear catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SmartBear''s developer surface includes authentication, documentation, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Smartbear Plans Pricing
  plan_count: 1
  slug: smartbear-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Smartbear Rate Limits
  slug: smartbear-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SmartBear API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: smartbear-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: SmartBear API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: smartbear-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 28.8
    contract_quality: 59.0
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 23.7
  open_source:
    applies: true
    score: 50.0
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smartbear/refs/heads/main/screenshots/smartbear-2026-06-20T194038.png
security:
- kind: authentication
  name: Smartbear Authentication
  slug: smartbear-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Smartbear Domain Security
  slug: smartbear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Smartbear Trust Center
  slug: smartbear-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: smartbear
tags:
- API Design
- API Documentation
- API Testing
- Contract Testing
- Governance
- Monitoring
- Platform
website: https://smartbear.com/
---
