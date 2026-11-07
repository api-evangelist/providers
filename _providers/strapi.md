---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 34
  human_in_the_loop: 4
  name: Strapi Agentic Access
  operation_count: 58
  slug: strapi-agentic-access
  summary_line: 58 operations · 34 acting · 4 human-in-the-loop
api_count: 3
apis:
- description: Strapi includes a built-in webhook system that notifies external services whenever content entries or media assets are created, updated, deleted, published, or unpublished. Webhooks are configured thr
  name: Strapi Webhooks
  slug: strapi-webhooks
- baseURL: https://{host}
  baseurl_source: declared
  description: Authentication endpoints for administrator accounts used to access the Strapi admin panel.
  name: Strapi Admin Authentication API
  slug: strapi-admin-authentication-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for managing administrator roles (Super Admin, Editor, Author) and their associated permissions.
  name: Strapi Admin Roles API
  slug: strapi-admin-roles-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for managing administrator user accounts that have access to the Strapi admin panel.
  name: Strapi Admin Users API
  slug: strapi-admin-users-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for managing API tokens used to authenticate REST and GraphQL API requests.
  name: Strapi API Tokens API
  slug: strapi-api-tokens-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for user authentication including login, registration, and password management using JWT tokens.
  name: Strapi Authentication API
  slug: strapi-authentication-api
- baseURL: https://{host}
  baseurl_source: declared
  description: CRUD operations on content-type entries. Strapi auto-generates these endpoints for each content-type defined in the application.
  name: Strapi Content Entries API
  slug: strapi-content-entries-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for managing content entries through the admin panel Content Manager interface.
  name: Strapi Content Manager API
  slug: strapi-content-manager-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for managing content-type definitions through the Content-Type Builder.
  name: Strapi Content Types API
  slug: strapi-content-types-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for viewing and configuring permissions assigned to roles.
  name: Strapi Permissions API
  slug: strapi-permissions-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for managing user roles and their associated permissions.
  name: Strapi Roles API
  slug: strapi-roles-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for managing transfer tokens used for data transfer operations between Strapi instances.
  name: Strapi Transfer Tokens API
  slug: strapi-transfer-tokens-api
- baseURL: https://{host}
  baseurl_source: declared
  description: File upload and media library management endpoints powered by the Upload plugin.
  name: Strapi Upload API
  slug: strapi-upload-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for managing end-user accounts and profiles.
  name: Strapi Users API
  slug: strapi-users-api
- baseURL: https://{host}
  baseurl_source: declared
  description: Endpoints for managing webhook configurations from the admin panel.
  name: Strapi Webhooks API
  slug: strapi-webhooks-api
artifact_total: 51
asyncapis:
- description: Strapi includes a built-in webhook system that notifies external services whenever certain events occur in the CMS. Rather than polling the Strapi API for changes, you can configure Strapi to send HTT
  name: Strapi Webhooks
  slug: strapi-webhooks-asyncapi
collections:
- collection_type: open
  name: Strapi Admin Panel Admin Authentication API
  slug: open-strapi-admin-authentication-api
- collection_type: open
  name: Strapi Admin Panel API
  slug: open-strapi-admin-panel-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Admin Roles API
  slug: open-strapi-admin-roles-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Admin Users API
  slug: open-strapi-admin-users-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication API Tokens API
  slug: open-strapi-api-tokens-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication API
  slug: open-strapi-authentication-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Content Entries API
  slug: open-strapi-content-entries-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Content Manager API
  slug: open-strapi-content-manager-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Content Types API
  slug: open-strapi-content-types-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Permissions API
  slug: open-strapi-permissions-api
- collection_type: open
  name: Strapi REST API
  slug: open-strapi-rest-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Roles API
  slug: open-strapi-roles-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Transfer Tokens API
  slug: open-strapi-transfer-tokens-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Upload API
  slug: open-strapi-upload-api
- collection_type: open
  name: Strapi Users and Permissions API
  slug: open-strapi-users-and-permissions-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Users API
  slug: open-strapi-users-api
- collection_type: open
  name: Strapi Admin Panel Admin Authentication Webhooks API
  slug: open-strapi-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/strapi/plans/strapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/strapi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/strapi/rate-limits/strapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/strapi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/strapi/finops/strapi-finops.yml
  title: ''
  type: FinOps
  url: finops/strapi-finops.yml
