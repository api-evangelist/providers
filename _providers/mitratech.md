---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
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
artifact_total: 21
common:
- group: other
  href: https://artifacts.apis.io/mitratech/capabilities/mitratech-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mitratech-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/mitratech/overlays/mitratech-tap-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mitratech-tap-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/mitratech/security/mitratech-domain-security.yml
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
  href: https://artifacts.apis.io/mitratech/changelog/mitratech-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mitratech-changelog.yml
- group: design
  href: https://artifacts.apis.io/mitratech/lifecycle/mitratech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mitratech-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/mitratech/authentication/mitratech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mitratech-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mitratech/scopes/mitratech-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mitratech-scopes.yml
- group: design
  href: https://artifacts.apis.io/mitratech/conventions/mitratech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mitratech-conventions.yml
- group: design
  href: https://artifacts.apis.io/mitratech/errors/mitratech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mitratech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mitratech/conformance/mitratech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mitratech-conformance.yml
- group: design
  href: https://artifacts.apis.io/mitratech/data-model/mitratech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mitratech-data-model.yml
- group: start
  href: https://artifacts.apis.io/mitratech/sandbox/mitratech-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mitratech-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/mitratech/mcp/mitratech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mitratech-mcp.yml
- group: build
  href: https://artifacts.apis.io/mitratech/mcp/mitratech-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mitratech-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/mitratech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/mitratech/llms/mitratech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mitratech-llms.txt
- group: agent
  href: https://artifacts.apis.io/mitratech/well-known/mitratech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mitratech-well-known.yml
- group: build
  href: https://artifacts.apis.io/mitratech/packages/mitratech-packages.yml
  title: ''
  type: Packages
  url: packages/mitratech-packages.yml
- group: commercial
  href: https://artifacts.apis.io/mitratech/plans/mitratech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mitratech-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mitratech/rate-limits/mitratech-rate-limits.yml
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
finops:
- has_sources: true
  method: derived
  name: Mitratech Finops
  primary_unit: ''
  service_category: ''
  slug: mitratech-finops
  template: true
image: https://mitratech.com/wp-content/uploads/Mitratech_Web-Assets_Home-Feature-Image-HD-1024x577.png
layout: provider
mcp_servers:
- description: Remote MCP server at mitratech.com over streamable HTTP requiring OAuth.
  name: Mitratech MCP Server
  slug: mitratech-mcp-oauth-server
modified: '2026-09-13'
name: Mitratech
nav: Providers
network: true
overview: 'Mitratech publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dashboard API, Files API, Grid Configurations API, and 7 more. Tagged areas include Legal, Legal Operations, Enterprise Legal Management, Matter Management, and Governance Risk and Compliance.


  The Mitratech catalog on APIs.io includes 1 Spectral governance ruleset.


  Mitratech''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 26 more developer resources.'
plans:
- name: Mitratech Plans Pricing
  plan_count: 0
  slug: mitratech-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Mitratech Rate Limits
  slug: mitratech-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Mitratech API Rules
  rule_count: 39
  severity_counts:
    error: 33
    hint: 0
    info: 2
    warn: 4
  slug: mitratech-rules
scopes:
- name: Mitratech Scopes
  scope_count: 2
  slug: mitratech-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 44.7
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 28.9
  previous_composite: 48.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mitratech/mitratech-2026-10-11T111142.png
security:
- kind: authentication
  name: Mitratech Authentication
  slug: mitratech-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mitratech Domain Security
  slug: mitratech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: mitratech-tap-initiate-workflow
  slug: mitratech-tap-initiate-workflow
- name: mitratech-tap-triage-assigned-work
  slug: mitratech-tap-triage-assigned-work
- name: mitratech-tap-workflow-evidence
  slug: mitratech-tap-workflow-evidence
slug: mitratech
tags:
- Legal
- Legal Operations
- Enterprise Legal Management
- Matter Management
- Governance Risk and Compliance
- Compliance
- Workflow Automation
- Contract Lifecycle Management
- HR Compliance
- Risk Management
- Immigration
- OData
- MCP
website: https://mitratech.com/
---
