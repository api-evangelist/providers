---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Shawbrook Bank Agentic Access
  operation_count: 86
  slug: shawbrook-bank-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Account Access Consents API from Shawbrook Bank — 2 operation(s) for account access consents.
  name: Shawbrook Bank Account Access Consents API
  slug: shawbrook-bank-account-access-consents-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Accounts API from Shawbrook Bank — 2 operation(s) for accounts.
  name: Shawbrook Bank Accounts API
  slug: shawbrook-bank-accounts-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting ATM data
  name: Shawbrook Bank ATM API
  slug: shawbrook-bank-atm-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Balances API from Shawbrook Bank — 2 operation(s) for balances.
  name: Shawbrook Bank Balances API
  slug: shawbrook-bank-balances-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Business Current Account data
  name: Shawbrook Bank BCA API
  slug: shawbrook-bank-bca-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Beneficiaries API from Shawbrook Bank — 2 operation(s) for beneficiaries.
  name: Shawbrook Bank Beneficiaries API
  slug: shawbrook-bank-beneficiaries-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Branch data
  name: Shawbrook Bank Branch API
  slug: shawbrook-bank-branch-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Commercial Credit Card data
  name: Shawbrook Bank CCC API
  slug: shawbrook-bank-ccc-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Direct Debits API from Shawbrook Bank — 2 operation(s) for direct debits.
  name: Shawbrook Bank Direct Debits API
  slug: shawbrook-bank-direct-debits-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Payment Consents API from Shawbrook Bank — 3 operation(s) for domestic payment consents.
  name: Shawbrook Bank Domestic Payment Consents API
  slug: shawbrook-bank-domestic-payment-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Payments API from Shawbrook Bank — 3 operation(s) for domestic payments.
  name: Shawbrook Bank Domestic Payments API
  slug: shawbrook-bank-domestic-payments-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Scheduled Payment Consents API from Shawbrook Bank — 2 operation(s) for domestic scheduled payment consents.
  name: Shawbrook Bank Domestic Scheduled Payment Consents API
  slug: shawbrook-bank-domestic-scheduled-payment-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Scheduled Payments API from Shawbrook Bank — 3 operation(s) for domestic scheduled payments.
  name: Shawbrook Bank Domestic Scheduled Payments API
  slug: shawbrook-bank-domestic-scheduled-payments-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Standing Order Consents API from Shawbrook Bank — 2 operation(s) for domestic standing order consents.
  name: Shawbrook Bank Domestic Standing Order Consents API
  slug: shawbrook-bank-domestic-standing-order-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Standing Orders API from Shawbrook Bank — 3 operation(s) for domestic standing orders.
  name: Shawbrook Bank Domestic Standing Orders API
  slug: shawbrook-bank-domestic-standing-orders-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The File Payment Consents API from Shawbrook Bank — 3 operation(s) for file payment consents.
  name: Shawbrook Bank File Payment Consents API
  slug: shawbrook-bank-file-payment-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The File Payments API from Shawbrook Bank — 4 operation(s) for file payments.
  name: Shawbrook Bank File Payments API
  slug: shawbrook-bank-file-payments-api
- baseURL: /open-banking/v4.0/cbpii
  baseurl_source: spec
  description: The Funds Confirmation Consents API from Shawbrook Bank — 2 operation(s) for funds confirmation consents.
  name: Shawbrook Bank Funds Confirmation Consents API
  slug: shawbrook-bank-funds-confirmation-consents-api
