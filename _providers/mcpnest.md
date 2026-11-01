---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Gateway API for MCPNest workspace tools.
  name: Gateway API
  slug: gateway-api
- description: 'MCPNest API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: MCPNest API
  slug: mcpnest-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/mcpnest/plans/mcpnest-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mcpnest-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mcpnest/rules/mcpnest-rules.yml
  title: ''
  type: Spectral
  url: rules/mcpnest-rules.yml
- group: design
  href: https://artifacts.apis.io/mcpnest/json-ld/mcpnest-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mcpnest-context.jsonld
- group: design
  href: https://artifacts.apis.io/mcpnest/vocabulary/mcpnest-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mcpnest-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mcpnest/data-model/mcpnest-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mcpnest-data-model.yml
- group: operate
  href: https://artifacts.apis.io/mcpnest/changelog/mcpnest-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mcpnest-changelog.yml
- group: auth
  href: https://artifacts.apis.io/mcpnest/authentication/mcpnest-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mcpnest-authentication.yml
- group: design
  href: https://artifacts.apis.io/mcpnest/conformance/mcpnest-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mcpnest-conformance.yml
- group: other
  href: https://artifacts.apis.io/mcpnest/hosts/mcpnest-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcpnest-hosts.yml
- group: other
  href: https://artifacts.apis.io/mcpnest/vendors/mcpnest-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mcpnest-vendors.yml
- group: build
  href: https://artifacts.apis.io/mcpnest/packages/mcpnest-packages.yml
  title: ''
  type: SDKs
  url: packages/mcpnest-packages.yml
- group: build
  href: https://artifacts.apis.io/mcpnest/packages/mcpnest-packages.yml
  title: ''
  type: Packages
  url: packages/mcpnest-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://mcpnest.io/servers/sandbox
- group: start
  title: ''
  type: Login
  url: https://mcpnest.io/auth/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://mcpnest.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://mcpnest.io/servers/mcp-chinese-getting-started-guide-1
- group: auth
  href: https://artifacts.apis.io/mcpnest/security/mcpnest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcpnest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcpnest.io/
- group: docs
  title: ''
  type: Documentation
  url: https://mcpnest.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://mcpnest.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://mcpnest.io/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcpnest.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mcpnest.io/terms
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://mcpnest.io/
  reason: no-developer-program
  state: none
created: '2026-10-18'
description: MCPNest provides a secure, governed platform for deploying and managing MCP servers at scale. It offers centralized access control, hosted infrastructure, audit logs, and deployment orchestration for engineering teams using tools like Claude, Cursor, and Windsurf. Users can discover, install, and govern MCP servers, access a registry of over 7,500 servers, and leverage features such as configuration validation, AI discovery, and enterprise governance. The service includes documentation, pricing plans, a status page, and support resources, aiming to simplify MCP server lifecycle management for developers and enterprises.
image: https://mcpnest.io/og-default.png
json_schemas:
- name: GetApiV1ServersSlugResponse
  property_count: 17
  slug: mcpnest-get-api-v1-servers-slug-response
- name: GetCategoriesResponse
  property_count: 1
  slug: mcpnest-get-categories-response
- name: GetServersResponse
  property_count: 2
  slug: mcpnest-get-servers-response
- name: GetServersSlugResponse
  property_count: 17
  slug: mcpnest-get-servers-slug-response
- name: PostApiHealthRequest
  property_count: 3
  slug: mcpnest-post-api-health-request
- name: PostApiHostedRequest
  property_count: 3
  slug: mcpnest-post-api-hosted-request
jsonld:
- class_count: 9
  name: Mcpnest Context
  property_count: 23
  slug: mcpnest-context
layout: provider
modified: '2026-10-18'
name: MCPNest
nav: Providers
network: true
overview: 'MCPNest is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cloud, DevOps, and Artificial Intelligence.


  The MCPNest catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MCPNest''s developer surface includes changelog, authentication, sandbox, getting-started guide, documentation, pricing, and 17 more developer resources.'
plans:
- name: Mcpnest Plans Pricing
  plan_count: 5
  slug: mcpnest-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: MCPNest API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: mcpnest-rules
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 33.3
    contract_quality: 24.7
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 45.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mcpnest Authentication
  slug: mcpnest-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mcpnest Domain Security
  slug: mcpnest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mcpnest
tags:
- Company
- Security
- Cloud
- DevOps
- Artificial Intelligence
website: https://mcpnest.io/
---
