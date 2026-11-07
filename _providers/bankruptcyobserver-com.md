---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Bankruptcy Observer MCP — agent-first access to US business bankruptcy filings, dockets, documents, and answers from the court record. Free name/case-number lookups; subscribe for full access.
  name: Bankruptcy Observer MCP
  slug: bankruptcy-observer-mcp
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/bankruptcyobserver-com/authentication/bankruptcyobserver-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bankruptcyobserver-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bankruptcyobserver-com/conformance/bankruptcyobserver-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bankruptcyobserver-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bankruptcyobserver-com/llms/bankruptcyobserver-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bankruptcyobserver-com-llms.txt
- group: build
  href: https://artifacts.apis.io/bankruptcyobserver-com/mcp/bankruptcyobserver-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bankruptcyobserver-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bankruptcyobserver-com/mcp/bankruptcyobserver-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bankruptcyobserver-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bankruptcyobserver-com/well-known/bankruptcyobserver-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bankruptcyobserver-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bankruptcyobserver-com/hosts/bankruptcyobserver-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankruptcyobserver-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bankruptcyobserver-com/vendors/bankruptcyobserver-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bankruptcyobserver-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bankruptcyobserver-com/security/bankruptcyobserver-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankruptcyobserver-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bankruptcyobserver.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mcp.bankruptcyobserver.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.bankruptcyobserver.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bankruptcyobserver.com/
- group: operate
  title: ''
  type: Support
  url: https://www.bankruptcyobserver.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.bankruptcyobserver.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bankruptcyobserver.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.bankruptcyobserver.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankruptcyobserver.com/privacy
created: '2026-11-02'
description: Stay ahead of US business bankruptcies without repeatedly checking bankruptcy websites. Get next-morning alerts, verify changes against the court record, and connect your AI agent through MCP for case-specific answers. Standard and Heavy include a 7-day free trial. Cancel anytime.
image: https://www.bankruptcyobserver.com/BKO/assets/images/bko_with_coffee.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.bankruptcyobserver.com.
  name: BankruptcyObserver MCP Server
  slug: bankruptcyobserver-com-mcp-yml
modified: '2026-11-02'
name: BankruptcyObserver
nav: Providers
network: true
overview: 'BankruptcyObserver is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Bankruptcy, Finance, Legal, Alerts, and US.


  BankruptcyObserver''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
random_paper: 23
scopes:
- name: Bankruptcyobserver Com Scopes
  scope_count: 0
  slug: bankruptcyobserver-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 27.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bankruptcyobserver Com Authentication
  slug: bankruptcyobserver-com-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Bankruptcyobserver Com Domain Security
  slug: bankruptcyobserver-com-domain-security
  summary_line: TLSv1.3
slug: bankruptcyobserver-com
tags:
- Bankruptcy
- Finance
- Legal
- Alerts
- US
website: https://bankruptcyobserver.com/
---
