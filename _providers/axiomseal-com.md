---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AxiomSeal provides a remote MCP server for AI clients, enabling memory storage and retrieval.
  name: AxiomSeal MCP
  slug: axiomseal-mcp
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/axiomseal-com/plans/axiomseal-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axiomseal-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://axiomseal.com/compliance
- group: auth
  title: ''
  type: Security
  url: https://axiomseal.com/privacy
- group: agent
  href: https://artifacts.apis.io/axiomseal-com/llms/axiomseal-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axiomseal-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/axiomseal-com/mcp/axiomseal-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/axiomseal-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/axiomseal-com/well-known/axiomseal-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axiomseal-com-security.txt
- group: auth
  href: https://artifacts.apis.io/axiomseal-com/well-known/axiomseal-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axiomseal-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/axiomseal-com/well-known/axiomseal-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axiomseal-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/axiomseal-com/hosts/axiomseal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axiomseal-com-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://axiomseal.com/support
- group: auth
  href: https://artifacts.apis.io/axiomseal-com/security/axiomseal-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/axiomseal-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/axiomseal-com/security/axiomseal-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/axiomseal-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/axiomseal-com/security/axiomseal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiomseal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axiomseal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://axiomseal.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://axiomseal.com/docs
- group: company
  title: ''
  type: Blog
  url: https://axiomseal.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://axiomseal.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://axiomseal.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axiomseal.com/datenschutz
- group: start
  title: ''
  type: SignUp
  url: https://axiomseal.com/register
- group: start
  title: ''
  type: Login
  url: https://axiomseal.com/login
coverage:
  checked: '2026-11-02'
  detail: API documentation pages (/api-docs, /redoc) redirect to login, requiring authentication to access specs.
  evidence:
  - status: 307
    url: https://axiomseal.com/api-docs
  - status: 307
    url: https://axiomseal.com/redoc
  reason: auth-required
  state: gated
created: '2026-11-02'
description: AxiomSeal provides persistent AI memory that runs 19 validation tests on every write, grades quality (gold/silver/bronze), and seals each memory in a tamper-evident SHA-512 chain. Swiss-hosted, GDPR-compliant, built in Switzerland for Claude Code, Cursor, and any MCP-compatible IDE.
image: https://axiomseal.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.axiomseal.com.
  name: AxiomSeal MCP Server
  slug: axiomseal-com-mcp-yml
modified: '2026-11-02'
name: AxiomSeal
nav: Providers
network: true
overview: 'AxiomSeal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Data Integrity, Swiss, and GDPR.


  AxiomSeal''s developer surface includes support, documentation, API reference, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Axiomseal Com Plans Pricing
  plan_count: 5
  slug: axiomseal-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 65.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 33.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axiomseal Com Domain Security
  slug: axiomseal-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Axiomseal Com Vulnerability Disclosure
  slug: axiomseal-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Axiomseal Com Trust Center
  slug: axiomseal-com-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: axiomseal-com
tags:
- Artificial Intelligence
- Memory
- Data Integrity
- Swiss
- GDPR
website: https://axiomseal.com/
---
