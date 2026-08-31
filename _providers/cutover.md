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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Cutover Core API is a RESTful, JSON:API-style interface for programmatically managing workspaces, runbooks, tasks, teams, and users in the Cutover collaborative automation platform. It uses predic
  name: Cutover Core API
  slug: cutover-core-api
artifact_total: 6
asyncapis:
- description: ''
  name: Cutover Events Webhooks
  slug: cutover-events-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cutover-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://cutover.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cutover.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cutover.com/cutover-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cutover.com/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cutover.com/cutover-api/developer-role
- group: operate
  title: ''
  type: Support
  url: https://developer.cutover.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.cutover.com/en/
- group: company
  title: ''
  type: Blog
  url: https://cutover.com/blog-and-news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gocutover
- group: commercial
  title: ''
  type: Pricing
  url: https://cutover.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cutover.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cutover.com/privacy-notice
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.cutover.com/updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cutover-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cutover-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cutover-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cutover-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cutover-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cutover-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cutover-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cutover-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cutover.com/security
- group: auth
  title: ''
  type: Security
  url: https://cutover.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cutover-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cutover-events-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cutover-llms.txt
created: '2026-07-17'
description: Cutover is a collaborative automation and IT resilience platform that codifies operational work as task-led runbooks for IT disaster recovery, application recovery, major incident management, and complex change and release events. The platform combines automated runbooks, real-time dashboards, immutable audit trails, and AI-assisted orchestration to reduce mean time to resolution and meet recovery time objectives across hybrid and multi-cloud estates. Cutover exposes a RESTful Core API (JSON:API-style envelopes, bearer User App Token authentication) for programmatically managing workspaces, runbooks, tasks, teams, and users, plus outbound event/webhook integrations, an open-source MCP server, and a broad third-party integration suite (ServiceNow, Jira, Datadog, AWS, Ansible, Jenkins, Slack, Microsoft Teams and more).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cutover.png
layout: provider
mcp_servers:
- description: ''
  name: Cutover MCP Server
  slug: cutover-mcp-server
modified: '2026-07-18'
name: Cutover
nav: Providers
network: true
overview: 'Cutover publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, IT Operations, Disaster Recovery, and Incident Management.


  The Cutover catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cutover''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 20 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 46.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cutover/refs/heads/main/screenshots/cutover-2026-07-25T211011.png
security:
- kind: authentication
  name: Cutover Authentication
  slug: cutover-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cutover Domain Security
  slug: cutover-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cutover Trust Center
  slug: cutover-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: cutover
tags:
- Company
- Business Applications
- IT Operations
- Disaster Recovery
- Incident Management
- Runbook Automation
- Orchestration
- Workflow-Automation
- DevOps
website: https://cutover.com
---
