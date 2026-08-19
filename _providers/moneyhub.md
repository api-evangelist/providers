---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 36
  human_in_the_loop: 0
  name: Moneyhub Agentic Access
  operation_count: 77
  slug: moneyhub-agentic-access
  summary_line: 77 operations · 36 acting
api_count: 2
apis:
- description: 'The Moneyhub Data API (v2.0) is a RESTful, JSON, bearer-token API for Open Banking account aggregation and financial intelligence: connect accounts, read balances, holdings, standing orders, statement'
  name: Moneyhub Data & Intelligence API
  slug: moneyhub-data-api
- description: Moneyhub's Open Banking Payments API initiates account-to-account payments (Payment Initiation Service) over the UK Faster Payments rails as a cheaper, near-instant alternative to cards, direct debits
  name: Moneyhub Open Banking Payments API
  slug: moneyhub-open-banking-payments-api
artifact_total: 12
asyncapis:
- description: ''
  name: Moneyhub Webhooks
  slug: moneyhub-webhooks
collections:
- collection_type: postman
  name: Moneyhub Data API
  slug: postman-moneyhub-data-api-swagger
- collection_type: open
  name: Moneyhub Data API
  slug: open-moneyhub-data-api-swagger
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/moneyhub/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moneyhub-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/moneyhub-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://moneyhub.com/policies/security-and-trust-at-moneyhub/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moneyhub-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://moneyhub.com/policies/security-and-trust-at-moneyhub/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moneyhub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moneyhub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moneyhub-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moneyhub-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moneyhub-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moneyhub-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moneyhub-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moneyhub-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.moneyhubenterprise.com/docs/system-availability-and-performance-metrics
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.moneyhubenterprise.com/docs/versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/moneyhub-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moneyhub-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moneyhub-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moneyhub-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/moneyhub-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moneyhub-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moneyhub-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/moneyhub-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moneyhub-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/moneyhub-data-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.moneyhub.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.moneyhubenterprise.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moneyhubenterprise.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://moneyhub.github.io/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moneyhubenterprise.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://identity.moneyhub.co.uk/oidc/.well-known/openid-configuration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moneyhub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moneyhub
- group: company
  title: ''
  type: Blog
  url: https://www.moneyhub.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.moneyhub.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moneyhub.com/policies/global-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moneyhub.com/privacy-policy/
created: '2026-07-24'
description: 'Moneyhub is a UK open banking and open finance platform, headquartered in London with offices in Bristol and Ljubljana, that lets banks, pension providers, wealth managers, insurers and fintechs embed account aggregation, transaction data enrichment, financial insight and account-to-account payment initiation into their own products. Regulated by the FCA as an Account Information Service Provider (AISP), Payment Initiation Service Provider (PISP) and Credit Information Services Provider (CISP), Moneyhub ships a genuinely API-first surface: a RESTful, Swagger/OpenAPI-documented Data & Intelligence API for AIS aggregation, enrichment and affordability, and an Open Banking Payments API that initiates instant Faster Payments over the UK''s Open Banking rails as a cheaper alternative to cards and direct debits. Authentication and payment consent run entirely through an OpenID Connect / OAuth2 identity layer at identity.moneyhub.co.uk, with client-credentials, authorization-code
  and jwt-bearer grants and fine-grained scopes for data and payment initiation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: moneyhub-mcp.yml
  slug: moneyhub-mcpyml
modified: '2026-07-24'
name: Moneyhub
nav: Providers
network: true
overview: 'Moneyhub publishes 1 API on the [APIs.io](https://apis.io/) network: Data & Intelligence API. Tagged areas include Payments, United Kingdom, Open Banking, Open Finance, and Account-to-Account.


  The Moneyhub catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Moneyhub''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, engineering blog, and 31 more developer resources.'
random_paper: 126
scopes:
- name: Moneyhub Scopes
  scope_count: 108
  slug: moneyhub-scopes
  summary_line: 108 scopes
score:
  band: strong
  composite: 61.9
  delta: 4.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 30.3
    contract_quality: 52.1
    developer_ergonomics: 60.7
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 48.7
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 84.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moneyhub/refs/heads/main/screenshots/moneyhub-2026-08-07T184155.png
security:
- kind: authentication
  name: Moneyhub Authentication
  slug: moneyhub-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Moneyhub Domain Security
  slug: moneyhub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Moneyhub Vulnerability Disclosure
  slug: moneyhub-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Moneyhub Trust Center
  slug: moneyhub-trust-center
  summary_line: ISO 27001
slug: moneyhub
tags:
- Payments
- United Kingdom
- Open Banking
- Open Finance
- Account-to-Account
- Payment Initiation
- Data Aggregation
- AISP
- PISP
- Fintech
website: https://www.moneyhub.com/
---
