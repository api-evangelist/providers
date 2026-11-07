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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://my-server.chaincontext.dev
  baseurl_source: declared
  description: 'ChainContext API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: ChainContext API
  slug: chaincontext-dev-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/chaincontext-dev/plans/chaincontext-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chaincontext-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chaincontext-dev/rules/chaincontext-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/chaincontext-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/chaincontext-dev/vocabulary/chaincontext-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chaincontext-dev-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/chaincontext-dev/changelog/chaincontext-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chaincontext-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/chaincontext-dev/conformance/chaincontext-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chaincontext-dev-conformance.yml
- group: auth
  href: https://artifacts.apis.io/chaincontext-dev/well-known/chaincontext-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chaincontext-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/chaincontext-dev/well-known/chaincontext-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chaincontext-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/chaincontext-dev/hosts/chaincontext-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chaincontext-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/chaincontext-dev/vendors/chaincontext-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chaincontext-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chaincontext.dev/terms
- group: operate
  title: ''
  type: Support
  url: https://chaincontext.gitbook.io/help-center
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chaincontext.dev/
- group: auth
  title: ''
  type: Security
  url: https://chaincontext.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chaincontext.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://chaincontext.dev/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://chaincontext.dev/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chaincontext
- group: operate
  title: ''
  type: ChangeLog
  url: https://chaincontext.dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://chaincontext.dev/blog
- group: docs
  title: ''
  type: APIReference
  url: https://chaincontext.gitbook.io/help-center/account/api-reference
- group: start
  title: ''
  type: SignUp
  url: https://app.chaincontext.dev/auth/register
- group: start
  title: ''
  type: GettingStarted
  url: https://chaincontext.gitbook.io/help-center/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.chaincontext.dev/
- group: auth
  href: https://artifacts.apis.io/chaincontext-dev/security/chaincontext-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chaincontext-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chaincontext-dev/security/chaincontext-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chaincontext-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chaincontext.dev/
coverage:
  checked: '2026-11-03'
  detail: API reference page is a JavaScript‑rendered GitBook site with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://chaincontext.gitbook.io/help-center/account/api-reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: ChainContext provides a no‑code platform for building and hosting Multi‑Chain Protocol (MCP) servers that connect to EVM and Solana networks. Users can select from pre‑configured recipes for DeFi yield, liquidation monitoring, DAO governance, trading, analytics, or security, then deploy a hosted server that AI agents can call to read data, generate prompts, and create unsigned transaction calldata. The service includes built‑in monitoring, pre‑simulation, human‑in‑the‑loop approvals, and optional per‑call monetization in USDC.
image: https://chaincontext.dev/og-image.png
layout: provider
modified: '2026-11-03'
name: ChainContext
nav: Providers
network: true
overview: 'ChainContext is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include MCP Builder, DeFi, Governance, Trading, and Analytics.


  The ChainContext catalog on APIs.io includes 1 Spectral governance ruleset.


  ChainContext''s developer surface includes changelog, support, pricing, engineering blog, API reference, signup flow, getting-started guide, and 19 more developer resources.'
plans:
- name: Chaincontext Dev Plans Pricing
  plan_count: 4
  slug: chaincontext-dev-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: ChainContext API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: chaincontext-dev-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 17.9
    discoverability: 67.0
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chaincontext Dev Domain Security
  slug: chaincontext-dev-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Chaincontext Dev Vulnerability Disclosure
  slug: chaincontext-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chaincontext-dev
tags:
- MCP Builder
- DeFi
- Governance
- Trading
- Analytics
- Security
- Artificial Intelligence
- Blockchain
website: https://chaincontext.dev/
---
