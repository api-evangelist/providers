---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Africacompliancedata Com Agentic Access
  operation_count: 58
  slug: africacompliancedata-com-agentic-access
  summary_line: 58 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.africacompliancedata.com
  baseurl_source: declared
  description: 'Coverage, full country profiles, your account and your Pro country pack. All plans (tax sections of the profile: Compliance, and Pro for the countries of its pack).'
  name: africacompliancedata-com Countries API
  slug: africacompliancedata-com-countries-api
- baseURL: https://api.africacompliancedata.com
  baseurl_source: declared
  description: All plans, including calendar feeds; the holiday watch from Developer up.
  name: africacompliancedata-com Holidays and business days API
  slug: africacompliancedata-com-holidays-and-business-days-api
- baseURL: https://api.africacompliancedata.com
  baseurl_source: declared
  description: Signed country-year bundles for computing on your own machine (the SDKs' private mode). Holiday parts on all plans; tax parts on Pro (countries of its pack) and Compliance.
  name: africacompliancedata-com Private mode API
  slug: africacompliancedata-com-private-mode-api
- baseURL: https://api.africacompliancedata.com
  baseurl_source: declared
  description: No key needed.
  name: africacompliancedata-com Public API
  slug: africacompliancedata-com-public-api
- baseURL: https://api.africacompliancedata.com
  baseurl_source: declared
  description: Pro (countries of its pack) and Compliance plans; the finance-law digest is Compliance only.
  name: africacompliancedata-com Tax data API
  slug: africacompliancedata-com-tax-data-api
- baseURL: https://api.africacompliancedata.com
  baseurl_source: declared
  description: 'Signed notifications when a country''s data changes, and the change log (every changed value with its reason): Developer and Pro for holiday changes, Compliance for every change.'
  name: africacompliancedata-com Webhooks API
  slug: africacompliancedata-com-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Africacompliancedata Com Webhooks
  slug: africacompliancedata-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/africacompliancedata-com/agentic-access/africacompliancedata-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/africacompliancedata-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/africacompliancedata-com/rate-limits/africacompliancedata-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/africacompliancedata-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/africacompliancedata-com/plans/africacompliancedata-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/africacompliancedata-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/africacompliancedata-com/rules/africacompliancedata-com-rules.yml
  title: ''
  type: Spectral
  url: rules/africacompliancedata-com-rules.yml
- group: design
  href: https://artifacts.apis.io/africacompliancedata-com/json-ld/africacompliancedata-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/africacompliancedata-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/africacompliancedata-com/vocabulary/africacompliancedata-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/africacompliancedata-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/africacompliancedata-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/africacompliancedata-com/asyncapi/africacompliancedata-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/africacompliancedata-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/africacompliancedata-com/data-model/africacompliancedata-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/africacompliancedata-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/africacompliancedata-com/security/africacompliancedata-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/africacompliancedata-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/africacompliancedata-com/authentication/africacompliancedata-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/africacompliancedata-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/africacompliancedata-com/errors/africacompliancedata-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/africacompliancedata-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/africacompliancedata-com/conformance/africacompliancedata-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/africacompliancedata-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/africacompliancedata-com/llms/africacompliancedata-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/africacompliancedata-com-llms.txt
- group: build
  href: https://artifacts.apis.io/africacompliancedata-com/mcp/africacompliancedata-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/africacompliancedata-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/africacompliancedata-com/mcp/africacompliancedata-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/africacompliancedata-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/africacompliancedata-com/well-known/africacompliancedata-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/africacompliancedata-com-security.txt
- group: auth
  href: https://artifacts.apis.io/africacompliancedata-com/well-known/africacompliancedata-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/africacompliancedata-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/africacompliancedata-com/well-known/africacompliancedata-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/africacompliancedata-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/africacompliancedata-com/hosts/africacompliancedata-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/africacompliancedata-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/africacompliancedata-com/vendors/africacompliancedata-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/africacompliancedata-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/africacompliancedata-com/packages/africacompliancedata-com-packages.yml
  title: ''
  type: SDKs
  url: packages/africacompliancedata-com-packages.yml
- group: build
  href: https://artifacts.apis.io/africacompliancedata-com/packages/africacompliancedata-com-packages.yml
  title: ''
  type: Packages
  url: packages/africacompliancedata-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://africacompliancedata.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://africacompliancedata.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://africacompliancedata.com/docs
- group: auth
  href: https://artifacts.apis.io/africacompliancedata-com/security/africacompliancedata-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/africacompliancedata-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/africacompliancedata-com/security/africacompliancedata-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/africacompliancedata-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://africacompliancedata.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://africacompliancedata.com/openapi.json
  - status: null
    url: https://api.africacompliancedata.com/openapi.json
  - status: 401
    url: https://africacompliancedata.com/mcp
  - status: 401
    url: https://api.africacompliancedata.com/mcp
  - status: 401
    url: https://africacompliancedata.com/v1/graphql
  - status: 401
    url: https://api.africacompliancedata.com/v1/graphql
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Africa Compliance Data provides a public API and dataset covering holidays, business days, VAT rates, withholding tax, tax identification formats, filing deadlines, payroll tax and social‑security rates for all 54 African countries, sourced from official government publications and updated regularly.
image: https://africacompliancedata.com/brand/og.png
json_schemas:
- name: Change
  property_count: 12
  slug: africacompliancedata-com-change
- name: ContributionPeriod
  property_count: 24
  slug: africacompliancedata-com-contribution-period
- name: CountryBundle
  property_count: 3
  slug: africacompliancedata-com-country-bundle
- name: PayrollTaxPeriod
  property_count: 12
  slug: africacompliancedata-com-payroll-tax-period
- name: RateOnDate
  property_count: 16
  slug: africacompliancedata-com-rate-on-date
- name: TaxIdRules
  property_count: 2
  slug: africacompliancedata-com-tax-id-rules
jsonld:
- class_count: 17
  name: Africacompliancedata Com Context
  property_count: 84
  slug: africacompliancedata-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.africacompliancedata.com.
  name: africacompliancedata-com MCP Server
  slug: africacompliancedata-com-mcp-yml
modified: '2026-10-30'
name: africacompliancedata-com
nav: Providers
network: true
overview: 'africacompliancedata-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Countries API, Holidays and business days API, Private mode API, and 3 more. Tagged areas include Africa, Compliance, Tax, Holidays, and Data.


  The africacompliancedata-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  africacompliancedata-com''s developer surface includes authentication, API reference, and 27 more developer resources.'
plans:
- name: Africacompliancedata Com Plans Pricing
  plan_count: 4
  slug: africacompliancedata-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Africacompliancedata Com Rate Limits
  slug: africacompliancedata-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: africacompliancedata-com API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 3
  slug: africacompliancedata-com-rules
scopes:
- name: Africacompliancedata Com Scopes
  scope_count: 0
  slug: africacompliancedata-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 49.5
    contract_governance: 79.1
    contract_quality: 71.2
    developer_ergonomics: 32.6
    discoverability: 65.0
    operational_transparency: 46.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Africacompliancedata Com Authentication
  slug: africacompliancedata-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Africacompliancedata Com Domain Security
  slug: africacompliancedata-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Africacompliancedata Com Vulnerability Disclosure
  slug: africacompliancedata-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: list-countries
  slug: africacompliancedata-com-list-countries
slug: africacompliancedata-com
tags:
- Africa
- Compliance
- Tax
- Holidays
- Data
- API
website: https://africacompliancedata.com/
---
