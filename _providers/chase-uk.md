---
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Chase Uk Agentic Access
  operation_count: 74
  slug: chase-uk-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: Chase UK's Account Information Service (AIS) dedicated interface, conformant to the OBIE Read/Write API Standard, letting FCA-authorised AISPs retrieve a consenting customer's account, balance, transa
  name: Chase UK Account and Transaction Information API (AIS)
  slug: chase-uk-account-information-api
- description: Chase UK's Payment Initiation Service (PIS) dedicated interface, conformant to the OBIE Read/Write API Standard, enabling FCA-authorised PISPs to create single immediate payments, future-dated payment
  name: Chase UK Payment Initiation API (PIS)
  slug: chase-uk-payment-initiation-api
- description: Chase UK's Confirmation of Funds (CBPII) dedicated interface, conformant to the OBIE Read/Write API Standard, allowing an FCA-authorised card-based payment instrument issuer to check whether a specifi
  name: Chase UK Confirmation of Funds API (CBPII)
  slug: chase-uk-confirmation-of-funds-api
artifact_total: 8
common:
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
  name: chase-uk-mcp.yml
  slug: chase-uk-mcpyml
modified: '2026-07-23'
name: Chase UK
nav: Providers
network: true
overview: 'Chase UK publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account and Transaction Information API (AIS), Payment Initiation API (PIS), and Confirmation of Funds API (CBPII). Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Chase UK''s developer surface includes authentication, documentation, getting-started guide, support, sandbox, and 22 more developer resources.'
random_paper: 8
scopes:
- name: Chase Uk Scopes
  scope_count: 3
  slug: chase-uk-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 43.8
  delta: 1.3
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 16.7
    contract_quality: 55.9
    developer_ergonomics: 47.0
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 42.5
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
- Financial Services
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
