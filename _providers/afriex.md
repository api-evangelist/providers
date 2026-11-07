---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    mcp_tool_quality: three_quarters
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Afriex publishes a hosted, remote Model Context Protocol server at https://mcp.afriex.com/mcp that exposes 26 tools covering the Business API surface — customers, transactions, payment methods, instit
  name: Afriex MCP Server
  slug: afriex-mcp-server
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: View and top up your business wallet balances.
  name: Afriex Balance API
  slug: afriex-balance-api
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: Create hosted checkout sessions.
  name: Afriex Checkout Sessions API
  slug: afriex-checkout-sessions-api
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: Create and manage your customers.
  name: Afriex Customers API
  slug: afriex-customers-api
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: Generate presigned URLs for secure file uploads.
  name: Afriex Media API
  slug: afriex-media-api
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: Register and resolve customer payout and collection methods.
  name: Afriex Payment Methods API
  slug: afriex-payment-methods-api
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: Fetch real-time exchange rates.
  name: Afriex Rates API
  slug: afriex-rates-api
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: The SME Registration API from Afriex — 2 operation(s) for sme registration.
  name: Afriex SME Registration API
  slug: afriex-sme-registration-api
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: Create and track deposits, withdrawals, and swaps.
  name: Afriex Transactions API
  slug: afriex-transactions-api
- baseURL: https://api.afriex.com
  baseurl_source: declared
  description: Webhook event payloads and sandbox webhook testing.
  name: Afriex Webhooks API
  slug: afriex-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Afriex Business Webhooks
  slug: afriex-business-webhooks
common:
- group: other
  href: https://artifacts.apis.io/afriex/capabilities/afriex-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/afriex-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/afriex/security/afriex-domain-security.yml
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
  href: https://artifacts.apis.io/afriex/llms/afriex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afriex-llms.txt
- group: other
  href: https://artifacts.apis.io/afriex/a2a/afriex-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/afriex-a2a.yml
- group: agent
  href: https://artifacts.apis.io/afriex/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/afriex/packages/afriex-packages.yml
  title: ''
  type: Packages
  url: packages/afriex-packages.yml
- group: build
  href: https://artifacts.apis.io/afriex/packages/afriex-packages.yml
  title: ''
  type: SDKs
  url: packages/afriex-packages.yml
- group: auth
  href: https://artifacts.apis.io/afriex/authentication/afriex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/afriex-authentication.yml
- group: design
  href: https://artifacts.apis.io/afriex/conventions/afriex-conventions.yml
  title: ''
  type: Conventions
  url: conventions/afriex-conventions.yml
- group: design
  href: https://artifacts.apis.io/afriex/conventions/afriex-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/afriex-conventions.yml
- group: design
  href: https://artifacts.apis.io/afriex/errors/afriex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/afriex-problem-types.yml
- group: design
  href: https://artifacts.apis.io/afriex/lifecycle/afriex-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/afriex-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/afriex/conformance/afriex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/afriex-conformance.yml
- group: design
  href: https://artifacts.apis.io/afriex/data-model/afriex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/afriex-data-model.yml
- group: start
  href: https://artifacts.apis.io/afriex/sandbox/afriex-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/afriex-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/afriex/rate-limits/afriex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/afriex-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/afriex/plans/afriex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/afriex-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/afriex/well-known/afriex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/afriex-well-known.yml
- group: other
  href: https://artifacts.apis.io/afriex/overlays/afriex-business-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/afriex-business-overlay.yaml
created: '2026-09-12'
description: 'Afriex is a cross-border payments and remittance company that moves money between Africa, North America, Europe and Asia. Its consumer app handles person-to-person remittances, while the Afriex Business API gives companies programmatic access to the same rails: customer onboarding and KYC, payment methods across bank accounts, mobile money, SWIFT, UPI, Interac and USDC/USDT crypto wallets, multi-currency wallet balances and real-time FX rates, deposits, withdrawals and in-wallet currency swaps, hosted checkout sessions, virtual and pool collection accounts, and RSA-signed webhooks for transaction lifecycle events. The API is documented with an OpenAPI 3.1 contract, a first-party TypeScript SDK, and a hosted remote MCP server that exposes the same surface to AI agents.'
finops:
- has_sources: true
  method: derived
  name: Afriex Finops
  primary_unit: ''
  service_category: ''
  slug: afriex-finops
  template: true
image: https://cdn.prod.website-files.com/62ce94ab2b9c3a3597a7acd4/62f26e44523cfa8d7d76823e_Website%20Open%20Graph.webp
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.afriex.com over HTTP requiring an API key; 26 tools listed.
  name: Afriex MCP Server
  slug: afriex-api
modified: '2026-09-12'
name: Afriex
nav: Providers
network: true
overview: 'Afriex publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Balance API, Checkout Sessions API, Customers API, and 7 more. Tagged areas include Payments, Remittances, Cross-Border Payments, Fintech, and Financial Services.


  The Afriex catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Afriex''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, authentication, sandbox, and 23 more developer resources.'
plans:
- name: Afriex Plans Pricing
  plan_count: 0
  slug: afriex-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Afriex Rate Limits
  slug: afriex-rate-limits
rules:
- authorship: generated
  effective_rule_count: 118
  extends:
  - spectral:oas
  name: Afriex API Rules
  rule_count: 77
  severity_counts:
    error: 68
    hint: 0
    info: 1
    warn: 8
  slug: afriex-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 62.6
    developer_ergonomics: 73.8
    discoverability: 75.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 50.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/afriex/afriex-2026-10-11T093034.png
security:
- kind: authentication
  name: Afriex Authentication
  slug: afriex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Afriex Domain Security
  slug: afriex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Afriex
  slug: afriex-business-api-skill
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
- Webhook
- A2A
website: https://www.afriex.com/
---
