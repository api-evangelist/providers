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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-12'
api_count: 17
apis:
- description: The chatbot API from VCV — 2 operation(s) for chatbot.
  name: VCV chatbot API
  slug: vcv-chatbot-api
- description: The companies API from VCV — 1 operation(s) for companies.
  name: VCV companies API
  slug: vcv-companies-api
- description: The countries API from VCV — 2 operation(s) for countries.
  name: VCV countries API
  slug: vcv-countries-api
- description: The enumeration API from VCV — 3 operation(s) for enumeration.
  name: VCV enumeration API
  slug: vcv-enumeration-api
- description: The integration API from VCV — 7 operation(s) for integration.
  name: VCV integration API
  slug: vcv-integration-api
- description: The interview API from VCV — 3 operation(s) for interview.
  name: VCV interview API
  slug: vcv-interview-api
- description: The invite API from VCV — 2 operation(s) for invite.
  name: VCV invite API
  slug: vcv-invite-api
- description: The Languages API from VCV — 1 operation(s) for languages.
  name: VCV Languages API
  slug: vcv-languages-api
- description: The limits API from VCV — 1 operation(s) for limits.
  name: VCV limits API
  slug: vcv-limits-api
- description: The response API from VCV — 12 operation(s) for response.
  name: VCV response API
  slug: vcv-response-api
- description: The survey API from VCV — 4 operation(s) for survey.
  name: VCV survey API
  slug: vcv-survey-api
- description: The tags API from VCV — 4 operation(s) for tags.
  name: VCV tags API
  slug: vcv-tags-api
- description: The test API from VCV — 4 operation(s) for test.
  name: VCV test API
  slug: vcv-test-api
- description: The users API from VCV — 2 operation(s) for users.
  name: VCV users API
  slug: vcv-users-api
- description: The vacancy API from VCV — 23 operation(s) for vacancy.
  name: VCV vacancy API
  slug: vcv-vacancy-api
- description: The videointerview API from VCV — 4 operation(s) for videointerview.
  name: VCV videointerview API
  slug: vcv-videointerview-api
- description: The webhook API from VCV — 2 operation(s) for webhook.
  name: VCV webhook API
  slug: vcv-webhook-api
artifact_total: 21
asyncapis:
- description: VCV delivers outbound webhooks for recruitment events. Subscriptions are managed via the Open API v3 company-webhooks endpoints (create/list/get/ update/delete), each carrying a target url, an event t
  name: VCV Webhooks
  slug: vcv-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://vcv.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vcv.ru/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.vcv.ru/
- group: commercial
  title: ''
  type: Pricing
  url: https://vcv.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://vcv.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://my.vcv.ai/registration/en
- group: start
  title: ''
  type: Login
  url: https://my.vcv.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vcv.ai/pages/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vcv.ai/pages/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://vcv.ai/contact
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/vcvpages
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vcv-ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/vcv-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vcv-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vcv-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vcv-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vcv-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vcv-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vcv-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/vcv-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vcv-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vcv-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vcv-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vcv-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/vcv-packages.yml
created: '2026-07-17'
description: VCV is a recruitment-automation platform offering video interviews, candidate screening, assessments, and chatbot pre-screening for high-volume, graduate, and professional hiring, used by enterprises like PwC, PepsiCo, and Danone. Its VCV Open API v3 is a bearer-token REST API covering vacancies, candidate responses, video interviews, tests, surveys, invites, tags, users, and company webhooks, documented via Swagger UI at developer.vcv.ru.
image: https://static.tildacdn.net/tild3164-3465-4133-a335-363938393334/vcv_badge.png
layout: provider
mcp_servers:
- description: ''
  name: vcv-mcp.yml
  slug: vcv-mcpyml
modified: '2026-07-21'
name: VCV
nav: Providers
network: true
overview: 'VCV publishes 17 APIs on the [APIs.io](https://apis.io/) network, including chatbot API, companies API, countries API, and 14 more. Tagged areas include Company, Recruiting, Human Resources, Video Interviews, and Talent Acquisition.


  The VCV catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VCV''s developer surface includes documentation, API reference, pricing, engineering blog, signup flow, support, authentication, and 19 more developer resources.'
random_paper: 95
score:
  band: thin
  composite: 41.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 56.8
    developer_ergonomics: 36.4
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 41.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Vcv Authentication
  slug: vcv-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vcv Domain Security
  slug: vcv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vcv
tags:
- Company
- Recruiting
- Human Resources
- Video Interviews
- Talent Acquisition
- Hiring
- Assessments
website: https://vcv.ai
---
