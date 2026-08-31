---
access_model:
  confidence: medium
  label: TPP onboarding · FAPI-secured
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Kroo Agentic Access
  operation_count: 74
  slug: kroo-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: The Account Access Consents API from Kroo — 2 operation(s) for account access consents.
  name: Kroo Account Access Consents API
  slug: kroo-account-access-consents-api
- description: The Accounts API from Kroo — 2 operation(s) for accounts.
  name: Kroo Accounts API
  slug: kroo-accounts-api
- description: The Balances API from Kroo — 2 operation(s) for balances.
  name: Kroo Balances API
  slug: kroo-balances-api
- description: The Beneficiaries API from Kroo — 2 operation(s) for beneficiaries.
  name: Kroo Beneficiaries API
  slug: kroo-beneficiaries-api
- description: The Direct Debits API from Kroo — 2 operation(s) for direct debits.
  name: Kroo Direct Debits API
  slug: kroo-direct-debits-api
- description: The Domestic Payment Consents API from Kroo — 3 operation(s) for domestic payment consents.
  name: Kroo Domestic Payment Consents API
  slug: kroo-domestic-payment-consents-api
- description: The Domestic Payments API from Kroo — 3 operation(s) for domestic payments.
  name: Kroo Domestic Payments API
  slug: kroo-domestic-payments-api
- description: The Domestic Scheduled Payment Consents API from Kroo — 2 operation(s) for domestic scheduled payment consents.
  name: Kroo Domestic Scheduled Payment Consents API
  slug: kroo-domestic-scheduled-payment-consents-api
- description: The Domestic Scheduled Payments API from Kroo — 3 operation(s) for domestic scheduled payments.
  name: Kroo Domestic Scheduled Payments API
  slug: kroo-domestic-scheduled-payments-api
- description: The Domestic Standing Order Consents API from Kroo — 2 operation(s) for domestic standing order consents.
  name: Kroo Domestic Standing Order Consents API
  slug: kroo-domestic-standing-order-consents-api
- description: The Domestic Standing Orders API from Kroo — 3 operation(s) for domestic standing orders.
  name: Kroo Domestic Standing Orders API
  slug: kroo-domestic-standing-orders-api
- description: The File Payment Consents API from Kroo — 3 operation(s) for file payment consents.
  name: Kroo File Payment Consents API
  slug: kroo-file-payment-consents-api
- description: The File Payments API from Kroo — 4 operation(s) for file payments.
  name: Kroo File Payments API
  slug: kroo-file-payments-api
- description: The Funds Confirmation Consents API from Kroo — 2 operation(s) for funds confirmation consents.
  name: Kroo Funds Confirmation Consents API
  slug: kroo-funds-confirmation-consents-api
- description: The Funds Confirmations API from Kroo — 1 operation(s) for funds confirmations.
  name: Kroo Funds Confirmations API
  slug: kroo-funds-confirmations-api
- description: The International Payment Consents API from Kroo — 3 operation(s) for international payment consents.
  name: Kroo International Payment Consents API
  slug: kroo-international-payment-consents-api
- description: The International Payments API from Kroo — 3 operation(s) for international payments.
  name: Kroo International Payments API
  slug: kroo-international-payments-api
- description: The International Scheduled Payments API from Kroo — 3 operation(s) for international scheduled payments.
  name: Kroo International Scheduled Payments API
  slug: kroo-international-scheduled-payments-api
- description: The International Scheduled Payments Consents API from Kroo — 3 operation(s) for international scheduled payments consents.
  name: Kroo International Scheduled Payments Consents API
  slug: kroo-international-scheduled-payments-consents-api
- description: The International Standing Orders API from Kroo — 3 operation(s) for international standing orders.
  name: Kroo International Standing Orders API
  slug: kroo-international-standing-orders-api
- description: The International Standing Orders Consents API from Kroo — 2 operation(s) for international standing orders consents.
  name: Kroo International Standing Orders Consents API
  slug: kroo-international-standing-orders-consents-api
- description: The Offers API from Kroo — 2 operation(s) for offers.
  name: Kroo Offers API
  slug: kroo-offers-api
- description: The Parties API from Kroo — 3 operation(s) for parties.
  name: Kroo Parties API
  slug: kroo-parties-api
- description: The Products API from Kroo — 2 operation(s) for products.
  name: Kroo Products API
  slug: kroo-products-api
- description: The Scheduled Payments API from Kroo — 2 operation(s) for scheduled payments.
  name: Kroo Scheduled Payments API
  slug: kroo-scheduled-payments-api
- description: The Standing Orders API from Kroo — 2 operation(s) for standing orders.
  name: Kroo Standing Orders API
  slug: kroo-standing-orders-api
- description: The Statements API from Kroo — 5 operation(s) for statements.
  name: Kroo Statements API
  slug: kroo-statements-api
- description: The Transactions API from Kroo — 2 operation(s) for transactions.
  name: Kroo Transactions API
  slug: kroo-transactions-api
artifact_total: 34
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kroo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kroo-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kroo-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kroo-confirmation-funds-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kroo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kroo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kroo-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kroo-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kroo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.kroo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kroo.banfico.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kroo.com/open-banking-performance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kroo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.kroo.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.kroo.com/support-is-here
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kroo.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kroo.com/privacy-notices
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kroobank
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kroo-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kroo-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://kroo.com/.well-known/security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/kroo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kroo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kroo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kroo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kroo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kroo-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kroo-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kroo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-23'
description: Kroo Bank Ltd is a UK app-based challenger bank, founded in 2016 and granted a full UK banking licence by the PRA/FCA in 2021 (restrictions lifted in 2022), that launched its digital-only personal current account in December 2022. Independent and venture-backed rather than mutual or part of a larger group, Kroo offers a fee-free everyday current account, interest-paying balances and "Kroo Pots", fee-free spending abroad, and FSCS deposit protection up to GBP 85,000. As an FCA-authorised ASPSP under PSD2, Kroo is a regulated Open Banking provider (though not one of the nine CMA9-mandated banks and, as a branchless digital bank, it publishes no Open Data reference APIs for ATMs or branches). It exposes the UK Open Banking Implementation Entity (OBIE) Read/Write API family - Account and Transaction Information, Payment Initiation, and Confirmation of Funds - through a Banfico-hosted developer portal at developer.kroo.banfico.io, secured with FAPI-grade OAuth2/OIDC, PSD2 strong
  customer authentication implemented as a CIBA decoupled (poll-mode) flow, and mutual-TLS client authentication using OBIE/eIDAS certificates, validated with the OpenID Foundation conformance suite.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Kroo MCP Server
  slug: kroo-mcp-server
modified: '2026-07-23'
name: Kroo
nav: Providers
network: true
overview: 'Kroo publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, Balances API, and 25 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Kroo''s developer surface includes authentication, documentation, engineering blog, support, and 26 more developer resources.'
random_paper: 2
scopes:
- name: Kroo Scopes
  scope_count: 3
  slug: kroo-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.1
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
    contract_quality: 54.4
    developer_ergonomics: 37.5
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 42.1
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
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 68.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kroo/refs/heads/main/screenshots/kroo-2026-07-25T224303.png
security:
- kind: authentication
  name: Kroo Authentication
  slug: kroo-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Kroo Domain Security
  slug: kroo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kroo Vulnerability Disclosure
  slug: kroo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kroo
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
- Challenger Bank
- Fintech
website: https://www.kroo.com/
---
