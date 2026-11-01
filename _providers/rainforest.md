---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 53
  human_in_the_loop: 1
  name: Rainforest Agentic Access
  operation_count: 82
  slug: rainforest-agentic-access
  summary_line: 82 operations · 53 acting · 1 human-in-the-loop
api_count: 7
apis:
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for ACH return functions.
  name: Rainforest ACH Returns API
  slug: rainforest-ach-returns-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for api key functions.
  name: Rainforest API Keys API
  slug: rainforest-api-keys-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for billing profile functions.
  name: Rainforest Billing Profiles API
  slug: rainforest-billing-profiles-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for BIN lookup functions.
  name: Rainforest BIN Lookups API
  slug: rainforest-bin-lookups-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for chargeback functions.
  name: Rainforest Chargebacks API
  slug: rainforest-chargebacks-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for deposit method config functions.
  name: Rainforest Deposit Method Configs API
  slug: rainforest-deposit-method-configs-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for deposit method functions.
  name: Rainforest Deposit Methods API
  slug: rainforest-deposit-methods-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for deposit functions.
  name: Rainforest Deposits API
  slug: rainforest-deposits-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for device functions.
  name: Rainforest Devices API
  slug: rainforest-devices-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for file upload config functions.
  name: Rainforest File Upload Configs API
  slug: rainforest-file-upload-configs-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for file upload functions.
  name: Rainforest File Uploads API
  slug: rainforest-file-uploads-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for forwarding sensitive data to 3rd parties.
  name: Rainforest Forward Requests API
  slug: rainforest-forward-requests-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for health functions.
  name: Rainforest Health API
  slug: rainforest-health-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for merchant application functions.
  name: Rainforest Merchant Applications API
  slug: rainforest-merchant-applications-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for merchant functions.
  name: Rainforest Merchants API
  slug: rainforest-merchants-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for payin configs functions.
  name: Rainforest Payin Configs API
  slug: rainforest-payin-configs-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for payin functions.
  name: Rainforest Payins API
  slug: rainforest-payins-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for payment method configs functions.
  name: Rainforest Payment Method Configs API
  slug: rainforest-payment-method-configs-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for payment method domain functions.
  name: Rainforest Payment Method Domains API
  slug: rainforest-payment-method-domains-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for payment method functions.
  name: Rainforest Payment Methods API
  slug: rainforest-payment-methods-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for payment functions.
  name: Rainforest Payments API
  slug: rainforest-payments-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for refund functions.
  name: Rainforest Refunds API
  slug: rainforest-refunds-api
- baseURL: https://api.rainforestpay.com
  baseurl_source: declared
  description: Resources for session functions.
  name: Rainforest Sessions API
  slug: rainforest-sessions-api
arazzos:
- description: Create a payin config with an idempotency key, process the payin, and confirm its status.
  name: Rainforest — configure and process a payin
  slug: rainforest-collect-payment
- description: Create a merchant, submit its application, and confirm it reaches ACTIVE.
  name: Rainforest — onboard a merchant
  slug: rainforest-onboard-merchant
artifact_total: 83
asyncapis:
- description: ''
  name: Rainforest Webhooks
  slug: rainforest-webhooks
collections:
- collection_type: postman
  name: Authentication ACH Returns API
  slug: postman-rainforest-ach-returns-api
- collection_type: postman
  name: Authentication ACH Returns API Keys API
  slug: postman-rainforest-api-keys-api
- collection_type: postman
  name: Authentication ACH Returns Billing Profiles API
  slug: postman-rainforest-billing-profiles-api
- collection_type: postman
  name: Authentication ACH Returns BIN Lookups API
  slug: postman-rainforest-bin-lookups-api
- collection_type: postman
  name: Authentication ACH Returns Chargebacks API
  slug: postman-rainforest-chargebacks-api
- collection_type: postman
  name: Authentication ACH Returns Deposit Method Configs API
  slug: postman-rainforest-deposit-method-configs-api
- collection_type: postman
  name: Authentication ACH Returns Deposit Methods API
  slug: postman-rainforest-deposit-methods-api
- collection_type: postman
  name: Authentication ACH Returns Deposits API
  slug: postman-rainforest-deposits-api
- collection_type: postman
  name: Authentication ACH Returns Devices API
  slug: postman-rainforest-devices-api
- collection_type: postman
  name: Authentication ACH Returns File Upload Configs API
  slug: postman-rainforest-file-upload-configs-api
- collection_type: postman
  name: Authentication ACH Returns File Uploads API
  slug: postman-rainforest-file-uploads-api
- collection_type: postman
  name: Authentication ACH Returns Forward Requests API
  slug: postman-rainforest-forward-requests-api
- collection_type: postman
  name: Authentication ACH Returns Health API
  slug: postman-rainforest-health-api
- collection_type: postman
  name: Authentication ACH Returns Merchant Applications API
  slug: postman-rainforest-merchant-applications-api
- collection_type: postman
  name: Authentication ACH Returns Merchants API
  slug: postman-rainforest-merchants-api
