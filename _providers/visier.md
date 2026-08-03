---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 184
  human_in_the_loop: 10
  name: Visier Agentic Access
  operation_count: 366
  slug: visier-agentic-access
  summary_line: 366 operations · 184 acting · 10 human-in-the-loop
api_count: 10
apis:
- description: 'Administration APIs for managing a Visier deployment: tenants, users, user groups, profiles, permissions, projects, production versions, system status, sources, email domains, and network subnets. 125'
  name: Visier Administration APIs
  slug: administration
- description: 'Analytic Model APIs for querying and configuring the Visier data model: analytic objects, properties, metrics, dimensions, concepts, object configuration, and personalized alerts. 87 operations across'
  name: Visier Analytic Model APIs
  slug: analytic-model
- description: 'Authentication APIs for obtaining access to the Visier platform: basic authentication for a Visier secure token (VisierASIDToken), impersonation tokens, and OAuth 2.0 authorize/token/ userinfo endpoin'
  name: Visier Authentication APIs
  slug: authentication
- description: 'Data In APIs for loading data into Visier: Direct Data Intake (DDI), Data Upload, Data Intake, data and job handling, PGP key management, and table sources. 66 operations across 6 tags.'
  name: Visier Data In APIs
  slug: data-in
- description: 'Data Out APIs for retrieving information from Visier: the Data Query API (aggregate, list, and snapshot queries), the Vee API for natural-language questions, data version export, source file download,'
  name: Visier Data Out APIs
  slug: data-out
- description: Webhooks APIs (Beta) for registering your own HTTPS endpoints with Visier and listening for platform events such as job success/failure, data version publish, alert notifications, data upload, plan ro
  name: Visier Webhooks APIs
  slug: webhooks
- description: 'Planning APIs for Visier Strategic Workforce Planning: plan administration and plan data load operations for creating, updating, and loading data into workforce plans.'
  name: Visier Planning Public APIs
  slug: planning
- description: 'Dataset API providing access to Visier Compensation Benchmarks: market compensation data by job, location, industry, and company size, for benchmarking pay against external market reference points.'
  name: Visier Compensation Benchmarks API
  slug: compensation-benchmarks
- description: 'Skills Intelligence Engine API for skills taxonomy and inference: browse and search skills, skill groups and skill categories, standardize job titles, extract skills from free text, and match skills t'
  name: Visier Skills Intelligence Engine API
  slug: skills-intelligence-engine
- description: Visier's hosted Model Context Protocol server, exposing Vee (natural-language workforce question answering) and structured data-query tools to MCP clients such as Claude Desktop and Cursor over HTTPS/
  name: Visier Query MCP Server
  slug: query-mcp
artifact_total: 19
asyncapis:
- description: ''
  name: Visier Webhooks
  slug: visier-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.visier.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.visier.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.visier.com/developer/Default.htm
- group: docs
  title: ''
  type: APIReference
  url: https://docs.visier.com/developer/apis/apis.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.visier.com/developer/apis/apis-get-started-home.htm
- group: operate
  title: ''
  type: Support
  url: https://my.visier.com/csm?id=community_home
- group: company
  title: ''
  type: Blog
  url: https://www.visier.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/visier
- group: start
  title: ''
  type: SignUp
  url: https://www.visier.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.visier.com/terms-of-use-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.visier.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/visier-alpine?tab=collections
- group: operate
  title: ''
  type: StatusPage
  url: https://status.visier.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.visier.com/developer/apis/version-control.htm
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/visier-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.visier.com/.well-known/security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/visier-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.visier.com/trust/compliance/
- group: build
  title: ''
  type: CLI
  url: cli/visier-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/visier-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/visier-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/visier-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/visier-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/visier-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/visier-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/visier-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/visier-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/visier-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/visier-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/visier-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/visier-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/visier-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/visier-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/visier-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/visier-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/visier-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/visier-agentic-access.yml
created: '2026-08-02'
description: Visier is a workforce and people analytics platform that consolidates HR, talent, compensation, and operational data into a purpose-built people data model, then exposes that model for analysis, planning, and AI-assisted question answering. Visier publishes a broad suite of public REST APIs — Data In (Direct Data Intake, Data Upload, job handling), Data Out (Data Query, Vee, exports), Administration (tenants, users, profiles, permissions, projects), Analytic Model (data model, concepts, metrics, dimensions), Planning, Webhooks, and dataset APIs such as Compensation Benchmarks and the Skills Intelligence Engine. OpenAPI v3 definitions for every collection are published on GitHub at visier/openapi-clients, generated Python SDKs ship to PyPI, and a hosted Visier Query MCP server exposes Vee and data-query tools to MCP clients over OAuth 2.0.
image: https://www.visier.com/static/visier-og-image-289b36a6392a307b7342ffcf69bdee4c.jpg
layout: provider
mcp_servers:
- description: ''
  name: visier-mcp.yml
  slug: visier-mcpyml
modified: '2026-08-02'
name: Visier
nav: Providers
network: true
overview: 'Visier publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Administration APIs, Analytic Model APIs, Authentication APIs, and 6 more. Tagged areas include Company, People Analytics, Workforce Analytics, Human Resources, and HR Technology.


  The Visier catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Visier''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 31 more developer resources.'
random_paper: 88
rate_limits:
- limit_count: 2
  name: Visier Rate Limits
  slug: visier-rate-limits
scopes:
- name: Visier Scopes
  scope_count: 2
  slug: visier-scopes
  summary_line: 2 scopes · authorizationCode/password
score:
  band: strong
  composite: 60.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.2
    developer_ergonomics: 77.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 76.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Visier Authentication
  slug: visier-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Visier Domain Security
  slug: visier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Visier Vulnerability Disclosure
  slug: visier-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Visier Trust Center
  slug: visier-trust-center
  summary_line: SOC 2, CSA STAR Level 1
slug: visier
tags:
- Company
- People Analytics
- Workforce Analytics
- Human Resources
- HR Technology
- Workforce Planning
- Analytics
- Business Intelligence
- Compensation
- Skills
- Artificial Intelligence
- Model Context Protocol
website: https://www.visier.com/
---
