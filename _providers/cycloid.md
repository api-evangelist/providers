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
  band: agent-ready
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cycloid Agentic Access
  operation_count: 16
  slug: cycloid-agentic-access
  summary_line: 16 operations · 4 acting
api_count: 8
apis:
- description: Cloud cost provider accounts, dashboards, and tag mappings.
  name: Cycloid CloudCost API
  slug: cycloid-cloudcost-api
- description: Git config repositories used by stacks and pipelines.
  name: Cycloid ConfigRepositories API
  slug: cycloid-configrepositories-api
- description: Credential storage and rotation.
  name: Cycloid Credentials API
  slug: cycloid-credentials-api
- description: Inventory of cloud resources and state locking.
  name: Cycloid Inventory API
  slug: cycloid-inventory-api
- description: Manage organizations, members, teams, and events.
  name: Cycloid Organizations API
  slug: cycloid-organizations-api
- description: CI/CD pipelines, components, and build tracking.
  name: Cycloid Pipelines API
  slug: cycloid-pipelines-api
- description: Projects and environments inside an organization.
  name: Cycloid Projects API
  slug: cycloid-projects-api
- description: Stacks (Service Catalog) and StackForms.
  name: Cycloid ServiceCatalogs API
  slug: cycloid-servicecatalogs-api
artifact_total: 31
collections:
- collection_type: postman
  name: Cycloid HTTP CloudCost API
  slug: postman-cycloid-cloudcost-api
- collection_type: postman
  name: Cycloid HTTP CloudCost ConfigRepositories API
  slug: postman-cycloid-configrepositories-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Credentials API
  slug: postman-cycloid-credentials-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Inventory API
  slug: postman-cycloid-inventory-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Organizations API
  slug: postman-cycloid-organizations-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Pipelines API
  slug: postman-cycloid-pipelines-api
- collection_type: postman
  name: Cycloid HTTP CloudCost Projects API
  slug: postman-cycloid-projects-api
- collection_type: postman
  name: Cycloid HTTP CloudCost ServiceCatalogs API
  slug: postman-cycloid-servicecatalogs-api
- collection_type: open
  name: Cycloid HTTP API
  slug: open-cycloid-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cycloid/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cycloid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cycloid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cycloid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cycloid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cycloid-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cycloid
- group: company
  title: ''
  type: Website
  url: https://www.cycloid.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cycloid.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cycloid.io/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cycloidio
- group: company
  title: ''
  type: Blog
  url: https://www.cycloid.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cycloid.io
- group: start
  title: ''
  type: Login
  url: https://console.cycloid.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cycloid.io/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cycloid.io/legal/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.cycloid.io/contact
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cycloid-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cycloid-organization-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cycloid-stack-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cycloid-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/cycloid-api-capabilities.yml
- group: design
  title: ''
  type: Rules
  url: rules/cycloid-api-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/cycloidio/cycloid-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.cycloid.io/llms.txt
created: '2026-03-27'
description: Cycloid is a unified Internal Developer Portal & Platform combining self-service Service Catalogs (Stacks and StackForms), Infrastructure as Code orchestration, multi-cloud asset inventory (Asset Inventory and InfraView), CI/CD pipeline centralization, FinOps and GreenOps cost / carbon dashboards, RBAC governance, and an MCP server for natural-language interaction. Cycloid exposes a public HTTP REST API at http-api.cycloid.io for programmatic management of organizations, projects, environments, stacks, pipelines, credentials, config repositories, and cloud cost dashboards. Authentication is via API key or OAuth2 with token refresh; the canonical Swagger / Redoc reference is published at docs.cycloid.io.
finops:
- name: Cycloid Finops
  service_category: API
  slug: cycloid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cycloid.png
json_schemas:
- name: Organization
  property_count: 5
  slug: cycloid-organization
- name: Stack
  property_count: 8
  slug: cycloid-stack
jsonld:
- class_count: 20
  name: Cycloid Context
  property_count: 0
  slug: cycloid-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Cycloid
nav: Providers
network: true
overview: 'Cycloid publishes 8 APIs on the [APIs.io](https://apis.io/) network, including CloudCost API, ConfigRepositories API, Credentials API, and 5 more. Tagged areas include Asset Inventory, CI/CD, Cloud Cost Management, Cloud Management, and Developer Experience.


  The Cycloid catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cycloid''s developer surface includes authentication, documentation, pricing, engineering blog, and 21 more developer resources.'
plans:
- name: Cycloid Plans Pricing
  plan_count: 3
  slug: cycloid-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Cycloid Rate Limits
  slug: cycloid-rate-limits
rules:
- name: Cycloid API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: cycloid-api-rules
- name: Cycloid API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cycloid-jsonschema-spectral-rules
scopes:
- name: Cycloid Scopes
  scope_count: 2
  slug: cycloid-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 58.9
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 62.0
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 31.3
    operational_transparency: 52.6
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cycloid/refs/heads/main/screenshots/cycloid-2026-06-20T175412.png
security:
- kind: authentication
  name: Cycloid Authentication
  slug: cycloid-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Cycloid Domain Security
  slug: cycloid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cycloid Trust Center
  slug: cycloid-trust-center
  summary_line: SOC 2, ISO 27001
slug: cycloid
tags:
- Asset Inventory
- CI/CD
- Cloud Cost Management
- Cloud Management
- Developer Experience
- DevOps
- FinOps
- GitOps
- GreenOps
- Infrastructure as Code
- Internal Developer Platform
- Internal Developer Portal
- Multi-Cloud
- Platform Engineering
- RBAC
- Self-Service
- Service Catalog
- StackForms
- Terraform
website: https://www.cycloid.io
---
