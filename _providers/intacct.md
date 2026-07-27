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
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 27.9
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Modern REST API for Sage Intacct using standard HTTP verbs and predictable URLs to operate on Intacct objects and data. Authenticates with OAuth 2.0 and supports batch, bulk, and composite requests. S
  name: Sage Intacct REST API
  slug: sage-intacct-rest-api
- description: The long-standing XML/HTTP Web Services API for Sage Intacct, session-based with sender and user credentials. Still fully supported alongside the REST API; official SDKs (PHP, .NET, Node.js) are built
  name: Sage Intacct XML Web Services API
  slug: sage-intacct-xml-web-services-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.sageintacct.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sage.com/intacct
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sage.com/intacct/docs/openapi
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sage.com/intacct/apis/intacct/1/intacct-openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intacct
- group: company
  title: ''
  type: Blog
  url: https://www.sage.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.sage.com/en-us/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sage.com/en-us/sage-business-cloud/intacct/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://developer.sage.com/intacct
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sage.com/en-us/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sage.com/en-us/legal/privacy-and-cookies/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sage.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.sage.com/en-gb/trust-security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.sage.com/en-us/trust-security/security/technical/standards-compliance/
- group: build
  title: ''
  type: Packages
  url: packages/intacct-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/intacct-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/intacct-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/intacct-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/intacct-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/intacct-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/intacct-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intacct-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/intacct-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/intacct-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/intacct-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/intacct-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/intacct-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intacct-llms.txt
created: '2026-07-17'
description: 'Sage Intacct is a cloud-based financial management and accounting (ERP) platform for growing and mid-market businesses, delivering core financials, accounts payable and receivable, cash management, order and purchasing, multi-entity and global consolidations, project accounting, revenue recognition, dashboards and advanced reporting. The Sage Intacct Developer program exposes this functionality through two programmable interfaces: a modern REST API (OAuth 2.0, batch/bulk/composite requests) and the long-standing XML Web Services API, backed by official SDKs for PHP, .NET, and Node.js/JavaScript. New objects and features ship on the REST API first, and Sage''s AI Gateway adds a governed Model Context Protocol (MCP) surface for AI agents on top of the same APIs.'
image: https://logo.clearbit.com/sageintacct.com
layout: provider
mcp_servers:
- description: ''
  name: intacct-mcp.yml
  slug: intacct-mcpyml
modified: '2026-07-19'
name: Sage Intacct
nav: Providers
network: true
overview: 'Sage Intacct publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, ERP, Financial Management, and Cloud Accounting.


  Sage Intacct''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 22 more developer resources.'
random_paper: 62
scopes:
- name: Intacct Scopes
  scope_count: 4
  slug: intacct-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials/tokenExchange
score:
  band: developing
  composite: 47.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 47.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 89.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intacct/refs/heads/main/screenshots/intacct-2026-07-25T222634.png
security:
- kind: authentication
  name: Intacct Authentication
  slug: intacct-authentication
  summary_line: oauth2/openIdConnect/apiKey · 2 schemes
- kind: domain-security
  name: Intacct Domain Security
  slug: intacct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Intacct Vulnerability Disclosure
  slug: intacct-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Intacct Trust Center
  slug: intacct-trust-center
  summary_line: SOC 1 Type II (SSAE 18 / ISAE 3402), SOC 2 Type II, ISO 27001, PCI DSS Level 1, HIPAA, GDPR, ISAE 3000
slug: intacct
tags:
- Company
- Accounting
- ERP
- Financial Management
- Cloud Accounting
- Invoicing
- Payments
- SaaS
- REST API
- OAuth
website: https://www.sageintacct.com/
---
