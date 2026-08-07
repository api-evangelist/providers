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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'REST/JSON server-side API for investor accreditation, KYC/KYB/AML, identity, risk monitoring, and case management. v2 (current) authenticates with a Bearer API key; v1 (legacy) and the JavaScript SDK '
  name: Parallel Markets Server API
  slug: parallel-markets-server-api
artifact_total: 6
asyncapis:
- description: ''
  name: Parallel Markets Webhooks
  slug: parallel-markets-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://parallelmarkets.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.parallelmarkets.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.parallelmarkets.com/docs/server
- group: docs
  title: ''
  type: APIReference
  url: https://developer.parallelmarkets.com/docs/server/case-management-api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.parallelmarkets.com/docs/sandbox-quickstart
- group: start
  title: ''
  type: Sandbox
  url: sandbox/parallel-markets-sandbox.yml
- group: operate
  title: ''
  type: Support
  url: https://support.parallelmarkets.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parallel-markets
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/parallelmarkets/parallel-api-public/collection/cqp1t8k/parallel-markets-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.parallelmarkets.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/parallel-markets-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.parallelmarkets.com/docs/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://parallelmarkets.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parallelmarkets.com/terms-of-service
- group: build
  title: ''
  type: Packages
  url: packages/parallel-markets-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/parallel-markets-packages.yml
- group: design
  title: ''
  type: Components
  url: components/parallel-markets-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parallel-markets-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/parallel-markets-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parallel-markets-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parallel-markets-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parallel-markets-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/parallel-markets-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/parallel-markets-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parallel-markets-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parallel-markets-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parallel-markets-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parallel-markets-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parallel-markets-domain-security.yml
created: '2026-07-17'
description: Parallel Markets (an iCapital company) is the leader in reusable financial identity, providing an end-to-end solution for investor onboarding, verification, and monitoring. Its platform handles investor accreditation for 506(c) offerings, Know-Your-Customer (KYC), Know-Your-Business (KYB), Anti-Money-Laundering (AML) and sanctions/risk monitoring, beneficial-ownership mapping, and identity verification. Partners integrate a client-side JavaScript SDK that collects user information in an accreditation, KYC, KYB, or general onboarding flow, plus a server-side REST API (Server API and Case Management API) and signed webhooks that push accreditation, identity, and risk updates. The reusable "Passport" lets users assert their identity and accreditation status across third-party platforms. Trusted by investment advisors, asset managers, brokers, and fundraising platforms.
image: https://developer.parallelmarkets.com/img/logo.png
layout: provider
mcp_servers:
- description: ''
  name: parallel-markets-mcp.yml
  slug: parallel-markets-mcpyml
modified: '2026-07-20'
name: Parallel Markets
nav: Providers
network: true
overview: 'Parallel Markets publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Identity Verification, KYC, and AML.


  The Parallel Markets catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Parallel Markets'' developer surface includes documentation, API reference, getting-started guide, sandbox, support, changelog, authentication, and 22 more developer resources.'
random_paper: 67
scopes:
- name: Parallel Markets Scopes
  scope_count: 4
  slug: parallel-markets-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 69.6
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 52.6
  previous_composite: 45.8
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Parallel Markets Authentication
  slug: parallel-markets-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Parallel Markets Domain Security
  slug: parallel-markets-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: parallel-markets
tags:
- Company
- Identity
- Identity Verification
- KYC
- AML
- Accreditation
- Compliance
- Financial Services
- Onboarding
- Investor Verification
- Webhooks
website: https://parallelmarkets.com
---
