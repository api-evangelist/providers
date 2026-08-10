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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Wellhub Agentic Access
  operation_count: 10
  slug: wellhub-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 4
apis:
- description: Endpoints for listing companies associated with the authenticated entity.
  name: Wellhub Companies API
  slug: wellhub-companies-api
- description: Endpoints for listing employees associated with a company or entity.
  name: Wellhub Employees API
  slug: wellhub-employees-api
- description: 'Endpoints for managing eligibility batch jobs. A job follows a lifecycle: Create → Add Items → Submit → Monitor. After submission, the job transitions through the following statuses: - `PENDING` — job'
  name: Wellhub Jobs API
  slug: wellhub-jobs-api
- description: Endpoints for obtaining access tokens using the OAuth 2.0 Client Credentials flow.
  name: Wellhub OAuth API
  slug: wellhub-oauth-api
artifact_total: 10
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wellhub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-hub.wellhub.com/docs/integrations/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer-hub.wellhub.com/docs/integrations/api/eligibility/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-hub.wellhub.com/docs/integrations/api/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/wellhub-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wellhub-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wellhub-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wellhub-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wellhub-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wellhub-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wellhub-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wellhub-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.wellhub.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wellhub-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/wellhub-sync-eligibility.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wellhub-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wellhub-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/wellhub-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellhub-domain-security.yml
- group: start
  title: ''
  type: SignUp
  url: https://clients.wellhub.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wellhub.com/en-us/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wellhub.com/en-us/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.gympass.com/us/blog
- group: operate
  title: ''
  type: Support
  url: https://www.gympass.com/us/faq
- group: company
  title: ''
  type: Website
  url: https://wellhub.com
created: '2026-07-17'
description: 'Wellhub (formerly Gympass) is a corporate wellbeing platform that gives employees access to a network of fitness, mindfulness, therapy, nutrition, and sleep partners through their employer''s benefits program. For system integrators it publishes a public Integrations API: an OAuth2 client-credentials REST API that lets a client''s HR or payroll system sync employee eligibility to Wellhub in real time, so employees gain access on hire and lose it on termination. The API models eligibility as batch jobs (create a job, add up to 500 items, submit, then poll status and read per-record errors) and is documented on a Stoplight-powered developer hub with a downloadable OpenAPI 3.0 contract and a synthetic-data Sandbox. Wellhub is backed by Atomico, HV Capital, and SoftBank Vision Fund.'
image: https://wellhub.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: wellhub-mcp.yml
  slug: wellhub-mcpyml
modified: '2026-07-21'
name: Wellhub
nav: Providers
network: true
overview: 'Wellhub publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Employees API, Jobs API, and 1 more. Tagged areas include Company, Health, Wellbeing, Corporate Benefits, and Fitness.


  Wellhub''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, signup flow, engineering blog, and 18 more developer resources.'
random_paper: 59
rate_limits:
- limit_count: 10
  name: Wellhub Rate Limits
  slug: wellhub-rate-limits
score:
  band: developing
  composite: 49.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.5
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Wellhub Authentication
  slug: wellhub-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wellhub Domain Security
  slug: wellhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wellhub Trust Center
  slug: wellhub-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: wellhub
tags:
- Company
- Health
- Wellbeing
- Corporate Benefits
- Fitness
- HR
- Eligibility
- Employee Benefits
website: https://wellhub.com
---
