---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The chatbot API from VCV — 2 operation(s) for chatbot.
  name: VCV chatbot API
  slug: vcv-chatbot-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The companies API from VCV — 1 operation(s) for companies.
  name: VCV companies API
  slug: vcv-companies-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The countries API from VCV — 2 operation(s) for countries.
  name: VCV countries API
  slug: vcv-countries-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The enumeration API from VCV — 3 operation(s) for enumeration.
  name: VCV enumeration API
  slug: vcv-enumeration-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The integration API from VCV — 7 operation(s) for integration.
  name: VCV integration API
  slug: vcv-integration-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The interview API from VCV — 3 operation(s) for interview.
  name: VCV interview API
  slug: vcv-interview-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The invite API from VCV — 2 operation(s) for invite.
  name: VCV invite API
  slug: vcv-invite-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The Languages API from VCV — 1 operation(s) for languages.
  name: VCV Languages API
  slug: vcv-languages-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The limits API from VCV — 1 operation(s) for limits.
  name: VCV limits API
  slug: vcv-limits-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The response API from VCV — 12 operation(s) for response.
  name: VCV response API
  slug: vcv-response-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The survey API from VCV — 4 operation(s) for survey.
  name: VCV survey API
  slug: vcv-survey-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The tags API from VCV — 4 operation(s) for tags.
  name: VCV tags API
  slug: vcv-tags-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The test API from VCV — 4 operation(s) for test.
  name: VCV test API
  slug: vcv-test-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The users API from VCV — 2 operation(s) for users.
  name: VCV users API
  slug: vcv-users-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The vacancy API from VCV — 23 operation(s) for vacancy.
  name: VCV vacancy API
  slug: vcv-vacancy-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The videointerview API from VCV — 4 operation(s) for videointerview.
  name: VCV videointerview API
  slug: vcv-videointerview-api
- baseURL: https://my.vcv.ai
  baseurl_source: declared
  description: The webhook API from VCV — 2 operation(s) for webhook.
  name: VCV webhook API
  slug: vcv-webhook-api
artifact_total: 38
asyncapis:
- description: VCV delivers outbound webhooks for recruitment events. Subscriptions are managed via the Open API v3 company-webhooks endpoints (create/list/get/ update/delete), each carrying a target url, an event t
  name: VCV Webhooks
  slug: vcv-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VCV chatbot API
  slug: open-vcv-chatbot-api
- collection_type: open
  name: VCV chatbot companies API
  slug: open-vcv-companies-api
- collection_type: open
  name: VCV chatbot countries API
  slug: open-vcv-countries-api
- collection_type: open
  name: VCV chatbot enumeration API
  slug: open-vcv-enumeration-api
- collection_type: open
  name: VCV chatbot integration API
  slug: open-vcv-integration-api
- collection_type: open
  name: VCV chatbot interview API
  slug: open-vcv-interview-api
- collection_type: open
  name: VCV chatbot invite API
  slug: open-vcv-invite-api
- collection_type: open
  name: VCV chatbot Languages API
  slug: open-vcv-languages-api
- collection_type: open
  name: VCV chatbot limits API
  slug: open-vcv-limits-api
- collection_type: open
  name: VCV chatbot response API
  slug: open-vcv-response-api
- collection_type: open
  name: VCV chatbot survey API
  slug: open-vcv-survey-api
- collection_type: open
  name: VCV chatbot tags API
  slug: open-vcv-tags-api
- collection_type: open
  name: VCV chatbot test API
  slug: open-vcv-test-api
- collection_type: open
  name: VCV chatbot users API
  slug: open-vcv-users-api
- collection_type: open
  name: VCV chatbot vacancy API
  slug: open-vcv-vacancy-api
- collection_type: open
  name: VCV chatbot videointerview API
  slug: open-vcv-videointerview-api
- collection_type: open
  name: VCV chatbot webhook API
  slug: open-vcv-webhook-api
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: VCV
nav: Providers
network: true
overview: 'VCV publishes 17 APIs on the [APIs.io](https://apis.io/) network, including chatbot API, companies API, countries API, and 14 more. Tagged areas include Company, Recruiting, Human Resources, Video Interviews, and Talent Acquisition.


  The VCV catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VCV''s developer surface includes documentation, API reference, pricing, engineering blog, signup flow, support, authentication, and 19 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 55.4
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 38.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vcv/refs/heads/main/screenshots/vcv-2026-09-02T165534.png
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
