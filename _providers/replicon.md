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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Proprietary JSON-over-HTTPS web-service API for the Replicon Time Intelligence Platform and Polaris PSA — users, clients, projects, tasks, time, billing/costing and analytics. Tenants resolve their re
  name: Replicon & Polaris API
  slug: replicon-polaris-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replicon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.replicon.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.replicon.com/help/
- group: docs
  title: ''
  type: APIReference
  url: https://learning.deltek.com/bundle/RepliconRESTService/page/RepliconDevRes_RESTS_APIReference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.replicon.com/help/getting-started-with-the-replicon-and-polaris-api/
- group: operate
  title: ''
  type: Support
  url: https://www.replicon.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.replicon.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/replicon
- group: commercial
  title: ''
  type: Pricing
  url: https://www.replicon.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.replicon.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.replicon.com/legal/privacy/
- group: start
  title: ''
  type: Login
  url: https://polarislogin.replicon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.replicon.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/replicon-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/replicon-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/replicon-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/replicon-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/replicon-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/replicon-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/replicon-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/replicon-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.deltek.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/replicon-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/replicon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.deltek.com/company/security-and-trust/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/replicon-llms.txt
created: '2026-07-17'
description: Replicon, now a Deltek company, is a time-tracking, project time and expense, and professional-services automation (PSA) platform. Its Time Intelligence Platform and the Polaris PSA product manage timesheets, projects, tasks, clients, resources, billing and costing for professional-services and enterprise teams. Replicon exposes a proprietary JSON-over-HTTPS web-service API (no public OpenAPI) covering users, clients, projects, tasks, time, billing and analytics; callers resolve a tenant swimlane through a global discovery service and authenticate with an Api-token header or HTTP Basic.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/replicon.png
layout: provider
modified: '2026-07-20'
name: Replicon
nav: Providers
network: true
overview: 'Replicon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Software, Time Tracking, Timesheets, and Project Management.


  Replicon''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 19 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 37.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 37.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Replicon Authentication
  slug: replicon-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Replicon Domain Security
  slug: replicon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Replicon Vulnerability Disclosure
  slug: replicon-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Replicon Trust Center
  slug: replicon-trust-center
  summary_line: ISO/IEC 27001:2013
slug: replicon
tags:
- Company
- Enterprise Software
- Time Tracking
- Timesheets
- Project Management
- Professional Services Automation
- Workforce Management
- Billing
website: https://www.replicon.com
---
