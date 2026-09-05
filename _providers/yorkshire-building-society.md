---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
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
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Yorkshire Building Society Agentic Access
  operation_count: 78
  slug: yorkshire-building-society-agentic-access
  summary_line: 78 operations · 23 acting
api_count: 4
apis:
- description: OBIE Dynamic Client Registration (DCR) API v3.1 - lets an FCA-authorised TPP present its OBIE/eIDAS software statement and register a client application with the YBS and Chelsea Building Society autho
  name: Yorkshire Building Society Dynamic Client Registration API
  slug: ybs-dynamic-client-registration-api
- description: 'OBIE token endpoint (Generate Access Token API v3.1.0) - the OAuth2/OIDC token endpoint used by onboarded TPPs to exchange authorization codes and client credentials for access tokens against the YBS '
  name: Yorkshire Building Society Generate Access Token API
  slug: ybs-generate-access-token-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Account Access API from Yorkshire Building Society — 2 operation(s) for account access.
  name: Yorkshire Building Society Account Access API
  slug: yorkshire-building-society-account-access-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Accounts API from Yorkshire Building Society — 2 operation(s) for accounts.
  name: Yorkshire Building Society Accounts API
  slug: yorkshire-building-society-accounts-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Balances API from Yorkshire Building Society — 2 operation(s) for balances.
  name: Yorkshire Building Society Balances API
  slug: yorkshire-building-society-balances-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Beneficiaries API from Yorkshire Building Society — 2 operation(s) for beneficiaries.
  name: Yorkshire Building Society Beneficiaries API
  slug: yorkshire-building-society-beneficiaries-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Direct Debits API from Yorkshire Building Society — 2 operation(s) for direct debits.
  name: Yorkshire Building Society Direct Debits API
  slug: yorkshire-building-society-direct-debits-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Domestic Payments API from Yorkshire Building Society — 5 operation(s) for domestic payments.
  name: Yorkshire Building Society Domestic Payments API
  slug: yorkshire-building-society-domestic-payments-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Domestic Scheduled Payments API from Yorkshire Building Society — 4 operation(s) for domestic scheduled payments.
  name: Yorkshire Building Society Domestic Scheduled Payments API
  slug: yorkshire-building-society-domestic-scheduled-payments-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Domestic Standing Orders API from Yorkshire Building Society — 4 operation(s) for domestic standing orders.
  name: Yorkshire Building Society Domestic Standing Orders API
  slug: yorkshire-building-society-domestic-standing-orders-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Event Subscriptions API from Yorkshire Building Society — 2 operation(s) for event subscriptions.
  name: Yorkshire Building Society Event Subscriptions API
  slug: yorkshire-building-society-event-subscriptions-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The File Payments API from Yorkshire Building Society — 6 operation(s) for file payments.
  name: Yorkshire Building Society File Payments API
  slug: yorkshire-building-society-file-payments-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Funds Confirmations API from Yorkshire Building Society — 3 operation(s) for funds confirmations.
  name: Yorkshire Building Society Funds Confirmations API
  slug: yorkshire-building-society-funds-confirmations-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The International Payments API from Yorkshire Building Society — 5 operation(s) for international payments.
  name: Yorkshire Building Society International Payments API
  slug: yorkshire-building-society-international-payments-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The International Scheduled Payments API from Yorkshire Building Society — 5 operation(s) for international scheduled payments.
  name: Yorkshire Building Society International Scheduled Payments API
  slug: yorkshire-building-society-international-scheduled-payments-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The International Standing Orders API from Yorkshire Building Society — 4 operation(s) for international standing orders.
  name: Yorkshire Building Society International Standing Orders API
  slug: yorkshire-building-society-international-standing-orders-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Offers API from Yorkshire Building Society — 2 operation(s) for offers.
  name: Yorkshire Building Society Offers API
  slug: yorkshire-building-society-offers-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Parties API from Yorkshire Building Society — 3 operation(s) for parties.
  name: Yorkshire Building Society Parties API
  slug: yorkshire-building-society-parties-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Payment Details API from Yorkshire Building Society — 7 operation(s) for payment details.
  name: Yorkshire Building Society Payment Details API
  slug: yorkshire-building-society-payment-details-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Products API from Yorkshire Building Society — 2 operation(s) for products.
  name: Yorkshire Building Society Products API
  slug: yorkshire-building-society-products-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Scheduled Payments API from Yorkshire Building Society — 2 operation(s) for scheduled payments.
  name: Yorkshire Building Society Scheduled Payments API
  slug: yorkshire-building-society-scheduled-payments-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Standing Orders API from Yorkshire Building Society — 2 operation(s) for standing orders.
  name: Yorkshire Building Society Standing Orders API
  slug: yorkshire-building-society-standing-orders-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Statements API from Yorkshire Building Society — 4 operation(s) for statements.
  name: Yorkshire Building Society Statements API
  slug: yorkshire-building-society-statements-api