- group: other
  href: https://artifacts.apis.io/strapi/capabilities/strapi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/strapi-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/strapi/agentic-access/strapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/strapi-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/strapi/security/strapi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/strapi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/strapi/security/strapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strapi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/strapi/authentication/strapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/strapi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/strapi
- group: company
  title: ''
  type: Website
  url: https://strapi.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.strapi.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/strapi/strapi
- group: company
  title: ''
  type: Blog
  url: https://strapi.io/blog
- group: operate
  title: ''
  type: Forums
  url: https://forum.strapi.io
- group: operate
  title: ''
  type: Discord
  url: https://discord.strapi.io
- group: operate
  title: ''
  type: RoadMap
  url: https://feedback.strapi.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/strapi/strapi/releases
- group: commercial
  title: ''
  type: Pricing
  url: https://strapi.io/pricing-cloud
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/openapi/strapi-rest-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/openapi/strapi-admin-panel-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/openapi/strapi-users-and-permissions-api-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/asyncapi/strapi-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/json-schema/strapi-content-entry-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/strapi/refs/heads/main/json-ld/strapi-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.strapi.io/llms.txt
created: '2025-01-01'
description: Strapi is an open-source, headless CMS built with Node.js that gives developers full control over their content API. It provides a customizable admin panel for content management, automatically generates REST and GraphQL APIs for every content-type, and supports flexible database options including SQLite, PostgreSQL, MySQL, and MongoDB. Strapi v5 introduces a Document Service API with flattened response format, improved TypeScript support, and an enhanced content delivery API for building fast, decoupled frontends.
examples:
- key_count: 2
  name: Strapi Admin Login Example
  slug: strapi-admin-login-example
- key_count: 2
  name: Strapi Create Entry Example
  slug: strapi-create-entry-example
- key_count: 2
  name: Strapi Find Entries Example
  slug: strapi-find-entries-example
- key_count: 2
  name: Strapi Register User Example
  slug: strapi-register-user-example
finops:
- has_sources: true
  method: derived
  name: Strapi Finops
  primary_unit: project
  service_category: ''
  slug: strapi-finops
  template: false
image: https://strapi.io/assets/strapi-logo-dark.svg
json_schemas:
- name: Strapi Content Entry
  property_count: 7
  slug: strapi-content-entry
json_structures:
- name: Strapi Content Entry Structure
  property_count: 0
  slug: strapi-content-entry-structure
jsonld:
- class_count: 0
  name: Strapi Context
  property_count: 8
  slug: strapi-context
layout: provider
mcp_servers:
- description: Remote MCP server at strapi-docs.mcp.kapa.ai over HTTP.
  name: Strapi MCP Server
  slug: strapi
modified: '2026-05-19'
name: Strapi
nav: Providers
network: true
overview: 'Strapi publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks, Admin Authentication API, Admin Roles API, and 12 more. Tagged areas include Strapi, CMS, Content Management, Headless CMS, and Node.js.


  The Strapi catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Strapi''s developer surface includes authentication, documentation, GitHub presence, engineering blog, changelog, pricing, and 19 more developer resources.'
plans:
- name: Strapi Plans Pricing
  plan_count: 3
  slug: strapi-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Strapi Rate Limits
  slug: strapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Strapi — asyncapi rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: strapi-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Strapi — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: strapi-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Strapi API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 4
    warn: 5
  slug: strapi-rules
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 62.5
    catalog_earned_first_party: 12.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    contract_governance: 13.6
    contract_quality: 61.0
    developer_ergonomics: 28.6
    discoverability: 71.7
    operational_transparency: 34.2
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/strapi/strapi-2026-06-20T194615.png
security:
- kind: authentication
  name: Strapi Authentication
  slug: strapi-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Strapi Domain Security
  slug: strapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Strapi Trust Center
  slug: strapi-trust-center
  summary_line: SOC 2, GDPR
slug: strapi
tags:
- Strapi
- CMS
- Content Management
- Headless CMS
- Node.js
- Open Source
website: https://strapi.io
---