- baseURL: /open-banking/v4.0/cbpii
  baseurl_source: spec
  description: The Funds Confirmations API from Shawbrook Bank — 1 operation(s) for funds confirmations.
  name: Shawbrook Bank Funds Confirmations API
  slug: shawbrook-bank-funds-confirmations-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Payment Consents API from Shawbrook Bank — 3 operation(s) for international payment consents.
  name: Shawbrook Bank International Payment Consents API
  slug: shawbrook-bank-international-payment-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Payments API from Shawbrook Bank — 3 operation(s) for international payments.
  name: Shawbrook Bank International Payments API
  slug: shawbrook-bank-international-payments-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Scheduled Payments API from Shawbrook Bank — 3 operation(s) for international scheduled payments.
  name: Shawbrook Bank International Scheduled Payments API
  slug: shawbrook-bank-international-scheduled-payments-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Scheduled Payments Consents API from Shawbrook Bank — 3 operation(s) for international scheduled payments consents.
  name: Shawbrook Bank International Scheduled Payments Consents API
  slug: shawbrook-bank-international-scheduled-payments-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Standing Orders API from Shawbrook Bank — 3 operation(s) for international standing orders.
  name: Shawbrook Bank International Standing Orders API
  slug: shawbrook-bank-international-standing-orders-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Standing Orders Consents API from Shawbrook Bank — 2 operation(s) for international standing orders consents.
  name: Shawbrook Bank International Standing Orders Consents API
  slug: shawbrook-bank-international-standing-orders-consents-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Offers API from Shawbrook Bank — 2 operation(s) for offers.
  name: Shawbrook Bank Offers API
  slug: shawbrook-bank-offers-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Parties API from Shawbrook Bank — 3 operation(s) for parties.
  name: Shawbrook Bank Parties API
  slug: shawbrook-bank-parties-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Personal Current Account data
  name: Shawbrook Bank PCA API
  slug: shawbrook-bank-pca-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Products API from Shawbrook Bank — 2 operation(s) for products.
  name: Shawbrook Bank Products API
  slug: shawbrook-bank-products-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Scheduled Payments API from Shawbrook Bank — 2 operation(s) for scheduled payments.
  name: Shawbrook Bank Scheduled Payments API
  slug: shawbrook-bank-scheduled-payments-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Unsecured SME Loan data
  name: Shawbrook Bank SME API
  slug: shawbrook-bank-sme-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Standing Orders API from Shawbrook Bank — 2 operation(s) for standing orders.
  name: Shawbrook Bank Standing Orders API
  slug: shawbrook-bank-standing-orders-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Statements API from Shawbrook Bank — 5 operation(s) for statements.
  name: Shawbrook Bank Statements API
  slug: shawbrook-bank-statements-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Transactions API from Shawbrook Bank — 2 operation(s) for transactions.
  name: Shawbrook Bank Transactions API
  slug: shawbrook-bank-transactions-api
artifact_total: 39
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shawbrook-bank-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/OpenBankingUK/opendata-api-spec-compiled/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shawbrook-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shawbrook-bank-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shawbrook-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shawbrook-bank-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shawbrook-bank-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shawbrook-bank-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shawbrook-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shawbrook-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shawbrook-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shawbrook-bank-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shawbrook-bank-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shawbrook-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/shawbrook-bank-account-info-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.shawbrook.co.uk/
- group: company
  title: ''
  type: About
  url: https://www.shawbrook.co.uk/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.shawbrook.co.uk/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://www.shawbrook.co.uk/help/
- group: operate
  title: ''
  type: Contact
  url: https://www.shawbrook.co.uk/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shawbrook.co.uk/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shawbrook-bank/
created: '2026-07-23'
description: 'Shawbrook Bank Limited is a specialist UK savings and lending bank (trading as Shawbrook, part of Shawbrook Group plc, which listed on the London Stock Exchange in October 2025 after being owned by a consortium led by BC Partners and Pollen Street Capital since 2017). It is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA, and its deposits are protected by the Financial Services Compensation Scheme. Shawbrook focuses on personal and business savings and specialist lending (property finance, SME and asset finance, and consumer lending) rather than personal current accounts, so it is not one of the nine CMA-mandated banks (CMA9). As an FCA-authorised deposit-taker it operates within the UK Open Banking / PSD2 framework: it consumes Open Banking (using account verification via Consents.Online to confirm customers'' linked nominated accounts) more than it publishes ASPSP surfaces. As of this review Shawbrook does not
  operate a public developer portal, and no Shawbrook Open Data (ATM/branch/product) endpoint or bank-specific Read/Write API host could be confirmed live; the OBIE Open Data and Read/Write API families are represented here as the shared Open Banking standard that an FCA-authorised ASPSP conforms to, not as verified Shawbrook contracts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Shawbrook Bank
nav: Providers
network: true
overview: 'Shawbrook Bank publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, ATM API, and 31 more. Tagged areas include Financial-Services, Banking, Savings, Specialist Lending, and Open Banking.


  Shawbrook Bank''s developer surface includes authentication, engineering blog, support, and 20 more developer resources.'
random_paper: 5
scopes:
- name: Shawbrook Bank Scopes
  scope_count: 3
  slug: shawbrook-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 50.9
    developer_ergonomics: 30.4
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 65.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shawbrook-bank/refs/heads/main/screenshots/shawbrook-bank-2026-09-02T155119.png
security:
- kind: authentication
  name: Shawbrook Bank Authentication
  slug: shawbrook-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Shawbrook Bank Domain Security
  slug: shawbrook-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: shawbrook-bank
tags:
- Financial-Services
- Banking
- Savings
- Specialist Lending
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
website: https://www.shawbrook.co.uk/
---
