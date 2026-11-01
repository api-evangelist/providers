---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fxpeek Com Agentic Access
  operation_count: 8
  slug: fxpeek-com-agentic-access
  summary_line: 8 operations
api_count: 2
apis:
- description: Source‑linked historical reference exchange rates for invoices, reporting, CSV export and developer workflows.
  name: FXpeek Historical Exchange Rate API
  slug: fxpeek-historical-exchange-rate-api
- description: Business version of the historical exchange rate API.
  name: FXpeek Business API
  slug: fxpeek-business-api
artifact_total: 7
common:
- group: docs
  title: ''
  type: Documentation
  url: https://fxpeek.com/guides/usd-to-eur-exchange-rate
- group: agent
  href: https://artifacts.apis.io/fxpeek-com/agentic-access/fxpeek-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fxpeek-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/fxpeek-com/plans/fxpeek-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fxpeek-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fxpeek-com/rules/fxpeek-com-rules.yml
  title: ''
  type: Spectral
  url: rules/fxpeek-com-rules.yml
- group: design
  href: https://artifacts.apis.io/fxpeek-com/conformance/fxpeek-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fxpeek-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fxpeek-com/llms/fxpeek-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fxpeek-com-llms.txt
- group: build
  href: https://artifacts.apis.io/fxpeek-com/mcp/fxpeek-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fxpeek-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/fxpeek-com/mcp/fxpeek-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fxpeek-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/fxpeek-com/hosts/fxpeek-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fxpeek-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/fxpeek-com/vendors/fxpeek-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fxpeek-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://fxpeek.com/en/register
- group: operate
  title: ''
  type: ChangeLog
  url: https://fxpeek.com/en/changelog
- group: auth
  href: https://artifacts.apis.io/fxpeek-com/security/fxpeek-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fxpeek-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fxpeek.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://business.fxpeek.com
- group: docs
  title: ''
  type: APIReference
  url: https://fxpeek.com/en/api
- group: operate
  title: ''
  type: Support
  url: https://fxpeek.com/en/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Jenpo/historical-exchange-rate-api-examples
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fxpeek.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fxpeek.com/en/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/workspace/fxpeek
created: '2026-10-30'
description: FXpeek provides a historical exchange rate API and currency tools, offering source‑linked CSV exports, charting, and lightweight API access for dated conversions. It focuses on underserved and long‑tail currency pairs, delivering reliable reference data for researchers, developers, accountants, and analysts.
image: https://fxpeek.com/images/fxpeek-hero-pexels.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at fxpeek.com.
  name: fxpeek-com MCP Server
  slug: fxpeek-com-mcp-yml
modified: '2026-10-30'
name: fxpeek-com
nav: Providers
network: true
overview: 'fxpeek-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Currency, API, and Data.


  The fxpeek-com catalog on APIs.io includes 1 Spectral governance ruleset.


  fxpeek-com''s developer surface includes documentation, signup flow, changelog, API reference, support, and 16 more developer resources.'
plans:
- name: Fxpeek Com Plans Pricing
  plan_count: 4
  slug: fxpeek-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: fxpeek-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: fxpeek-com-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 62.6
    contract_governance: 65.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 65.0
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fxpeek Com Domain Security
  slug: fxpeek-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fxpeek-com
tags:
- Company
- Finance
- Currency
- API
- Data
website: https://fxpeek.com/
---
