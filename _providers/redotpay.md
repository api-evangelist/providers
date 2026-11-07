---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
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
  score: 12.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Production RedotPay HTTP API surface behind the redotpay CLI and the redotpay-payment MCP server. Provides OAuth2 device-flow authentication and the agentic Machine Payments Protocol (MPP) endpoint th
  name: RedotPay Agentic Payments API
  slug: redotpay-agentic-payments-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/redotpay/security/redotpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/redotpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.redotpay.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/redotpay/redotpay-cli
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.redotpay.com
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.redotpay.com
- group: company
  title: ''
  type: Blog
  url: https://blog.redotpay.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redotpay
- group: start
  title: ''
  type: SignUp
  url: https://www.redotpay.com
- group: build
  href: https://artifacts.apis.io/redotpay/packages/redotpay-packages.yml
  title: ''
  type: Packages
  url: packages/redotpay-packages.yml
- group: build
  href: https://artifacts.apis.io/redotpay/cli/redotpay-cli.yml
  title: ''
  type: CLI
  url: cli/redotpay-cli.yml
- group: agent
  href: https://artifacts.apis.io/redotpay/mcp/redotpay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/redotpay-mcp.yml
- group: agent
  href: https://artifacts.apis.io/redotpay/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/redotpay/authentication/redotpay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/redotpay-authentication.yml
- group: auth
  href: https://artifacts.apis.io/redotpay/scopes/redotpay-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/redotpay-scopes.yml
- group: design
  href: https://artifacts.apis.io/redotpay/conventions/redotpay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/redotpay-conventions.yml
- group: design
  href: https://artifacts.apis.io/redotpay/conventions/redotpay-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/redotpay-conventions.yml
- group: design
  href: https://artifacts.apis.io/redotpay/conformance/redotpay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/redotpay-conformance.yml
- group: design
  href: https://artifacts.apis.io/redotpay/lifecycle/redotpay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/redotpay-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/redotpay/llms/redotpay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/redotpay-llms.txt
- group: agent
  href: https://artifacts.apis.io/redotpay/well-known/redotpay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/redotpay-well-known.yml
created: '2026-07-17'
description: 'RedotPay is a global stablecoin-based payment fintech that integrates blockchain solutions with traditional banking and finance infrastructures. The platform lets millions of people spend and send digital assets through a crypto-backed Visa card, a multi-currency wallet, P2P trading, international transfers, and stablecoin earning. Its developer-facing surface is agentic: a first-party Rust CLI (redotpay) and a local MCP server / Agent Skill (redotpay-payment) that let AI agents settle HTTP 402 "Payment Required" challenges over the Machine Payments Protocol (MPP), using OAuth2 device-flow login and per-payment idempotency against the production RedotPay API.'
image: https://www.redotpay.com/logo.svg
layout: provider
mcp_servers:
- description: First-party local MCP server (redotpay-payment) that lets AI agents settle MPP HTTP 402 payments on the user's behalf. Installed via the redotpay-payment-skill install.sh, which registers the MCP serv
  name: Redotpay MCP Server
  slug: redotpay-payment
modified: '2026-07-21'
name: Redotpay
nav: Providers
network: true
overview: 'Redotpay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Stablecoins, and Cryptocurrency.


  Redotpay''s developer surface includes documentation, support, engineering blog, signup flow, CLI, authentication, and 14 more developer resources.'
random_paper: 8
scopes:
- name: Redotpay Scopes
  scope_count: 1
  slug: redotpay-scopes
  summary_line: 1 scope
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 75.0
    operational_transparency: 2.6
  previous_composite: 18.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/redotpay/redotpay-2026-09-02T153151.png
security:
- kind: authentication
  name: Redotpay Authentication
  slug: redotpay-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Redotpay Domain Security
  slug: redotpay-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: redotpay-payment
  slug: redotpay-payment
slug: redotpay
tags:
- Company
- Payments
- Fintech
- Stablecoins
- Cryptocurrency
- Wallets
- Agentic Payments
- Machine Payments Protocol
- x402
- OAuth
- Authentication
website: https://www.redotpay.com
---
