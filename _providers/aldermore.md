---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Aldermore Agentic Access
  operation_count: 86
  slug: aldermore-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: The UK Open Banking Open Data API standard (public, unauthenticated reference data such as products, ATMs, and branches). Represented here as the shared OBIE Open Data standard - no Aldermore-publishe
  name: Aldermore Open Data API (OBIE Standard)
  slug: aldermore-open-data-api
- description: The UK Open Banking Read/Write Account and Transaction Information (AIS) API standard, FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication. Represented here as the share
  name: Aldermore Account & Transaction Information API (OBIE Read/Write Standard)
  slug: aldermore-account-information-api
- description: The UK Open Banking Read/Write Payment Initiation (PIS) API standard, FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication. Represented here as the shared OBIE standard -
  name: Aldermore Payment Initiation API (OBIE Read/Write Standard)
  slug: aldermore-payment-initiation-api
- description: The UK Open Banking Read/Write Confirmation of Funds (CBPII) API standard, FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication. Represented here as the shared OBIE stand
  name: Aldermore Confirmation of Funds API (OBIE Read/Write Standard)
  slug: aldermore-confirmation-of-funds-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aldermore-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aldermore-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aldermore-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aldermore-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aldermore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.aldermore.co.uk/.well-known/security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aldermore-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/aldermore-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/aldermore-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/aldermore-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aldermore-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aldermore-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aldermore-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aldermore-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aldermore-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aldermore-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aldermore-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aldermore-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aldermore-confirmation-of-funds-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aldermore-open-data-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.aldermore.co.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aldermore
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aldermorebank
- group: operate
  title: ''
  type: Support
  url: https://www.aldermore.co.uk/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aldermore.co.uk/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aldermore.co.uk/legal/privacy-policy/
- group: commercial
  title: ''
  type: Legal
  url: https://www.aldermore.co.uk/legal/
created: '2026-07-23'
description: Aldermore Bank plc is a UK specialist bank founded in 2009 and headquartered in Reading, offering savings accounts and specialist lending across residential and buy-to-let mortgages, commercial and property finance, asset finance, invoice finance, and motor finance (through sister company MotoNovo Finance). Aldermore Group is wholly owned by South Africa's FirstRand Group, which acquired it in 2018 and, as of 2026, has begun a process to sell the UK business and exit the market. Aldermore Bank plc is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA (Financial Services Register number 204503). It is a branchless, digitally-delivered specialist lender rather than a full-service current-account bank, and it is NOT one of the nine CMA-mandated banks (CMA9). Because it does not provide personal or business current accounts, its UK Open Banking (OBIE / PSD2) payment-account footprint is minimal, and no public Aldermore
  developer portal, Open Data endpoint, or bank-proprietary API surface could be confirmed at bootstrap; the OBIE Open Data and Read/Write API families below are represented as the shared UK Open Banking standard, unverified for this bank.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: aldermore-mcp.yml
  slug: aldermore-mcpyml
modified: '2026-07-23'
name: Aldermore Bank
nav: Providers
network: true
overview: 'Aldermore Bank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Aldermore Open Data API (OBIE Standard), Aldermore Account & Transaction Information API (OBIE Read/Write Standard), Aldermore Payment Initiation API (OBIE Read/Write Standard), and 1 more. Tagged areas include Financial Services, Banking, Savings, Specialist Lending, and Open Banking.


  Aldermore Bank''s developer surface includes authentication, support, legal docs, and 25 more developer resources.'
random_paper: 5
scopes:
- name: Aldermore Scopes
  scope_count: 3
  slug: aldermore-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 59.7
    developer_ergonomics: 19.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 42.1
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
    score: 78.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aldermore/refs/heads/main/screenshots/aldermore-2026-07-25T195550.png
security:
- kind: authentication
  name: Aldermore Authentication
  slug: aldermore-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Aldermore Domain Security
  slug: aldermore-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Aldermore Vulnerability Disclosure
  slug: aldermore-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: aldermore
tags:
- Financial Services
- Banking
- Savings
- Specialist Lending
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
website: https://www.aldermore.co.uk/
---
