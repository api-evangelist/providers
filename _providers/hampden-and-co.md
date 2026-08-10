---
access_model:
  confidence: medium
  label: TPP onboarding · eIDAS/OBIE certificates required
  onboarding: unknown
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Hampden And Co Agentic Access
  operation_count: 74
  slug: hampden-and-co-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 4
apis:
- description: Public, unauthenticated Open Data reference API conforming to the OBIE UK Open Banking Open Data standard (product reference data such as personal and business current accounts). Listed on Hampden & C
  name: Hampden & Co Open Data API
  slug: hampden-and-co-open-data-api
- description: OBIE Read/Write Account Information Service (AIS) - accounts, balances, transactions, beneficiaries, standing orders, direct debits, statements, and parties - as a FAPI-secured PSD2 dedicated interfac
  name: Hampden & Co Account & Transaction Information API
  slug: hampden-and-co-account-information-api
- description: OBIE Read/Write Payment Initiation Service (PIS) - domestic, scheduled, standing-order, international, and file payments - as a FAPI-secured PSD2 dedicated interface. The harvested OpenAPI is the shar
  name: Hampden & Co Payment Initiation API
  slug: hampden-and-co-payment-initiation-api
- description: 'OBIE Read/Write Confirmation of Funds Service (CBPII) allowing an authorised card-based payment instrument issuer to confirm the availability of funds, as a FAPI-secured PSD2 dedicated interface. The '
  name: Hampden & Co Confirmation of Funds API
  slug: hampden-and-co-confirmation-of-funds-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hampden-and-co-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hampden-and-co-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hampden-and-co-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hampden-and-co-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.hampdenbank.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer-sandbox.hampdendigital.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-sandbox.hampdendigital.com/home
- group: start
  title: ''
  type: SignUp
  url: https://www.hampdenbank.com/tpp-registration
- group: auth
  title: ''
  type: Compliance
  url: https://www.openbanking.org.uk/regulated-providers/hampden-co-plc/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hampden-bank
- group: company
  title: ''
  type: Blog
  url: https://www.hampdenbank.com/insights
- group: operate
  title: ''
  type: Support
  url: https://www.hampdenbank.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hampdenbank.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hampdenbank.com/privacy-notice
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.hampdenbank.com/cookie-policy
- group: design
  title: ''
  type: Conventions
  url: conventions/hampden-and-co-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hampden-and-co-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hampden-and-co-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hampden-and-co-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hampden-and-co-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hampden-and-co-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hampden-and-co-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hampden-and-co-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://standards.openbanking.org.uk/api-specifications/latest/
created: '2026-07-23'
description: 'Hampden & Co (trading as Hampden Bank since March 2024) is an independent UK private bank headquartered at 20/21 Charlotte Square, Edinburgh, with offices in London and Manchester, serving high-net-worth individuals, their families, and their businesses with day-to-day banking, deposits, and specialist lending. Incorporated in 2010 as "Scoban" and launched in 2015, it was the first newly created UK private bank in three decades; it is a shareholder-owned public limited company (SC386922) - not a mutual or building society - backed by cornerstone shareholders and hundreds of smaller investors, and passed £1 billion in deposits in 2025. It is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. Although not one of the CMA9 mandated banks, Hampden & Co is an FCA-authorised ASPSP registered with the Open Banking Implementation Entity (OBIE) and exposes a PSD2 dedicated interface: an Open Data reference API plus the OBIE
  Read/Write family (Account & Transaction Information, Payment Initiation, and Confirmation of Funds), onboarded through a developer sandbox portal and secured with FAPI-grade OAuth2/OIDC, mutual-TLS, PSD2 strong customer authentication, and eIDAS/OBIE certificate-based dynamic client registration.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: hampden-and-co-mcp.yml
  slug: hampden-and-co-mcpyml
modified: '2026-07-23'
name: Hampden & Co
nav: Providers
network: true
overview: 'Hampden & Co publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account & Transaction Information API, Payment Initiation API, and Confirmation of Funds API. Tagged areas include Financial Services, Banking, Private Banking, Open Banking, and PSD2.


  Hampden & Co''s developer surface includes authentication, documentation, signup flow, engineering blog, support, API reference, and 19 more developer resources.'
random_paper: 64
scopes:
- name: Hampden And Co Scopes
  scope_count: 3
  slug: hampden-and-co-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 59.7
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 48.1
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
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 77.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hampden-and-co/refs/heads/main/screenshots/hampden-and-co-2026-07-25T220602.png
security:
- kind: authentication
  name: Hampden And Co Authentication
  slug: hampden-and-co-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Hampden And Co Domain Security
  slug: hampden-and-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hampden-and-co
tags:
- Financial Services
- Banking
- Private Banking
- Open Banking
- PSD2
- OBIE
- FAPI
- United Kingdom
- Payments
- Account Information
website: https://www.hampdenbank.com/
---
