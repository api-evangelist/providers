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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Create and manage data migration (import) jobs.
  name: Import2 Imports API
  slug: import2-imports-api
- description: Supported source and destination migration tools.
  name: Import2 Tools API
  slug: import2-tools-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Import2 Imports API
  slug: open-import2-imports-api
- collection_type: open
  name: Import2 Imports Tools API
  slug: open-import2-tools-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/import2-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.import2.com
- group: start
  title: ''
  type: Portal
  url: https://partners.import2.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.import2.com/
- group: docs
  title: ''
  type: APIReference
  url: https://import2.github.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.import2.com/how-it-works
- group: operate
  title: ''
  type: Support
  url: https://help.import2.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.import2.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.import2.com/session/new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.import2.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.import2.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/import2
- group: auth
  title: ''
  type: Authentication
  url: authentication/import2-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/import2-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/import2-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/import2-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/import2-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/import2-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/import2-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/import2-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.import2.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/import2-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/import2-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/import2-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/import2-llms.txt
created: '2026-07-17'
description: Import2 is a fully automated data-migration platform that moves customer data between SaaS applications — CRM, helpdesk, and project-management tools — without CSV exports or custom development. Users connect a source and destination app and Import2 moves records, custom fields, pipelines, and deal stages directly over each app's API, processing data in real time on a temporary machine that is destroyed after the migration. It supports 50+ tools (Salesforce, HubSpot, Zendesk, Pipedrive, Asana, Monday.com, Jira and more) and offers a free sample migration before a full run. Import2 also exposes a partner/vendor API (v2.1) so SaaS vendors can create and track automated migrations programmatically, plus sibling tools ViaCSV and MyCRMBackup.
image: https://cdn.prod.website-files.com/698e5a4787478ca03bb07614/699307813937eab1c0993d3d_webclip.png
layout: provider
mcp_servers:
- description: ''
  name: Import2 MCP Server
  slug: import2-mcp-server
modified: '2026-07-19'
name: Import2
nav: Providers
network: true
overview: 'Import2 publishes 2 APIs on the [APIs.io](https://apis.io/) network: Imports API and Tools API. Tagged areas include Company, Data Migration, Data Integration, CRM, and Help Desk.


  Import2''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, pricing, signup flow, and 19 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 1
  name: Import2 Rate Limits
  slug: import2-rate-limits
score:
  band: developing
  composite: 39.5
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 14.2
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 39.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/import2/refs/heads/main/screenshots/import2-2026-07-25T222154.png
security:
- kind: authentication
  name: Import2 Authentication
  slug: import2-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Import2 Domain Security
  slug: import2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Import2 Trust Center
  slug: import2-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
slug: import2
tags:
- Company
- Data Migration
- Data Integration
- CRM
- Help Desk
- Software-as-a-Service
- Migration
- Onboarding
website: https://www.import2.com
---
