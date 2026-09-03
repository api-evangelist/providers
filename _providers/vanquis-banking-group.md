---
access_model:
  confidence: medium
  label: Self-serve onboarding via Open Banking Directory
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - onboarding
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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Vanquis Banking Group Agentic Access
  operation_count: 74
  slug: vanquis-banking-group-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: Vanquis Bank's OpenID / OBIE Dynamic Client Registration (DCR) endpoint, documented on the Vanquis developer portal, allowing onboarded Third Party Providers to register OAuth clients programmatically
  name: Vanquis Bank Dynamic Client Registration API
  slug: vanquis-dynamic-client-registration-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Account Access API from Vanquis Banking Group — 2 operation(s) for account access.
  name: Vanquis Banking Group Account Access API
  slug: vanquis-banking-group-account-access-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Accounts API from Vanquis Banking Group — 2 operation(s) for accounts.
  name: Vanquis Banking Group Accounts API
  slug: vanquis-banking-group-accounts-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Balances API from Vanquis Banking Group — 2 operation(s) for balances.
  name: Vanquis Banking Group Balances API
  slug: vanquis-banking-group-balances-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Beneficiaries API from Vanquis Banking Group — 2 operation(s) for beneficiaries.
  name: Vanquis Banking Group Beneficiaries API
  slug: vanquis-banking-group-beneficiaries-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Direct Debits API from Vanquis Banking Group — 2 operation(s) for direct debits.
  name: Vanquis Banking Group Direct Debits API
  slug: vanquis-banking-group-direct-debits-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The Domestic Payments API from Vanquis Banking Group — 5 operation(s) for domestic payments.
  name: Vanquis Banking Group Domestic Payments API
  slug: vanquis-banking-group-domestic-payments-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The Domestic Scheduled Payments API from Vanquis Banking Group — 4 operation(s) for domestic scheduled payments.
  name: Vanquis Banking Group Domestic Scheduled Payments API
  slug: vanquis-banking-group-domestic-scheduled-payments-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The Domestic Standing Orders API from Vanquis Banking Group — 4 operation(s) for domestic standing orders.
  name: Vanquis Banking Group Domestic Standing Orders API
  slug: vanquis-banking-group-domestic-standing-orders-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The File Payments API from Vanquis Banking Group — 6 operation(s) for file payments.
  name: Vanquis Banking Group File Payments API
  slug: vanquis-banking-group-file-payments-api
- baseURL: /open-banking/v3.1/cbpii
  baseurl_source: spec
  description: The Funds Confirmations API from Vanquis Banking Group — 3 operation(s) for funds confirmations.
  name: Vanquis Banking Group Funds Confirmations API
  slug: vanquis-banking-group-funds-confirmations-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The International Payments API from Vanquis Banking Group — 5 operation(s) for international payments.
  name: Vanquis Banking Group International Payments API
  slug: vanquis-banking-group-international-payments-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The International Scheduled Payments API from Vanquis Banking Group — 5 operation(s) for international scheduled payments.
  name: Vanquis Banking Group International Scheduled Payments API
  slug: vanquis-banking-group-international-scheduled-payments-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The International Standing Orders API from Vanquis Banking Group — 4 operation(s) for international standing orders.
  name: Vanquis Banking Group International Standing Orders API
  slug: vanquis-banking-group-international-standing-orders-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Offers API from Vanquis Banking Group — 2 operation(s) for offers.
  name: Vanquis Banking Group Offers API
  slug: vanquis-banking-group-offers-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Parties API from Vanquis Banking Group — 3 operation(s) for parties.
  name: Vanquis Banking Group Parties API
  slug: vanquis-banking-group-parties-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The Payment Details API from Vanquis Banking Group — 7 operation(s) for payment details.
  name: Vanquis Banking Group Payment Details API
  slug: vanquis-banking-group-payment-details-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Products API from Vanquis Banking Group — 2 operation(s) for products.
  name: Vanquis Banking Group Products API
  slug: vanquis-banking-group-products-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Scheduled Payments API from Vanquis Banking Group — 2 operation(s) for scheduled payments.
  name: Vanquis Banking Group Scheduled Payments API
  slug: vanquis-banking-group-scheduled-payments-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Standing Orders API from Vanquis Banking Group — 2 operation(s) for standing orders.
  name: Vanquis Banking Group Standing Orders API
  slug: vanquis-banking-group-standing-orders-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Statements API from Vanquis Banking Group — 4 operation(s) for statements.
  name: Vanquis Banking Group Statements API
  slug: vanquis-banking-group-statements-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Transactions API from Vanquis Banking Group — 3 operation(s) for transactions.
  name: Vanquis Banking Group Transactions API
  slug: vanquis-banking-group-transactions-api
