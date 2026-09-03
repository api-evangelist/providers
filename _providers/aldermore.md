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
  band: agent-ready
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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Aldermore Agentic Access
  operation_count: 86
  slug: aldermore-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Account Access Consents API from Aldermore Bank — 2 operation(s) for account access consents.
  name: Aldermore Bank Account Access Consents API
  slug: aldermore-account-access-consents-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Accounts API from Aldermore Bank — 2 operation(s) for accounts.
  name: Aldermore Bank Accounts API
  slug: aldermore-accounts-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting ATM data
  name: Aldermore Bank ATM API
  slug: aldermore-atm-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Balances API from Aldermore Bank — 2 operation(s) for balances.
  name: Aldermore Bank Balances API
  slug: aldermore-balances-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Business Current Account data
  name: Aldermore Bank BCA API
  slug: aldermore-bca-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Beneficiaries API from Aldermore Bank — 2 operation(s) for beneficiaries.
  name: Aldermore Bank Beneficiaries API
  slug: aldermore-beneficiaries-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Branch data
  name: Aldermore Bank Branch API
  slug: aldermore-branch-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Commercial Credit Card data
  name: Aldermore Bank CCC API
  slug: aldermore-ccc-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Direct Debits API from Aldermore Bank — 2 operation(s) for direct debits.
  name: Aldermore Bank Direct Debits API
  slug: aldermore-direct-debits-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Payment Consents API from Aldermore Bank — 3 operation(s) for domestic payment consents.
  name: Aldermore Bank Domestic Payment Consents API
  slug: aldermore-domestic-payment-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Payments API from Aldermore Bank — 3 operation(s) for domestic payments.
  name: Aldermore Bank Domestic Payments API
  slug: aldermore-domestic-payments-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Scheduled Payment Consents API from Aldermore Bank — 2 operation(s) for domestic scheduled payment consents.
  name: Aldermore Bank Domestic Scheduled Payment Consents API
  slug: aldermore-domestic-scheduled-payment-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Scheduled Payments API from Aldermore Bank — 3 operation(s) for domestic scheduled payments.
  name: Aldermore Bank Domestic Scheduled Payments API
  slug: aldermore-domestic-scheduled-payments-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Standing Order Consents API from Aldermore Bank — 2 operation(s) for domestic standing order consents.
  name: Aldermore Bank Domestic Standing Order Consents API
  slug: aldermore-domestic-standing-order-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The Domestic Standing Orders API from Aldermore Bank — 3 operation(s) for domestic standing orders.
  name: Aldermore Bank Domestic Standing Orders API
  slug: aldermore-domestic-standing-orders-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The File Payment Consents API from Aldermore Bank — 3 operation(s) for file payment consents.
  name: Aldermore Bank File Payment Consents API
  slug: aldermore-file-payment-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The File Payments API from Aldermore Bank — 4 operation(s) for file payments.
  name: Aldermore Bank File Payments API
  slug: aldermore-file-payments-api
- baseURL: /open-banking/v4.0/cbpii
  baseurl_source: spec
  description: The Funds Confirmation Consents API from Aldermore Bank — 2 operation(s) for funds confirmation consents.
  name: Aldermore Bank Funds Confirmation Consents API
  slug: aldermore-funds-confirmation-consents-api
- baseURL: /open-banking/v4.0/cbpii
  baseurl_source: spec
  description: The Funds Confirmations API from Aldermore Bank — 1 operation(s) for funds confirmations.
  name: Aldermore Bank Funds Confirmations API
  slug: aldermore-funds-confirmations-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Payment Consents API from Aldermore Bank — 3 operation(s) for international payment consents.
  name: Aldermore Bank International Payment Consents API
  slug: aldermore-international-payment-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Payments API from Aldermore Bank — 3 operation(s) for international payments.
  name: Aldermore Bank International Payments API
  slug: aldermore-international-payments-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Scheduled Payments API from Aldermore Bank — 3 operation(s) for international scheduled payments.
  name: Aldermore Bank International Scheduled Payments API
  slug: aldermore-international-scheduled-payments-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Scheduled Payments Consents API from Aldermore Bank — 3 operation(s) for international scheduled payments consents.
  name: Aldermore Bank International Scheduled Payments Consents API
  slug: aldermore-international-scheduled-payments-consents-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Standing Orders API from Aldermore Bank — 3 operation(s) for international standing orders.
  name: Aldermore Bank International Standing Orders API
  slug: aldermore-international-standing-orders-api
