---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 37.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Santander Uk Agentic Access
  operation_count: 86
  slug: santander-uk-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Account Access Consents API from Santander UK — 2 operation(s) for account access consents.
  name: Santander UK Account Access Consents API
  slug: santander-uk-account-access-consents-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Accounts API from Santander UK — 2 operation(s) for accounts.
  name: Santander UK Accounts API
  slug: santander-uk-accounts-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: Endpoint for getting ATM data
  name: Santander UK ATM API
  slug: santander-uk-atm-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Balances API from Santander UK — 2 operation(s) for balances.
  name: Santander UK Balances API
  slug: santander-uk-balances-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: Endpoint for getting Business Current Account data
  name: Santander UK BCA API
  slug: santander-uk-bca-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Beneficiaries API from Santander UK — 2 operation(s) for beneficiaries.
  name: Santander UK Beneficiaries API
  slug: santander-uk-beneficiaries-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: Endpoint for getting Branch data
  name: Santander UK Branch API
  slug: santander-uk-branch-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: Endpoint for getting Commercial Credit Card data
  name: Santander UK CCC API
  slug: santander-uk-ccc-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Direct Debits API from Santander UK — 2 operation(s) for direct debits.
  name: Santander UK Direct Debits API
  slug: santander-uk-direct-debits-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Domestic Payment Consents API from Santander UK — 3 operation(s) for domestic payment consents.
  name: Santander UK Domestic Payment Consents API
  slug: santander-uk-domestic-payment-consents-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Domestic Payments API from Santander UK — 3 operation(s) for domestic payments.
  name: Santander UK Domestic Payments API
  slug: santander-uk-domestic-payments-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Domestic Scheduled Payment Consents API from Santander UK — 2 operation(s) for domestic scheduled payment consents.
  name: Santander UK Domestic Scheduled Payment Consents API
  slug: santander-uk-domestic-scheduled-payment-consents-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Domestic Scheduled Payments API from Santander UK — 3 operation(s) for domestic scheduled payments.
  name: Santander UK Domestic Scheduled Payments API
  slug: santander-uk-domestic-scheduled-payments-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Domestic Standing Order Consents API from Santander UK — 2 operation(s) for domestic standing order consents.
  name: Santander UK Domestic Standing Order Consents API
  slug: santander-uk-domestic-standing-order-consents-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Domestic Standing Orders API from Santander UK — 3 operation(s) for domestic standing orders.
  name: Santander UK Domestic Standing Orders API
  slug: santander-uk-domestic-standing-orders-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The File Payment Consents API from Santander UK — 3 operation(s) for file payment consents.
  name: Santander UK File Payment Consents API
  slug: santander-uk-file-payment-consents-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The File Payments API from Santander UK — 4 operation(s) for file payments.
  name: Santander UK File Payments API
  slug: santander-uk-file-payments-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Funds Confirmation Consents API from Santander UK — 2 operation(s) for funds confirmation consents.
  name: Santander UK Funds Confirmation Consents API
  slug: santander-uk-funds-confirmation-consents-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Funds Confirmations API from Santander UK — 1 operation(s) for funds confirmations.
  name: Santander UK Funds Confirmations API
  slug: santander-uk-funds-confirmations-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The International Payment Consents API from Santander UK — 3 operation(s) for international payment consents.
  name: Santander UK International Payment Consents API
  slug: santander-uk-international-payment-consents-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The International Payments API from Santander UK — 3 operation(s) for international payments.
  name: Santander UK International Payments API
  slug: santander-uk-international-payments-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The International Scheduled Payments API from Santander UK — 3 operation(s) for international scheduled payments.
  name: Santander UK International Scheduled Payments API
  slug: santander-uk-international-scheduled-payments-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The International Scheduled Payments Consents API from Santander UK — 3 operation(s) for international scheduled payments consents.
  name: Santander UK International Scheduled Payments Consents API
  slug: santander-uk-international-scheduled-payments-consents-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The International Standing Orders API from Santander UK — 3 operation(s) for international standing orders.
  name: Santander UK International Standing Orders API
  slug: santander-uk-international-standing-orders-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The International Standing Orders Consents API from Santander UK — 2 operation(s) for international standing orders consents.
  name: Santander UK International Standing Orders Consents API
  slug: santander-uk-international-standing-orders-consents-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Offers API from Santander UK — 2 operation(s) for offers.
  name: Santander UK Offers API
  slug: santander-uk-offers-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Parties API from Santander UK — 3 operation(s) for parties.
  name: Santander UK Parties API
  slug: santander-uk-parties-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: Endpoint for getting Personal Current Account data
  name: Santander UK PCA API
  slug: santander-uk-pca-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Products API from Santander UK — 2 operation(s) for products.
  name: Santander UK Products API
  slug: santander-uk-products-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Scheduled Payments API from Santander UK — 2 operation(s) for scheduled payments.
  name: Santander UK Scheduled Payments API
  slug: santander-uk-scheduled-payments-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: Endpoint for getting Unsecured SME Loan data
  name: Santander UK SME API
  slug: santander-uk-sme-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Standing Orders API from Santander UK — 2 operation(s) for standing orders.
  name: Santander UK Standing Orders API
  slug: santander-uk-standing-orders-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Statements API from Santander UK — 5 operation(s) for statements.
  name: Santander UK Statements API
  slug: santander-uk-statements-api
