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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Goto Webinar Agentic Access
  operation_count: 53
  slug: goto-webinar-agentic-access
  summary_line: 53 operations · 22 acting
api_count: 1
apis:
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Session-level attendee reporting for GoTo Webinar — 5 operations covering the attendees of a session, a single attendee, and that attendee's poll answers, Q&A questions and survey responses.
  name: GoTo Webinar Attendees API
  slug: goto-webinar-attendees-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Panelist management for a GoTo Webinar webinar — 4 operations to list, invite, remove and resend the invitation for the presenters on a webinar.
  name: GoTo Webinar Panelists API
  slug: goto-webinar-panelists-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Registration management for GoTo Webinar — 5 operations to create, list, read and delete registrants, plus read the registration form fields and custom questions configured on a webinar.
  name: GoTo Webinar Registrants API
  slug: goto-webinar-registrants-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Session reporting for GoTo Webinar — 7 operations covering an organizer's sessions in a date range, the sessions of a webinar, one session, its attendance performance, and its polls, Q&A questions and
  name: GoTo Webinar Sessions API
  slug: goto-webinar-sessions-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: 'The core GoTo Webinar surface — 15 operations to schedule, read, update, cancel and copy webinars, list in-session and account-wide webinars, read meeting times, start URLs, audio settings, recording '
  name: GoTo Webinar Webinars API
  slug: goto-webinar-webinars-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Co-organizer management for a GoTo Webinar webinar — 4 operations to list, add, remove and resend invitations for co-hosts, internal by organizerKey or external by email.
  name: GoTo Webinar Co Organizers API
  slug: goto-webinar-co-organizers-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Recording asset search for GoTo Webinar — 2 operations to search stored recordings for the authenticated organizer or, with an admin token, across an entire account. Assets can be reused as the source
  name: GoTo Webinar Recording Assets API
  slug: goto-webinar-recordingassets-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Webhook management for GoTo Webinar — 11 operations to create the delivery secret key, register and activate webhook callbacks, and create, read, update and delete the per-user subscriptions that make
  name: GoTo Webinar Webhooks API
  slug: goto-webinar-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Goto Webinar Webhooks
  slug: goto-webinar-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GoTo Webinar REST API v2 Attendees API
  slug: open-goto-webinar-attendees-api
- collection_type: open
  name: GoTo Webinar REST API v2 Attendees Panelists API
  slug: open-goto-webinar-panelists-api
- collection_type: open
  name: GoTo Webinar REST API v2 Attendees Registrants API
  slug: open-goto-webinar-registrants-api
- collection_type: open
  name: GoTo Webinar REST API v2 Attendees Sessions API
  slug: open-goto-webinar-sessions-api
- collection_type: open
  name: GoTo Webinar REST API v2 Attendees Webinars API
  slug: open-goto-webinar-webinars-api
- collection_type: open
  name: GoTo Webinar REST API v2
  slug: open-goto-webinar
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/goto-webinar-openapi.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goto-webinar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goto-webinar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goto-webinar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/goto-webinar-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/goto-webinar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/goto-webinar-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/goto-webinar-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/goto-webinar-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goto-webinar-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/goto-webinar-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/goto-webinar-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.goto.com/company/trust/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/goto-webinar-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/goto-webinar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.goto.com/company/trust/security-measures
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/goto-webinar-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goto-webinar-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goto-webinar-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/goto-webinar-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goto-webinar-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/goto-webinar-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/goto-webinar-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/goto-webinar-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: collections/goto-webinar-v2-provider.postman_collection.json
- group: company
  title: ''
  type: Website
  url: https://www.goto.com/webinar
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.goto.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.goto.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.goto.com/GoToWebinarV2
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.goto.com/guides/Get%20Started/00_Ref-Get-Started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoTo-Developers
- group: company
  title: ''
  type: Blog
  url: https://www.goto.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goto.com/pricing/webinar
- group: start
  title: ''
  type: SignUp
  url: https://developer.goto.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goto.com/company/legal/api-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goto.com/company/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goto.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.goto.com/support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goto
created: '2026-05-11'
description: GoTo Webinar is a webinar and virtual event platform from GoTo (formerly LogMeIn) used by marketing, training, and corporate communications teams to host live and on-demand webinars with registration, polling, Q&A, recordings, and analytics. The product integrates with marketing automation and CRM systems to drive lead capture and attendee follow-up. The GoTo Webinar v2 REST API exposes organizer, webinar, session, registrant, attendee, and analytics endpoints under api.getgo.com and uses OAuth2 for authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goto-webinar.png
layout: provider
modified: '2026-08-13'
name: GoTo Webinar
nav: Providers
network: true
overview: 'GoTo Webinar publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Panelists API, Registrants API, and 5 more. Tagged areas include Webinars, Virtual Events, Video Conferencing, Marketing, and Lead Capture.


  The GoTo Webinar catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoTo Webinar''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Goto Webinar Plans Pricing
  plan_count: 3
  slug: goto-webinar-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Goto Webinar Rate Limits
  slug: goto-webinar-rate-limits
scopes:
- name: Goto Webinar Scopes
  scope_count: 1
  slug: goto-webinar-scopes
  summary_line: 1 scope · authorizationCode/password
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 59.9
    developer_ergonomics: 67.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goto-webinar/refs/heads/main/screenshots/goto-webinar-2026-06-20T182256.png
security:
- kind: authentication
  name: Goto Webinar Authentication
  slug: goto-webinar-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Goto Webinar Domain Security
  slug: goto-webinar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Goto Webinar Vulnerability Disclosure
  slug: goto-webinar-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Goto Webinar Trust Center
  slug: goto-webinar-trust-center
  summary_line: SOC 2 (Type II), SOC 3, C5 (BSI Cloud Computing Compliance Criteria Catalogue)
slug: goto-webinar
tags:
- Webinars
- Virtual Events
- Video Conferencing
- Marketing
- Lead Capture
- Registration
- Webhook
- Event Management
- Collaboration
- Analytics
website: https://www.goto.com/webinar
---
