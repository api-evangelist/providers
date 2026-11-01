---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: MCP JSON-RPC API providing tools for organization lookup, search, sanctions checks, and other public data from Russian registers.
  name: egrul.org MCP API
  slug: egrul-org-mcp-api
- description: 'egrul-org API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: egrul-org API
  slug: egrul-org-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/egrul-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/egrul-org/rate-limits/egrul-org-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/egrul-org-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/egrul-org/plans/egrul-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/egrul-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/egrul-org/rules/egrul-org-rules.yml
  title: ''
  type: Spectral
  url: rules/egrul-org-rules.yml
- group: design
  href: https://artifacts.apis.io/egrul-org/json-ld/egrul-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/egrul-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/egrul-org/vocabulary/egrul-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/egrul-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/egrul-org/data-model/egrul-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/egrul-org-data-model.yml
- group: auth
  href: https://artifacts.apis.io/egrul-org/authentication/egrul-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/egrul-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/egrul-org/conformance/egrul-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/egrul-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/egrul-org/mcp/egrul-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/egrul-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/egrul-org/hosts/egrul-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/egrul-org-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://egrul.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://egrul.org/privacy/
- group: auth
  href: https://artifacts.apis.io/egrul-org/security/egrul-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/egrul-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://egrul.org/
- group: docs
  title: ''
  type: Documentation
  url: https://egrul.org/about/
- group: start
  title: ''
  type: GettingStarted
  url: https://egrul.org/services/
- group: commercial
  title: ''
  type: Pricing
  url: https://egrul.org/subscribe/
- group: start
  title: ''
  type: SignUp
  url: https://egrul.org/subscribe/
created: '2026-10-30'
description: egrul.org provides API access to Russian official registers including the Unified State Register of Legal Entities (EGRUL) and the Unified State Register of Individual Entrepreneurs (EGRIP). It offers XML and JSON endpoints for querying organization and individual data, supporting verification of counterparties, compliance checks, and access to archival extracts. The service includes subscription plans for bulk data downloads, real-time lookup, and integration with accounting and risk management systems. Data sources encompass Federal Tax Service, Rosstat, Prosecutor General, FIPS, Ministry of Internal Affairs, Federal Penitentiary Service, Rosfinmonitoring, and sanctions lists.
image: https://egrul.org/images/main.png
json_schemas:
- name: GetMonitoringResponse
  property_count: 5
  slug: egrul-org-get-monitoring-response
- name: Get7730588444JsonGzResponse
  property_count: 4
  slug: egrul-org-get7730588444-json-gz-response
- name: Get7730588444XmlGzResponse
  property_count: 3
  slug: egrul-org-get7730588444-xml-gz-response
- name: PostMonitoringInsertPhpRequest
  property_count: 5
  slug: egrul-org-post-monitoring-insert-php-request
- name: PostMonitoringInsertPhpResponse
  property_count: 2
  slug: egrul-org-post-monitoring-insert-php-response
- name: PostMonitoringUpdatePhpRequest
  property_count: 3
  slug: egrul-org-post-monitoring-update-php-request
jsonld:
- class_count: 9
  name: Egrul Org Context
  property_count: 7
  slug: egrul-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at egrul.org over HTTP; 39 tools listed.
  name: egrul-org MCP Server
  slug: egrul-org
modified: '2026-10-30'
name: egrul-org
nav: Providers
network: true
overview: 'egrul-org is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Government, Data, and Russia.


  The egrul-org catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  egrul-org''s developer surface includes authentication, documentation, getting-started guide, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Egrul Org Plans Pricing
  plan_count: 1
  slug: egrul-org-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Egrul Org Rate Limits
  slug: egrul-org-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: egrul-org API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: egrul-org-rules
scopes:
- name: Egrul Org Scopes
  scope_count: 0
  slug: egrul-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 84.1
    catalog_earned_first_party: 0.0
    catalog_gap: 30.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 79.1
    contract_quality: 47.1
    developer_ergonomics: 39.8
    discoverability: 56.7
    operational_transparency: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Egrul Org Authentication
  slug: egrul-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Egrul Org Domain Security
  slug: egrul-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: egrul-org
tags:
- Company
- Finance
- Government
- Data
- Russia
website: https://egrul.org/
---
