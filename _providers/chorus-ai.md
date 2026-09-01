---
access_model:
  confidence: high
  label: Enterprise / Contact Sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - openapi
  - pricing-page
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Auth API from Chorus.ai — 1 operation(s) for auth.
  name: Chorus.ai Auth API
  slug: chorus-ai-auth-api
- description: The Conversations API from Chorus.ai — 11 operation(s) for conversations.
  name: Chorus.ai Conversations API
  slug: chorus-ai-conversations-api
- description: The Emails API from Chorus.ai — 3 operation(s) for emails.
  name: Chorus.ai Emails API
  slug: chorus-ai-emails-api
- description: The Engagement filter API from Chorus.ai — 3 operation(s) for engagement filter.
  name: Chorus.ai Engagement filter API
  slug: chorus-ai-engagement-filter-api
- description: The Event API from Chorus.ai — 1 operation(s) for event.
  name: Chorus.ai Event API
  slug: chorus-ai-event-api
- description: The External Moments API from Chorus.ai — 2 operation(s) for external moments.
  name: Chorus.ai External Moments API
  slug: chorus-ai-external-moments-api
- description: The Integrations Calendar API from Chorus.ai — 4 operation(s) for integrations calendar.
  name: Chorus.ai Integrations Calendar API
  slug: chorus-ai-integrations-calendar-api
- description: The Integrations CRM API from Chorus.ai — 1 operation(s) for integrations crm.
  name: Chorus.ai Integrations CRM API
  slug: chorus-ai-integrations-crm-api
- description: The Integrations Email API from Chorus.ai — 4 operation(s) for integrations email.
  name: Chorus.ai Integrations Email API
  slug: chorus-ai-integrations-email-api
- description: The Integrations Meet API from Chorus.ai — 6 operation(s) for integrations meet.
  name: Chorus.ai Integrations Meet API
  slug: chorus-ai-integrations-meet-api
- description: The Playlists API from Chorus.ai — 4 operation(s) for playlists.
  name: Chorus.ai Playlists API
  slug: chorus-ai-playlists-api
- description: The Public External Moments API from Chorus.ai — 2 operation(s) for public external moments.
  name: Chorus.ai Public External Moments API
  slug: chorus-ai-public-external-moments-api
- description: The Public Playlist Moments API from Chorus.ai — 2 operation(s) for public playlist moments.
  name: Chorus.ai Public Playlist Moments API
  slug: chorus-ai-public-playlist-moments-api
- description: The Reports API from Chorus.ai — 1 operation(s) for reports.
  name: Chorus.ai Reports API
  slug: chorus-ai-reports-api
- description: The Sales Qualifications API from Chorus.ai — 5 operation(s) for sales qualifications.
  name: Chorus.ai Sales Qualifications API
  slug: chorus-ai-sales-qualifications-api
- description: The Saved Search API from Chorus.ai — 2 operation(s) for saved search.
  name: Chorus.ai Saved Search API
  slug: chorus-ai-saved-search-api
- description: The Scorecards API from Chorus.ai — 2 operation(s) for scorecards.
  name: Chorus.ai Scorecards API
  slug: chorus-ai-scorecards-api
- description: The Session management API from Chorus.ai — 3 operation(s) for session management.
  name: Chorus.ai Session management API
  slug: chorus-ai-session-management-api
- description: The Teams API from Chorus.ai — 2 operation(s) for teams.
  name: Chorus.ai Teams API
  slug: chorus-ai-teams-api
- description: The Users API from Chorus.ai — 5 operation(s) for users.
  name: Chorus.ai Users API
  slug: chorus-ai-users-api
- description: The Video Conferences API from Chorus.ai — 2 operation(s) for video conferences.
  name: Chorus.ai Video Conferences API
  slug: chorus-ai-video-conferences-api
- description: The Webhook API from Chorus.ai — 1 operation(s) for webhook.
  name: Chorus.ai Webhook API
  slug: chorus-ai-webhook-api
artifact_total: 31
asyncapis:
- description: ''
  name: Chorus Ai Webhooks
  slug: chorus-ai-webhooks
collections:
- collection_type: open
  name: Chorus API
  slug: open-chorus-ai
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/zoominfo/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/chorus-ai-capability-edges.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chorus-ai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chorus-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chorus.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/chorus-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chorus-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chorus-ai-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/chorus-ai-openapi.yml
- group: docs
  title: ''
  type: Documentation
  url: https://chorus.ai/api-docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.chorus.ai/
- group: build
  title: ''
  type: Postman
  url: https://api-docs.chorus.ai/
- group: design
  title: ''
  type: Conventions
  url: conventions/chorus-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chorus-ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chorus-ai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/chorus-ai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/chorus-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chorus-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoominfo.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/chorus-ai-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chorus-ai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/chorus-ai-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/chorus-ai-packages.yml
- group: auth
  title: ''
  type: Security
  url: security/chorus-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chorus-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/chorus-ai-trust-center.yml
- group: operate
  title: ''
  type: Support
  url: https://www.zoominfo.com/about/help-center
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoominfo.com/products/chorus/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoominfo.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoominfo.com/legal/privacy-policy
created: '2026-05-08'
description: Chorus.ai is a conversation intelligence platform, acquired by ZoomInfo in 2021 and sold as "Chorus by ZoomInfo", that records, transcribes and analyzes customer-facing calls, meetings and emails to surface deal insights and coach sales reps. It publishes a single public REST contract — the Chorus API, an OpenAPI 3.0.3 document with 81 operations served unauthenticated at https://chorus.ai/api/openapi.json — covering engagement search, recording upload and media retrieval, coaching moments and playlists, scorecards, AI sales-qualification analysis with CRM writeback, and webhook registration. The API is JSON:API shaped on its /api/v1 surface with an older flat /v3 surface alongside it. Notably, the chorus.ai marketing site has been retired to a redirect shell pointing at zoominfo.com, but the API and both of its documentation surfaces remain live on the original domain.
finops:
- name: Chorus Ai Finops
  service_category: Sales
  slug: chorus-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chorus-ai.png
layout: provider
modified: '2026-08-13'
name: Chorus.ai
nav: Providers
network: true
overview: 'Chorus.ai publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Conversations API, Emails API, and 19 more. Tagged areas include Sales, Revenue Intelligence, Conversation, Analytics, and ZoomInfo.


  The Chorus.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Chorus.ai''s developer surface includes authentication, documentation, API reference, support, pricing, and 26 more developer resources.'
plans:
- name: Chorus Ai Plans Pricing
  plan_count: 0
  slug: chorus-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Chorus Ai Rate Limits
  slug: chorus-ai-rate-limits
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 64.8
    developer_ergonomics: 33.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 47.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chorus-ai/refs/heads/main/screenshots/chorus-ai-2026-08-17T082957.png
security:
- kind: authentication
  name: Chorus Ai Authentication
  slug: chorus-ai-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Chorus Ai Domain Security
  slug: chorus-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Chorus Ai Vulnerability Disclosure
  slug: chorus-ai-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Chorus Ai Trust Center
  slug: chorus-ai-trust-center
  summary_line: source, source_status, verified, quote, held, frameworks, explicitly_not_held
slug: chorus-ai
tags:
- Sales
- Revenue Intelligence
- Conversation
- Analytics
- ZoomInfo
- Conversation Intelligence
- Sales Enablement
- Call Recording
- Transcription
- Speech Analytics
- CRM
- Coaching
website: https://www.chorus.ai/
---
