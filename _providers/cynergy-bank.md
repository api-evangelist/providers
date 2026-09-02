---
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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Cynergy Bank Agentic Access
  operation_count: 74
  slug: cynergy-bank-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: The Account Access Consents API from Cynergy Bank — 2 operation(s) for account access consents.
  name: Cynergy Bank Account Access Consents API
  slug: cynergy-bank-account-access-consents-api
- description: The Accounts API from Cynergy Bank — 2 operation(s) for accounts.
  name: Cynergy Bank Accounts API
  slug: cynergy-bank-accounts-api
- description: The Balances API from Cynergy Bank — 2 operation(s) for balances.
  name: Cynergy Bank Balances API
  slug: cynergy-bank-balances-api
- description: The Beneficiaries API from Cynergy Bank — 2 operation(s) for beneficiaries.
  name: Cynergy Bank Beneficiaries API
  slug: cynergy-bank-beneficiaries-api
- description: The Direct Debits API from Cynergy Bank — 2 operation(s) for direct debits.
  name: Cynergy Bank Direct Debits API
  slug: cynergy-bank-direct-debits-api
- description: The Domestic Payment Consents API from Cynergy Bank — 3 operation(s) for domestic payment consents.
  name: Cynergy Bank Domestic Payment Consents API
  slug: cynergy-bank-domestic-payment-consents-api
- description: The Domestic Payments API from Cynergy Bank — 3 operation(s) for domestic payments.
  name: Cynergy Bank Domestic Payments API
  slug: cynergy-bank-domestic-payments-api
- description: The Domestic Scheduled Payment Consents API from Cynergy Bank — 2 operation(s) for domestic scheduled payment consents.
  name: Cynergy Bank Domestic Scheduled Payment Consents API
  slug: cynergy-bank-domestic-scheduled-payment-consents-api
- description: The Domestic Scheduled Payments API from Cynergy Bank — 3 operation(s) for domestic scheduled payments.
  name: Cynergy Bank Domestic Scheduled Payments API
  slug: cynergy-bank-domestic-scheduled-payments-api
- description: The Domestic Standing Order Consents API from Cynergy Bank — 2 operation(s) for domestic standing order consents.
  name: Cynergy Bank Domestic Standing Order Consents API
  slug: cynergy-bank-domestic-standing-order-consents-api
- description: The Domestic Standing Orders API from Cynergy Bank — 3 operation(s) for domestic standing orders.
  name: Cynergy Bank Domestic Standing Orders API
  slug: cynergy-bank-domestic-standing-orders-api
- description: The File Payment Consents API from Cynergy Bank — 3 operation(s) for file payment consents.
  name: Cynergy Bank File Payment Consents API
  slug: cynergy-bank-file-payment-consents-api
- description: The File Payments API from Cynergy Bank — 4 operation(s) for file payments.
  name: Cynergy Bank File Payments API
  slug: cynergy-bank-file-payments-api
- description: The Funds Confirmation Consents API from Cynergy Bank — 2 operation(s) for funds confirmation consents.
  name: Cynergy Bank Funds Confirmation Consents API
  slug: cynergy-bank-funds-confirmation-consents-api
- description: The Funds Confirmations API from Cynergy Bank — 1 operation(s) for funds confirmations.
  name: Cynergy Bank Funds Confirmations API
  slug: cynergy-bank-funds-confirmations-api
- description: The International Payment Consents API from Cynergy Bank — 3 operation(s) for international payment consents.
  name: Cynergy Bank International Payment Consents API
  slug: cynergy-bank-international-payment-consents-api
- description: The International Payments API from Cynergy Bank — 3 operation(s) for international payments.
  name: Cynergy Bank International Payments API
  slug: cynergy-bank-international-payments-api
- description: The International Scheduled Payments API from Cynergy Bank — 3 operation(s) for international scheduled payments.
  name: Cynergy Bank International Scheduled Payments API
  slug: cynergy-bank-international-scheduled-payments-api
- description: The International Scheduled Payments Consents API from Cynergy Bank — 3 operation(s) for international scheduled payments consents.
  name: Cynergy Bank International Scheduled Payments Consents API
  slug: cynergy-bank-international-scheduled-payments-consents-api