- collection_type: postman
  name: Authentication ACH Returns Payin Configs API
  slug: postman-rainforest-payin-configs-api
- collection_type: postman
  name: Authentication ACH Returns Payins API
  slug: postman-rainforest-payins-api
- collection_type: postman
  name: Authentication ACH Returns Payment Method Configs API
  slug: postman-rainforest-payment-method-configs-api
- collection_type: postman
  name: Authentication ACH Returns Payment Method Domains API
  slug: postman-rainforest-payment-method-domains-api
- collection_type: postman
  name: Authentication ACH Returns Payment Methods API
  slug: postman-rainforest-payment-methods-api
- collection_type: postman
  name: Authentication ACH Returns Payments API
  slug: postman-rainforest-payments-api
- collection_type: postman
  name: Authentication ACH Returns Refunds API
  slug: postman-rainforest-refunds-api
- collection_type: postman
  name: Authentication ACH Returns Sessions API
  slug: postman-rainforest-sessions-api
- collection_type: open
  name: Authentication ACH Returns API
  slug: open-rainforest-ach-returns-api
- collection_type: open
  name: Authentication ACH Returns API Keys API
  slug: open-rainforest-api-keys-api
- collection_type: open
  name: Authentication ACH Returns Billing Profiles API
  slug: open-rainforest-billing-profiles-api
- collection_type: open
  name: Authentication ACH Returns BIN Lookups API
  slug: open-rainforest-bin-lookups-api
- collection_type: open
  name: Authentication ACH Returns Chargebacks API
  slug: open-rainforest-chargebacks-api
- collection_type: open
  name: Authentication ACH Returns Deposit Method Configs API
  slug: open-rainforest-deposit-method-configs-api
- collection_type: open
  name: Authentication ACH Returns Deposit Methods API
  slug: open-rainforest-deposit-methods-api
- collection_type: open
  name: Authentication ACH Returns Deposits API
  slug: open-rainforest-deposits-api
- collection_type: open
  name: Authentication ACH Returns Devices API
  slug: open-rainforest-devices-api
- collection_type: open
  name: Authentication ACH Returns File Upload Configs API
  slug: open-rainforest-file-upload-configs-api
- collection_type: open
  name: Authentication ACH Returns File Uploads API
  slug: open-rainforest-file-uploads-api
- collection_type: open
  name: Authentication ACH Returns Forward Requests API
  slug: open-rainforest-forward-requests-api
- collection_type: open
  name: Authentication ACH Returns Health API
  slug: open-rainforest-health-api
- collection_type: open
  name: Authentication ACH Returns Merchant Applications API
  slug: open-rainforest-merchant-applications-api
- collection_type: open
  name: Authentication ACH Returns Merchants API
  slug: open-rainforest-merchants-api
- collection_type: open
  name: Authentication ACH Returns Payin Configs API
  slug: open-rainforest-payin-configs-api
- collection_type: open
  name: Authentication ACH Returns Payins API
  slug: open-rainforest-payins-api
- collection_type: open
  name: Authentication ACH Returns Payment Method Configs API
  slug: open-rainforest-payment-method-configs-api
- collection_type: open
  name: Authentication ACH Returns Payment Method Domains API
  slug: open-rainforest-payment-method-domains-api
- collection_type: open
  name: Authentication ACH Returns Payment Methods API
  slug: open-rainforest-payment-methods-api
- collection_type: open
  name: Authentication ACH Returns Payments API
  slug: open-rainforest-payments-api
- collection_type: open
  name: Authentication ACH Returns Refunds API
  slug: open-rainforest-refunds-api
- collection_type: open
  name: Authentication ACH Returns Sessions API
  slug: open-rainforest-sessions-api
common:
- group: commercial
  href: https://artifacts.apis.io/rainforest/plans/rainforest-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rainforest-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/rainforest/capabilities/rainforest-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/rainforest-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/rainforest/overview
- group: company
  title: ''
  type: Website
  url: https://www.rainforestpay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rainforestpay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rainforestpay.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rainforestpay.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rainforestpay.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.rainforestpay.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rainforestpay
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rainforestpay.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.sandbox.rainforestpay.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rainforestpay.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rainforestpay.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rainforestpay.com/
- group: operate
  href: https://artifacts.apis.io/rainforest/changelog/rainforest-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rainforest-changelog.yml
- group: other
  title: ''
  type: Glossary
  url: https://www.rainforestpay.com/glossary
- group: auth
  href: https://artifacts.apis.io/rainforest/authentication/rainforest-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rainforest-authentication.yml
- group: agent
  href: https://artifacts.apis.io/rainforest/agentic-access/rainforest-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rainforest-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/rainforest/security/rainforest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rainforest-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/rainforest/security/rainforest-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/rainforest-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.rainforestpay.com/data-security-compliance
- group: design
  href: https://artifacts.apis.io/rainforest/conformance/rainforest-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rainforest-conformance.yml
