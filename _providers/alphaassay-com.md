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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Research-only, demote-only statistical validation for trading signals.
  name: AlphaAssay API
  slug: alphaassay-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/alphaassay-com/plans/alphaassay-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alphaassay-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/alphaassay-com/changelog/alphaassay-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alphaassay-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/alphaassay-com/errors/alphaassay-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alphaassay-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alphaassay-com/conformance/alphaassay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alphaassay-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alphaassay-com/llms/alphaassay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alphaassay-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/alphaassay-com/mcp/alphaassay-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alphaassay-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alphaassay-com/well-known/alphaassay-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alphaassay-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/alphaassay-com/hosts/alphaassay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphaassay-com-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://alphaassay.com/trust
- group: operate
  title: ''
  type: ChangeLog
  url: https://alphaassay.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://alphaassay.com/blog/was-your-edge-ever-real
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.alphaassay.com</code
- group: auth
  href: https://artifacts.apis.io/alphaassay-com/security/alphaassay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphaassay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alphaassay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://alphaassay.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://alphaassay.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://alphaassay.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://alphaassay.com/docs/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alphaassay.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alphaassay.com/privacy
created: '2026-11-01'
description: AlphaAssay provides statistical validation for trading signals, offering out‑of‑sample testing, over‑fitting checks, and structured verdicts. The platform targets AI agents and traders, delivering certifications, calibration tools, and transparent methodology to ensure signal reliability. It includes a public API, documentation, pricing details, and a trust framework for secure signal verification.
image: https://alphaassay.com/assets/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at alphaassay.com.
  name: AlphaAssay MCP Server
  slug: alphaassay-com-mcp-yml
modified: '2026-11-01'
name: AlphaAssay
nav: Providers
network: true
overview: 'AlphaAssay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Trading, Artificial Intelligence, and Validation.


  AlphaAssay''s developer surface includes changelog, engineering blog, documentation, pricing, getting-started guide, API reference, and 14 more developer resources.'
plans:
- name: Alphaassay Com Plans Pricing
  plan_count: 3
  slug: alphaassay-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 51.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 32.2
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alphaassay Com Domain Security
  slug: alphaassay-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: alphaassay-com
tags:
- Finance
- Trading
- Artificial Intelligence
- Validation
website: https://alphaassay.com/
---
