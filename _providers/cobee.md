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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Cobee Agentic Access
  operation_count: 21
  slug: cobee-agentic-access
  summary_line: 21 operations · 12 acting
api_count: 2
apis:
- description: The Companies API from Cobee by Pluxee — 16 operation(s) for companies.
  name: Cobee by Pluxee Companies API
  slug: cobee-companies-api
- description: The Oauth API from Cobee by Pluxee — 1 operation(s) for oauth.
  name: Cobee by Pluxee Oauth API
  slug: cobee-oauth-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://cobee.io/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.cobee.io/en/get_started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.cobee.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.cobee.io/en/api-reference/api_introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.cobee.io/en/get_started
- group: company
  title: ''
  type: Blog
  url: https://cobee.io/en/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://cobee.io/en/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.cobee.io/sign-in
- group: operate
  title: ''
  type: Support
  url: https://www.pluxee.es/helpcenter/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cobee.io/en/terms-condition/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cobee.io/en/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cobee-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cobee-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cobee-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cobee-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cobee-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cobee-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cobee-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cobee-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cobee-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cobee-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cobee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cobee-domain-security.yml
created: '2026-07-17'
description: Cobee is a Madrid-based flexible employee benefits and compensation platform, acquired by Pluxee (Sodexo group) in 2024. It lets companies manage a modular multi-benefit program (meal, transport, training, health and life insurance, wellbeing and employee discounts) from a single dashboard, delivered to employees through a Cobee VISA card and mobile app. Cobee exposes a REST Public API (v3, OpenAPI 3.0.1) for HR and payroll integrations, covering companies, employees, benefit models, payroll cycles, and benefit consumptions, with OAuth 2.0 client-credentials (Auth0-issued JWT) auth and a separate staging sandbox. The Public API is currently available to Spanish customers, with credentials issued by the customer's Customer Success Manager.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cobee.png
layout: provider
mcp_servers:
- description: ''
  name: cobee-mcp.yml
  slug: cobee-mcpyml
modified: '2026-07-18'
name: Cobee by Pluxee
nav: Providers
network: true
overview: 'Cobee by Pluxee publishes 2 APIs on the [APIs.io](https://apis.io/) network: Companies API and Oauth API. Tagged areas include Company, Employee Benefits, Compensation, Human Resources, and Payroll.


  Cobee by Pluxee''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, authentication, and 17 more developer resources.'
random_paper: 36
score:
  band: developing
  composite: 45.0
  delta: -0.8
  facets:
    commercial_clarity: 52.6
    contract_quality: 47.5
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cobee/refs/heads/main/screenshots/cobee-2026-07-25T205844.png
security:
- kind: authentication
  name: Cobee Authentication
  slug: cobee-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Cobee Domain Security
  slug: cobee-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Cobee Trust Center
  slug: cobee-trust-center
  summary_line: trust center published
slug: cobee
tags:
- Company
- Employee Benefits
- Compensation
- Human Resources
- Payroll
- Fintech
- Spain
- Flexible Benefits
website: https://cobee.io/en/
---
