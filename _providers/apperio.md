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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Apperio Agentic Access
  operation_count: 30
  slug: apperio-agentic-access
  summary_line: 30 operations · 17 acting
api_count: 5
apis:
- description: A set of non resource based endpoints that power various components within Apperio. These endpoints primarily support discovery and data investigation.
  name: Apperio Analytics API
  slug: apperio-analytics-api
- description: The e-billing endpoints provide access to the e-billing invoices in Apperio. They allow you to retrieve information about the invoices and the approval workflow, and also to approve and reject invoice
  name: Apperio E-billing API
  slug: apperio-e-billing-api
- description: 'The filter endpoints provide resource discovery in Apperio. This has two basic mechanisms. Firstly there are the resource discovery endpoints. These are: * `/api/v1/filter/engagements/` * `/api/v1/fil'
  name: Apperio Filter API
  slug: apperio-filter-api
- description: A set of endpoints returning information about a specific matter.
  name: Apperio Matter information API
  slug: apperio-matter-information-api
- description: The users endpoints allow you to manage your API tokens. Tokens are used to authenticate requests to the Apperio API. You can list your existing tokens, delete tokens that are no longer needed, and ac
  name: Apperio Users API
  slug: apperio-users-api
artifact_total: 11
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apperio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.apperio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.apperio.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.apperio.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/apperio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apperio-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apperio-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apperio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apperio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.apperio.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apperio-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apperio-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apperio-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apperio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.apperio.com/information-security
- group: auth
  title: ''
  type: TrustCenter
  url: security/apperio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apperio-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apperio-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apperio-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apperio-llms.txt
- group: start
  title: ''
  type: Login
  url: https://app.apperio.com/login/
- group: operate
  title: ''
  type: Support
  url: https://www.apperio.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.apperio.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apperio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apperio.com/privacy-notice
- group: company
  title: ''
  type: Website
  url: https://www.apperio.com
created: '2026-07-17'
description: Apperio is a legal spend management and matter management platform for in-house legal teams and the law firms they work with. It connects directly to law-firm time-and-billing systems to give continuous, real-time visibility into billed and unbilled ("work in progress") legal spend, benchmarking to negotiate rates, and AI-assisted e-billing review against Outside Counsel Guidelines. The Apperio REST API exposes the same secure data that powers the platform's analytics — legal-spend analytics, matter (engagement) and invoice discovery, matter tagging, and e-billing invoice approval workflows — across its two-sided business/law-firm model. Apperio is a Seedcamp portfolio company and is now part of Persuit.
image: https://developer.apperio.com/static/favicon-32x32.png
layout: provider
mcp_servers:
- description: ''
  name: apperio-mcp.yml
  slug: apperio-mcpyml
modified: '2026-07-17'
name: Apperio
nav: Providers
network: true
overview: 'Apperio publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, E-billing API, Filter API, and 2 more. Tagged areas include Legal, Legal Spend Management, Legal Tech, E-Billing, and Matter Management.


  Apperio''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 20 more developer resources.'
random_paper: 38
rate_limits:
- limit_count: 2
  name: Apperio Rate Limits
  slug: apperio-rate-limits
score:
  band: developing
  composite: 52.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.5
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 52.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Apperio Authentication
  slug: apperio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apperio Domain Security
  slug: apperio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Apperio Trust Center
  slug: apperio-trust-center
  summary_line: ISO/IEC 27001, SOC 2 Type 2, Cyber Essentials
slug: apperio
tags:
- Legal
- Legal Spend Management
- Legal Tech
- E-Billing
- Matter Management
- Legal Operations
- Analytics
- Company
website: https://www.apperio.com
---
