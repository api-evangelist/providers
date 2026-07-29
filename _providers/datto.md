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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-07-28'
api_count: 10
apis:
- description: Operations on accounts
  name: Datto /v2/account API
  slug: datto-v2-account-api
- description: Fetching RMM Activity Logs
  name: Datto /v2/activity-logs API
  slug: datto-v2-activity-logs-api
- description: Operations on alerts
  name: Datto /v2/alert API
  slug: datto-v2-alert-api
- description: Operations on audit data
  name: Datto /v2/audit API
  slug: datto-v2-audit-api
- description: Operations on devices
  name: Datto /v2/device API
  slug: datto-v2-device-api
- description: Operations on filters
  name: Datto /v2/filter API
  slug: datto-v2-filter-api
- description: Operations on jobs
  name: Datto /v2/job API
  slug: datto-v2-job-api
- description: Operations on sites
  name: Datto /v2/site API
  slug: datto-v2-site-api
- description: RMM API System operations
  name: Datto /v2/system API
  slug: datto-v2-system-api
- description: Operations on users
  name: Datto /v2/user API
  slug: datto-v2-user-api
artifact_total: 14
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.datto.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://rmm.datto.com/help/en/Content/2SETUP/APIv2.htm
- group: docs
  title: ''
  type: APIReference
  url: https://concord-api.centrastage.net/api/swagger-ui/index.html
- group: start
  title: ''
  type: SignUp
  url: https://www.datto.com/developers/join
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datto.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.datto.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.datto.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kaseya.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kaseya.com/legal/kaseya-privacy-statement/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.kaseya.com/trust-center/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datto.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/datto-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/datto-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datto-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/datto-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/datto-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/datto-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/datto-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/datto-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datto-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/datto-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/datto-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datto-domain-security.yml
created: '2026-07-17'
description: Datto is a data-protection and IT-management vendor for managed service providers (MSPs) and internal IT teams, now part of Kaseya. Its platform spans business continuity and disaster recovery (SIRIS, ALTO, Endpoint Backup), SaaS Protection for Microsoft 365 and Google Workspace, Remote Monitoring and Management (Datto RMM), Autotask professional services automation (PSA), networking (Wi-Fi, switches, firewalls, Secure Edge), and cybersecurity (Managed SOC, EDR, antivirus). Datto RMM publishes a versioned REST API (v2, OpenAPI 3.1) with platform-specific regional hosts on the CentraStage infrastructure, OAuth 2.0 access tokens, request-rate limiting, and paginated responses, letting partners programmatically manage sites, devices, alerts, jobs, audits, and account variables. Datto runs a formal Developer Program offering sandbox environments, technical enablement, and an integrations marketplace for vendors building on its solutions.
image: https://www.datto.com/wp-content/uploads/datto-opengraph.jpg
layout: provider
mcp_servers:
- description: ''
  name: datto-mcp.yml
  slug: datto-mcpyml
modified: '2026-07-18'
name: Datto
nav: Providers
network: true
overview: 'Datto publishes 10 APIs on the [APIs.io](https://apis.io/) network, including /v2/account API, /v2/activity-logs API, /v2/alert API, and 7 more. Tagged areas include Company, Data Protection, Backup, Disaster Recovery, and Managed Service Providers.


  Datto''s developer surface includes documentation, API reference, signup flow, pricing, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 60
rate_limits:
- limit_count: 0
  name: Datto Rate Limits
  slug: datto-rate-limits
score:
  band: developing
  composite: 45.8
  delta: -1.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 44.8
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 46.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datto/refs/heads/main/screenshots/datto-2026-07-25T211420.png
security:
- kind: authentication
  name: Datto Authentication
  slug: datto-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Datto Domain Security
  slug: datto-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datto
tags:
- Company
- Data Protection
- Backup
- Disaster Recovery
- Managed Service Providers
- Remote Monitoring and Management
- Endpoint Management
- Cybersecurity
- IT Operations
- SaaS Protection
website: https://www.datto.com/developers/
---
