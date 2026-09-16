---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-09-15'
api_count: 1
apis:
- description: Non-custodial USDC payments REST API on Base. Covers one-time payments, verification, subscriptions, merchant-triggered charges, refunds, allowance restore/revoke, and gas sponsorship. Production runs
  name: P2Flux API
  slug: p2flux-api
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/security/p2flux-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/p2flux-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://p2flux.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://p2flux.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://p2flux.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://p2flux.com/docs/quickstart.html
- group: docs
  title: ''
  type: APIReference
  url: https://p2flux.com/docs/api.html
- group: commercial
  title: ''
  type: Pricing
  url: https://p2flux.com/#pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://p2flux.com/status.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://p2flux.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://p2flux.com/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://p2flux.com/integration-enquiries.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/P2Flux
- group: agent
  title: ''
  type: LLMsTxt
  url: https://p2flux.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/well-known/p2flux-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/p2flux-api-well-known.yml
- group: start
  title: ''
  type: APIOnboarding
  url: https://p2flux.com/.well-known/api-onboarding
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/packages/p2flux-api-packages.yml
  title: ''
  type: Packages
  url: packages/p2flux-api-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/packages/p2flux-api-packages.yml
  title: ''
  type: SDKs
  url: packages/p2flux-api-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/components/p2flux-api-components.yml
  title: ''
  type: Components
  url: components/p2flux-api-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/sandbox/p2flux-api-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/p2flux-api-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/rate-limits/p2flux-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/p2flux-api-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/plans/p2flux-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/p2flux-api-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/conventions/p2flux-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/p2flux-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/conventions/p2flux-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/p2flux-api-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/authentication/p2flux-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/p2flux-api-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/errors/p2flux-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/p2flux-api-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/errors/p2flux-api-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/p2flux-api-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/conformance/p2flux-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/p2flux-api-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/lifecycle/p2flux-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/p2flux-api-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/mcp/p2flux-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/p2flux-api-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/data-model/p2flux-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/p2flux-api-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/p2flux-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-15'
description: Non-custodial USDC payments API on the Base blockchain. Provides REST endpoints for one-time USDC payment intents with on-chain verification, recurring/subscription payments with merchant-triggered charges, and refunds. Payments are authorized per-request via HMAC-signed capabilities plus the payer's EIP-712 wallet signature — no signup, no dashboard, no issued credentials, and no custody of funds.
image: https://p2flux.com/assets/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: P2Flux API MCP Server
  slug: p2flux-api-mcp-server
modified: '2026-09-15'
name: P2Flux API
nav: Providers
network: true
overview: 'P2Flux API publishes 1 API on the [APIs.io](https://apis.io/) network: P2Flux API. Tagged areas include Payments, Payment API, Cryptocurrency, Stablecoins, and USDC.


  P2Flux API''s developer surface includes documentation, getting-started guide, API reference, pricing, support, sandbox, authentication, and 24 more developer resources.'
plans:
- name: P2Flux Api Plans Pricing
  plan_count: 0
  slug: p2flux-api-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 13
  name: P2Flux Api Rate Limits
  slug: p2flux-api-rate-limits
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 46.0
    catalog_earned_first_party: 12.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 70.8
    discoverability: 70.4
    operational_transparency: 52.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: P2Flux Api Authentication
  slug: p2flux-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: P2Flux Api Domain Security
  slug: p2flux-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: p2flux-api
tags:
- Payments
- Payment API
- Cryptocurrency
- Stablecoins
- USDC
- Base
- Recurring Payments
- Subscription
- Refunds
- Non-Custodial
website: https://p2flux.com/
---
