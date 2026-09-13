---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.6
  scored_at: '2026-09-12'
api_count: 2
apis:
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: The Afriex Business API is a REST API for cross-border money movement. It covers customer creation and KYC verification, payment-method registration across bank accounts, mobile money, SWIFT, UPI, Int
  name: Afriex Business API
  slug: afriex-business-api
- description: Afriex publishes a hosted, remote Model Context Protocol server at https://mcp.afriex.com/mcp that exposes 26 tools covering the Business API surface — customers, transactions, payment methods, instit
  name: Afriex MCP Server
  slug: afriex-mcp-server
artifact_total: 8
asyncapis:
- description: ''
  name: Afriex Business Webhooks
  slug: afriex-business-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/afriex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.afriex.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.afriex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.afriex.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.afriex.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.afriex.com/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://business.afriex.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@afriex.com
- group: company
  title: ''
  type: Blog
  url: https://dev.to/afriex
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Afri-exchange
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.afriex.com/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.afriex.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://afriexinc.statuspage.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/afriex-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/afriex-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/afriex-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/afriex-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/afriex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/afriex-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/afriex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/afriex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/afriex-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/afriex-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/afriex-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/afriex-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/afriex-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/afriex-plans-pricing.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/afriex-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/afriex-business-overlay.yaml
created: '2026-09-12'
description: 'Afriex is a cross-border payments and remittance company that moves money between Africa, North America, Europe and Asia. Its consumer app handles person-to-person remittances, while the Afriex Business API gives companies programmatic access to the same rails: customer onboarding and KYC, payment methods across bank accounts, mobile money, SWIFT, UPI, Interac and USDC/USDT crypto wallets, multi-currency wallet balances and real-time FX rates, deposits, withdrawals and in-wallet currency swaps, hosted checkout sessions, virtual and pool collection accounts, and RSA-signed webhooks for transaction lifecycle events. The API is documented with an OpenAPI 3.1 contract, a first-party TypeScript SDK, and a hosted remote MCP server that exposes the same surface to AI agents.'
image: https://cdn.prod.website-files.com/62ce94ab2b9c3a3597a7acd4/62f26e44523cfa8d7d76823e_Website%20Open%20Graph.webp
layout: provider
mcp_servers:
- description: ''
  name: Afriex MCP Server
  slug: afriex-mcp-server
modified: '2026-09-12'
name: Afriex
nav: Providers
network: true
overview: 'Afriex publishes 1 API on the [APIs.io](https://apis.io/) network: Business API. Tagged areas include Payments, Remittances, Cross-Border Payments, Fintech, and Financial Services.


  The Afriex catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Afriex''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 23 more developer resources.'
plans:
- name: Afriex Plans Pricing
  plan_count: 0
  slug: afriex-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Afriex Rate Limits
  slug: afriex-rate-limits
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 68.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    operational_transparency: 28.9
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Afriex Authentication
  slug: afriex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Afriex Domain Security
  slug: afriex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: afriex
tags:
- Payments
- Remittances
- Cross-Border Payments
- Fintech
- Financial Services
- Foreign Exchange
- Mobile Money
- Money Transfer
- Africa
- Stablecoins
- Virtual Accounts
- Webhooks
website: https://www.afriex.com/
---
