---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Xoomar Com Agentic Access
  operation_count: 44
  slug: xoomar-com-agentic-access
  summary_line: 44 operations
api_count: 1
apis:
- baseURL: https://xoomar.com
  baseurl_source: declared
  description: SEC and FINRA data on US listed companies
  name: XOOMAR Companies API
  slug: xoomar-com-companies-api
- baseURL: https://xoomar.com
  baseurl_source: declared
  description: Crypto derivatives and on-exchange data
  name: XOOMAR Crypto API
  slug: xoomar-com-crypto-api
- baseURL: https://xoomar.com
  baseurl_source: declared
  description: Positioning, rates, Fed, Treasury and the calendar
  name: XOOMAR Macro API
  slug: xoomar-com-macro-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/xoomar-com/agentic-access/xoomar-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xoomar-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/xoomar-com/plans/xoomar-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xoomar-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/xoomar-com/rules/xoomar-com-rules.yml
  title: ''
  type: Spectral
  url: rules/xoomar-com-rules.yml
- group: design
  href: https://artifacts.apis.io/xoomar-com/vocabulary/xoomar-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xoomar-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/xoomar-com/errors/xoomar-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xoomar-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xoomar-com/conformance/xoomar-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xoomar-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/xoomar-com/llms/xoomar-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xoomar-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/xoomar-com/mcp/xoomar-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/xoomar-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/xoomar-com/hosts/xoomar-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xoomar-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/xoomar-com/vendors/xoomar-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xoomar-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xoomar.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://xoomar.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xoomar.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://xoomar.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://xoomar.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://xoomar.com/changelog
- group: auth
  href: https://artifacts.apis.io/xoomar-com/authentication/xoomar-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xoomar-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/xoomar-com/security/xoomar-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xoomar-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xoomar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://xoomar.com/markets/api
created: '2026-11-03'
description: XOOMAR is a capital markets data company offering free market data from primary sources via an open API, along with custom software development for financial institutions. It provides comprehensive market coverage, real‑time updates, and tools to integrate data into trading, analytics, and compliance workflows, serving traders, analysts, and developers seeking reliable financial data solutions.
image: https://xoomar.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at xoomar.com requiring an API key.
  name: XOOMAR MCP Server
  slug: xoomar-com-mcp-yml
modified: '2026-11-03'
name: XOOMAR
nav: Providers
network: true
overview: 'XOOMAR publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Companies API, Crypto API, and Macro API. Tagged areas include Capital Markets, Data, Financial Services, and Software.


  The XOOMAR catalog on APIs.io includes 1 Spectral governance ruleset.


  XOOMAR''s developer surface includes signup flow, pricing, changelog, authentication, documentation, and 15 more developer resources.'
plans:
- name: Xoomar Com Plans Pricing
  plan_count: 4
  slug: xoomar-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: XOOMAR API Rules
  rule_count: 68
  severity_counts:
    error: 65
    hint: 0
    info: 1
    warn: 2
  slug: xoomar-com-rules
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 53.3
    developer_ergonomics: 21.4
    discoverability: 56.7
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Xoomar Com Authentication
  slug: xoomar-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Xoomar Com Domain Security
  slug: xoomar-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xoomar-com
tags:
- Capital Markets
- Data
- Financial Services
- Software
website: https://xoomar.com/
---
