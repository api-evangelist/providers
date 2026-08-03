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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Unified REST API surface across Nova Credit's products (Credit Passport v4, Cash Atlas v2, Income Navigator v2, Eligibility Compass v1). Server-side clients authenticate with HTTP Basic to mint a shor
  name: Nova Credit Platform API
  slug: nova-credit-platform-api
artifact_total: 6
asyncapis:
- description: ''
  name: Nova Credit Webhooks
  slug: nova-credit-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.novacredit.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.novacredit.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.novacredit.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.novacredit.com/credit-passport/v4
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.novacredit.com/credit-passport-quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.novacredit.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://novacreditsupport.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.novacredit.com/corporate-blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/novacredit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.novacredit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.novacredit.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/nova-credit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nova-credit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nova-credit-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nova-credit-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nova-credit-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nova-credit-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nova-credit-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/nova-credit-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nova-credit-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nova-credit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nova-credit-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nova-credit-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nova-credit-trust-center.yml
created: '2026-07-17'
description: Nova Credit is a fintech consumer-credit-data platform that gives lenders and financial institutions a single API to access unified consumer credit data from more than 26 sources — international credit bureaus, bank-transaction aggregators, payroll systems, and automated document data. Its products (Credit Passport, Cash Atlas, Income Navigator, and Eligibility Compass) let institutions underwrite qualified newcomers and thin-file applicants with translated international credit history, run cashflow-based underwriting from bank data, automate income verification with fraud detection, and speed income/asset verification for affordable housing. The developer platform exposes REST APIs over api.novacredit.com with a dedicated sandbox host, HTTP Basic to short-lived Bearer authentication, JWE-encrypted report payloads, hosted NovaConnect consent webviews, webhooks, SCIM and SSO.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nova-credit.png
layout: provider
mcp_servers:
- description: ''
  name: nova-credit-mcp.yml
  slug: nova-credit-mcpyml
modified: '2026-07-20'
name: Nova Credit
nav: Providers
network: true
overview: 'Nova Credit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Credit Data, Consumer Credit, Credit Bureau, and Income Verification.


  The Nova Credit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nova Credit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 17 more developer resources.'
random_paper: 71
score:
  band: developing
  composite: 43.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 43.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Nova Credit Authentication
  slug: nova-credit-authentication
  summary_line: http-basic/http-bearer · 2 schemes
- kind: domain-security
  name: Nova Credit Domain Security
  slug: nova-credit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nova Credit Trust Center
  slug: nova-credit-trust-center
  summary_line: trust center published
slug: nova-credit
tags:
- Company
- Credit Data
- Consumer Credit
- Credit Bureau
- Income Verification
- Underwriting
- Fintech
- Financial Services
- Lending
- Cash Flow Underwriting
- Identity
website: https://www.novacredit.com
---
