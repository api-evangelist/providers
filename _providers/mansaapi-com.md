---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: African data infrastructure for developers and AI agents. Live market data, NGX equities, ETFs, indices, location data, and identity reference data.
  name: Mansa API
  slug: mansa-api
- baseURL: https://mansaapi.com
  baseurl_source: declared
  description: African data infrastructure for developers and AI agents. Live market data, NGX equities, ETFs, indices, location data, and identity reference data built in Lagos.
  name: Mansa API API
  slug: mansa-api-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/mansaapi-com/rules/mansaapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/mansaapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/mansaapi-com/vocabulary/mansaapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mansaapi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mansaapi-com/conformance/mansaapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mansaapi-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/mansaapi-com/plans/mansaapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mansaapi-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/mansaapi-com/authentication/mansaapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mansaapi-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/mansaapi-com/lifecycle/mansaapi-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/mansaapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mansaapi-com/lifecycle/mansaapi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mansaapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mansaapi-com/errors/mansaapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mansaapi-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/mansaapi-com/llms/mansaapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mansaapi-com-llms.txt
- group: build
  href: https://artifacts.apis.io/mansaapi-com/mcp/mansaapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mansaapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/mansaapi-com/mcp/mansaapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mansaapi-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/mansaapi-com/hosts/mansaapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mansaapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/mansaapi-com/vendors/mansaapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mansaapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/mansaapi-com/packages/mansaapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/mansaapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/mansaapi-com/packages/mansaapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/mansaapi-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mansaapi.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://mansaapi.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mansaapi.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://mansaapi.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HeyZod
- group: docs
  title: ''
  type: Documentation
  url: https://mansaapi.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://mansaapi.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://mansaapi.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://mansaapi.com/docs/quickstart/node-bank-codes
- group: docs
  title: ''
  type: APIReference
  url: https://mansaapi.com/reference/african-bank-codes
- group: auth
  href: https://artifacts.apis.io/mansaapi-com/security/mansaapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mansaapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mansaapi.com/
created: '2026-10-30'
description: Mansa API provides a comprehensive African data layer offering identity, market, and location information via a clean, unified API. Developers can access bank codes, SWIFT details, market data across African exchanges, country profiles, and public holidays. The service includes free tier access, detailed documentation, SDKs, and a sandbox for testing, targeting fintech, financial services, and AI agents needing reliable African financial and geographic data.
image: https://mansaapi.com/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at mansaapi.com.
  name: mansaapi-com MCP Server
  slug: mansaapi-com-mcp-yml
modified: '2026-10-30'
name: mansaapi-com
nav: Providers
network: true
overview: 'mansaapi-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Mansa API API, and 1 more. Tagged areas include Company, Fintech, African Data, Markets, and Location.


  The mansaapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  mansaapi-com''s developer surface includes authentication, pricing, documentation, changelog, engineering blog, getting-started guide, API reference, and 20 more developer resources.'
plans:
- name: Mansaapi Com Plans Pricing
  plan_count: 8
  slug: mansaapi-com-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: mansaapi-com API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: mansaapi-com-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 34.5
    discoverability: 65.0
    operational_transparency: 26.3
  previous_composite: 45.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mansaapi-com/mansaapi-com-2026-11-03T135311.png
security:
- kind: authentication
  name: Mansaapi Com Authentication
  slug: mansaapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mansaapi Com Domain Security
  slug: mansaapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mansaapi-com
tags:
- Company
- Fintech
- African Data
- Markets
- Location
website: https://mansaapi.com/
---
