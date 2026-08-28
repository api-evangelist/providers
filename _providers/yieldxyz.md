---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Non-custodial yield REST API to discover yields, construct unsigned transaction flows (enter/exit/manage), and read unified balances across 80+ networks.
  name: Yield.xyz API
  slug: yieldxyz-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yieldxyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yield.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.yield.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yield.xyz/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.yield.xyz/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yield.xyz/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stakekit
- group: operate
  title: ''
  type: Support
  url: https://docs.yield.xyz/docs/faqs
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.yield.xyz/docs/rate-limits-and-plans
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.stakek.it/sign-up/register-interest
- group: start
  title: ''
  type: Login
  url: https://dashboard.stakek.it/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.yield.xyz/docs/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.yield.xyz/docs/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yield.xyz
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.yield.xyz/changelog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.yield.xyz
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yieldxyz-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yieldxyz-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/yieldxyz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/yieldxyz-packages.yml
- group: design
  title: ''
  type: Components
  url: components/yieldxyz-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yieldxyz-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yieldxyz-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yieldxyz-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/yieldxyz-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yieldxyz-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yieldxyz-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yieldxyz-well-known.yml
created: '2026-07-17'
description: Yield.xyz (formerly StakeKit) is a non-custodial, on-chain yield infrastructure API that lets wallets, custodians, exchanges, and AI agents integrate staking, restaking, liquid staking, DeFi lending, vaults, RWA yields, and perpetuals across 80+ networks and thousands of yield opportunities through a single standardized interface. The REST API discovers yields, constructs complete unsigned transaction flows (enter/exit/manage), and returns unified balances while signing and execution stay entirely with the developer. It powers platforms including Ledger, Zerion, and Tangem, and ships SDKs, an embeddable Widget, an AgentKit MCP server, and packaged agent Skills.
image: https://yield.xyz/images/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Yield.xyz MCP Server
  slug: yieldxyz-mcp-server
modified: '2026-07-21'
name: Yield.xyz
nav: Providers
network: true
overview: 'Yield.xyz publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Staking, DeFi, and Yield.


  Yield.xyz''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 22 more developer resources.'
plans:
- name: Yieldxyz Plans
  plan_count: 3
  slug: yieldxyz-plans
random_paper: 16
rate_limits:
- limit_count: 3
  name: Yieldxyz Rate Limits
  slug: yieldxyz-rate-limits
score:
  band: thin
  composite: 36.0
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 36.0
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yieldxyz/refs/heads/main/screenshots/yieldxyz-2026-08-17T083017.png
security:
- kind: authentication
  name: Yieldxyz Authentication
  slug: yieldxyz-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Yieldxyz Domain Security
  slug: yieldxyz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: yieldxyz
tags:
- Company
- Crypto Web3
- Staking
- DeFi
- Yield
- Blockchain
- Restaking
- Vault
- Web3 Infrastructure
- Non-Custodial
website: https://yield.xyz
---