- baseURL: https://api-portal.omni.slz.santander.co.uk/external/opendata
  baseurl_source: declared
  description: The Transactions API from Santander UK — 2 operation(s) for transactions.
  name: Santander UK Transactions API
  slug: santander-uk-transactions-api
artifact_total: 39
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/santander-uk-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/santander-uk-opendata-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/santander-uk-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/santander-uk-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/santander-uk-confirmation-funds-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/santander-uk-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/santander-uk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/santander-uk-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/santander-uk-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/santander-uk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/santander-uk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/santander-uk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/santander-uk-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/santander-uk-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/santander-uk-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/santander-uk-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/santander-uk-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openbanking.org.uk/terms
- group: company
  title: ''
  type: Website
  url: https://www.santander.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.santander.co.uk/sanuk/external/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.santander.co.uk/sanuk/external/product
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox-developer.santander.co.uk/sanuk/external-sandbox/faq-page
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/santander-uk
- group: operate
  title: ''
  type: StatusPage
  url: https://www.santander.co.uk/personal/support/service-status
- group: company
  title: ''
  type: About
  url: https://www.santander.co.uk/about-santander
created: '2026-07-23'
description: Santander UK plc is a major British retail and commercial bank and one of the CMA9 banks mandated to deliver UK Open Banking. It is a wholly owned, ring-fenced subsidiary of Banco Santander S.A. of Madrid, Spain, and was formed from the former Abbey National, Alliance & Leicester, and the savings business of Bradford & Bingley. Operating from Milton Keynes with a registered office in London, it serves around 14 million active personal, business, and corporate customers. Santander UK is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. Under PSD2 and the CMA Order it publishes a developer portal ("Santander Developers") exposing free, unauthenticated Open Data APIs (ATMs, branches, and product reference data) plus the OBIE Read/Write API family - Account & Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) - conformant to the Open Banking Implementation Entity standard and secured
  with FAPI-grade OAuth2/OIDC, mutual-TLS client authentication, and PSD2 strong customer authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Santander UK
nav: Providers
network: true
overview: 'Santander UK publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, ATM API, and 31 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Santander UK''s developer surface includes authentication, documentation, sandbox, and 23 more developer resources.'
random_paper: 11
scopes:
- name: Santander Uk Scopes
  scope_count: 3
  slug: santander-uk-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 50.9
    developer_ergonomics: 43.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: derived
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/santander-uk/refs/heads/main/screenshots/santander-uk-2026-09-02T154404.png
security:
- kind: authentication
  name: Santander Uk Authentication
  slug: santander-uk-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Santander Uk Domain Security
  slug: santander-uk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: santander-uk
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
- FAPI
website: https://www.santander.co.uk/
---
