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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 28.8
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'RESTful JSON web service exposing OneStream Data Automation functions: Authentication, Data Management (ExecuteSequence, ExecuteStep), and Data Provider (ADO datasets from adapters, Cube Views, SQL, a'
  name: OneStream Web (REST) API
  slug: onestream-web-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.onestream.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.onestream.com
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.onestream.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.onestream.com/docs/Content/REST%20API/REST%20API%20Overview.html
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.onestream.com/docs/Content/REST%20API/OneStream%20REST%20API%20Implementation.html
- group: operate
  title: ''
  type: Support
  url: https://www.onestream.com/support/
- group: operate
  title: ''
  type: Community
  url: https://community.onestreamsoftware.com/
- group: company
  title: ''
  type: Blog
  url: https://www.onestream.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneStreamSoftware
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onestream.com/saas-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onestream.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.onestream.com/request-demo/
- group: other
  title: ''
  type: Marketplace
  url: https://solution-exchange.onestream.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/onestream-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/onestream-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onestream-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/onestream-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/onestream-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onestream-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.onestream.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/onestream-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onestream-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/onestream-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onestream-llms.txt
created: '2026-07-17'
description: OneStream is an enterprise finance platform that unifies financial and operational data into a single source of truth, spanning financial close and consolidation, planning, budgeting, forecasting and financial planning & analysis (FP&A), account reconciliation, and reporting. It applies AI and machine learning to automate core finance work so teams can focus on analysis and decision-making. For developers and integrators OneStream exposes the OneStream Web (REST) API — a client-agnostic JSON-over-HTTPS service with Authentication, Data Management, and Data Provider endpoints — secured with bearer tokens (Personal Access Tokens via OneStream IdentityServer, or OAuth 2.0 client_credentials through Microsoft Entra ID, Okta, or PingFederate) and extended through the Solution Exchange (MarketPlace, PartnerPlace, OpenPlace).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onestream.png
layout: provider
mcp_servers:
- description: ''
  name: onestream-mcp.yml
  slug: onestream-mcpyml
modified: '2026-07-20'
name: OneStream
nav: Providers
network: true
overview: 'OneStream publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software, Finance, Corporate Performance Management, and Financial Planning and Analysis.


  OneStream''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Onestream Authentication
  slug: onestream-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Onestream Domain Security
  slug: onestream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Onestream Trust Center
  slug: onestream-trust-center
  summary_line: SOC 1, SOC 2 Type II, ISO 27001, FedRAMP ATO, CSA CAIQ / STAR, NIST 800-53 (aligned)
slug: onestream
tags:
- Company
- Software
- Finance
- Corporate Performance Management
- Financial Planning and Analysis
- Financial Close
- Consolidation
- Enterprise
- API
website: https://www.onestream.com
---
