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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Lloyds Banking Group Agentic Access
  operation_count: 95
  slug: lloyds-banking-group-agentic-access
  summary_line: 95 operations · 26 acting
api_count: 5
apis:
- description: OBIE Event Notifications API delivering aggregated and real-time event signals (e.g. consent revocation, resource-update notifications) to registered TPPs. FAPI-secured; requires developer-portal onbo
  name: Lloyds Banking Group Event Notifications API
  slug: event-notifications-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Account Access Consents API from Lloyds Banking Group — 2 operation(s) for account access consents.
  name: Lloyds Banking Group Account Access Consents API
  slug: lloyds-banking-group-account-access-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Accounts API from Lloyds Banking Group — 2 operation(s) for accounts.
  name: Lloyds Banking Group Accounts API
  slug: lloyds-banking-group-accounts-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: Endpoint for getting ATM data
  name: Lloyds Banking Group ATM API
  slug: lloyds-banking-group-atm-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Balances API from Lloyds Banking Group — 2 operation(s) for balances.
  name: Lloyds Banking Group Balances API
  slug: lloyds-banking-group-balances-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: Endpoint for getting Business Current Account data
  name: Lloyds Banking Group BCA API
  slug: lloyds-banking-group-bca-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Beneficiaries API from Lloyds Banking Group — 2 operation(s) for beneficiaries.
  name: Lloyds Banking Group Beneficiaries API
  slug: lloyds-banking-group-beneficiaries-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: Endpoint for getting Branch data
  name: Lloyds Banking Group Branch API
  slug: lloyds-banking-group-branch-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: Endpoint for getting Commercial Credit Card data
  name: Lloyds Banking Group CCC API
  slug: lloyds-banking-group-ccc-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Direct Debits API from Lloyds Banking Group — 2 operation(s) for direct debits.
  name: Lloyds Banking Group Direct Debits API
  slug: lloyds-banking-group-direct-debits-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Domestic Payment Consents API from Lloyds Banking Group — 3 operation(s) for domestic payment consents.
  name: Lloyds Banking Group Domestic Payment Consents API
  slug: lloyds-banking-group-domestic-payment-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Domestic Payments API from Lloyds Banking Group — 3 operation(s) for domestic payments.
  name: Lloyds Banking Group Domestic Payments API
  slug: lloyds-banking-group-domestic-payments-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Domestic Scheduled Payment Consents API from Lloyds Banking Group — 2 operation(s) for domestic scheduled payment consents.
  name: Lloyds Banking Group Domestic Scheduled Payment Consents API
  slug: lloyds-banking-group-domestic-scheduled-payment-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Domestic Scheduled Payments API from Lloyds Banking Group — 3 operation(s) for domestic scheduled payments.
  name: Lloyds Banking Group Domestic Scheduled Payments API
  slug: lloyds-banking-group-domestic-scheduled-payments-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Domestic Standing Order Consents API from Lloyds Banking Group — 2 operation(s) for domestic standing order consents.
  name: Lloyds Banking Group Domestic Standing Order Consents API
  slug: lloyds-banking-group-domestic-standing-order-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Domestic Standing Orders API from Lloyds Banking Group — 3 operation(s) for domestic standing orders.
  name: Lloyds Banking Group Domestic Standing Orders API
  slug: lloyds-banking-group-domestic-standing-orders-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Domestic VRP Consents API from Lloyds Banking Group — 3 operation(s) for domestic vrp consents.
  name: Lloyds Banking Group Domestic VRP Consents API
  slug: lloyds-banking-group-domestic-vrp-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Domestic VRPs API from Lloyds Banking Group — 3 operation(s) for domestic vrps.
  name: Lloyds Banking Group Domestic VRPs API
  slug: lloyds-banking-group-domestic-vrps-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The File Payment Consents API from Lloyds Banking Group — 3 operation(s) for file payment consents.
  name: Lloyds Banking Group File Payment Consents API
  slug: lloyds-banking-group-file-payment-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The File Payments API from Lloyds Banking Group — 4 operation(s) for file payments.
  name: Lloyds Banking Group File Payments API
  slug: lloyds-banking-group-file-payments-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Funds Confirmation Consents API from Lloyds Banking Group — 2 operation(s) for funds confirmation consents.
  name: Lloyds Banking Group Funds Confirmation Consents API
  slug: lloyds-banking-group-funds-confirmation-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Funds Confirmations API from Lloyds Banking Group — 1 operation(s) for funds confirmations.
  name: Lloyds Banking Group Funds Confirmations API
  slug: lloyds-banking-group-funds-confirmations-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The International Payment Consents API from Lloyds Banking Group — 3 operation(s) for international payment consents.
  name: Lloyds Banking Group International Payment Consents API
  slug: lloyds-banking-group-international-payment-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The International Payments API from Lloyds Banking Group — 3 operation(s) for international payments.
  name: Lloyds Banking Group International Payments API
  slug: lloyds-banking-group-international-payments-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The International Scheduled Payments API from Lloyds Banking Group — 3 operation(s) for international scheduled payments.
  name: Lloyds Banking Group International Scheduled Payments API
  slug: lloyds-banking-group-international-scheduled-payments-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The International Scheduled Payments Consents API from Lloyds Banking Group — 3 operation(s) for international scheduled payments consents.
  name: Lloyds Banking Group International Scheduled Payments Consents API
  slug: lloyds-banking-group-international-scheduled-payments-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The International Standing Orders API from Lloyds Banking Group — 3 operation(s) for international standing orders.
  name: Lloyds Banking Group International Standing Orders API
  slug: lloyds-banking-group-international-standing-orders-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The International Standing Orders Consents API from Lloyds Banking Group — 2 operation(s) for international standing orders consents.
  name: Lloyds Banking Group International Standing Orders Consents API
  slug: lloyds-banking-group-international-standing-orders-consents-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Offers API from Lloyds Banking Group — 2 operation(s) for offers.
  name: Lloyds Banking Group Offers API
  slug: lloyds-banking-group-offers-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Parties API from Lloyds Banking Group — 3 operation(s) for parties.
  name: Lloyds Banking Group Parties API
  slug: lloyds-banking-group-parties-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: Endpoint for getting Personal Current Account data
  name: Lloyds Banking Group PCA API
  slug: lloyds-banking-group-pca-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Products API from Lloyds Banking Group — 2 operation(s) for products.
  name: Lloyds Banking Group Products API
  slug: lloyds-banking-group-products-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Scheduled Payments API from Lloyds Banking Group — 2 operation(s) for scheduled payments.
  name: Lloyds Banking Group Scheduled Payments API
  slug: lloyds-banking-group-scheduled-payments-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: Endpoint for getting Unsecured SME Loan data
  name: Lloyds Banking Group SME API
  slug: lloyds-banking-group-sme-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Standing Orders API from Lloyds Banking Group — 2 operation(s) for standing orders.
  name: Lloyds Banking Group Standing Orders API
  slug: lloyds-banking-group-standing-orders-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Statements API from Lloyds Banking Group — 5 operation(s) for statements.
  name: Lloyds Banking Group Statements API
  slug: lloyds-banking-group-statements-api
