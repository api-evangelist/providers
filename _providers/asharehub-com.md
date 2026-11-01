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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: REST API providing Chinese A-share market data as documented in the public API reference.
  name: AShareHub API
  slug: asharehub-api
- description: 'asharehub-com API as documented publicly: 38 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: asharehub-com API
  slug: asharehub-com-api
artifact_total: 9
common:
- group: operate
  href: https://artifacts.apis.io/asharehub-com/rate-limits/asharehub-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/asharehub-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/asharehub-com/plans/asharehub-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asharehub-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asharehub-com/rules/asharehub-com-rules.yml
  title: ''
  type: Spectral
  url: rules/asharehub-com-rules.yml
- group: design
  href: https://artifacts.apis.io/asharehub-com/vocabulary/asharehub-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asharehub-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/asharehub-com/changelog/asharehub-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/asharehub-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/asharehub-com/authentication/asharehub-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asharehub-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/asharehub-com/conformance/asharehub-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asharehub-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asharehub-com/llms/asharehub-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asharehub-com-llms.txt
- group: build
  href: https://artifacts.apis.io/asharehub-com/mcp/asharehub-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/asharehub-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/asharehub-com/mcp/asharehub-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asharehub-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/asharehub-com/hosts/asharehub-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asharehub-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/asharehub-com/packages/asharehub-com-packages.yml
  title: ''
  type: SDKs
  url: packages/asharehub-com-packages.yml
- group: build
  href: https://artifacts.apis.io/asharehub-com/packages/asharehub-com-packages.yml
  title: ''
  type: Packages
  url: packages/asharehub-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/asharehub-com/security/asharehub-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asharehub-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asharehub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://asharehub.com/en/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://asharehub.com/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://asharehub.com/en/console/pricing
- group: start
  title: ''
  type: SignUp
  url: https://asharehub.com/en/console/register
- group: start
  title: ''
  type: Login
  url: https://asharehub.com/en/console/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChuYiCui1/AShareHub
coverage:
  checked: '2026-10-30'
  detail: Public API documentation is available but no OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://asharehub.com/en/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Chinese A-share market data API providing institutional-grade daily prices, valuations, capital flows, financial statements, and technical indicators for Shanghai and Shenzhen exchanges. Accessible via REST, Python SDK, and MCP, it serves quants, analysts, and fintech teams. The service offers comprehensive coverage back to 2010, including market microstructure data, and supports both English and Chinese documentation.
image: https://asharehub.com/static/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at asharehub.com requiring an API key.
  name: asharehub-com MCP Server
  slug: asharehub-com-mcp-yml
modified: '2026-10-30'
name: asharehub-com
nav: Providers
network: true
overview: 'asharehub-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Market-Data, A-Share, and API.


  The asharehub-com catalog on APIs.io includes 1 Spectral governance ruleset.


  asharehub-com''s developer surface includes changelog, authentication, documentation, getting-started guide, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Asharehub Com Plans Pricing
  plan_count: 3
  slug: asharehub-com-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Asharehub Com Rate Limits
  slug: asharehub-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: asharehub-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: asharehub-com-rules
scopes:
- name: Asharehub Com Scopes
  scope_count: 0
  slug: asharehub-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.3
    catalog_earned_first_party: 0.0
    catalog_gap: 40.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.1
    contract_governance: 79.1
    contract_quality: 28.2
    developer_ergonomics: 40.5
    discoverability: 56.7
    operational_transparency: 49.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asharehub Com Authentication
  slug: asharehub-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Asharehub Com Domain Security
  slug: asharehub-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asharehub-com
tags:
- Company
- Finance
- Market-Data
- A-Share
- API
- Python-SDK
website: https://asharehub.com/
---
