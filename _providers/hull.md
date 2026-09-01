---
access_model:
  confidence: high
  label: Closed — platform shut down 31 December 2022
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.hull.io/pricing/
  - https://www.hull.io/faq/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Flat REST API for Hull's Customer Data Platform, addressing objects by ID under the /api/v1 prefix on a per-organization hullapp.io subdomain. Covers Users, Accounts, Events, Segments, organization/co
  name: Hull HTTP API
  slug: hull-http-api
artifact_total: 9
asyncapis:
- description: ''
  name: Hull Webhooks
  slug: hull-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.hull.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hull.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hull.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.hull.io/docs/reference/http_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hull.io/docs/guides/
- group: company
  title: ''
  type: Blog
  url: https://www.hull.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hull.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hull.io/pp/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hull
- group: auth
  title: ''
  type: Authentication
  url: authentication/hull-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hull-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hull-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hull-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hull.io/
- group: build
  title: ''
  type: Packages
  url: packages/hull-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hull-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hull-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hull-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hull-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hull-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hull-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hull-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.hull.io/faq/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changes.hull.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hull-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.hull.io/faq/
- group: commercial
  title: ''
  type: Plans
  url: plans/hull-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hull-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hull-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hull-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.hull.io/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/hull-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.hull.io/security/
created: '2026-07-17'
description: Hull is a real-time Customer Data Platform (CDP) that unifies customer data from every source — web, product, CRM, marketing and support tools, databases and files — into a single User and Account profile using claim-based identity resolution. It ingests, computes and enriches data through a data-lifecycle pipeline (Ingest / Compute / Notify), organizes people and companies into Segments, and syncs the resulting profiles out to more than fifty tools via Connectors ("ships"). Developers integrate through a flat HTTP API at https://{organization}.hullapp.io/api/v1 covering Users, Accounts, Events, Segments, Status and Bulk operations, plus first-party Node, browser, PHP and Ruby client libraries and an outgoing/incoming webhook surface. Hull was acquired by MessageBird (now Bird) and the platform was switched off at 09:00 ET on 31 December 2022, with all infrastructure decommissioned and customer data deleted; the marketing site and documentation remain published but the API host
  no longer answers.
image: https://www.hull.io/assets/images/logo/logo_dark@2x.png
layout: provider
mcp_servers:
- description: ''
  name: Hull MCP Server
  slug: hull-mcp-server
modified: '2026-08-13'
name: Hull
nav: Providers
network: true
overview: 'Hull publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Data Platform, CDP, Identity Resolution, and Data Integration.


  The Hull catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hull''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, authentication, support, and 26 more developer resources.'
plans:
- name: Hull Plans Pricing
  plan_count: 3
  slug: hull-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Hull Rate Limits
  slug: hull-rate-limits
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 48.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 72.4
  previous_composite: 50.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hull/refs/heads/main/screenshots/hull-2026-07-25T221636.png
security:
- kind: authentication
  name: Hull Authentication
  slug: hull-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Hull Domain Security
  slug: hull-domain-security
  summary_line: DMARC
- kind: vulnerability-disclosure
  name: Hull Vulnerability Disclosure
  slug: hull-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Hull Trust Center
  slug: hull-trust-center
  summary_line: SOC 2 Type 2, GDPR, EU-US Privacy Shield, Penetration testing
slug: hull
tags:
- Company
- Customer Data Platform
- CDP
- Identity Resolution
- Data Integration
- Customer Data
- Marketing
- Real-Time
- iPaaS
- Analytics
website: https://www.hull.io
---
