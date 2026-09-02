---
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
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Allica Bank Agentic Access
  operation_count: 37
  slug: allica-bank-agentic-access
  summary_line: 37 operations · 11 acting
api_count: 2
apis:
- description: Allica Bank's UK Open Banking Confirmation of Funds (CBPII) capability, exposed through the OBIE Read/Write Standard and the `fundsconfirmations` OAuth scope, allowing authorised Card-Based Payment In
  name: Allica Bank Confirmation of Funds API
  slug: allica-bank-confirmation-of-funds-api
- description: OBIE Dynamic Client Registration (DCR) v3.2 endpoint used by regulated Third Party Providers to register OAuth clients with Allica Bank using Software Statement Assertions issued by the Open Banking D
  name: Allica Bank Dynamic Client Registration API
  slug: allica-bank-dynamic-client-registration-api
- description: The Account Access API from Allica Bank — 2 operation(s) for account access.
  name: Allica Bank Account Access API
  slug: allica-bank-account-access-api
- description: The Accounts API from Allica Bank — 2 operation(s) for accounts.
  name: Allica Bank Accounts API
  slug: allica-bank-accounts-api
- description: The Balances API from Allica Bank — 2 operation(s) for balances.
  name: Allica Bank Balances API
  slug: allica-bank-balances-api
- description: The Beneficiaries API from Allica Bank — 1 operation(s) for beneficiaries.
  name: Allica Bank Beneficiaries API
  slug: allica-bank-beneficiaries-api
- description: The Direct Debits API from Allica Bank — 1 operation(s) for direct debits.
  name: Allica Bank Direct Debits API
  slug: allica-bank-direct-debits-api
- description: The Domestic Payments API from Allica Bank — 5 operation(s) for domestic payments.
  name: Allica Bank Domestic Payments API
  slug: allica-bank-domestic-payments-api
- description: The Domestic Scheduled Payments API from Allica Bank — 4 operation(s) for domestic scheduled payments.
  name: Allica Bank Domestic Scheduled Payments API
  slug: allica-bank-domestic-scheduled-payments-api
- description: The Domestic Standing Orders API from Allica Bank — 4 operation(s) for domestic standing orders.
  name: Allica Bank Domestic Standing Orders API
  slug: allica-bank-domestic-standing-orders-api
- description: The File Payments API from Allica Bank — 5 operation(s) for file payments.
  name: Allica Bank File Payments API
  slug: allica-bank-file-payments-api
- description: The Offers API from Allica Bank — 1 operation(s) for offers.
  name: Allica Bank Offers API
  slug: allica-bank-offers-api
- description: The Parties API from Allica Bank — 2 operation(s) for parties.
  name: Allica Bank Parties API
  slug: allica-bank-parties-api
- description: The Payment Details API from Allica Bank — 3 operation(s) for payment details.
  name: Allica Bank Payment Details API
  slug: allica-bank-payment-details-api
- description: The Products API from Allica Bank — 1 operation(s) for products.
  name: Allica Bank Products API
  slug: allica-bank-products-api
- description: The Scheduled Payments API from Allica Bank — 1 operation(s) for scheduled payments.
  name: Allica Bank Scheduled Payments API
  slug: allica-bank-scheduled-payments-api
- description: The Standing Orders API from Allica Bank — 1 operation(s) for standing orders.
  name: Allica Bank Standing Orders API
  slug: allica-bank-standing-orders-api
- description: The Transactions API from Allica Bank — 1 operation(s) for transactions.
  name: Allica Bank Transactions API
  slug: allica-bank-transactions-api
artifact_total: 24
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/allica-bank-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/allica-bank-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/allica-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allica-bank-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allica-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allica-bank-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allica-bank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/allica-bank-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.allica.bank/responsible-disclosure
- group: design
  title: ''
  type: Conventions
  url: conventions/allica-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/allica-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allica-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allica-bank-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allica-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/allica-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allica-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allica-bank-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/allica-bank-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/allica-bank-account-information-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/allica-bank-payment-initiation-overlay.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.api.ob.allica.bank/perry/developer/welcome
- group: company
  title: ''
  type: Website
  url: https://www.allica.bank/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.api.ob.allica.bank/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.api.ob.allica.bank/perry/developer/welcome
- group: auth
  title: ''
  type: Authentication
  url: https://auth1.api.ob.allica.bank/.well-known/openid-configuration
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/allicabank
- group: company
  title: ''
  type: Blog
  url: https://www.allica.bank/blog
- group: operate
  title: ''
  type: Support
  url: https://help.allica.bank/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allica.bank/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allica.bank/privacy-policy
created: '2026-07-23'
description: Allica Bank Limited is a UK financial-technology bank built specifically for established small and medium-sized businesses, offering business current accounts, savings, commercial mortgages, asset finance, and invoice finance. It is a privately owned, venture-backed challenger bank (not a mutual or building society), authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and PRA (FRN 821851), registered in England and Wales (company number 07706156). As an FCA-authorised ASPSP it participates in UK Open Banking under the Open Banking Implementation Entity (OBIE) Read/Write Standard and PSD2 - it is not one of the nine CMA9 mandated banks, but publishes a public developer portal exposing Account and Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (fundsconfirmations) APIs for its Business Rewards accounts. Access is secured with FAPI-grade OAuth2/OIDC, PSD2 strong customer authentication, mutual-TLS
  client authentication, and dynamic client registration using Open Banking Directory / eIDAS certificates and Software Statement Assertions.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Allica Bank MCP Server
  slug: allica-bank-mcp-server
modified: '2026-07-24'
name: Allica Bank
nav: Providers
network: true
overview: 'Allica Bank publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account Access API, Accounts API, Balances API, and 13 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Allica Bank''s developer surface includes authentication, sandbox, getting-started guide, documentation, engineering blog, support, and 25 more developer resources.'
random_paper: 0
scopes:
- name: Allica Bank Scopes
  scope_count: 17
  slug: allica-bank-scopes
  summary_line: 17 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 50.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 78.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allica-bank/refs/heads/main/screenshots/allica-bank-2026-07-25T195713.png
security:
- kind: authentication
  name: Allica Bank Authentication
  slug: allica-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Allica Bank Domain Security
  slug: allica-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Allica Bank Vulnerability Disclosure
  slug: allica-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: allica-bank
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- FAPI
- United Kingdom
- Payments
- Account Information
- SME
- Business Banking
- Fintech
website: https://www.allica.bank/
---
