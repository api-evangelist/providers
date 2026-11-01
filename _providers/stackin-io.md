---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://mcp.stackin.io
  baseurl_source: declared
  description: 'stackin-io API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: stackin-io API
  slug: stackin-io-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/stackin-io/rate-limits/stackin-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stackin-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/stackin-io/plans/stackin-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stackin-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/stackin-io/rules/stackin-io-rules.yml
  title: ''
  type: Spectral
  url: rules/stackin-io-rules.yml
- group: design
  href: https://artifacts.apis.io/stackin-io/json-ld/stackin-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stackin-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/stackin-io/vocabulary/stackin-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stackin-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/stackin-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/stackin-io/data-model/stackin-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stackin-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/stackin-io/conventions/stackin-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/stackin-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/stackin-io/conventions/stackin-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stackin-io-conventions.yml
- group: start
  href: https://artifacts.apis.io/stackin-io/sandbox/stackin-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/stackin-io-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/stackin-io/authentication/stackin-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stackin-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/stackin-io/errors/stackin-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stackin-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stackin-io/conformance/stackin-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stackin-io-conformance.yml
- group: build
  href: https://artifacts.apis.io/stackin-io/mcp/stackin-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/stackin-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/stackin-io/mcp/stackin-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stackin-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/stackin-io/well-known/stackin-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/stackin-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/stackin-io/hosts/stackin-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stackin-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/stackin-io/vendors/stackin-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stackin-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/stackin-io/packages/stackin-io-packages.yml
  title: ''
  type: SDKs
  url: packages/stackin-io-packages.yml
- group: build
  href: https://artifacts.apis.io/stackin-io/packages/stackin-io-packages.yml
  title: ''
  type: Packages
  url: packages/stackin-io-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stackin.io/blog/quickstart
- group: auth
  href: https://artifacts.apis.io/stackin-io/security/stackin-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stackin-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stackin.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackin.io
- group: commercial
  title: ''
  type: Pricing
  url: https://app.stackin.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.stackin.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.stackin.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://wa.me/554888135243
- group: start
  title: ''
  type: SignUp
  url: https://app.stackin.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.stackin.io/login
- group: company
  title: ''
  type: Blog
  url: https://docs.stackin.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackin-io
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://docs.stackin.io/mcp
  - status: 200
    url: https://stackin.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Stackin provides a Brazilian fiscal API platform that enables developers to issue electronic invoices (NF-e) and service invoices (NFS-e) via a simple REST interface. The service handles document generation, tax calculation, and submission to government tax authorities, offering both sandbox (free) and production environments with dashboards for tracking. It aims to simplify compliance for SaaS, e‑commerce, and ERP solutions in Brazil.
image: https://app.stackin.io/logo.svg
json_schemas:
- name: PostStackinRequest
  property_count: 4
  slug: stackin-io-post-stackin-request
jsonld:
- class_count: 1
  name: Stackin Io Context
  property_count: 4
  slug: stackin-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.stackin.io.
  name: stackin-io MCP Server
  slug: stackin-io-mcp-yml
modified: '2026-10-31'
name: stackin-io
nav: Providers
network: true
overview: 'stackin-io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Tax, Brazil, Invoicing, and SaaS.


  The stackin-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  stackin-io''s developer surface includes sandbox, authentication, getting-started guide, documentation, pricing, support, signup flow, and 25 more developer resources.'
plans:
- name: Stackin Io Plans Pricing
  plan_count: 4
  slug: stackin-io-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Stackin Io Rate Limits
  slug: stackin-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: stackin-io API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: stackin-io-rules
scopes:
- name: Stackin Io Scopes
  scope_count: 0
  slug: stackin-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 89.7
    catalog_earned_first_party: 0.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 46.9
    developer_ergonomics: 61.2
    discoverability: 65.0
    operational_transparency: 33.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Stackin Io Authentication
  slug: stackin-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stackin Io Domain Security
  slug: stackin-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: invoice
  slug: stackin-io-invoice
slug: stackin-io
tags:
- Finance
- Tax
- Brazil
- Invoicing
- SaaS
website: https://stackin.io/
---
