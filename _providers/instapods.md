---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://app.instapods.com
  baseurl_source: declared
  description: 'ExpressTech Systems API as documented publicly: 25 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: ExpressTech Systems API
  slug: instapods-api
artifact_total: 14
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.instapods.com/quickstart
- group: commercial
  href: https://artifacts.apis.io/instapods/plans/instapods-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/instapods-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/instapods/rules/instapods-rules.yml
  title: ''
  type: Spectral
  url: rules/instapods-rules.yml
- group: design
  href: https://artifacts.apis.io/instapods/json-ld/instapods-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/instapods-context.jsonld
- group: design
  href: https://artifacts.apis.io/instapods/vocabulary/instapods-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/instapods-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/instapods/data-model/instapods-data-model.yml
  title: ''
  type: DataModel
  url: data-model/instapods-data-model.yml
- group: build
  href: https://artifacts.apis.io/instapods/cli/instapods-cli.yml
  title: ''
  type: CLI
  url: cli/instapods-cli.yml
- group: auth
  href: https://artifacts.apis.io/instapods/security/instapods-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/instapods-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/instapods/authentication/instapods-authentication.yml
  title: ''
  type: Authentication
  url: authentication/instapods-authentication.yml
- group: design
  href: https://artifacts.apis.io/instapods/conformance/instapods-conformance.yml
  title: ''
  type: Conformance
  url: conformance/instapods-conformance.yml
- group: agent
  href: https://artifacts.apis.io/instapods/llms/instapods-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instapods-llms.txt
- group: other
  href: https://artifacts.apis.io/instapods/a2a/instapods-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/instapods-a2a.yml
- group: agent
  href: https://artifacts.apis.io/instapods/mcp/instapods-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/instapods-mcp.yml
- group: auth
  href: https://artifacts.apis.io/instapods/well-known/instapods-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/instapods-security.txt
- group: agent
  href: https://artifacts.apis.io/instapods/well-known/instapods-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/instapods-well-known.yml
- group: other
  href: https://artifacts.apis.io/instapods/hosts/instapods-hosts.yml
  title: ''
  type: Hosts
  url: hosts/instapods-hosts.yml
- group: other
  href: https://artifacts.apis.io/instapods/vendors/instapods-vendors.yml
  title: ''
  type: Vendors
  url: vendors/instapods-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instapods
- group: auth
  href: https://artifacts.apis.io/instapods/security/instapods-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/instapods-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/instapods/security/instapods-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instapods-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instapods.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.instapods.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.instapods.com/api-reference/overview
- group: company
  title: ''
  type: Blog
  url: https://instapods.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://instapods.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://instapods.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instapods.com
- group: operate
  title: ''
  type: Roadmap
  url: https://instapods.com/roadmap/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instapods.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instapods.com/privacy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.instapods.com/mcp
  - status: 401
    url: https://app.instapods.com/api/mcp
  - status: 200
    url: https://instapods.com/
  reason: partner-login
  state: gated
created: '2026-10-17'
description: ExpressTech Systems provides a platform that instantly deploys applications to the web, offering a seamless experience for developers to move from local development to live production. Users can launch apps with a single command, integrate with AI assistants, and manage hosting, databases, and scaling without complex infrastructure. The service includes a free tier, credit incentives, and extensive documentation covering deployment, APIs, pricing, and support, aiming to simplify app deployment for both hobbyists and enterprises.
image: https://instapods.com/og-image.png
json_schemas:
- name: GetApiPodsMyAppEventsResponse
  property_count: 9
  slug: instapods-get-api-pods-my-app-events-response
- name: PostApiImportsRequest
  property_count: 3
  slug: instapods-post-api-imports-request
- name: PostApiImportsResponse
  property_count: 3
  slug: instapods-post-api-imports-response
- name: PostApiPodsFromZipResponse
  property_count: 5
  slug: instapods-post-api-pods-from-zip-response
- name: PostApiPodsMyAppAppsCrmSetupRequest
  property_count: 1
  slug: instapods-post-api-pods-my-app-apps-crm-setup-request
- name: PostApiPodsRequest
  property_count: 3
  slug: instapods-post-api-pods-request
jsonld:
- class_count: 14
  name: Instapods Context
  property_count: 30
  slug: instapods-context
layout: provider
mcp_servers:
- description: Remote MCP server at instapods.main-vite.mintlify.me.
  name: ExpressTech Systems MCP Server
  slug: instapods-mcp-yml
modified: '2026-10-17'
name: ExpressTech Systems
nav: Providers
network: true
overview: 'ExpressTech Systems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Deployment, Cloud, AI Integration, and Developer Tools.


  The ExpressTech Systems catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ExpressTech Systems'' developer surface includes getting-started guide, CLI, authentication, documentation, API reference, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Instapods Plans Pricing
  plan_count: 5
  slug: instapods-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ExpressTech Systems API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: instapods-rules
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 26.2
    developer_ergonomics: 54.8
    discoverability: 65.0
    operational_transparency: 36.8
  previous_composite: 46.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Instapods Authentication
  slug: instapods-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Instapods Domain Security
  slug: instapods-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Instapods Vulnerability Disclosure
  slug: instapods-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: instapods
tags:
- Company
- Deployment
- Cloud
- AI Integration
- Developer Tools
website: https://instapods.com/
---
