---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 50
  human_in_the_loop: 3
  name: N8N Agentic Access
  operation_count: 73
  slug: n8n-agentic-access
  summary_line: 73 operations · 50 acting · 3 human-in-the-loop
api_count: 15
apis:
- description: Build with the precision of code or the speed of drag-n-drop. Host with on-prem control or in-the-cloud convenience. n8n gives you more freedom to implement multi-step AI agents and integrate apps tha
  name: N8n
  slug: n8n
- description: Operations about security audit
  name: N8n Audit API
  slug: n8n-audit-api
- description: Operations about community packages
  name: N8n CommunityPackage API
  slug: n8n-communitypackage-api
- description: Operations about credentials
  name: N8n Credential API
  slug: n8n-credential-api
- description: Operations about data tables and their rows
  name: N8n DataTable API
  slug: n8n-datatable-api
- description: API capability discovery
  name: N8n Discover API
  slug: n8n-discover-api
- description: Operations about executions
  name: N8n Execution API
  slug: n8n-execution-api
- description: Operations about folders
  name: N8n Folders API
  slug: n8n-folders-api
- description: Operations about insights
  name: N8n Insights API
  slug: n8n-insights-api
- description: Operations about projects
  name: N8n Projects API
  slug: n8n-projects-api
- description: Operations about source control
  name: N8n SourceControl API
  slug: n8n-sourcecontrol-api
- description: Operations about tags
  name: N8n Tags API
  slug: n8n-tags-api
- description: Operations about users
  name: N8n User API
  slug: n8n-user-api
- description: Operations about variables
  name: N8n Variables API
  slug: n8n-variables-api
- description: Operations about workflows
  name: N8n Workflow API
  slug: n8n-workflow-api
artifact_total: 43
collections:
- collection_type: open
  name: n8n Public API
  slug: open-n8n
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/n8n-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/n8n-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/n8n-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/n8n-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/n8n-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/n8n
- group: start
  title: ''
  type: Portal
  url: https://n8n.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.n8n.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.n8n.io/try-it-out/quickstart/
- group: start
  title: ''
  type: Login
  url: https://app.n8n.cloud/login
- group: start
  title: ''
  type: Signup
  url: https://app.n8n.cloud/magic-link
- group: commercial
  title: ''
  type: Pricing
  url: https://n8n.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.n8n.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.n8n.io/release-notes/
- group: operate
  title: ''
  type: Community
  url: https://community.n8n.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/n8n-io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://n8n.io/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://n8n.io/legal/
- group: auth
  title: ''
  type: Security
  url: https://n8n.io/legal/security/
- group: agent
  title: ''
  type: MCPServer
  url: https://blog.n8n.io/n8n-mcp-server/
created: '2025-06-06'
description: Build with the precision of code or the speed of drag-n-drop. Host with on-prem control or in-the-cloud convenience. n8n gives you more freedom to implement multi-step AI agents and integrate apps than any other tool.
features:
- 'Starter €20/mo: 2,500 executions, unlimited users, 1 project'
- 'Pro €50/mo: 10K executions, 3 projects, admin roles, 7-day insights'
- 'Business €667/mo: 40K executions, SSO/SAML/LDAP, git, self-hosted'
- 'Enterprise custom: unlimited projects, 200+ concurrent, 365-day insights'
- 'REST API: 60 req/min/workspace'
- Webhook trigger and concurrent execution scale with tier
- 1,200+ pre-built integrations
- Visual node-based workflow editor
- Code nodes (JavaScript, Python via Pyodide)
- AI Workflow Builder for natural-language workflow creation
- AI Agent nodes (LangChain integration)
- Self-hosted Community Edition (free)
- Self-hosted Enterprise Edition (paid Business+)
- Webhooks (in/out), schedule triggers, manual triggers
- Multi-environment (dev/stage/prod) on Business+
- Git-based version control on Business+
finops:
- name: N8N Finops
  service_category: Workflow Automation
  slug: n8n-finops
graphqls:
- description: n8n does not currently expose a public GraphQL API. The primary programmatic interface is a REST API documented at [https://docs.n8n.io/api/api-reference/](https://docs.n8n.io/api/api-reference/). How
  name: n8n GraphQL Schema
  slug: n8n-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/n8n.png
json_structures:
- name: N8N Structure
  property_count: 0
  slug: n8n-structure
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: N8n
nav: Providers
network: true
overview: 'N8n publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Audit API, CommunityPackage API, Credential API, and 11 more. Tagged areas include Agents, Artificial Intelligence, and Integrations.


  N8n''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: N8N Plans Pricing
  plan_count: 4
  slug: n8n-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 3
  name: N8N Rate Limits
  slug: n8n-rate-limits
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 59.9
    developer_ergonomics: 54.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/n8n/refs/heads/main/screenshots/n8n-2026-06-20T185922.png
security:
- kind: authentication
  name: N8N Authentication
  slug: n8n-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: N8N Domain Security
  slug: n8n-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: N8N Vulnerability Disclosure
  slug: n8n-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: N8N Trust Center
  slug: n8n-trust-center
  summary_line: SOC 2, GDPR
slug: n8n
tags:
- Agents
- Artificial Intelligence
- Integrations
website: https://n8n.io/
---
