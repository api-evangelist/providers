---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 66.7
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 10
  name: Plansource Agentic Access
  operation_count: 80
  slug: plansource-agentic-access
  summary_line: 80 operations · 44 acting · 10 human-in-the-loop
api_count: 1
apis:
- description: The PlanSource Admin API v2 - a collection of categorized RESTful endpoints that let partners, brokers, organizations and carriers get, create and update employees (subscribers), dependents, beneficia
  name: PlanSource Benefits Administration API
  slug: plansource-benefits-administration-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://plansource.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.plansource.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.plansource.com/docs/plansource-administrative-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.plansource.com/v2.0/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.plansource.com/docs/utilize-postman
- group: build
  title: ''
  type: Postman
  url: https://www.getpostman.com/collections/93f063e64815e4122102
- group: operate
  title: ''
  type: Support
  url: https://developer.plansource.com/docs/contact-support
- group: company
  title: ''
  type: Blog
  url: https://plansource.com/blog/
- group: start
  title: ''
  type: Login
  url: https://benefits.plansource.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plansource.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plansource.com/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: security/plansource-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.plansource.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plansource-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plansource-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plansource-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plansource-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plansource-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/plansource-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plansource-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plansource-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/plansource-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plansource-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plansource-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plansource-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/plansource-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plansource-agentic-access.yml
created: '2026-08-06'
description: PlanSource is a benefits administration and employee-benefits engagement platform used by employers, brokers, carriers and HR/payroll partners to run enrollment, eligibility, billing and benefits communication. Its public developer surface is the PlanSource Benefits Administration API (Admin API v2), a RESTful HTTPS API of 80 operations across 62 paths covering employee (subscriber) demographics, dependents, beneficiaries, coverages and stacked coverage lines, payroll deductions with lookup codes and pre-tax/post-tax/employer/imputed amounts, Evidence of Insurability decisions and form completions, ACA offer and enrollee reporting data, administrator accounts, and organization portal page content. It is designed to replace fixed-schedule EDI files with near real-time sync between an HCM/payroll system of record and PlanSource. Authentication is OAuth 2.0 client credentials (scope admin_api_v2) or a legacy AuthenticationString + Signature header pair, with OpenID Connect and
  SAML 2.0 available for end-user single sign-on. The API is documented on a ReadMe developer portal that publishes llms.txt, an agent-skills manifest and an OAuth-gated MCP server, and PlanSource maintains a SafeBase trust center listing SOC 2 Type 2, ISO/IEC 27001:2022, HIPAA, CCPA and 23 NYCRR 500.
image: https://plansource.com/wp-content/uploads/2026/01/ps_social-share-img.webp
layout: provider
mcp_servers:
- description: ''
  name: plansource-mcp.yml
  slug: plansource-mcpyml
modified: '2026-08-06'
name: PlanSource
nav: Providers
network: true
overview: 'PlanSource publishes 1 API on the [APIs.io](https://apis.io/) network: Benefits Administration API. Tagged areas include Employee Benefits, Benefits Administration, Insurance, Human Resources, and Payroll.


  PlanSource''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 21 more developer resources.'
random_paper: 67
scopes:
- name: Plansource Scopes
  scope_count: 8
  slug: plansource-scopes
  summary_line: 8 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 53.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.0
    developer_ergonomics: 78.3
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Plansource Authentication
  slug: plansource-authentication
  summary_line: oauth2/apiKey/openIdConnect/saml2 · 5 schemes
- kind: domain-security
  name: Plansource Domain Security
  slug: plansource-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Plansource Trust Center
  slug: plansource-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, HIPAA, CCPA, 23 NYCRR 500
slug: plansource
tags:
- Employee Benefits
- Benefits Administration
- Insurance
- Human Resources
- Payroll
- Health Insurance
- Enrollment
- HR Technology
- Evidence of Insurability
- ACA Reporting
- Eligibility
- Single Sign-On
website: https://plansource.com/
---