artifact_total: 27
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vanquis-banking-group-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vanquis-banking-group-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vanquis-banking-group-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vanquis-banking-group-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vanquis-banking-group-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.vanquis.com/
- group: company
  title: ''
  type: Website
  url: https://www.vanquisbankinggroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.vanquis.com/developer-portal/
- group: docs
  title: ''
  type: Documentation
  url: https://openbanking.atlassian.net/wiki/spaces/DZ/overview
- group: start
  title: ''
  type: SignUp
  url: https://directory.openbanking.org.uk/s/login/SelfRegister
- group: operate
  title: ''
  type: Support
  url: https://directory.openbanking.org.uk/obieservicedesk/s/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vanquis/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vanquis.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vanquis.com/legal/privacy/
- group: operate
  title: ''
  type: Contact
  url: https://www.vanquis.com/contact-us/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vanquis-banking-group-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vanquis-banking-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vanquis-banking-group-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/vanquis-banking-group-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vanquis-banking-group-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/vanquis-banking-group-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vanquis-banking-group-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vanquis-banking-group-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vanquis-banking-group-aisp-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/vanquis-banking-group-pisp-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/vanquis-banking-group-cbpii-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/vanquis-banking-group-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/vanquis-read-account-transactions.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/vanquis-initiate-domestic-payment.md
created: '2026-07-23'
description: Vanquis Banking Group plc (formerly Provident Financial plc, rebranded 2023) is a UK specialist non-prime lender and savings bank headquartered in Bradford, England, listed on the London Stock Exchange under the ticker VANQ and serving around 1.75 million customers under the Vanquis, Moneybarn and Snoop brands. It offers credit cards, unsecured personal loans, second-charge mortgages, retail savings (easy-access, fixed-rate, notice and ISA accounts) and consumer vehicle finance to customers underserved by mainstream lenders. Its banking subsidiary, Vanquis Bank Limited, is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority (Financial Services Register no. 221156) and, as an FCA-authorised ASPSP, is a UK Open Banking participant (not one of the CMA9). Vanquis exposes the OBIE Read/Write API family - Account and Transaction Information (AIS), Payment Initiation (PIS) and Confirmation of Funds (CBPII) at v3.1.10 - plus Dynamic Client
  Registration, onboarded and secured through the Open Banking Directory under the PSD2 / FAPI security profile (OAuth2/OIDC, mutual-TLS and strong customer authentication). As a credit-card and savings specialist with no branch or current-account estate, Vanquis publishes no public Open Data (ATM/Branch/PCA/BCA) API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Vanquis Banking Group MCP Server
  slug: vanquis-banking-group-mcp-server
modified: '2026-07-23'
name: Vanquis Banking Group
nav: Providers
network: true
overview: 'Vanquis Banking Group publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Account Access API, Accounts API, Balances API, and 18 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Vanquis Banking Group''s developer surface includes authentication, documentation, signup flow, support, and 25 more developer resources.'
random_paper: 10
scopes:
- name: Vanquis Banking Group Scopes
  scope_count: 3
  slug: vanquis-banking-group-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 49.3
    developer_ergonomics: 44.6
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
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
    score: 70.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vanquis-banking-group/refs/heads/main/screenshots/vanquis-banking-group-2026-09-02T165416.png
security:
- kind: authentication
  name: Vanquis Banking Group Authentication
  slug: vanquis-banking-group-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Vanquis Banking Group Domain Security
  slug: vanquis-banking-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vanquis-banking-group
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Specialist Lender
- Credit Cards
- Account Information
- Payments
website: https://www.vanquis.com/
---
