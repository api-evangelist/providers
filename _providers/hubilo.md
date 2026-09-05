---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - '{''url'': ''https://hubilo.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.virtualpro.com/ — a different registrable domain (hubilo.com -> virtualpro.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Hubilo Agentic Access
  operation_count: 30
  slug: hubilo-agentic-access
  summary_line: 30 operations · 15 acting
api_count: 1
apis:
- baseURL: https://api.hubilo.com
  baseurl_source: declared
  description: The Event API from hubilo — 3 operation(s) for event.
  name: hubilo Event API
  slug: hubilo-event-api
- baseURL: https://api.hubilo.com
  baseurl_source: declared
  description: The Exhibitor API from hubilo — 7 operation(s) for exhibitor.
  name: hubilo Exhibitor API
  slug: hubilo-exhibitor-api
- baseURL: https://api.hubilo.com
  baseurl_source: declared
  description: The Organiser API from hubilo — 1 operation(s) for organiser.
  name: hubilo Organiser API
  slug: hubilo-organiser-api
- baseURL: https://api.hubilo.com
  baseurl_source: declared
  description: The Session API from hubilo — 6 operation(s) for session.
  name: hubilo Session API
  slug: hubilo-session-api
- baseURL: https://api.hubilo.com
  baseurl_source: declared
  description: The Speaker API from hubilo — 2 operation(s) for speaker.
  name: hubilo Speaker API
  slug: hubilo-speaker-api
- baseURL: https://api.hubilo.com
  baseurl_source: declared
  description: The Upload Media API from hubilo — 2 operation(s) for upload media.
  name: hubilo Upload Media API
  slug: hubilo-upload-media-api
- baseURL: https://api.hubilo.com
  baseurl_source: declared
  description: The User API from hubilo — 9 operation(s) for user.
  name: hubilo User API
  slug: hubilo-user-api
artifact_total: 20
asyncapis:
- description: ''
  name: Hubilo Webhooks
  slug: hubilo-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hubilo (Virtual PRO) Public Event API
  slug: open-hubilo-event-api
- collection_type: open
  name: Hubilo (Virtual PRO) Public Event Exhibitor API
  slug: open-hubilo-exhibitor-api
- collection_type: open
  name: Hubilo (Virtual PRO) Public Event Organiser API
  slug: open-hubilo-organiser-api
- collection_type: open
  name: Hubilo (Virtual PRO) Public Event Session API
  slug: open-hubilo-session-api
- collection_type: open
  name: Hubilo (Virtual PRO) Public Event Speaker API
  slug: open-hubilo-speaker-api
- collection_type: open
  name: Hubilo (Virtual PRO) Public Event Upload Media API
  slug: open-hubilo-upload-media-api
- collection_type: open
  name: Hubilo (Virtual PRO) Public Event User API
  slug: open-hubilo-user-api
common:
- group: company
  title: ''
  type: Website
  url: https://hubilo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hubilo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hubilo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hubilo.com/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/7951787/S1a4YSxN
- group: commercial
  title: ''
  type: Pricing
  url: https://www.virtualpro.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://admin.virtualpro.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.virtualpro.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brandlive.com/legal
- group: operate
  title: ''
  type: Support
  url: https://support.brandlive.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/hubilo-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hubilo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hubilo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hubilo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hubilo-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hubilo-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hubilo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hubilo-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hubilo-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hubilo-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hubilo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hubilo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/hubilo-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hubilo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hubilo-domain-security.yml
created: '2026-07-17'
description: 'Hubilo (now branded Virtual PRO) is an enterprise virtual, hybrid, and in-person event platform used by conference producers and corporate event teams to create, promote, run, and analyze multi-session, multi-day events. Its Public API v1.2 lets organisers manage events, agenda sessions and tracks, speakers, attendees (users) and member groups, exhibitor booths, the organiser profile, and media uploads, plus a webhooks surface for activity notifications. Authentication is an organiser-level Access Token (Authorization: Bearer) and the API enforces a combined limit of 20 requests per second per organiser. Hubilo is a portfolio company of Balderton Capital.'
image: https://framerusercontent.com/images/WwfBR1oRs750Jqr5sx6xqvIOc.png
layout: provider
modified: '2026-07-19'
name: hubilo
nav: Providers
network: true
overview: 'hubilo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Event API, Exhibitor API, Organiser API, and 4 more. Tagged areas include Company, Event, Virtual Events, Webinars, and Event Management.


  The hubilo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  hubilo''s developer surface includes documentation, API reference, pricing, signup flow, support, authentication, changelog, and 19 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 1
  name: Hubilo Rate Limits
  slug: hubilo-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 21.5
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hubilo/refs/heads/main/screenshots/hubilo-2026-07-25T221615.png
security:
- kind: authentication
  name: Hubilo Authentication
  slug: hubilo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hubilo Domain Security
  slug: hubilo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hubilo
tags:
- Company
- Event
- Virtual Events
- Webinars
- Event Management
- Hybrid Events
- Attendee Engagement
website: https://hubilo.com/
---
