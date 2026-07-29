---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Santander Uk Agentic Access
  operation_count: 86
  slug: santander-uk-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: Free, public, unauthenticated Open Data reference API publishing Santander UK ATMs, branches, and product information (personal & business current accounts, unsecured SME loans, commercial credit card
  name: Santander UK Open Data API
  slug: santander-uk-open-data-api
- description: 'OBIE Read/Write Account and Transaction Information (AIS) API for accessing account, balance, transaction, and party data with customer consent. FAPI-secured (OAuth2/OIDC, mTLS, PSD2 SCA); onboarding '
  name: Santander UK Account & Transaction Information API
  slug: santander-uk-account-information-api
- description: OBIE Read/Write Payment Initiation (PIS) API for initiating domestic, scheduled, standing-order, international, and file payments on behalf of customers. FAPI-secured (OAuth2/OIDC, mTLS, PSD2 SCA); on
  name: Santander UK Payment Initiation API
  slug: santander-uk-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API allowing an authorised card-based payment instrument issuer to confirm the availability of funds on a customer account. FAPI-secured (OAuth2/OIDC, mTL
  name: Santander UK Confirmation of Funds API
  slug: santander-uk-confirmation-of-funds-api
artifact_total: 8
common:
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
overview: 'Santander UK publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data API, Account & Transaction Information API, Payment Initiation API, and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Santander UK''s developer surface includes authentication, documentation, sandbox, and 17 more developer resources.'
random_paper: 44
scopes:
- name: Santander Uk Scopes
  scope_count: 3
  slug: santander-uk-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 39.4
  delta: -1.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.6
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 65.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Financial Services
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