- baseURL: https://ob-ybs.api.ybs.co.uk/open-banking/v3.1/aisp
  baseurl_source: declared
  description: The Transactions API from Yorkshire Building Society — 3 operation(s) for transactions.
  name: Yorkshire Building Society Transactions API
  slug: yorkshire-building-society-transactions-api
artifact_total: 29
asyncapis:
- description: ''
  name: Yorkshire Building Society Events Webhooks
  slug: yorkshire-building-society-events-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/yorkshire-building-society-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yorkshire-building-society-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yorkshire-building-society-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/yorkshire-building-society-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yorkshire-building-society-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yorkshire-building-society-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yorkshire-building-society-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yorkshire-building-society-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yorkshire-building-society-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yorkshire-building-society-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/yorkshire-building-society-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/yorkshire-building-society-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yorkshire-building-society-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/yorkshire-building-society-events-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/yorkshire-building-society-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/yorkshire-building-society-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yorkshire-building-society-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/yorkshire-building-society-account-information-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/yorkshire-building-society-payment-initiation-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/yorkshire-building-society-confirmation-of-funds-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/yorkshire-building-society-event-subscriptions-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ybs.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ybs.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ybs.co.uk/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.ybs.co.uk/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developers.ybs.co.uk/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.ybs.co.uk/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developers.ybs.co.uk/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yorkshire-building-society
created: '2026-07-23'
description: Yorkshire Building Society (YBS) is a UK mutual building society founded in 1864 and headquartered in Bradford, West Yorkshire. As a member-owned mutual rather than a shareholder-owned bank, it is owned by and run for the benefit of its savers and borrowers, with more than three million customers and around £66 billion in assets across the YBS Group, which trades under the Yorkshire Building Society, Chelsea Building Society (CBS), Norwich & Peterborough and Accord Mortgages brands. YBS is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA as an FCA-authorised ASPSP. Although it is not one of the CMA9 banks mandated to build Open Banking, YBS is a voluntary participant in the UK Open Banking / PSD2 ecosystem and operates a public developer portal at developers.ybs.co.uk that documents its OBIE Read/Write API family - Account Information (AIS), Payment Initiation (PIS), Confirmation of Funds (CBPII), Event Subscriptions,
  Dynamic Client Registration, and token issuance - conformant to the Open Banking Implementation Entity (OBIE) Read/Write Data API Standard v3.1.2. Access to the production and sandbox surfaces (ob-ybs.api.ybs.co.uk / ob-che.api.ybs.co.uk and the matching sandbox hosts) is secured with FAPI-grade OAuth2/OIDC, PSD2 strong customer authentication, mutual-TLS transport authentication and PS256-signed JWTs, and is available to FCA-authorised third-party providers holding eIDAS/OBIE certificates.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Yorkshire Building Society
nav: Providers
network: true
overview: 'Yorkshire Building Society publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Account Access API, Accounts API, Balances API, and 19 more. Tagged areas include Financial-Services, Banking, Building Society, Open Banking, and PSD2.


  The Yorkshire Building Society catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Yorkshire Building Society''s developer surface includes authentication, sandbox, documentation, getting-started guide, support, and 25 more developer resources.'
random_paper: 8
scopes:
- name: Yorkshire Building Society Scopes
  scope_count: 4
  slug: yorkshire-building-society-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 60.7
    developer_ergonomics: 63.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yorkshire-building-society/refs/heads/main/screenshots/yorkshire-building-society-2026-08-17T083019.png
security:
- kind: authentication
  name: Yorkshire Building Society Authentication
  slug: yorkshire-building-society-authentication
  summary_line: oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Yorkshire Building Society Domain Security
  slug: yorkshire-building-society-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yorkshire-building-society
tags:
- Financial-Services
- Banking
- Building Society
- Open Banking
- PSD2
- OBIE
- FAPI
- United Kingdom
- Payments
- Account Information
- Fintech
website: https://www.ybs.co.uk/
---
