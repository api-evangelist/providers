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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 3
  name: Telr Agentic Access
  operation_count: 5
  slug: telr-agentic-access
  summary_line: 5 operations · 4 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Marketplace / split-payment Service API for sub-merchant onboarding, multi-split payments, debit/credit of sub-merchant accounts, payouts, and transaction reconciliation. Authenticated with HTTP Basic
  name: Telr Accounts and Split Payments API
  slug: telr-accounts-split-payments-api
- description: Remote creation of QuickLink payment links and e-invoices with extra data fields, for merchants who collect payment without a full checkout integration.
  name: Telr QuickLink and E-Invoicing API
  slug: telr-quicklink-einvoicing-api
- description: EMV Secure Remote Commerce (Click to Pay) checkout, available as a seamless integration or through the remote JSON API for tokenized card-on-file payments.
  name: Telr Click to Pay (C2P) API
  slug: telr-click-to-pay-api
- baseURL: https://secure.telr.com/gateway
  baseurl_source: declared
  description: Repeat billing / recurring agreement management.
  name: Telr Agreements API
  slug: telr-agreements-api
- baseURL: https://secure.telr.com/gateway
  baseurl_source: declared
  description: Redirect-based hosted checkout (order.json).
  name: Telr Hosted Payment Page API
  slug: telr-hosted-payment-page-api
- baseURL: https://secure.telr.com/gateway
  baseurl_source: declared
  description: Newer REST order API with HTTP Basic auth.
  name: Telr Payments API API
  slug: telr-payments-api-api
- baseURL: https://secure.telr.com/gateway
  baseurl_source: declared
  description: Direct server-to-server card and wallet transactions (remote.json).
  name: Telr Remote API
  slug: telr-remote-api
artifact_total: 25
asyncapis:
- description: ''
  name: Telr Webhooks
  slug: telr-webhooks
collections:
- collection_type: postman
  name: Telr Payment Gateway Agreements API
  slug: postman-telr-agreements-api
- collection_type: postman
  name: Telr Payment Gateway Agreements Hosted Payment Page API
  slug: postman-telr-hosted-payment-page-api
- collection_type: postman
  name: Telr Payment Gateway Agreements Payments API API
  slug: postman-telr-payments-api-api
- collection_type: postman
  name: Telr Payment Gateway Agreements Remote API
  slug: postman-telr-remote-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Telr Payment Gateway Agreements API
  slug: open-telr-agreements-api
- collection_type: open
  name: Telr Payment Gateway Agreements Hosted Payment Page API
  slug: open-telr-hosted-payment-page-api
- collection_type: open
  name: Telr Payment Gateway Agreements Payments API API
  slug: open-telr-payments-api-api
- collection_type: open
  name: Telr Payment Gateway Agreements Remote API
  slug: open-telr-remote-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/telr/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/telr-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/telr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telr-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://telr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telr.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/telr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/telr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/telr-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telr
- group: company
  title: ''
  type: Blog
  url: https://telr.com/blog/
- group: build
  title: ''
  type: Packages
  url: packages/telr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/telr-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telr-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/telr-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/telr-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/telr-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://telr.com/secure
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/telr-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/telr-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telr-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telr-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/telr-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/telr-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/telr-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: collections/telr.postman_collection.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Telr-PG
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.telr.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.telr.com/reference/get-started
- group: operate
  title: ''
  type: Support
  url: https://telr.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://telr.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://telr.com/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://telr.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://telr.com/privacy-policy/
created: '2026-07-17'
description: Telr is a Dubai-headquartered online payment gateway operating across the MENA region (UAE, Saudi Arabia, Bahrain, Jordan), supporting 120+ currencies and 30 languages. Its HTTPS/JSON gateway exposes a Hosted Payment Page, a Remote (direct) card and wallet API, repeat-billing agreements, mobile SDKs, and a newer REST Payments API - all PCI DSS v4.0 Level 1 and NESA certified.
finops:
- name: Telr Finops
  service_category: Financial Services
  slug: telr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telr.png
layout: provider
modified: '2026-07-18'
name: Telr
nav: Providers
network: true
overview: 'Telr publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agreements API, Hosted Payment Page API, Payments API API, and 1 more. Tagged areas include Payments, Payment Gateway, Fintech, MENA, and UAE.


  The Telr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Telr''s developer surface includes authentication, documentation, engineering blog, sandbox, getting-started guide, support, pricing, and 30 more developer resources.'
plans:
- name: Telr Plans Pricing
  plan_count: 7
  slug: telr-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Telr Rate Limits
  slug: telr-rate-limits
score:
  band: exemplar
  composite: 68.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 61.1
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 68.9
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
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telr/refs/heads/main/screenshots/telr-2026-08-17T082306.png
security:
- kind: authentication
  name: Telr Authentication
  slug: telr-authentication
  summary_line: http/custom · 2 schemes
- kind: domain-security
  name: Telr Domain Security
  slug: telr-domain-security
  summary_line: no transport/DNS hardening detected
- kind: vulnerability-disclosure
  name: Telr Vulnerability Disclosure
  slug: telr-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Telr Trust Center
  slug: telr-trust-center
  summary_line: PCI DSS v4.0 Level 1, NESA, Central Bank of the UAE Retail Payment Services License, 3-D Secure, GDPR
slug: telr
tags:
- Payments
- Payment Gateway
- Fintech
- MENA
- UAE
website: https://telr.com/
---
