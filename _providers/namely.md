---
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.1
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API v1 for a Namely HRIS tenant. Covers employee profiles (including the tenant's own custom fields), the profile field and section schema, groups, group types and teams, job titles and job tiers
  name: Namely API
  slug: namely-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/namely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://namely.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.namely.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.namely.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.namely.com/docs/namely-api/12dab89109ded-namely-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.namely.com/docs/namely-api/72f9086e4f0e7-introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/namely-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://namely.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://namely.com/employee-support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/namely
- group: commercial
  title: ''
  type: Pricing
  url: https://namely.com/lp/pricing/
- group: start
  title: ''
  type: Login
  url: https://namely.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://namely.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://namely.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.namely.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/namely-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/namely-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/namely-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/namely-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/namely-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/namely-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/namely-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/namely-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/namely-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/namely-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/namely-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/namely-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/namely-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://namely.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/namely-llms.txt
created: '2026-08-26'
description: Namely is a mid-market Human Capital Management (HCM) platform combining HR, payroll, onboarding, benefits administration, time and attendance, performance management and applicant tracking, delivered as a multi-tenant SaaS on customer subdomains. It publishes a public developer portal on Stoplight carrying a Swagger 2.0 contract for its REST API v1 (39 paths, 54 operations, 95 schemas) covering employee profiles, the tenant-specific profile field schema, groups and teams, job titles and tiers, company resources, the social home feed, notifications and reports. Alongside the REST API, Namely runs a SCIM 2.0 provisioning surface acting as the source of record for identity providers such as Okta, and supports SAML 2.0 single sign-on as a service provider. Authentication is either a 3-legged OAuth 2.0 authorization code grant for partner integrations or a Personal Access Token for a customer's own integrations, both minted inside the customer's own tenant. Namely merged into the
  combined Vensure Employer Solutions / PrismHR organisation in September 2022.
image: https://namely.com/wp-content/uploads/2023/11/Namely.svg
layout: provider
mcp_servers:
- description: 'Namely ships NO MCP server. This file is a DERIVED candidate tool surface computed from the 54 operations in Namely''s published Swagger 2.0 contract, so that the shape of an agent-native Namely is on '
  name: Namely MCP tool candidate
  slug: namely-mcp-tool-candidate
modified: '2026-08-26'
name: Namely
nav: Providers
network: true
overview: 'Namely publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include HR, Human Capital Management, Payroll, Employee Data, and Onboarding.


  Namely''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 24 more developer resources.'
plans:
- name: Namely Plans Pricing
  plan_count: 4
  slug: namely-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Namely Rate Limits
  slug: namely-rate-limits
score:
  band: strong
  composite: 57.4
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 30.3
    contract_quality: 41.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 55.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Namely Authentication
  slug: namely-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Namely Domain Security
  slug: namely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: namely
tags:
- HR
- Human Capital Management
- Payroll
- Employee Data
- Onboarding
- Benefits
- Applicant Tracking
- Performance Management
- SCIM
- Single Sign-On
- Identity Provisioning
- Workforce Management
website: https://namely.com/
---
