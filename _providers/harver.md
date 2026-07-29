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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Harver Agentic Access
  operation_count: 54
  slug: harver-agentic-access
  summary_line: 54 operations · 26 acting
api_count: 9
apis:
- description: The accounts API from Harver — 16 operation(s) for accounts.
  name: Harver accounts API
  slug: harver-accounts-api
- description: The applications API from Harver — 12 operation(s) for applications.
  name: Harver applications API
  slug: harver-applications-api
- description: The candidate-statuses API from Harver — 1 operation(s) for candidate-statuses.
  name: Harver candidate-statuses API
  slug: harver-candidate-statuses-api
- description: The candidateApplications API from Harver — 1 operation(s) for candidateapplications.
  name: Harver candidateApplications API
  slug: harver-candidateapplications-api
- description: The oauth API from Harver — 3 operation(s) for oauth.
  name: Harver oauth API
  slug: harver-oauth-api
- description: The scheduling API from Harver — 2 operation(s) for scheduling.
  name: Harver scheduling API
  slug: harver-scheduling-api
- description: The user-profile API from Harver — 3 operation(s) for user-profile.
  name: Harver user-profile API
  slug: harver-user-profile-api
- description: The vacancies API from Harver — 6 operation(s) for vacancies.
  name: Harver vacancies API
  slug: harver-vacancies-api
- description: The webhook API from Harver — 1 operation(s) for webhook.
  name: Harver webhook API
  slug: harver-webhook-api
artifact_total: 15
asyncapis:
- description: ''
  name: Harver Webhooks
  slug: harver-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://harver.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.harver.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.harver.com/docs
- group: company
  title: ''
  type: Blog
  url: https://harver.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://knowledge.harver.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harver.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harver-engineering
- group: auth
  title: ''
  type: Authentication
  url: authentication/harver-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/harver-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/harver-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harver-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/harver-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://harver.com/security/
- group: design
  title: ''
  type: DataModel
  url: data-model/harver-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/harver-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/harver-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/harver-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harver-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/harver-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/harver-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/harver-security.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harver-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: https://harver.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/harver-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harver-domain-security.yml
created: '2026-07-17'
description: Harver is a Talent Intelligence platform for pre-employment assessment, automated interview scheduling and reference checking that helps organizations make data-driven, less-biased hiring decisions at scale. Harver's Public API (OpenAPI 3.0, v1.37.0) is available to Harver customers and lets ATS and HR systems submit candidates, create applications and magic-links, retrieve matching scores, module results and report links, manage vacancies, locations, regions and job functions, and subscribe to candidate-lifecycle webhooks. Authentication is OAuth2 client_credentials; resources use a JSON:API-style envelope, responses are rate-limited (Ratelimit-Limit/Reset, 429) and carry an X-Correlation-Id. Harver was surfaced as an Insight Partners portfolio company.
image: https://harver.com/wp-content/uploads/2026/01/harver-lp-brand-V2-1.jpg
layout: provider
mcp_servers:
- description: ''
  name: harver-mcp.yml
  slug: harver-mcpyml
modified: '2026-07-19'
name: Harver
nav: Providers
network: true
overview: 'Harver publishes 9 APIs on the [APIs.io](https://apis.io/) network, including accounts API, applications API, candidate-statuses API, and 6 more. Tagged areas include Company, HR, HR Tech, Recruiting, and Hiring.


  The Harver catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Harver''s developer surface includes documentation, API reference, engineering blog, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 41.6
  delta: -0.3
  facets:
    commercial_clarity: 18.4
    contract_quality: 58.2
    developer_ergonomics: 42.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 41.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harver/refs/heads/main/screenshots/harver-2026-07-25T220747.png
security:
- kind: authentication
  name: Harver Authentication
  slug: harver-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Harver Domain Security
  slug: harver-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Harver Vulnerability Disclosure
  slug: harver-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: harver
tags:
- Company
- HR
- HR Tech
- Recruiting
- Hiring
- Talent Intelligence
- Pre-Employment Assessment
- Candidate Experience
- Applicant Tracking
website: https://harver.com/
---
