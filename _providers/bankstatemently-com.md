---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Bankstatemently API for converting bank statement PDFs to structured data.
  name: Bankstatemently API
  slug: bankstatemently-api
- baseURL: https://api.bankstatemently.com/v1
  baseurl_source: declared
  description: '[Bankstatemently - PDF to CSV Bank Statement Converter](https://bankstatemently.com)'
  name: Bankstatemently API V1 API
  slug: bankstatemently-api-v1-api
artifact_total: 9
common:
- group: operate
  href: https://artifacts.apis.io/bankstatemently-com/rate-limits/bankstatemently-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bankstatemently-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bankstatemently-com/plans/bankstatemently-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bankstatemently-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bankstatemently-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bankstatemently-com/data-model/bankstatemently-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bankstatemently-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bankstatemently-com/conventions/bankstatemently-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bankstatemently-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/bankstatemently-com/conventions/bankstatemently-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bankstatemently-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bankstatemently-com/security/bankstatemently-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bankstatemently-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bankstatemently-com/authentication/bankstatemently-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bankstatemently-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bankstatemently-com/errors/bankstatemently-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bankstatemently-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/bankstatemently-com/llms/bankstatemently-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bankstatemently-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bankstatemently-com/mcp/bankstatemently-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bankstatemently-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bankstatemently-com/well-known/bankstatemently-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bankstatemently-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bankstatemently-com/well-known/bankstatemently-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bankstatemently-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bankstatemently-com/hosts/bankstatemently-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankstatemently-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bankstatemently-com/vendors/bankstatemently-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bankstatemently-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bankstatemently.com/terms
- group: operate
  title: ''
  type: Support
  url: https://bankstatemently.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bankstatemently.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://bankstatemently.com/developers/api
- group: auth
  href: https://artifacts.apis.io/bankstatemently-com/security/bankstatemently-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bankstatemently-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bankstatemently-com/security/bankstatemently-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankstatemently-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bankstatemently.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://bankstatemently.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://bankstatemently.com/developers
- group: company
  title: ''
  type: Blog
  url: https://bankstatemently.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bankstatemently
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/52862871/2sBXcKBHki
created: '2026-11-02'
description: Bank statement converter with 99.9% accuracy, backed by an open-source benchmark. Convert PDFs to CSV, Excel, QuickBooks, or Xero. JSON via a REST API. Bankstatemently offers a dual‑engine processing system (deterministic rules + AI validation) delivering near‑perfect extraction for accountants, bookkeepers, and financial professionals.
image: https://bankstatemently.com/favicons/favicon_256x256.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.bankstatemently.com requiring an API key.
  name: Bankstatemently MCP Server
  slug: bankstatemently-com-mcp-yml
modified: '2026-11-02'
name: Bankstatemently
nav: Providers
network: true
overview: 'Bankstatemently publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API V1 API, and 1 more. Tagged areas include Finance, Banking, Data Conversion, and Software-as-a-Service.


  Bankstatemently''s developer surface includes authentication, support, API reference, pricing, documentation, engineering blog, and 21 more developer resources.'
plans:
- name: Bankstatemently Com Plans Pricing
  plan_count: 4
  slug: bankstatemently-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Bankstatemently Com Rate Limits
  slug: bankstatemently-com-rate-limits
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 32.6
    discoverability: 56.7
    operational_transparency: 44.7
  previous_composite: 40.7
  provenance:
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bankstatemently Com Authentication
  slug: bankstatemently-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bankstatemently Com Domain Security
  slug: bankstatemently-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bankstatemently Com Vulnerability Disclosure
  slug: bankstatemently-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: convert-statement
  slug: bankstatemently-com-convert_statement
slug: bankstatemently-com
tags:
- Finance
- Banking
- Data Conversion
- Software-as-a-Service
website: https://bankstatemently.com/
---
