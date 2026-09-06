---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Capitalist Agentic Access
  operation_count: 1
  slug: capitalist-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- baseURL: https://api2.capitalist.net
  baseurl_source: declared
  description: The current Capitalist API — published as the "Integration API" — enables programmatic mass payouts, currency and digital-asset conversion, and balance, transaction and merchant-order reporting across
  name: Capitalist API
  slug: capitalist-api
- baseURL: https://api.capitalist.net
  baseurl_source: declared
  description: 'The first generation of the Capitalist API: a single HTTP POST endpoint at https://api.capitalist.net where an `operation` form field selects the call (get_accounts, import_batch_advanced, process_bat'
  name: Capitalist Payments API (v1, deprecated)
  slug: capitalist-capitalist-payments-api-api
artifact_total: 12
asyncapis:
- description: ''
  name: Capitalist Webhooks
  slug: capitalist-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Capitalist Payments Capitalist Payments API API
  slug: open-capitalist-capitalist-payments-api-api
- collection_type: open
  name: Capitalist Payments API
  slug: open-capitalist
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/capitalist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capitalist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/capitalist-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/capitalist-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/capitalist-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/capitalist-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/capitalist-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/capitalist-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/capitalist-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/capitalist-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/capitalist-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/capitalist-finops.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/capitalist-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/capitalist-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/capitalist-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/capitalist-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/capitalist-mcp.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capitalist-net
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capitalist-inc
- group: company
  title: ''
  type: Website
  url: https://capitalist.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://capitalist.net/developers/api
- group: docs
  title: ''
  type: Documentation
  url: https://capitalist.net/developers/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.capitalist.net/api/integration-api.html
- group: operate
  title: ''
  type: Support
  url: https://capitalist.net/support
- group: company
  title: ''
  type: Blog
  url: https://capitalist.net/news
- group: start
  title: ''
  type: Signup
  url: https://capitalist.net/reg
- group: start
  title: ''
  type: Login
  url: https://capitalist.net/login
- group: commercial
  title: ''
  type: Pricing
  url: https://capitalist.net/fees
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capitalist.net/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capitalist.net/useragreement
created: '2024-11-05'
description: Capitalist is a payment platform that lets businesses make mass payouts and receive money across multiple payment systems and cryptocurrencies without having to open separate accounts with each. The Capitalist Integration API automates bulk payouts to cards, bank transfers, mobile operators, fast payment systems, e-wallets and cryptocurrencies, converts between fiat and digital-asset balances, reads exchange rates and account balances, retrieves transaction and merchant-order history, and runs end-user KYC — for fintech, affiliate-network, and marketplace use cases operating across the CIS region and globally.
finops:
- name: Capitalist Finops
  service_category: API
  slug: capitalist-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capitalist.png
layout: provider
modified: '2026-09-05'
name: Capitalist
nav: Providers
network: true
overview: 'Capitalist publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Payments API (v1, deprecated), and 1 more. Tagged areas include Bulk Payouts, Cryptocurrency, Finance, Mass Payments, and Payment Platform.


  The Capitalist catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Capitalist''s developer surface includes authentication, documentation, API reference, support, engineering blog, signup flow, pricing, and 24 more developer resources.'
plans:
- name: Capitalist Plans Pricing
  plan_count: 0
  slug: capitalist-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Capitalist Rate Limits
  slug: capitalist-rate-limits
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.6
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 58.4
    developer_ergonomics: 54.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/capitalist/refs/heads/main/screenshots/capitalist-2026-06-20T173944.png
security:
- kind: authentication
  name: Capitalist Authentication
  slug: capitalist-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Capitalist Domain Security
  slug: capitalist-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: capitalist
tags:
- Bulk Payouts
- Cryptocurrency
- Finance
- Mass Payments
- Payment Platform
- Payments
- Payouts
- Remittance
website: https://capitalist.net/
---