- baseURL: https://api.lloydsbank.com/open-banking/v2.2
  baseurl_source: declared
  description: The Transactions API from Lloyds Banking Group — 2 operation(s) for transactions.
  name: Lloyds Banking Group Transactions API
  slug: lloyds-banking-group-transactions-api
artifact_total: 43
asyncapis:
- description: ''
  name: Lloyds Banking Group Event Notifications Webhooks
  slug: lloyds-banking-group-event-notifications-webhooks
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lloyds-banking-group-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lloyds-banking-group-opendata-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lloyds-banking-group-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lloyds-banking-group-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lloyds-banking-group-confirmation-funds-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/lloyds-banking-group-vrp-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lloyds-banking-group-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lloyds-banking-group-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lloyds-banking-group-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lloyds-banking-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lloyds-banking-group-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lloyds-banking-group-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lloyds-banking-group-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lloyds-banking-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lloyds-banking-group-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lloyds-banking-group-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lloyds-banking-group-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.lloydsbankinggroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lloydsbanking.com/prod01/lbg/home
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lloydsbanking.com/prod01/lbg/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lloydsbanking.com/prod01/lbg/products
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lloydsbanking.com/prod01/lbg/products
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LloydsBanking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lloyds-banking-group
- group: company
  title: ''
  type: Blog
  url: https://www.lloydsbankinggroup.com/insights.html
- group: operate
  title: ''
  type: Support
  url: https://developer.lloydsbanking.com/prod01/lbg/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lloydsbankinggroup.com/privacy.html
created: '2026-07-23'
description: Lloyds Banking Group plc is the United Kingdom's largest retail and commercial banking group, serving personal, business, and corporate customers through the Lloyds Bank, Halifax, Bank of Scotland, MBNA, and Scottish Widows brands. Formed in 2009 through the acquisition of HBOS by Lloyds TSB, it is a publicly listed company on the London Stock Exchange (LLOY) and a FTSE 100 constituent - not a mutual or building society. It is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. As one of the nine CMA-mandated banks (CMA9), Lloyds operates a public developer platform at developer.lloydsbanking.com that publishes UK Open Banking (OBIE / PSD2) APIs - unauthenticated Open Data reference APIs for ATMs, branches, and product information, plus the FAPI-secured Read/Write family - Account and Transaction Information (AIS), Payment Initiation (PIS), Confirmation of Funds (CBPII), Variable Recurring Payments (VRP), and Event
  Notifications - conformant to the Open Banking Implementation Entity (OBIE) Read/Write API Standard, secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication using OBIE/eIDAS certificates.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Lloyds Banking Group
nav: Providers
network: true
overview: 'Lloyds Banking Group publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, ATM API, and 33 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  The Lloyds Banking Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lloyds Banking Group''s developer surface includes authentication, getting-started guide, documentation, API reference, engineering blog, support, and 22 more developer resources.'
random_paper: 3
scopes:
- name: Lloyds Banking Group Scopes
  scope_count: 3
  slug: lloyds-banking-group-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 59.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 36
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
    score: 55.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lloyds-banking-group/refs/heads/main/screenshots/lloyds-banking-group-2026-07-25T225413.png
security:
- kind: authentication
  name: Lloyds Banking Group Authentication
  slug: lloyds-banking-group-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Lloyds Banking Group Domain Security
  slug: lloyds-banking-group-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lloyds-banking-group
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- CMA9
- United Kingdom
- Payments
- Account Information
- Open Data
- FAPI
website: https://www.lloydsbankinggroup.com/
---