- description: The International Standing Orders API from Cynergy Bank — 3 operation(s) for international standing orders.
  name: Cynergy Bank International Standing Orders API
  slug: cynergy-bank-international-standing-orders-api
- description: The International Standing Orders Consents API from Cynergy Bank — 2 operation(s) for international standing orders consents.
  name: Cynergy Bank International Standing Orders Consents API
  slug: cynergy-bank-international-standing-orders-consents-api
- description: The Offers API from Cynergy Bank — 2 operation(s) for offers.
  name: Cynergy Bank Offers API
  slug: cynergy-bank-offers-api
- description: The Parties API from Cynergy Bank — 3 operation(s) for parties.
  name: Cynergy Bank Parties API
  slug: cynergy-bank-parties-api
- description: The Products API from Cynergy Bank — 2 operation(s) for products.
  name: Cynergy Bank Products API
  slug: cynergy-bank-products-api
- description: The Scheduled Payments API from Cynergy Bank — 2 operation(s) for scheduled payments.
  name: Cynergy Bank Scheduled Payments API
  slug: cynergy-bank-scheduled-payments-api
- description: The Standing Orders API from Cynergy Bank — 2 operation(s) for standing orders.
  name: Cynergy Bank Standing Orders API
  slug: cynergy-bank-standing-orders-api
- description: The Statements API from Cynergy Bank — 5 operation(s) for statements.
  name: Cynergy Bank Statements API
  slug: cynergy-bank-statements-api
- description: The Transactions API from Cynergy Bank — 2 operation(s) for transactions.
  name: Cynergy Bank Transactions API
  slug: cynergy-bank-transactions-api
artifact_total: 33
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cynergy-bank-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cynergy-bank-account-information-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cynergy-bank-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cynergy-bank-confirmation-of-funds-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cynergy-bank-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cynergy-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cynergy-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cynergy-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cynergy-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cynergy-bank-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cynergy-bank-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cynergy-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cynergy-bank-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cynergy-bank-tool-crosswalk.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cynergy-bank-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cynergy-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cynergy-bank-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cynergybank.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.openbanking.cynergybank.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cynergybank.co.uk/support/open-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/cynergy-bank
- group: operate
  title: ''
  type: Support
  url: https://www.cynergybank.co.uk/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cynergybank.co.uk/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cynergybank.co.uk/privacy-policy/legal-cynergy-bank
- group: build
  title: ''
  type: DocumentLibrary
  url: https://www.cynergybank.co.uk/document-library
- group: auth
  title: ''
  type: Security
  url: https://www.cynergybank.co.uk/support/security-and-fraud/information-security
created: '2026-07-23'
description: Cynergy Bank is an FCA- and PRA-authorised UK specialist bank (FCA reference 575105) serving the blended personal and business banking needs of business owners, property entrepreneurs, and family businesses. It was formed in December 2018 when Cynergy Capital acquired Bank of Cyprus UK for approximately £103m and rebranded the business as Cynergy Bank. Although it is not one of the nine CMA-mandated banks (CMA9), as a UK ASPSP it complies with PSD2 and the UK Open Banking Standard, publishing a dedicated third-party interface for the Open Banking Implementation Entity (OBIE) Read/Write APIs — Account & Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII). Access is restricted to FCA- or EEA-regulated Third Party Providers and is secured with FAPI-grade OAuth2/OIDC, mutual-TLS client authentication, and PSD2 strong customer authentication using OBIE/eIDAS certificates, onboarded through the bank's Open Banking developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Cynergy Bank MCP Server
  slug: cynergy-bank-mcp-server
modified: '2026-07-24'
name: Cynergy Bank
nav: Providers
network: true
overview: 'Cynergy Bank publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, Balances API, and 25 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Cynergy Bank''s developer surface includes authentication, documentation, support, and 24 more developer resources.'
random_paper: 8
scopes:
- name: Cynergy Bank Scopes
  scope_count: 3
  slug: cynergy-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 28.0
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cynergy-bank/refs/heads/main/screenshots/cynergy-bank-2026-07-25T211048.png
security:
- kind: authentication
  name: Cynergy Bank Authentication
  slug: cynergy-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Cynergy Bank Domain Security
  slug: cynergy-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cynergy-bank
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Confirmation of Funds
- Specialist Lender
website: https://www.cynergybank.co.uk/
---
