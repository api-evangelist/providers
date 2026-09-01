---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Gb Bank Agentic Access
  operation_count: 86
  slug: gb-bank-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: The Account Access Consents API from GB Bank — 2 operation(s) for account access consents.
  name: GB Bank Account Access Consents API
  slug: gb-bank-account-access-consents-api
- description: The Accounts API from GB Bank — 2 operation(s) for accounts.
  name: GB Bank Accounts API
  slug: gb-bank-accounts-api
- description: Endpoint for getting ATM data
  name: GB Bank ATM API
  slug: gb-bank-atm-api
- description: The Balances API from GB Bank — 2 operation(s) for balances.
  name: GB Bank Balances API
  slug: gb-bank-balances-api
- description: Endpoint for getting Business Current Account data
  name: GB Bank BCA API
  slug: gb-bank-bca-api
- description: The Beneficiaries API from GB Bank — 2 operation(s) for beneficiaries.
  name: GB Bank Beneficiaries API
  slug: gb-bank-beneficiaries-api
- description: Endpoint for getting Branch data
  name: GB Bank Branch API
  slug: gb-bank-branch-api
- description: Endpoint for getting Commercial Credit Card data
  name: GB Bank CCC API
  slug: gb-bank-ccc-api
- description: The Direct Debits API from GB Bank — 2 operation(s) for direct debits.
  name: GB Bank Direct Debits API
  slug: gb-bank-direct-debits-api
- description: The Domestic Payment Consents API from GB Bank — 3 operation(s) for domestic payment consents.
  name: GB Bank Domestic Payment Consents API
  slug: gb-bank-domestic-payment-consents-api
- description: The Domestic Payments API from GB Bank — 3 operation(s) for domestic payments.
  name: GB Bank Domestic Payments API
  slug: gb-bank-domestic-payments-api
- description: The Domestic Scheduled Payment Consents API from GB Bank — 2 operation(s) for domestic scheduled payment consents.
  name: GB Bank Domestic Scheduled Payment Consents API
  slug: gb-bank-domestic-scheduled-payment-consents-api
- description: The Domestic Scheduled Payments API from GB Bank — 3 operation(s) for domestic scheduled payments.
  name: GB Bank Domestic Scheduled Payments API
  slug: gb-bank-domestic-scheduled-payments-api
- description: The Domestic Standing Order Consents API from GB Bank — 2 operation(s) for domestic standing order consents.
  name: GB Bank Domestic Standing Order Consents API
  slug: gb-bank-domestic-standing-order-consents-api
- description: The Domestic Standing Orders API from GB Bank — 3 operation(s) for domestic standing orders.
  name: GB Bank Domestic Standing Orders API
  slug: gb-bank-domestic-standing-orders-api
- description: The File Payment Consents API from GB Bank — 3 operation(s) for file payment consents.
  name: GB Bank File Payment Consents API
  slug: gb-bank-file-payment-consents-api
- description: The File Payments API from GB Bank — 4 operation(s) for file payments.
  name: GB Bank File Payments API
  slug: gb-bank-file-payments-api
- description: The Funds Confirmation Consents API from GB Bank — 2 operation(s) for funds confirmation consents.
  name: GB Bank Funds Confirmation Consents API
  slug: gb-bank-funds-confirmation-consents-api
- description: The Funds Confirmations API from GB Bank — 1 operation(s) for funds confirmations.
  name: GB Bank Funds Confirmations API
  slug: gb-bank-funds-confirmations-api
- description: The International Payment Consents API from GB Bank — 3 operation(s) for international payment consents.
  name: GB Bank International Payment Consents API
  slug: gb-bank-international-payment-consents-api
- description: The International Payments API from GB Bank — 3 operation(s) for international payments.
  name: GB Bank International Payments API
  slug: gb-bank-international-payments-api
- description: The International Scheduled Payments API from GB Bank — 3 operation(s) for international scheduled payments.
  name: GB Bank International Scheduled Payments API
  slug: gb-bank-international-scheduled-payments-api
- description: The International Scheduled Payments Consents API from GB Bank — 3 operation(s) for international scheduled payments consents.
  name: GB Bank International Scheduled Payments Consents API
  slug: gb-bank-international-scheduled-payments-consents-api
