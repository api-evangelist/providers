---
access_model:
  confidence: medium
  label: TPP onboarding · OBIE/eIDAS certificates required
  onboarding: unknown
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: C Hoare And Co Agentic Access
  operation_count: 66
  slug: c-hoare-and-co-agentic-access
  summary_line: 66 operations · 20 acting
api_count: 3
apis:
- description: OBIE Read/Write Account & Transaction Information (AIS) API — lets onboarded, consented AISP third-party providers retrieve C. Hoare & Co. account, balance, transaction, beneficiary, standing order, d
  name: C. Hoare & Co. Account and Transaction Information API
  slug: c-hoare-and-co-account-and-transaction-api
- description: 'OBIE Read/Write Payment Initiation (PIS) API — lets onboarded, consented PISP third-party providers initiate domestic and scheduled payments and standing orders and retrieve payment/consent status on '
  name: C. Hoare & Co. Payment Initiation API
  slug: c-hoare-and-co-payment-initiation-api
- description: OBIE Dynamic Client Registration (DCR) proxy — lets third-party providers submit a signed Software Statement Assertion to register an OAuth2 client with C. Hoare & Co. as part of TPP onboarding. Publi
  name: C. Hoare & Co. Dynamic Client Registration API
  slug: c-hoare-and-co-dynamic-client-registration-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/c-hoare-and-co-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/c-hoare-and-co-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/c-hoare-and-co-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/c-hoare-and-co-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hoaresbank.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hoaresbank.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hoaresbank.co.uk/open-banking
- group: other
  title: ''
  type: OpenID
  url: https://developer.hoaresbank.co.uk/.well-known/openid-configuration
- group: operate
  title: ''
  type: Support
  url: https://www.hoaresbank.co.uk/contact-us
- group: operate
  title: ''
  type: Support
  url: mailto:developersupport@hoaresbank.co.uk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hoaresbank.co.uk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hoaresbank.co.uk/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://www.hoaresbank.co.uk/legal
- group: auth
  title: ''
  type: Compliance
  url: https://register.fca.org.uk/s/firm?id=001b000000MfFMxAAN
- group: other
  title: ''
  type: Registration
  url: https://www.openbanking.org.uk/regulated-providers/c-hoare-co-2/
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/c-hoare-&-co
- group: design
  title: ''
  type: Conventions
  url: conventions/c-hoare-and-co-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/c-hoare-and-co-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/c-hoare-and-co-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/c-hoare-and-co-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/c-hoare-and-co-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/c-hoare-and-co-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/c-hoare-and-co-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/c-hoare-and-co-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/c-hoare-and-co-tool-crosswalk.yml
created: '2026-07-23'
description: C. Hoare & Co. (Hoares Bank) is the United Kingdom's oldest privately-owned bank, founded in 1672 by Sir Richard Hoare and owned continuously by the Hoare family for twelve generations, operating a bespoke private banking, lending, and wealth business from Fleet Street in London and an office in Cambridge. It is an FCA-authorised ASPSP (Account Servicing Payment Service Provider) and a regulated participant in UK Open Banking under PSD2. As a private bank it is not one of the CMA9 mandated institutions, so it does not publish the unauthenticated Open Data (ATM / branch / product) reference APIs; instead it exposes the OBIE Read/Write standard through a MuleSoft Anypoint developer portal at developer.hoaresbank.co.uk, publishing Account and Transaction Information (AIS), Payment Initiation (PIS), and Dynamic Client Registration conformant to the Open Banking Implementation Entity (OBIE) v3.1 standard. Production access is FAPI-secured with OAuth2/OIDC, PSD2 strong customer authentication,
  and mutual-TLS client authentication using OBIE/eIDAS certificates after third-party provider onboarding.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: c-hoare-and-co-mcp.yml
  slug: c-hoare-and-co-mcpyml
modified: '2026-07-23'
name: C. Hoare & Co.
nav: Providers
network: true
overview: 'C. Hoare & Co. publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account and Transaction Information API, Payment Initiation API, and Dynamic Client Registration API. Tagged areas include Financial Services, Banking, Private Bank, Open Banking, and PSD2.


  C. Hoare & Co.''s developer surface includes authentication, documentation, support, legal docs, and 22 more developer resources.'
random_paper: 46
scopes:
- name: C Hoare And Co Scopes
  scope_count: 2
  slug: c-hoare-and-co-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 39.0
  delta: -4.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 41.5
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 43.8
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
    score: 67.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/c-hoare-and-co/refs/heads/main/screenshots/c-hoare-and-co-2026-07-25T204150.png
security:
- kind: authentication
  name: C Hoare And Co Authentication
  slug: c-hoare-and-co-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: C Hoare And Co Domain Security
  slug: c-hoare-and-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: c-hoare-and-co
tags:
- Financial Services
- Banking
- Private Bank
- Open Banking
- PSD2
- OBIE
- FAPI
- United Kingdom
- Payments
- Account Information
website: https://www.hoaresbank.co.uk/
---
