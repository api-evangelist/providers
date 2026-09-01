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
  name: Chase Uk Agentic Access
  operation_count: 74
  slug: chase-uk-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: The Account Access Consents API from Chase UK — 2 operation(s) for account access consents.
  name: Chase UK Account Access Consents API
  slug: chase-uk-account-access-consents-api
- description: The Accounts API from Chase UK — 2 operation(s) for accounts.
  name: Chase UK Accounts API
  slug: chase-uk-accounts-api
- description: The Balances API from Chase UK — 2 operation(s) for balances.
  name: Chase UK Balances API
  slug: chase-uk-balances-api
- description: The Beneficiaries API from Chase UK — 2 operation(s) for beneficiaries.
  name: Chase UK Beneficiaries API
  slug: chase-uk-beneficiaries-api
- description: The Direct Debits API from Chase UK — 2 operation(s) for direct debits.
  name: Chase UK Direct Debits API
  slug: chase-uk-direct-debits-api
- description: The Domestic Payment Consents API from Chase UK — 3 operation(s) for domestic payment consents.
  name: Chase UK Domestic Payment Consents API
  slug: chase-uk-domestic-payment-consents-api
- description: The Domestic Payments API from Chase UK — 3 operation(s) for domestic payments.
  name: Chase UK Domestic Payments API
  slug: chase-uk-domestic-payments-api
- description: The Domestic Scheduled Payment Consents API from Chase UK — 2 operation(s) for domestic scheduled payment consents.
  name: Chase UK Domestic Scheduled Payment Consents API
  slug: chase-uk-domestic-scheduled-payment-consents-api
- description: The Domestic Scheduled Payments API from Chase UK — 3 operation(s) for domestic scheduled payments.
  name: Chase UK Domestic Scheduled Payments API
  slug: chase-uk-domestic-scheduled-payments-api
- description: The Domestic Standing Order Consents API from Chase UK — 2 operation(s) for domestic standing order consents.
  name: Chase UK Domestic Standing Order Consents API
  slug: chase-uk-domestic-standing-order-consents-api
- description: The Domestic Standing Orders API from Chase UK — 3 operation(s) for domestic standing orders.
  name: Chase UK Domestic Standing Orders API
  slug: chase-uk-domestic-standing-orders-api
- description: The File Payment Consents API from Chase UK — 3 operation(s) for file payment consents.
  name: Chase UK File Payment Consents API
  slug: chase-uk-file-payment-consents-api
- description: The File Payments API from Chase UK — 4 operation(s) for file payments.
  name: Chase UK File Payments API
  slug: chase-uk-file-payments-api
- description: The Funds Confirmation Consents API from Chase UK — 2 operation(s) for funds confirmation consents.
  name: Chase UK Funds Confirmation Consents API
  slug: chase-uk-funds-confirmation-consents-api
- description: The Funds Confirmations API from Chase UK — 1 operation(s) for funds confirmations.
  name: Chase UK Funds Confirmations API
  slug: chase-uk-funds-confirmations-api
- description: The International Payment Consents API from Chase UK — 3 operation(s) for international payment consents.
  name: Chase UK International Payment Consents API
  slug: chase-uk-international-payment-consents-api
- description: The International Payments API from Chase UK — 3 operation(s) for international payments.
  name: Chase UK International Payments API
  slug: chase-uk-international-payments-api
- description: The International Scheduled Payments API from Chase UK — 3 operation(s) for international scheduled payments.
  name: Chase UK International Scheduled Payments API
  slug: chase-uk-international-scheduled-payments-api
- description: The International Scheduled Payments Consents API from Chase UK — 3 operation(s) for international scheduled payments consents.
  name: Chase UK International Scheduled Payments Consents API
  slug: chase-uk-international-scheduled-payments-consents-api
- description: The International Standing Orders API from Chase UK — 3 operation(s) for international standing orders.
  name: Chase UK International Standing Orders API
  slug: chase-uk-international-standing-orders-api