- baseURL: /open-banking/v4.0/pisp
  baseurl_source: spec
  description: The International Standing Orders Consents API from Aldermore Bank — 2 operation(s) for international standing orders consents.
  name: Aldermore Bank International Standing Orders Consents API
  slug: aldermore-international-standing-orders-consents-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Offers API from Aldermore Bank — 2 operation(s) for offers.
  name: Aldermore Bank Offers API
  slug: aldermore-offers-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Parties API from Aldermore Bank — 3 operation(s) for parties.
  name: Aldermore Bank Parties API
  slug: aldermore-parties-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Personal Current Account data
  name: Aldermore Bank PCA API
  slug: aldermore-pca-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Products API from Aldermore Bank — 2 operation(s) for products.
  name: Aldermore Bank Products API
  slug: aldermore-products-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Scheduled Payments API from Aldermore Bank — 2 operation(s) for scheduled payments.
  name: Aldermore Bank Scheduled Payments API
  slug: aldermore-scheduled-payments-api
- baseURL: https://developer.openbanking.org.uk/reference-implementation/open-banking/v1.3
  baseurl_source: spec
  description: Endpoint for getting Unsecured SME Loan data
  name: Aldermore Bank SME API
  slug: aldermore-sme-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Standing Orders API from Aldermore Bank — 2 operation(s) for standing orders.
  name: Aldermore Bank Standing Orders API
  slug: aldermore-standing-orders-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Statements API from Aldermore Bank — 5 operation(s) for statements.
  name: Aldermore Bank Statements API
  slug: aldermore-statements-api
- baseURL: /open-banking/v4.0/aisp
  baseurl_source: spec
  description: The Transactions API from Aldermore Bank — 2 operation(s) for transactions.
  name: Aldermore Bank Transactions API
  slug: aldermore-transactions-api
artifact_total: 41
collections:
- collection_type: open
  name: Open Data API
  slug: open-aldermore-obie-open-data
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/aldermore-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aldermore-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aldermore-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aldermore-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aldermore-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aldermore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.aldermore.co.uk/.well-known/security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aldermore-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/aldermore-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/aldermore-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aldermore-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aldermore-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aldermore-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aldermore-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aldermore-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aldermore-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aldermore-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aldermore-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aldermore-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aldermore-confirmation-of-funds-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aldermore-open-data-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.aldermore.co.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aldermore
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aldermorebank
- group: operate
  title: ''
  type: Support
  url: https://www.aldermore.co.uk/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aldermore.co.uk/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aldermore.co.uk/legal/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.aldermore.co.uk/legal/
created: '2026-07-23'
description: Aldermore Bank plc is a UK specialist bank founded in 2009 and headquartered in Reading, offering savings accounts and specialist lending across residential and buy-to-let mortgages, commercial and property finance, asset finance, invoice finance, and motor finance (through sister company MotoNovo Finance). Aldermore Group is wholly owned by South Africa's FirstRand Group, which acquired it in 2018 and, as of 2026, has begun a process to sell the UK business and exit the market. Aldermore Bank plc is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA (Financial Services Register number 204503). It is a branchless, digitally-delivered specialist lender rather than a full-service current-account bank, and it is NOT one of the nine CMA-mandated banks (CMA9). Because it does not provide personal or business current accounts, its UK Open Banking (OBIE / PSD2) payment-account footprint is minimal, and no public Aldermore
  developer portal, Open Data endpoint, or bank-proprietary API surface could be confirmed at bootstrap; the OBIE Open Data and Read/Write API families below are represented as the shared UK Open Banking standard, unverified for this bank.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Aldermore Bank MCP Server
  slug: aldermore-bank-mcp-server
modified: '2026-07-23'
name: Aldermore Bank
nav: Providers
network: true
overview: 'Aldermore Bank publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, ATM API, and 31 more. Tagged areas include Financial-Services, Banking, Savings, Specialist Lending, and Open Banking.


  Aldermore Bank''s developer surface includes authentication, support, legal docs, and 26 more developer resources.'
random_paper: 10
scopes:
- name: Aldermore Scopes
  scope_count: 3
  slug: aldermore-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 50.9
    developer_ergonomics: 35.1
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 40.6
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
    score: 78.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aldermore/refs/heads/main/screenshots/aldermore-2026-07-25T195550.png
security:
- kind: authentication
  name: Aldermore Authentication
  slug: aldermore-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Aldermore Domain Security
  slug: aldermore-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aldermore Vulnerability Disclosure
  slug: aldermore-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aldermore
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
website: https://www.aldermore.co.uk/
---