- description: The International Standing Orders API from GB Bank — 3 operation(s) for international standing orders.
  name: GB Bank International Standing Orders API
  slug: gb-bank-international-standing-orders-api
- description: The International Standing Orders Consents API from GB Bank — 2 operation(s) for international standing orders consents.
  name: GB Bank International Standing Orders Consents API
  slug: gb-bank-international-standing-orders-consents-api
- description: The Offers API from GB Bank — 2 operation(s) for offers.
  name: GB Bank Offers API
  slug: gb-bank-offers-api
- description: The Parties API from GB Bank — 3 operation(s) for parties.
  name: GB Bank Parties API
  slug: gb-bank-parties-api
- description: Endpoint for getting Personal Current Account data
  name: GB Bank PCA API
  slug: gb-bank-pca-api
- description: The Products API from GB Bank — 2 operation(s) for products.
  name: GB Bank Products API
  slug: gb-bank-products-api
- description: The Scheduled Payments API from GB Bank — 2 operation(s) for scheduled payments.
  name: GB Bank Scheduled Payments API
  slug: gb-bank-scheduled-payments-api
- description: Endpoint for getting Unsecured SME Loan data
  name: GB Bank SME API
  slug: gb-bank-sme-api
- description: The Standing Orders API from GB Bank — 2 operation(s) for standing orders.
  name: GB Bank Standing Orders API
  slug: gb-bank-standing-orders-api
- description: The Statements API from GB Bank — 5 operation(s) for statements.
  name: GB Bank Statements API
  slug: gb-bank-statements-api
- description: The Transactions API from GB Bank — 2 operation(s) for transactions.
  name: GB Bank Transactions API
  slug: gb-bank-transactions-api
artifact_total: 39
collections:
- collection_type: open
  name: Open Data API
  slug: open-uk-open-banking-open-data-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gb-bank-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gb-bank-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gb-bank-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gb-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gb-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gb-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gb-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gb-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gb-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gb-bank-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gb-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.gbbank.co.uk/
- group: other
  title: ''
  type: Savings
  url: https://www.gbbank.co.uk/savings
- group: other
  title: ''
  type: MobileApp
  url: https://www.gbbank.co.uk/gb-bank-mobile-app
- group: operate
  title: ''
  type: Support
  url: https://www.gbbank.co.uk/help-and-support/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.gbbank.co.uk/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gbbank.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gbbank.co.uk/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thegbb
- group: other
  title: ''
  type: Standard
  url: https://github.com/OpenBankingUK/opendata-api-spec-compiled
- group: other
  title: ''
  type: Standard
  url: https://standards.openbanking.org.uk/
created: '2026-07-23'
description: GB Bank Limited is a UK challenger bank headquartered in Middlesbrough (2 Centre Square) with a London office (73 Brook Street, Mayfair). Wholly owned and privately backed rather than a mutual building society, it secured its full UK banking licence in 2022 and is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA (Financial Services Register number 850286). GB Bank funds SME regional property developers and investors with development finance, buy-to-let and bridging loans (typically between £26k and £5m across underserved UK regions) and funds that lending with retail deposits - fixed-rate bonds, notice accounts and easy-access savings accounts protected by the FSCS up to £85,000, managed through an online portal and a GB Bank mobile app. As a small, non-CMA9 FCA-authorised bank focused on savings and secured lending, GB Bank does not operate a public developer portal or a documented UK Open Banking (OBIE / PSD2) API
  surface; the Open Banking API families listed here are represented as the shared industry standard the bank would conform to as an FCA-authorised ASPSP, and are unverified for GB Bank pending a confirmed developer portal or Open Data endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: GB Bank
nav: Providers
network: true
overview: 'GB Bank publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, ATM API, and 31 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  GB Bank''s developer surface includes authentication, support, engineering blog, and 18 more developer resources.'
random_paper: 7
scopes:
- name: Gb Bank Scopes
  scope_count: 3
  slug: gb-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 50.9
    developer_ergonomics: 35.7
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 70.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gb-bank/refs/heads/main/screenshots/gb-bank-2026-07-25T215509.png
security:
- kind: authentication
  name: Gb Bank Authentication
  slug: gb-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Gb Bank Domain Security
  slug: gb-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gb-bank
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Savings
- Property Finance
- SME Lending
- Fintech
website: https://www.gbbank.co.uk/
---
