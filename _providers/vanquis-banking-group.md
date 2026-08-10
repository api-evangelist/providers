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
  name: Vanquis Banking Group Agentic Access
  operation_count: 74
  slug: vanquis-banking-group-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 4
apis:
- description: Vanquis Bank's OBIE Read/Write Account and Transaction Information API (AISP), conformant to the Open Banking Implementation Entity Read/Write Data API Standard v3.1.10. Enables authorised Account Inf
  name: Vanquis Bank Account and Transaction API (AIS)
  slug: vanquis-account-transaction-api
- description: Vanquis Bank's OBIE Read/Write Payment Initiation API (PISP), conformant to the Open Banking Implementation Entity Read/Write API Standard v3.1.10. Enables authorised Payment Initiation Service Provid
  name: Vanquis Bank Payment Initiation API (PIS)
  slug: vanquis-payment-initiation-api
- description: 'Vanquis Bank''s OBIE Read/Write Confirmation of Funds API (CBPII), conformant to the Open Banking Implementation Entity Read/Write API Standard v3.1.10. Allows authorised Card Based Payment Instrument '
  name: Vanquis Bank Confirmation of Funds API (CBPII)
  slug: vanquis-confirmation-of-funds-api
- description: Vanquis Bank's OpenID / OBIE Dynamic Client Registration (DCR) endpoint, documented on the Vanquis developer portal, allowing onboarded Third Party Providers to register OAuth clients programmatically
  name: Vanquis Bank Dynamic Client Registration API
  slug: vanquis-dynamic-client-registration-api
artifact_total: 9
common:
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
  name: vanquis-banking-group-mcp.yml
  slug: vanquis-banking-group-mcpyml
modified: '2026-07-23'
name: Vanquis Banking Group
nav: Providers
network: true
overview: 'Vanquis Banking Group publishes 3 APIs on the [APIs.io](https://apis.io/) network: Vanquis Bank Account and Transaction API (AIS), Vanquis Bank Payment Initiation API (PIS), and Vanquis Bank Confirmation of Funds API (CBPII). Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Vanquis Banking Group''s developer surface includes authentication, documentation, signup flow, support, and 24 more developer resources.'
random_paper: 64
scopes:
- name: Vanquis Banking Group Scopes
  scope_count: 3
  slug: vanquis-banking-group-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 44.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.0
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 44.0
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
    score: 70.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
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
- Financial Services
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
