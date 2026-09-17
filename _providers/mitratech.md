---
agent_readiness:
  band: agent-ready
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-09-16'
api_count: 2
apis:
- description: Modernized REST API shipped with TeamConnect Enterprise 7.2 and later, served from each customer's own TeamConnect instance at /webservice/enterprise/. Exposes Accounts, Appointments, Contacts, Docume
  name: Mitratech TeamConnect REST API
  slug: mitratech-teamconnect-rest-api
- description: Remote Model Context Protocol server served from mitratech.com over Streamable HTTP. Advertises OAuth 2.0 authorization-server metadata at /.well-known/oauth-authorization-server and protected-resourc
  name: Mitratech MCP Server
  slug: mitratech-mcp-server
- baseURL: https://{tenant}.tap.thinksmart.com/{tenant}/api
  baseurl_source: declared
  description: The Dashboard API from Mitratech — 1 operation(s) for dashboard.
  name: Mitratech Dashboard API
  slug: mitratech-dashboard-api
- baseURL: https://{tenant}.tap.thinksmart.com/{tenant}/api
  baseurl_source: declared
  description: The Files API from Mitratech — 1 operation(s) for files.
  name: Mitratech Files API
  slug: mitratech-files-api
- baseURL: https://{tenant}.tap.thinksmart.com/{tenant}/api
  baseurl_source: declared
  description: The GridConfigurations API from Mitratech — 3 operation(s) for gridconfigurations.
  name: Mitratech Grid Configurations API
  slug: mitratech-gridconfigurations-api
- baseURL: https://{tenant}.tap.thinksmart.com/{tenant}/api
  baseurl_source: declared
  description: The Templates API from Mitratech — 1 operation(s) for templates.
  name: Mitratech Templates API
  slug: mitratech-templates-api
- baseURL: https://{tenant}.tap.thinksmart.com/{tenant}/api
  baseurl_source: declared
  description: The Users API from Mitratech — 5 operation(s) for users.
  name: Mitratech Users API
  slug: mitratech-users-api
- baseURL: https://{tenant}.tap.thinksmart.com/{tenant}/api
  baseurl_source: declared
  description: The Workflow API from Mitratech — 1 operation(s) for workflow.
  name: Mitratech Workflow API
  slug: mitratech-workflow-api
- baseURL: https://{tenant}.tap.thinksmart.com/{tenant}/api
  baseurl_source: declared
  description: The Workflows API from Mitratech — 32 operation(s) for workflows.
  name: Mitratech Workflows API
  slug: mitratech-workflows-api
- baseURL: https://{your-tc-instance}/webservice/enterprise/v1
  baseurl_source: declared
  description: The Health Check API from Mitratech — 1 operation(s) for health check.
  name: Mitratech Health Check API
  slug: mitratech-health-check-api
artifact_total: 17
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/overlays/mitratech-tap-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mitratech-tap-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/security/mitratech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mitratech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mitratech.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://success.mitratech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://success.mitratech.com/TAP/TAP_Solutions/APIs_and_Integrations/TAP_API_Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://default.stagingtap.thinksmart.com/default/api/swagger/ui/index
- group: start
  title: ''
  type: GettingStarted
  url: https://success.mitratech.com/TAP/TAP_Solutions/APIs_and_Integrations
- group: operate
  title: ''
  type: Support
  url: https://success.mitratech.com/
- group: company
  title: ''
  type: Blog
  url: https://mitratech.com/resource-hub/mitratech-blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mitratech.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mitratech.com/legal-notice/
- group: start
  title: ''
  type: SignUp
  url: https://mitratech.com/contact-us/
- group: operate
  title: ''
  type: ChangeLog
  url: https://success.mitratech.com/TAP/ReleaseNotes
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/changelog/mitratech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mitratech-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/lifecycle/mitratech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mitratech-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/authentication/mitratech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mitratech-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/scopes/mitratech-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mitratech-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/conventions/mitratech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mitratech-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/errors/mitratech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mitratech-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/conformance/mitratech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mitratech-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/data-model/mitratech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mitratech-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/sandbox/mitratech-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mitratech-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/mcp/mitratech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mitratech-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/mcp/mitratech-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mitratech-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/llms/mitratech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mitratech-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/well-known/mitratech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mitratech-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/packages/mitratech-packages.yml
  title: ''
  type: Packages
  url: packages/mitratech-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/plans/mitratech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mitratech-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mitratech/refs/heads/main/rate-limits/mitratech-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mitratech-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ThinkSmart
- group: build
  title: ''
  type: Examples
  url: https://github.com/ThinkSmart/API_Examples
created: '2026-09-13'
description: 'Mitratech is an Austin, Texas based enterprise software company supplying legal operations, governance, risk and compliance, and HR compliance software to corporate legal departments, compliance teams and human resources organizations. Its platform spans enterprise legal management and matter management (TeamConnect), legal spend and e-billing, no-code workflow automation and intake (TAP Workflow Automation, acquired with ThinkSmart), policy and risk management (PolicyHub, Alyne), immigration case management (INSZoom), HR compliance, talent and background screening (Mineral, Trakstar, AssureHire, Circa), and contract lifecycle management. Programmatic access is delivered per-product and per-tenant rather than through a single public developer portal: TAP publishes an OData-style REST API with a live Swagger 2.0 API Explorer, TeamConnect 7.2+ ships a modernized OAuth 2.0 REST API on each customer instance, and mitratech.com itself serves an OAuth-protected Model Context Protocol
  server.'
image: https://mitratech.com/wp-content/uploads/Mitratech_Web-Assets_Home-Feature-Image-HD-1024x577.png
layout: provider
mcp_servers:
- description: ''
  name: Mitratech MCP Server
  slug: mitratech-mcp-server
- description: ''
  name: Mitratech MCP Server
  slug: mitratech-mcp-server-2
modified: '2026-09-13'
name: Mitratech
nav: Providers
network: true
overview: 'Mitratech publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Dashboard API, Files API, Grid Configurations API, and 5 more. Tagged areas include Legal, Legal Operations, Enterprise Legal Management, Matter Management, and Governance Risk and Compliance.


  Mitratech''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 25 more developer resources.'
plans:
- name: Mitratech Plans Pricing
  plan_count: 0
  slug: mitratech-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Mitratech Rate Limits
  slug: mitratech-rate-limits
scopes:
- name: Mitratech Scopes
  scope_count: 0
  slug: mitratech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 48.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 40.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Mitratech Authentication
  slug: mitratech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mitratech Domain Security
  slug: mitratech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mitratech
tags:
- Legal
- Legal Operations
- Enterprise Legal Management
- Matter Management
- Governance Risk and Compliance
- Compliance
- Workflow-Automation
- Contract Lifecycle Management
- HR Compliance
- Risk Management
- Immigration
- OData
- MCP
website: https://mitratech.com/
---
