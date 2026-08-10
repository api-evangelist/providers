---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 50
  human_in_the_loop: 1
  name: Triodos Bank Uk Agentic Access
  operation_count: 101
  slug: triodos-bank-uk-agentic-access
  summary_line: 101 operations · 50 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: The XS2A Account Information Service (AIS) from Triodos Bank UK - 13 operation(s) for consented, secure read access to Triodos payment account details, balances, and transaction history under the Berl
  name: Triodos Account Information Service (AIS) API
  slug: triodos-account-information-api
- description: The XS2A Payment Initiation Service (PIS) from Triodos Bank UK - 66 operation(s) for initiating, authorising, and tracking SEPA, cross-border, UK domestic, and periodic (recurring) payments from Triod
  name: Triodos Payment Initiation Service (PIS) API
  slug: triodos-payment-initiation-api
- description: The XS2A Confirmation of Funds Service (CoF/CBPII) from Triodos Bank UK - 9 operation(s) for card-based payment instrument issuers to check the availability of funds on a Triodos account under the Ber
  name: Triodos Confirmation of Funds Service (CoF) API
  slug: triodos-confirmation-of-funds-api
- description: The Triodos Auth service - 8 operation(s) implementing OAuth2 / OpenID Connect for XS2A third-party providers, including dynamic client registration, OpenID configuration discovery, authorization, tok
  name: Triodos XS2A Authorization (OAuth2/OIDC) API
  slug: triodos-authorization-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/triodos-bank-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/triodos-bank-uk-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/triodos-bank-uk-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: security/triodos-bank-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/triodos-bank-uk-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/triodos-bank-uk-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/triodos-bank-uk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/triodos-bank-uk-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/triodos-bank-uk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/triodos-bank-uk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/triodos-bank-uk-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/triodos-bank-uk-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/triodos-bank-uk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.triodos.co.uk/open-banking-developers
- group: start
  title: ''
  type: Sandbox
  url: sandbox/triodos-bank-uk-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/triodos-bank-uk-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/triodos-bank-uk-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/triodos-bank-uk-xs2a-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/triodos-bank-uk-auth-overlay.yaml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/triodos-bank-uk-changelog.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.triodos.com/reference
- group: start
  title: ''
  type: SignUp
  url: https://developer.triodos.com/docs/registration
- group: company
  title: ''
  type: Website
  url: https://www.triodos.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.triodos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.triodos.com/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.triodos.com/docs/getting-started
- group: other
  title: ''
  type: OpenBanking
  url: https://www.triodos.co.uk/open-banking-developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.triodos.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://developer.triodos.com/docs/support
- group: company
  title: ''
  type: Blog
  url: https://www.triodos.co.uk/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/triodos-bank
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.triodos.co.uk/privacy-statement
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/triodos-bank-uk-llms.txt
created: '2026-07-23'
description: Triodos Bank UK Limited is a values-based, sustainability-focused bank headquartered in Bristol, England, and the UK arm of Triodos Bank N.V. (founded 1980, Netherlands), one of Europe's leading ethical banks. Ownership of the parent sits with the SAAT foundation (Stichting Administratiekantoor Aandelen Triodos Bank), which issues depositary receipts rather than tradable shares, so Triodos is neither a conventional listed plc nor a customer mutual; it is a certified B Corporation that lends only to organisations delivering positive social, environmental, and cultural impact. Triodos Bank UK Ltd (company no. 11379025) is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and PRA (FRN 817008). As an FCA-authorised ASPSP it meets UK Open Banking / PSD2 obligations, but - unlike the CMA9 - it is a specialist lender that implements the Berlin Group NextGenPSD2 (XS2A) standard rather than the OBIE UK Read/Write standard, publishing a
  single developer platform at developer.triodos.com covering its UK, Netherlands, and Belgium account holders. Its production XS2A APIs provide Account Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CoF) services, secured with OAuth2/OpenID Connect authorization, mutual-TLS client authentication, eIDAS/QWAC certificates, and PSD2 strong customer authentication, with a full sandbox for onboarding and testing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: triodos-bank-uk-mcp.yml
  slug: triodos-bank-uk-mcpyml
modified: '2026-07-23'
name: Triodos Bank UK
nav: Providers
network: true
overview: 'Triodos Bank UK publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Triodos Account Information Service (AIS) API, Triodos Payment Initiation Service (PIS) API, Triodos Confirmation of Funds Service (CoF) API, and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and XS2A.


  Triodos Bank UK''s developer surface includes authentication, sandbox, changelog, API reference, signup flow, documentation, getting-started guide, and 27 more developer resources.'
random_paper: 106
scopes:
- name: Triodos Bank Uk Scopes
  scope_count: 5
  slug: triodos-bank-uk-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 51.2
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 94.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Triodos Bank Uk Authentication
  slug: triodos-bank-uk-authentication
  summary_line: oauth2/openIdConnect/mutualTLS/httpMessageSignature/http-basic · 4 schemes
- kind: domain-security
  name: Triodos Bank Uk Domain Security
  slug: triodos-bank-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Triodos Bank Uk Vulnerability Disclosure
  slug: triodos-bank-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: triodos-bank-uk
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- XS2A
- Berlin Group
- United Kingdom
- Payments
- Account Information
- Confirmation of Funds
- Ethical Banking
- Sustainable Finance
- Specialist Lender
website: https://www.triodos.co.uk/
---
