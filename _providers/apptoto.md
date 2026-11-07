---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Apptoto Agentic Access
  operation_count: 43
  slug: apptoto-agentic-access
  summary_line: 43 operations · 24 acting
api_count: 1
apis:
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Address Books API from Apptoto — 1 operation(s) for address books.
  name: Apptoto Address Books API
  slug: apptoto-address-books-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Availability API from Apptoto — 1 operation(s) for availability.
  name: Apptoto Availability API
  slug: apptoto-availability-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Book Now API from Apptoto — 1 operation(s) for book now.
  name: Apptoto Book Now API
  slug: apptoto-book-now-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Booking Pages API from Apptoto — 1 operation(s) for booking pages.
  name: Apptoto Booking Pages API
  slug: apptoto-booking-pages-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Bookings API from Apptoto — 1 operation(s) for bookings.
  name: Apptoto Bookings API
  slug: apptoto-bookings-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Calendars API from Apptoto — 1 operation(s) for calendars.
  name: Apptoto Calendars API
  slug: apptoto-calendars-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Contact API from Apptoto — 1 operation(s) for contact.
  name: Apptoto Contact API
  slug: apptoto-contact-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Contacts API from Apptoto — 2 operation(s) for contacts.
  name: Apptoto Contacts API
  slug: apptoto-contacts-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Conversation Messages API from Apptoto — 1 operation(s) for conversation messages.
  name: Apptoto Conversation Messages API
  slug: apptoto-conversation-messages-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Conversation Reply API from Apptoto — 1 operation(s) for conversation reply.
  name: Apptoto Conversation Reply API
  slug: apptoto-conversation-reply-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Conversation Templates API from Apptoto — 1 operation(s) for conversation templates.
  name: Apptoto Conversation Templates API
  slug: apptoto-conversation-templates-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Conversations API from Apptoto — 1 operation(s) for conversations.
  name: Apptoto Conversations API
  slug: apptoto-conversations-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Event API from Apptoto — 3 operation(s) for event.
  name: Apptoto Event API
  slug: apptoto-event-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Events API from Apptoto — 1 operation(s) for events.
  name: Apptoto Events API
  slug: apptoto-events-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Import API from Apptoto — 1 operation(s) for import.
  name: Apptoto Import API
  slug: apptoto-import-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Lists API from Apptoto — 1 operation(s) for lists.
  name: Apptoto Lists API
  slug: apptoto-lists-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Participant API from Apptoto — 2 operation(s) for participant.
  name: Apptoto Participant API
  slug: apptoto-participant-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Participants API from Apptoto — 2 operation(s) for participants.
  name: Apptoto Participants API
  slug: apptoto-participants-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Start Conversation API from Apptoto — 1 operation(s) for start conversation.
  name: Apptoto Start Conversation API
  slug: apptoto-start-conversation-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The Webhooks API from Apptoto — 1 operation(s) for webhooks.
  name: Apptoto Webhooks API
  slug: apptoto-webhooks-api
- baseURL: https://api.apptoto.com
  baseurl_source: declared
  description: The User Info API from Apptoto — 1 operation(s) for user info.
  name: Apptoto User Info API
  slug: apptoto-user-info-api
artifact_total: 30
asyncapis:
- description: ''
  name: Apptoto Webhooks
  slug: apptoto-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/apptoto/agentic-access/apptoto-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apptoto-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/apptoto/rate-limits/apptoto-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apptoto-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/apptoto/plans/apptoto-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apptoto-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/apptoto/rules/apptoto-rules.yml
  title: ''
  type: Spectral
  url: rules/apptoto-rules.yml
- group: agent
  href: https://artifacts.apis.io/apptoto/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apptoto/asyncapi/apptoto-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/apptoto-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/apptoto/authentication/apptoto-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apptoto-authentication.yml
- group: design
  href: https://artifacts.apis.io/apptoto/errors/apptoto-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apptoto-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apptoto/conformance/apptoto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apptoto-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apptoto/llms/apptoto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apptoto-llms.txt
- group: agent
  href: https://artifacts.apis.io/apptoto/well-known/apptoto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apptoto-well-known.yml
- group: other
  href: https://artifacts.apis.io/apptoto/hosts/apptoto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apptoto-hosts.yml
- group: other
  href: https://artifacts.apis.io/apptoto/vendors/apptoto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apptoto-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.apptoto.com/apptoto-manual/article/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apptoto.com/tos
- group: operate
  title: ''
  type: Support
  url: https://www.apptoto.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apptoto.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apptoto.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.apptoto.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apptoto.com/apptoto-manual/article/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://www.apptoto.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.apptoto.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/apptoto/scopes/apptoto-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/apptoto-scopes.yml
- group: auth
  href: https://artifacts.apis.io/apptoto/security/apptoto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apptoto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apptoto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.apptoto.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apptoto.com/pricing
- group: company
  title: ''
  type: About
  url: https://www.apptoto.com/about
coverage:
  checked: '2026-10-28'
  detail: Documentation is served as HTML pages requiring JavaScript to render markdown, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://apidocs.apptoto.com/reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Apptoto provides automated appointment reminders via SMS, email, and voice messages to reduce no‑shows, streamline scheduling, and improve client satisfaction. Founded in 2010, the platform offers a 14‑day free trial and integrates with calendars, payment systems, and popular apps. It serves businesses of all sizes to grow revenue through reliable communications.
layout: provider
modified: '2026-10-28'
name: Apptoto
nav: Providers
network: true
overview: 'Apptoto publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Address Books API, Availability API, Book Now API, and 18 more. Tagged areas include Company, Scheduling, Appointment-Reminders, SMS, and Email.


  The Apptoto catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Apptoto''s developer surface includes authentication, support, getting-started guide, engineering blog, API reference, documentation, pricing, and 21 more developer resources.'
plans:
- name: Apptoto Plans Pricing
  plan_count: 1
  slug: apptoto-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Apptoto Rate Limits
  slug: apptoto-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Apptoto API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 2
  slug: apptoto-rules
scopes:
- name: Apptoto Scopes
  scope_count: 16
  slug: apptoto-scopes
  summary_line: 16 scopes · authorizationCode
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 50.5
    catalog_earned_first_party: 16.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 59.2
    developer_ergonomics: 31.5
    discoverability: 60.7
    operational_transparency: 32.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/apptoto/apptoto-2026-11-03T121039.png
security:
- kind: authentication
  name: Apptoto Authentication
  slug: apptoto-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Apptoto Domain Security
  slug: apptoto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: apptoto-create-and-tag-contact
  slug: apptoto-create-and-tag-contact
slug: apptoto
tags:
- Company
- Scheduling
- Appointment-Reminders
- SMS
- Email
- Voice
website: https://apptoto.com/
---
