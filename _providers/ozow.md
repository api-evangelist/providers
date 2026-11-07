---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 2
  name: Ozow Agentic Access
  operation_count: 5
  slug: ozow-agentic-access
  summary_line: 5 operations · 2 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.ozow.com
  baseurl_source: declared
  description: Retrieve the list of supported banks for the payment flow.
  name: Ozow Banks API
  slug: ozow-banks-api
- baseURL: https://api.ozow.com
  baseurl_source: declared
  description: Create and initiate instant EFT payment requests.
  name: Ozow Payments API
  slug: ozow-payments-api
- baseURL: https://api.ozow.com
  baseurl_source: declared
  description: Refund previously completed EFT payments from the merchant float.
  name: Ozow Refunds API
  slug: ozow-refunds-api
- baseURL: https://api.ozow.com
  baseurl_source: declared
  description: Query transaction status by Ozow reference or merchant reference.
  name: Ozow Transactions API
  slug: ozow-transactions-api
artifact_total: 26
asyncapis:
- description: ''
  name: Ozow Webhooks
  slug: ozow-webhooks
collections:
- collection_type: postman
  name: Ozow Banks API
  slug: postman-ozow-banks-api
- collection_type: postman
  name: Ozow Banks Payments API
  slug: postman-ozow-payments-api
- collection_type: postman
  name: Ozow Banks Refunds API
  slug: postman-ozow-refunds-api
- collection_type: postman
  name: Ozow Banks Transactions API
  slug: postman-ozow-transactions-api
- collection_type: open
  name: Ozow Banks API
  slug: open-ozow-banks-api
- collection_type: open
  name: Ozow Banks Payments API
  slug: open-ozow-payments-api
- collection_type: open
  name: Ozow Banks Refunds API
  slug: open-ozow-refunds-api
- collection_type: open
  name: Ozow Banks Transactions API
  slug: open-ozow-transactions-api
common:
- group: other
  href: https://artifacts.apis.io/ozow/capabilities/ozow-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ozow-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ozow/overview
- group: agent
  href: https://artifacts.apis.io/ozow/agentic-access/ozow-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ozow-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ozow/security/ozow-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ozow-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ozow/security/ozow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ozow-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ozow/security/ozow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ozow-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ozow/authentication/ozow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ozow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://za.linkedin.com/company/ozowsecurepayments
- group: company
  title: ''
  type: Website
  url: https://ozow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hub.ozow.com/docs
- group: commercial
  href: https://artifacts.apis.io/ozow/plans/ozow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ozow-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ozow/rate-limits/ozow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ozow-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ozow/finops/ozow-finops.yml
  title: ''
  type: FinOps
  url: finops/ozow-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ozow.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.ozow.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://hub.ozow.com/docs
- group: operate
  title: ''
  type: Support
  url: https://ozow.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://ozow.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.ozow.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ozow.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ozow.com/privacy-policy
- group: build
  href: https://artifacts.apis.io/ozow/packages/ozow-packages.yml
  title: ''
  type: Packages
  url: packages/ozow-packages.yml
- group: agent
  href: https://artifacts.apis.io/ozow/mcp/ozow-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ozow-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ozow/llms/ozow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ozow-llms.txt
- group: other
  href: https://artifacts.apis.io/ozow/overlays/ozow-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ozow-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/ozow/conformance/ozow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ozow-conformance.yml
- group: auth
  href: https://artifacts.apis.io/ozow/security/ozow-trust-center.yml
  title: ''
  type: Compliance
  url: security/ozow-trust-center.yml
- group: design
  href: https://artifacts.apis.io/ozow/errors/ozow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ozow-problem-types.yml
- group: build
  href: https://artifacts.apis.io/ozow/errors/ozow-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/ozow-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/ozow/lifecycle/ozow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ozow-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/ozow/sandbox/ozow-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ozow-sandbox.yml
- group: design
  href: https://artifacts.apis.io/ozow/conventions/ozow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ozow-conventions.yml
- group: design
  href: https://artifacts.apis.io/ozow/components/ozow-components.yml
  title: ''
  type: Components
  url: components/ozow-components.yml
- group: design
  href: https://artifacts.apis.io/ozow/data-model/ozow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ozow-data-model.yml
- group: design
  href: https://artifacts.apis.io/ozow/asyncapi/ozow-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ozow-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/ozow/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Ozow (formerly i-Pay) is a South African fintech providing an instant EFT / "Pay by Bank" payment gateway. Merchants create a server-side payment request, redirect the customer to the Ozow secure bank-selection flow, and reconcile via a server-to-server notification. The REST API is ZAR-only (CountryCode ZA), authenticated with an ApiKey header and a SHA512 HashCheck built from a merchant PrivateKey.
finops:
- has_sources: true
  method: derived
  name: Ozow Finops
  primary_unit: transaction
  service_category: ''
  slug: ozow-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ozow.png
layout: provider
modified: '2026-07-17'
name: Ozow
nav: Providers
network: true
overview: 'Ozow publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Banks API, Payments API, Refunds API, and 1 more. Tagged areas include Payments, Instant EFT, Pay by Bank, Fintech, and South Africa.


  The Ozow catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Ozow''s developer surface includes authentication, documentation, engineering blog, getting-started guide, support, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Ozow Plans Pricing
  plan_count: 16
  slug: ozow-plans-pricing
- name: Ozow Price Estimates
  plan_count: 0
  slug: ozow-price-estimates
random_paper: 7
rate_limits:
- limit_count: 2
  name: Ozow Rate Limits
  slug: ozow-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Ozow API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: ozow-rules
score:
  band: strong
  composite: 55.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 58.5
    catalog_earned_first_party: 12.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    contract_governance: 31.8
    contract_quality: 56.4
    developer_ergonomics: 36.3
    discoverability: 73.2
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-africa
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ozow/ozow-2026-08-07T191227.png
security:
- kind: authentication
  name: Ozow Authentication
  slug: ozow-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ozow Domain Security
  slug: ozow-domain-security
  summary_line: HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ozow Vulnerability Disclosure
  slug: ozow-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ozow Trust Center
  slug: ozow-trust-center
  summary_line: PCI DSS Level 1, ISO/IEC 27001
skill_count: 3
skills:
- name: Collect an instant EFT payment and confirm it
  slug: ozow-collect-payment
- name: Reconcile a transaction by reference or id
  slug: ozow-reconcile-transaction
- name: Refund a completed EFT payment
  slug: ozow-refund-payment
slug: ozow
tags:
- Payments
- Instant EFT
- Pay by Bank
- Fintech
- South Africa
website: https://ozow.com/
---
