---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Datahyena Com Agentic Access
  operation_count: 10
  slug: datahyena-com-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- description: Public API providing funding, acquisition, executive move, and hiring signals.
  name: Datahyena Public API
  slug: datahyena-public-api
- baseURL: https://api.datahyena.com
  baseurl_source: declared
  description: Acquisition and merger signals with acquirer, target, amount, and source context.
  name: datahyena-com Acquisitions API
  slug: datahyena-com-acquisitions-api
- baseURL: https://api.datahyena.com
  baseurl_source: declared
  description: Company directory records with search and firmographic filters.
  name: datahyena-com Companies API
  slug: datahyena-com-companies-api
- baseURL: https://api.datahyena.com
  baseurl_source: declared
  description: Executive job-change signals across tracked companies and people.
  name: datahyena-com Exec Moves API
  slug: datahyena-com-exec-moves-api
- baseURL: https://api.datahyena.com
  baseurl_source: declared
  description: Funding rounds with company, investors, amount, round, and source context.
  name: datahyena-com Funding Events API
  slug: datahyena-com-funding-events-api
- baseURL: https://api.datahyena.com
  baseurl_source: declared
  description: 'Hiring signals from company job boards: leadership openings, founding roles, team scaling, technology hiring (beta) and hard-to-fill roles, plus each company''s current hiring profile. Build-outs, surg'
  name: datahyena-com Hiring Signals API
  slug: datahyena-com-hiring-signals-api
- baseURL: https://api.datahyena.com
  baseurl_source: declared
  description: Investor directory records with search, type, country, and domain filters.
  name: datahyena-com Investors API
  slug: datahyena-com-investors-api
artifact_total: 25
asyncapis:
- description: ''
  name: Datahyena Com Webhooks
  slug: datahyena-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/datahyena-com/agentic-access/datahyena-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/datahyena-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/datahyena-com/rate-limits/datahyena-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/datahyena-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/datahyena-com/plans/datahyena-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datahyena-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datahyena-com/rules/datahyena-com-rules.yml
  title: ''
  type: Spectral
  url: rules/datahyena-com-rules.yml
- group: design
  href: https://artifacts.apis.io/datahyena-com/json-ld/datahyena-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datahyena-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/datahyena-com/vocabulary/datahyena-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datahyena-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/datahyena-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/datahyena-com/asyncapi/datahyena-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/datahyena-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/datahyena-com/data-model/datahyena-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datahyena-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/datahyena-com/conventions/datahyena-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/datahyena-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/datahyena-com/authentication/datahyena-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datahyena-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/datahyena-com/errors/datahyena-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datahyena-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/datahyena-com/conformance/datahyena-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datahyena-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datahyena-com/llms/datahyena-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datahyena-com-llms.txt
- group: build
  href: https://artifacts.apis.io/datahyena-com/mcp/datahyena-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/datahyena-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/datahyena-com/mcp/datahyena-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datahyena-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/datahyena-com/well-known/datahyena-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datahyena-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/datahyena-com/hosts/datahyena-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datahyena-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/datahyena-com/vendors/datahyena-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datahyena-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://datahyena.com/docs/guides/quick-start
- group: auth
  href: https://artifacts.apis.io/datahyena-com/security/datahyena-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datahyena-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datahyena.com/
- group: docs
  title: ''
  type: Documentation
  url: https://datahyena.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://datahyena.com/docs/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://datahyena.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://datahyena.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datahyena.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datahyena.com/privacy/
- group: operate
  title: ''
  type: Contact
  url: https://datahyena.com/contact/
created: '2026-10-30'
description: Datahyena provides a focused company‑event signal API delivering clean, structured data on funding rounds, acquisitions, executive moves, and hiring signals. Over 100,000 companies and 50,000+ funding events are covered, with REST endpoints, webhooks, and MCP support. The service offers credit‑based pricing, a free tier, and extensive documentation for developers and sales teams.
image: https://datahyena.com/og/index.png
json_schemas:
- name: HiringProfileDto
  property_count: 11
  slug: datahyena-com-hiring-profile-dto
- name: PublicAcquisitionEventResponseItem
  property_count: 12
  slug: datahyena-com-public-acquisition-event-response-item
- name: PublicCompanyDto
  property_count: 19
  slug: datahyena-com-public-company-dto
- name: PublicFundingEventResponseItem
  property_count: 11
  slug: datahyena-com-public-funding-event-response-item
- name: PublicHiringSignalResponseItem
  property_count: 15
  slug: datahyena-com-public-hiring-signal-response-item
- name: PublicInvestorResponseItem
  property_count: 10
  slug: datahyena-com-public-investor-response-item
jsonld:
- class_count: 67
  name: Datahyena Com Context
  property_count: 160
  slug: datahyena-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.datahyena.com requiring OAuth.
  name: datahyena-com MCP Server
  slug: datahyena-com-mcp-yml
modified: '2026-10-30'
name: datahyena-com
nav: Providers
network: true
overview: 'datahyena-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Acquisitions API, Companies API, Exec Moves API, and 4 more. Tagged areas include Company, Data, Funding, M&A, and Hiring.


  The datahyena-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  datahyena-com''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Datahyena Com Plans Pricing
  plan_count: 4
  slug: datahyena-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Datahyena Com Rate Limits
  slug: datahyena-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: datahyena-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: datahyena-com-rules
scopes:
- name: Datahyena Com Scopes
  scope_count: 0
  slug: datahyena-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.2
  coverage:
    artifact_dirs: 32
    catalog_earned: 86.7
    catalog_earned_first_party: 0.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 63.8
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 26.8
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
  name: Datahyena Com Authentication
  slug: datahyena-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Datahyena Com Domain Security
  slug: datahyena-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: datahyena-com-fetch-company-timelines
  slug: datahyena-com-fetch-company-timelines
- name: integrate-datahyena
  slug: datahyena-com-integrate-datahyena
slug: datahyena-com
tags:
- Company
- Data
- Funding
- M&A
- Hiring
- API
website: https://datahyena.com/
---
