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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Fountain's REST API for managing hiring and frontline workforce data — applicants, openings, positions, locations, interview slots and sessions, workers, secure documents, labels, notes, custom attrib
  name: Fountain Platform API
  slug: fountain-platform-api
artifact_total: 6
asyncapis:
- description: ''
  name: Fountain Webhooks
  slug: fountain-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fountain-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fountain-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fountain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fountain.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fountain.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fountain.com/reference/hire-api-overview
- group: operate
  title: ''
  type: Support
  url: https://support.fountain.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.fountain.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fountain.com/
- group: start
  title: ''
  type: Login
  url: https://app.fountain.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://privacy.fountain.com/policies/en/?name=terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.fountain.com/policies/en/
- group: auth
  title: ''
  type: Security
  url: https://www.fountain.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.fountain.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.fountain.com/reference/deprecations
- group: auth
  title: ''
  type: Authentication
  url: authentication/fountain-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fountain-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fountain-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fountain-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fountain-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fountain-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fountain-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fountain-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fountain-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fountain-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fountain-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fountain-well-known.yml
created: '2026-07-17'
description: Fountain is an AI-powered frontline workforce management platform used by 500+ enterprise employers across retail, logistics, hospitality, healthcare, and food service to source, hire, onboard, schedule, and retain high-volume hourly workers. Its developer platform exposes a REST API — the Hire v2 API plus newer Workforce, Attendance, Scheduling, Compliance, Referral, Pool, and Pulse microservices — for programmatically managing applicants, openings, positions, locations, interview slots, workers, documents, custom attributes, and data exports. Authentication is OAuth2 client-credentials (with a legacy X-ACCESS-TOKEN key model on tenant hosts), webhooks are HMAC-SHA-256 signed, requests are rate limited to 120/minute, and deprecations are signaled with RFC 8594 Sunset headers.
image: https://logo.clearbit.com/fountain.com
layout: provider
modified: '2026-07-19'
name: Fountain
nav: Providers
network: true
overview: 'Fountain publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Hiring, Recruiting, and Applicant Tracking.


  The Fountain catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fountain''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 22 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 1
  name: Fountain Rate Limits
  slug: fountain-rate-limits
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 55.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 63.2
  previous_composite: 42.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fountain/refs/heads/main/screenshots/fountain-2026-07-25T215050.png
security:
- kind: authentication
  name: Fountain Authentication
  slug: fountain-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Fountain Domain Security
  slug: fountain-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fountain Vulnerability Disclosure
  slug: fountain-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fountain
tags:
- Company
- Enterprise
- Hiring
- Recruiting
- Applicant Tracking
- Human Resources
- Workforce Management
- Onboarding
- Scheduling
- HR Tech
- Frontline
website: https://developer.fountain.com/
---