- group: build
  href: https://artifacts.apis.io/rainforest/packages/rainforest-packages.yml
  title: ''
  type: Packages
  url: packages/rainforest-packages.yml
- group: build
  href: https://artifacts.apis.io/rainforest/packages/rainforest-packages.yml
  title: ''
  type: SDKs
  url: packages/rainforest-packages.yml
- group: agent
  href: https://artifacts.apis.io/rainforest/mcp/rainforest-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rainforest-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rainforest/llms/rainforest-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rainforest-llms.txt
- group: design
  href: https://artifacts.apis.io/rainforest/errors/rainforest-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rainforest-problem-types.yml
- group: build
  href: https://artifacts.apis.io/rainforest/errors/rainforest-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/rainforest-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/rainforest/lifecycle/rainforest-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rainforest-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.rainforestpay.com/docs/api-version-upgrades
- group: start
  href: https://artifacts.apis.io/rainforest/sandbox/rainforest-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/rainforest-sandbox.yml
- group: design
  href: https://artifacts.apis.io/rainforest/conventions/rainforest-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rainforest-conventions.yml
- group: design
  href: https://artifacts.apis.io/rainforest/conventions/rainforest-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/rainforest-conventions.yml
- group: design
  href: https://artifacts.apis.io/rainforest/components/rainforest-components.yml
  title: ''
  type: Components
  url: components/rainforest-components.yml
- group: design
  href: https://artifacts.apis.io/rainforest/data-model/rainforest-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rainforest-data-model.yml
- group: design
  href: https://artifacts.apis.io/rainforest/asyncapi/rainforest-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rainforest-webhooks.yml
- group: other
  href: https://artifacts.apis.io/rainforest/overlays/rainforest-payments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rainforest-payments-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/rainforest/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rainforest/arazzo/rainforest-collect-payment.yml
  title: ''
  type: Arazzo
  url: arazzo/rainforest-collect-payment.yml
- group: design
  href: https://artifacts.apis.io/rainforest/arazzo/rainforest-onboard-merchant.yml
  title: ''
  type: Arazzo
  url: arazzo/rainforest-onboard-merchant.yml
created: '2026-07-17'
description: Rainforest is a payfac-as-a-service (payment-facilitator-as-a-service) provider that lets vertical SaaS platforms embed payments and monetize them as revenue. Platforms integrate via embeddable, PCI-scope-reducing Components (loaded from a JavaScript bundle and configured in Component Studio) or a direct server-to-server REST API, and Rainforest handles merchant onboarding (KYC/KYB), card and ACH processing, payouts/deposits, chargebacks, disputes, and PCI compliance. The API is organized into Authentication/API keys, Merchants and merchant applications, Payments (payins, payment methods, refunds, chargebacks, ACH returns, devices), Deposits, File Uploads, Forward Requests, and Health, versioned by date (current 2024-10-16) and secured with HTTP Bearer API keys plus short-lived Component session tokens. Rainforest is PCI DSS Level 1 certified and hosted on AWS. Backed by Accel, Matrix Partners, and Y Combinator.
finops:
- has_sources: true
  method: derived
  name: Rainforest Finops
  primary_unit: item
  service_category: ''
  slug: rainforest-finops
  template: false
image: https://cdn.prod.website-files.com/682cdc7097ff49cf0ef60212/6848e7d5a49cad06f0ce0ffa_favicon%202.png
layout: provider
modified: '2026-07-20'
name: Rainforest
nav: Providers
network: true
overview: 'Rainforest publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including ACH Returns API, API Keys API, Billing Profiles API, and 20 more. Tagged areas include Company, Payments, Embedded Payments, Payment Facilitator, and Payment Processing.


  The Rainforest catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rainforest''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 34 more developer resources.'
plans:
- name: Rainforest Plans Pricing
  plan_count: 14
  slug: rainforest-plans-pricing
- name: Rainforest Price Estimates
  plan_count: 0
  slug: rainforest-price-estimates
random_paper: 5
score:
  band: exemplar
  composite: 66.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 58.0
    developer_ergonomics: 69.6
    discoverability: 71.4
    operational_transparency: 52.6
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rainforest/rainforest-2026-08-17T081441.png
security:
- kind: authentication
  name: Rainforest Authentication
  slug: rainforest-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rainforest Domain Security
  slug: rainforest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rainforest Trust Center
  slug: rainforest-trust-center
  summary_line: PCI DSS Level 1 Service Provider
skill_count: 4
skills:
- name: Collect a payment (payin) with Rainforest
  slug: rainforest-collect-payment
- name: Respond to a chargeback with Rainforest
  slug: rainforest-handle-chargeback
- name: Onboard a merchant with Rainforest
  slug: rainforest-onboard-merchant
- name: Void or refund a payin with Rainforest
  slug: rainforest-refund-payin
slug: rainforest
tags:
- Company
- Payments
- Embedded Payments
- Payment Facilitator
- Payment Processing
- Vertical SaaS
- Fintech
- ACH
website: https://www.rainforestpay.com/
---
