---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Paytabs Agentic Access
  operation_count: 2
  slug: paytabs-agentic-access
  summary_line: 2 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://secure.paytabs.com
  baseurl_source: declared
  description: Create and manage transactions.
  name: PayTabs Payments API
  slug: paytabs-payments-api
- baseURL: https://secure.paytabs.com
  baseurl_source: declared
  description: Query and manage existing transactions.
  name: PayTabs Transactions API
  slug: paytabs-transactions-api
artifact_total: 16
asyncapis:
- description: 'PayTabs delivers transaction outcomes to merchants via server-to-server HTTP POST notifications. There are two flavors of the same payload: the Callback (a one-time notification whose URL is passed pe'
  name: PayTabs IPN / Callback Notifications
  slug: paytabs-webhooks-asyncapi
collections:
- collection_type: postman
  name: PayTabs PT2 Payments API
  slug: postman-paytabs-payments-api
- collection_type: postman
  name: PayTabs PT2 Payments Transactions API
  slug: postman-paytabs-transactions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PayTabs PT2 Payments API
  slug: open-paytabs-payments-api
- collection_type: open
  name: PayTabs PT2 Payments Transactions API
  slug: open-paytabs-transactions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/paytabs/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paytabs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/paytabs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paytabs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paytabs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paytabs-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paytabscom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paytabs
- group: company
  title: ''
  type: Website
  url: https://paytabs.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paytabs.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/paytabs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paytabs-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paytabs-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://paytabs.com/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paytabs.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paytabs.com/PT2-API-Endpoints/Introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://documenter.getpostman.com/view/14575178/TWDRtfWG
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/14575178/TWDRtfWG
- group: operate
  title: ''
  type: Support
  url: https://support.paytabs.com/en/support/home
- group: commercial
  title: ''
  type: Pricing
  url: https://paytabs.com/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://merchant.paytabs.com/merchant/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai.paytabs.com/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai.paytabs.com/en/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paytabs.com/
- group: auth
  title: ''
  type: Security
  url: https://ai.paytabs.com/en/security-compliance/
- group: auth
  title: ''
  type: Compliance
  url: https://ai.paytabs.com/en/security-compliance/
- group: build
  title: ''
  type: Packages
  url: packages/paytabs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paytabs-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/paytabs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paytabs-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/paytabs-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/paytabs-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paytabs-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/paytabs-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paytabs-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paytabs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/paytabs-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paytabs-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/paytabs-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paytabs-webhooks-asyncapi.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paytabs-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: PayTabs is a Saudi-built payment orchestration and gateway provider serving merchants across MENA. The PT2 REST API accepts cards and local methods (mada, Meeza, KNET, OmanNet, Benefit, STC Pay, urpay) plus Apple Pay, Google Pay and Samsung Pay through hosted, managed and own-form flows, with tokenization, recurring billing and invoicing. The API is served on region-specific hosts and authenticated with a merchant server key.
finops:
- name: Paytabs Finops
  service_category: Payment Processing
  slug: paytabs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paytabs.png
layout: provider
modified: '2026-07-17'
name: PayTabs
nav: Providers
network: true
overview: 'PayTabs publishes 2 APIs on the [APIs.io](https://apis.io/) network: Payments API and Transactions API. Tagged areas include Payments, Payment Gateway, Fintech, MENA, and Saudi Arabia.


  The PayTabs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PayTabs'' developer surface includes authentication, documentation, engineering blog, getting-started guide, API reference, support, pricing, and 35 more developer resources.'
plans:
- name: Paytabs Plans Pricing
  plan_count: 2
  slug: paytabs-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Paytabs Rate Limits
  slug: paytabs-rate-limits
score:
  band: exemplar
  composite: 70.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 63.1
    developer_ergonomics: 78.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 70.6
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
    score: 78.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paytabs/refs/heads/main/screenshots/paytabs-2026-08-07T191705.png
security:
- kind: authentication
  name: Paytabs Authentication
  slug: paytabs-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Paytabs Domain Security
  slug: paytabs-domain-security
  summary_line: no transport/DNS hardening detected
- kind: vulnerability-disclosure
  name: Paytabs Vulnerability Disclosure
  slug: paytabs-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Paytabs Trust Center
  slug: paytabs-trust-center
  summary_line: PCI DSS Level 1, EMV 3-D Secure 2 (Modirum), mada / Saudi National Payment Gateway certified
slug: paytabs
tags:
- Payments
- Payment Gateway
- Fintech
- MENA
- Saudi Arabia
- Cards
- mada
website: https://paytabs.com/en/
---