- description: The International Standing Orders Consents API from Chase UK — 2 operation(s) for international standing orders consents.
  name: Chase UK International Standing Orders Consents API
  slug: chase-uk-international-standing-orders-consents-api
- description: The Offers API from Chase UK — 2 operation(s) for offers.
  name: Chase UK Offers API
  slug: chase-uk-offers-api
- description: The Parties API from Chase UK — 3 operation(s) for parties.
  name: Chase UK Parties API
  slug: chase-uk-parties-api
- description: The Products API from Chase UK — 2 operation(s) for products.
  name: Chase UK Products API
  slug: chase-uk-products-api
- description: The Scheduled Payments API from Chase UK — 2 operation(s) for scheduled payments.
  name: Chase UK Scheduled Payments API
  slug: chase-uk-scheduled-payments-api
- description: The Standing Orders API from Chase UK — 2 operation(s) for standing orders.
  name: Chase UK Standing Orders API
  slug: chase-uk-standing-orders-api
- description: The Statements API from Chase UK — 5 operation(s) for statements.
  name: Chase UK Statements API
  slug: chase-uk-statements-api
- description: The Transactions API from Chase UK — 2 operation(s) for transactions.
  name: Chase UK Transactions API
  slug: chase-uk-transactions-api
artifact_total: 33
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/chase-uk-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chase-uk-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chase-uk-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/chase-uk-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chase-uk-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.chase.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.openbanking-obie-sandbox.chase.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.openbanking-obie-sandbox.chase.co.uk/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chase.co.uk/gb/en/information-for-tpps/
- group: operate
  title: ''
  type: Support
  url: https://www.chase.co.uk/gb/en/support/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chase.co.uk/gb/en/legal/general-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chase.co.uk/gb/en/legal/privacy-notice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chase/
- group: design
  title: ''
  type: Conventions
  url: conventions/chase-uk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/chase-uk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chase-uk-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chase-uk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.chase.co.uk/gb/en/information-for-tpps/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chase-uk-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chase-uk-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/chase-uk-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chase-uk-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chase-uk-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/chase-uk-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/chase-uk-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/chase-uk-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/chase-uk-confirmation-funds-overlay.yaml
created: '2026-07-23'
description: Chase UK is the digital retail bank operated in the United Kingdom by J.P. Morgan Europe Limited, a wholly owned subsidiary of JPMorgan Chase & Co. that launched the Chase consumer brand in the UK in September 2021. It is an app-only challenger bank with no physical branches or ATM estate, offering current accounts, savings, and round-up features to personal customers, and is authorised and regulated in the UK by the Financial Conduct Authority (FCA) and the Prudential Regulation Authority (PRA). As a Payment Services Regulations 2017 account provider (ASPSP), Chase UK operates a dedicated Open Banking interface conformant to the UK Open Banking Implementation Entity (OBIE) Read/Write API Standard, exposing Account Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) services to FCA-authorised third-party providers. It is not one of the CMA9 mandated banks; access is granted through its developer sandbox and secured with FAPI-grade OAuth2/OIDC, PSD2
  strong customer authentication, and mutual-TLS using eIDAS QWAC or OBWAC certificates from the Open Banking Certificate Authority.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Chase UK MCP Server
  slug: chase-uk-mcp-server
modified: '2026-07-23'
name: Chase UK
nav: Providers
network: true
overview: 'Chase UK publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, Balances API, and 25 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Chase UK''s developer surface includes authentication, documentation, getting-started guide, support, sandbox, and 23 more developer resources.'
random_paper: 8
scopes:
- name: Chase Uk Scopes
  scope_count: 3
  slug: chase-uk-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 47.0
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
    score: 67.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chase-uk/refs/heads/main/screenshots/chase-uk-2026-07-25T205111.png
security:
- kind: authentication
  name: Chase Uk Authentication
  slug: chase-uk-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Chase Uk Domain Security
  slug: chase-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chase-uk
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Challenger Bank
- Fintech
website: https://www.chase.co.uk/
---
