---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 3
  name: Fazz Agentic Access
  operation_count: 8
  slug: fazz-agentic-access
  summary_line: 8 operations · 3 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Indonesia-market payments and disbursements (v4-ID) covering local virtual accounts and bank transfers, billed in IDR. Shares the Fazz/Xfers v4 request patterns with region-specific methods and destin
  name: Fazz Indonesia Payments API (v4-ID)
  slug: fazz-indonesia-payments-api
- description: HTTP POST webhook callbacks that notify your endpoint of payment and disbursement status changes in JSON, verified against your account signing secret.
  name: Fazz Callbacks (Webhooks)
  slug: fazz-callbacks
- baseURL: https://www.xfers.io/api/v4
  baseurl_source: declared
  description: Send API — disburse funds to recipients (payouts).
  name: Fazz Disbursements API
  slug: fazz-disbursements-api
- baseURL: https://www.xfers.io/api/v4
  baseurl_source: declared
  description: Create reusable payment method objects (PayNow, virtual bank account).
  name: Fazz Payment Methods API
  slug: fazz-payment-methods-api
- baseURL: https://www.xfers.io/api/v4
  baseurl_source: declared
  description: Accept API — create and query payments (collections).
  name: Fazz Payments API
  slug: fazz-payments-api
artifact_total: 24
asyncapis:
- description: ''
  name: Fazz Webhooks
  slug: fazz-webhooks
collections:
- collection_type: postman
  name: Fazz Payments API (Singapore v4) Disbursements API
  slug: postman-fazz-disbursements-api
- collection_type: postman
  name: Fazz Payments API (Singapore v4) Disbursements Payment Methods API
  slug: postman-fazz-payment-methods-api
- collection_type: postman
  name: Fazz API (Singapore v4) Disbursements Payments API
  slug: postman-fazz-payments-api
- collection_type: open
  name: Fazz Payments API (Singapore v4) Disbursements API
  slug: open-fazz-disbursements-api
- collection_type: open
  name: Fazz Payments API (Singapore v4) Disbursements Payment Methods API
  slug: open-fazz-payment-methods-api
- collection_type: open
  name: Fazz API (Singapore v4) Disbursements Payments API
  slug: open-fazz-payments-api
common:
- group: company
  title: ''
  type: Blog
  url: https://fazz.com/id/newsroom/
- group: other
  href: https://artifacts.apis.io/fazz/capabilities/fazz-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fazz-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fazz/overview
- group: agent
  href: https://artifacts.apis.io/fazz/agentic-access/fazz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fazz-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fazz/security/fazz-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fazz-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fazz/security/fazz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fazz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fazz/security/fazz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fazz-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fazz/authentication/fazz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fazz-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xfers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fazz-financial
- group: company
  title: ''
  type: Website
  url: https://fazz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fazz.com/
- group: commercial
  href: https://artifacts.apis.io/fazz/plans/fazz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fazz-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fazz/rate-limits/fazz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fazz-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fazz/finops/fazz-finops.yml
  title: ''
  type: FinOps
  url: finops/fazz-finops.yml
- group: build
  href: https://artifacts.apis.io/fazz/packages/fazz-packages.yml
  title: ''
  type: Packages
  url: packages/fazz-packages.yml
- group: build
  href: https://artifacts.apis.io/fazz/packages/fazz-packages.yml
  title: ''
  type: SDKs
  url: packages/fazz-packages.yml
- group: agent
  href: https://artifacts.apis.io/fazz/well-known/fazz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fazz-well-known.yml
- group: agent
  href: https://artifacts.apis.io/fazz/llms/fazz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fazz-llms.txt
- group: agent
  href: https://artifacts.apis.io/fazz/mcp/fazz-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fazz-mcp.yml
- group: other
  href: https://artifacts.apis.io/fazz/overlays/fazz-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fazz-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/fazz/conformance/fazz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fazz-conformance.yml
- group: design
  href: https://artifacts.apis.io/fazz/errors/fazz-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/fazz-error-codes.yml
- group: design
  href: https://artifacts.apis.io/fazz/lifecycle/fazz-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fazz-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fazz/conventions/fazz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fazz-conventions.yml
- group: design
  href: https://artifacts.apis.io/fazz/conventions/fazz-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/fazz-conventions.yml
- group: operate
  href: https://artifacts.apis.io/fazz/changelog/fazz-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fazz-changelog.yml
- group: start
  href: https://artifacts.apis.io/fazz/sandbox/fazz-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fazz-sandbox.yml
- group: design
  href: https://artifacts.apis.io/fazz/data-model/fazz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fazz-data-model.yml
- group: design
  href: https://artifacts.apis.io/fazz/asyncapi/fazz-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fazz-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/fazz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/fazz/collections/fazz.postman_collection.json
  title: ''
  type: Postman
  url: collections/fazz.postman_collection.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fazz.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fazz.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support-sg.fazz.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fazz.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fazz.com/privacy-policy
created: '2026-07-17'
description: Fazz is a Southeast Asian business banking and payments group formed from the 2021 merger of Indonesia's Payfazz and Singapore's Xfers. Its Fazz Business Payments API (served on the xfers.io hosts) lets platforms accept payments via local methods like PayNow QR and virtual bank accounts, and send bulk disbursements across Singapore (SGD) and Indonesia (IDR). Not to be confused with the consumer-facing Payfazz agent app.
finops:
- has_sources: true
  method: generated
  name: Fazz Finops
  primary_unit: ''
  service_category: Financial Services
  slug: fazz-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fazz.png
layout: provider
modified: '2026-10-06'
name: Fazz
nav: Providers
network: true
overview: 'Fazz publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Disbursements API, Payment Methods API, Payments API, and 2 more. Tagged areas include Fintech, Payments, Business Banking, Disbursements, and Southeast Asia.


  The Fazz catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Fazz''s developer surface includes engineering blog, authentication, documentation, changelog, sandbox, getting-started guide, support, and 30 more developer resources.'
plans:
- name: Fazz Plans Pricing
  plan_count: 2
  slug: fazz-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Fazz Rate Limits
  slug: fazz-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Fazz API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: fazz-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 8.1
    developer_ergonomics: 74.4
    discoverability: 73.2
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fazz/fazz-2026-07-25T214301.png
security:
- kind: authentication
  name: Fazz Authentication
  slug: fazz-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fazz Domain Security
  slug: fazz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fazz Vulnerability Disclosure
  slug: fazz-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Fazz Trust Center
  slug: fazz-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: Accept a payment with Fazz
  slug: fazz-accept-a-payment
- name: Create a reusable Fazz payment method
  slug: fazz-reusable-payment-method
- name: Send a disbursement with Fazz
  slug: fazz-send-a-disbursement
slug: fazz
tags:
- Fintech
- Payments
- Business Banking
- Disbursements
- Southeast Asia
- PayNow
- Virtual Accounts
website: https://fazz.com/
---
