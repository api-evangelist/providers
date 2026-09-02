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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 50
  human_in_the_loop: 1
  name: Triodos Bank Uk Agentic Access
  operation_count: 101
  slug: triodos-bank-uk-agentic-access
  summary_line: 101 operations · 50 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: 'This service may be used by an AISP to request information about the account of a PSU. The account is managed by the ASPSP providing the XS2A Interface. Functionality and restrictions of this service '
  name: Triodos Bank UK Account Information Service API
  slug: triodos-bank-uk-account-information-service-api
- description: The Authorization Endpoint performs authentication of the end-user.
  name: Triodos Bank UK Authorization Endpoint API
  slug: triodos-bank-uk-authorization-endpoint-api
- description: The Client Registration Endpoint performs registration of the client.
  name: Triodos Bank UK Client Registration Endpoint API
  slug: triodos-bank-uk-client-registration-endpoint-api
- description: The Configuration Endpoint provides configuration information about this OpenID service.
  name: Triodos Bank UK Configuration Endpoint API
  slug: triodos-bank-uk-configuration-endpoint-api
- description: This service may be used by a PIISP to request a confirmation of the availability of specific funds on the account of a PSU. The account is managed by the ASPSP providing the XS2A Interface. Functiona
  name: Triodos Bank UK Confirmation of Funds Service API
  slug: triodos-bank-uk-confirmation-of-funds-service-api
- description: The Extended Account Information Service API from Triodos Bank UK — 4 operation(s) for extended account information service.
  name: Triodos Bank UK Extended Account Information Service API
  slug: triodos-bank-uk-extended-account-information-service-api
- description: The Initial Access Token Service API from Triodos Bank UK — 1 operation(s) for initial access token service.
  name: Triodos Bank UK Initial Access Token Service API
  slug: triodos-bank-uk-initial-access-token-service-api
- description: This service may be used by a PISP to initiate a single payment on behalf of a PSU using a given account of that PSU. The account is managed by the ASPSP providing the XS2A Interface. Functionality an
  name: Triodos Bank UK Payment Initiation Service API
  slug: triodos-bank-uk-payment-initiation-service-api
- description: The Token Endpoint provides and revokes access tokens and refresh tokens.
  name: Triodos Bank UK Token Endpoint API
  slug: triodos-bank-uk-token-endpoint-api
- description: The UserInfo Endpoint provides information about the authenticated end-user.
  name: Triodos Bank UK UserInfo Endpoint API
  slug: triodos-bank-uk-userinfo-endpoint-api
artifact_total: 18
collections:
- collection_type: open
  name: Triodos Auth service
  slug: open-triodos-bank-uk-auth
- collection_type: open
  name: Triodos XS2A BG service
  slug: open-triodos-bank-uk-xs2a
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/triodos-bank-uk-capability-edges.yml
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
  name: Triodos Bank UK MCP Server
  slug: triodos-bank-uk-mcp-server
modified: '2026-07-23'
name: Triodos Bank UK
nav: Providers
network: true
overview: 'Triodos Bank UK publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account Information Service API, Authorization Endpoint API, Client Registration Endpoint API, and 7 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and XS2A.


  Triodos Bank UK''s developer surface includes authentication, sandbox, changelog, API reference, signup flow, documentation, getting-started guide, and 28 more developer resources.'
random_paper: 7
scopes:
- name: Triodos Bank Uk Scopes
  scope_count: 5
  slug: triodos-bank-uk-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 4.5
    contract_quality: 48.8
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: berlin-group-nextgenpsd2
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 94.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/triodos-bank-uk/refs/heads/main/screenshots/triodos-bank-uk-2026-08-17T082439.png
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
- Financial-Services
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
