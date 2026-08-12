---
access_model:
  confidence: medium
  label: Paid · Partner/sales onboarding (API keys via developer portal)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - documentation
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: 'The MX Platform API aggregates and enhances financial data, connecting apps and websites to tens of thousands of financial institutions. Covers users, members, accounts, transactions, categorization, '
  name: MX Platform API
  slug: mx-platform-api
- description: Data Access is MX's open-finance API platform for sharing an institution's financial data and accessing other institutions' data using FDX and OAuth standards, with tokenized, consumer-permissioned ac
  name: MX Data Access
  slug: mx-data-access
- description: MX Consent Management V4 API from MX — 4 path(s) described in OpenAPI.
  name: MX Consent Management V4 API
  slug: mx-consent-management-openapi
artifact_total: 12
asyncapis:
- description: ''
  name: Mx Webhooks
  slug: mx-webhooks
collections:
- collection_type: postman
  name: Consent Management V4 API
  slug: postman-mx-consent-management
- collection_type: postman
  name: MX Platform API
  slug: postman-mx-platform-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mx/overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/mx-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mx-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mx.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mxenabled
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/425337
- group: company
  title: ''
  type: Blog
  url: https://www.mx.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mx.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mx.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://support.mx.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mx.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.mx.com/api-reference/platform-api/overview/versioning
- group: auth
  title: ''
  type: Security
  url: https://mx.com/security-policy/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mx-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mx-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mx.com/trust/
- group: build
  title: ''
  type: Packages
  url: packages/mx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mx-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mx-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/mx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mx-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mx-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mx-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mx-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mx-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/mx-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mx-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mx-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mx-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.mx.com/sign_up
created: '2026-07-23'
description: MX Technologies is a privately held financial data platform headquartered in Lehi, Utah, operating as a B2B data aggregator and open-finance infrastructure provider rather than a chartered bank or credit union. MX connects consumer and business accounts across tens of thousands of financial institutions and fintechs, then cleanses, categorizes, and enhances the resulting transaction data so banks and fintechs can build verification, aggregation, and personal-finance experiences. Unlike most US banks, MX runs a real, self-documented developer surface — the MX Platform API (HTTP Basic auth over https://api.mx.com), a Consent Management API, and a Data Access product that shares and consumes institution data using FDX and OAuth standards — with downloadable OpenAPI 3.0 specifications published at docs.mx.com. MX is one of the major US open-finance aggregators (alongside Plaid, Finicity, and Akoya) and positions Data Access as FDX-conformant, consumer-permissioned, tokenized data
  sharing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: mx-mcp.yml
  slug: mx-mcpyml
modified: '2026-07-23'
name: MX
nav: Providers
network: true
overview: 'MX publishes 2 APIs on the [APIs.io](https://apis.io/) network: Platform API and Consent Management V4 API. Tagged areas include Financial Services, Banking, United States, Open Finance, and Data Aggregation.


  The MX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MX''s developer surface includes authentication, documentation, engineering blog, support, changelog, sandbox, signup flow, and 28 more developer resources.'
random_paper: 113
rate_limits:
- limit_count: 4
  name: Mx Rate Limits
  slug: mx-rate-limits
score:
  band: strong
  composite: 57.9
  delta: -3.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.6
    developer_ergonomics: 53.8
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 94.7
  previous_composite: 61.3
  provenance:
    conformance: first-party
    contracts:
      callable: 50.0
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
    score: 45.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mx/refs/heads/main/screenshots/mx-2026-08-07T184503.png
security:
- kind: authentication
  name: Mx Authentication
  slug: mx-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Mx Domain Security
  slug: mx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mx Vulnerability Disclosure
  slug: mx-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mx Trust Center
  slug: mx-trust-center
  summary_line: SOC 2, PCI DSS
slug: mx
tags:
- Financial Services
- Banking
- United States
- Open Finance
- Data Aggregation
- FDX
- Fintech
- Financial Data
website: https://www.mx.com/
---
