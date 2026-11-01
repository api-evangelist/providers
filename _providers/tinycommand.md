---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-10-31'
api_count: 5
apis:
- baseURL: https://mcp.tinycommand.com
  baseurl_source: declared
  description: 'TinyCommand Account & Workspace 9 articles Manage your workspace, team members, credits, bil API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026'
  name: TinyCommand Account & Workspace 9 articles Manage your workspace, team members, credits, bil API
  slug: account-api
- baseURL: https://mcp.tinycommand.com
  baseurl_source: declared
  description: 'TinyCommand core API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: TinyCommand core API
  slug: core-api
- baseURL: https://mcp.tinycommand.com
  baseurl_source: declared
  description: 'TinyCommand MCP Server 9 articles Drive your Tiny Command workspace from Claude Desktop, Cur API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026'
  name: TinyCommand MCP Server 9 articles Drive your Tiny Command workspace from Claude Desktop, Cur API
  slug: mcp-api
- baseURL: https://mcp.tinycommand.com
  baseurl_source: declared
  description: 'TinyCommand TinyTables 40 articles Spreadsheet-database hybrid, with 37 column types, six vi API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026'
  name: TinyCommand TinyTables 40 articles Spreadsheet-database hybrid, with 37 column types, six vi API
  slug: tables-api
- baseURL: https://mcp.tinycommand.com
  baseurl_source: declared
  description: 'TinyCommand TinyWorkflows 96 articles Visual automation builder. Connect apps, add logic, an API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026'
  name: TinyCommand TinyWorkflows 96 articles Visual automation builder. Connect apps, add logic, an API
  slug: workflows-api
artifact_total: 19
asyncapis:
- description: ''
  name: Tinycommand Webhooks
  slug: tinycommand-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://tinycommand.com/docs/forms/getting-started
- group: commercial
  href: https://artifacts.apis.io/tinycommand/plans/tinycommand-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tinycommand-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tinycommand/rules/tinycommand-rules.yml
  title: ''
  type: Spectral
  url: rules/tinycommand-rules.yml
- group: design
  href: https://artifacts.apis.io/tinycommand/json-ld/tinycommand-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tinycommand-context.jsonld
- group: design
  href: https://artifacts.apis.io/tinycommand/vocabulary/tinycommand-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tinycommand-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tinycommand/asyncapi/tinycommand-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tinycommand-webhooks.yml
- group: design
  href: https://artifacts.apis.io/tinycommand/data-model/tinycommand-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tinycommand-data-model.yml
- group: operate
  href: https://artifacts.apis.io/tinycommand/changelog/tinycommand-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tinycommand-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://tinycommand.com/security
- group: auth
  href: https://artifacts.apis.io/tinycommand/authentication/tinycommand-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tinycommand-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://tinycommand.com/docs/mcp/changelog
- group: design
  href: https://artifacts.apis.io/tinycommand/lifecycle/tinycommand-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tinycommand-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tinycommand/conformance/tinycommand-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tinycommand-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tinycommand/llms/tinycommand-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tinycommand-llms.txt
- group: agent
  href: https://artifacts.apis.io/tinycommand/well-known/tinycommand-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tinycommand-well-known.yml
- group: other
  href: https://artifacts.apis.io/tinycommand/hosts/tinycommand-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tinycommand-hosts.yml
- group: other
  href: https://artifacts.apis.io/tinycommand/vendors/tinycommand-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tinycommand-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://tinycommand.com/help-center
- group: auth
  title: ''
  type: Security
  url: https://tinycommand.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tinycommand.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://tinycommand.com/integrations/serper/actions/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://tinycommand.com/changelog
- group: auth
  href: https://artifacts.apis.io/tinycommand/security/tinycommand-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tinycommand-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tinycommand/security/tinycommand-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tinycommand-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tinycommand/security/tinycommand-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tinycommand-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tinycommand.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tinycommand.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://tinycommand.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://tinycommand.com/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tinycommand.com/terms-of-use
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tinycommand.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://tinycommand.com/docs
coverage:
  checked: '2026-10-19'
  detail: Documentation at https://tinycommand.com/docs is a JavaScript‑rendered Next.js site with no static OpenAPI spec.
  evidence:
  - status: 200
    url: https://tinycommand.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: TinyCommand provides an all‑in‑one platform that automates every stage of the hiring process, from lead capture and enrichment to AI‑driven candidate outreach, workflow orchestration, and analytics. The SaaS solution combines forms, tables, workflows, agents, email campaigns, SEO tools, and AI writers to help recruiters and hiring teams streamline recruitment, improve visibility, and close hires faster. It offers flexible pricing, a free forever plan, and integrations with popular tools, positioning itself as a comprehensive recruitment automation hub.
image: https://tinycommand.com/opengraph-image?947cca2a4766e94b
json_schemas:
- name: GetTablesTableidResponse
  property_count: 3
  slug: tinycommand-get-tables-tableid-response
- name: GetTablesTableidRowsResponse
  property_count: 4
  slug: tinycommand-get-tables-tableid-rows-response
- name: GetV1TablesResponse
  property_count: 1
  slug: tinycommand-get-v1-tables-response
- name: PatchTablesTableidRowsRowidResponse
  property_count: 4
  slug: tinycommand-patch-tables-tableid-rows-rowid-response
- name: PostTablesTableidRowsRequest
  property_count: 1
  slug: tinycommand-post-tables-tableid-rows-request
- name: PostTablesTableidRowsResponse
  property_count: 4
  slug: tinycommand-post-tables-tableid-rows-response
jsonld:
- class_count: 10
  name: Tinycommand Context
  property_count: 11
  slug: tinycommand-context
layout: provider
modified: '2026-10-19'
name: TinyCommand
nav: Providers
network: true
overview: 'TinyCommand is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Account & Workspace 9 articles Manage your workspace, team members, credits, bil API, core API, MCP Server 9 articles Drive your Tiny Command workspace from Claude Desktop, Cur API, and 2 more. Tagged areas include Company, Recruiting, Automation, Software-as-a-Service, and Artificial Intelligence.


  The TinyCommand catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  TinyCommand''s developer surface includes getting-started guide, changelog, authentication, support, documentation, pricing, engineering blog, and 25 more developer resources.'
plans:
- name: Tinycommand Plans Pricing
  plan_count: 4
  slug: tinycommand-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: TinyCommand API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: tinycommand-rules
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 33.5
    developer_ergonomics: 57.1
    discoverability: 73.2
    operational_transparency: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tinycommand Authentication
  slug: tinycommand-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Tinycommand Domain Security
  slug: tinycommand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tinycommand Vulnerability Disclosure
  slug: tinycommand-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Tinycommand Trust Center
  slug: tinycommand-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tinycommand
tags:
- Company
- Recruiting
- Automation
- Software-as-a-Service
- Artificial Intelligence
website: https://tinycommand.com/
---
