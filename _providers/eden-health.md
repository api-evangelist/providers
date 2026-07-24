---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 31.7
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 79
  human_in_the_loop: 0
  name: Eden Health Agentic Access
  operation_count: 173
  slug: eden-health-agentic-access
  summary_line: 173 operations · 79 acting
api_count: 43
apis:
- description: Configures routes, handlers, and global middleware.
  name: Eden Health grdn.handler API
  slug: eden-health-grdn-handler-api
- description: The grdn.routes.impl.addons API from Eden Health — 3 operation(s) for grdn.routes.impl.addons.
  name: Eden Health grdn.routes.impl.addons API
  slug: eden-health-grdn-routes-impl-addons-api
- description: Generic application handlers.
  name: Eden Health grdn.routes.impl.app API
  slug: eden-health-grdn-routes-impl-app-api
- description: 'Contains handlers for routes related to Appointments, Cases, Encounters etc. On timezones: Appointments are tied to Athena departments, and their date and start time are to be interpreted as represent'
  name: Eden Health grdn.routes.impl.appointments API
  slug: eden-health-grdn-routes-impl-appointments-api
- description: Contains handlers for routes related to provider patient assignments.
  name: Eden Health grdn.routes.impl.assignment API
  slug: eden-health-grdn-routes-impl-assignment-api
- description: The grdn.routes.impl.athena-providers API from Eden Health — 1 operation(s) for grdn.routes.impl.athena-providers.
  name: Eden Health grdn.routes.impl.athena-providers API
  slug: eden-health-grdn-routes-impl-athena-providers-api
- description: Direct authentication handlers
  name: Eden Health grdn.routes.impl.auth API
  slug: eden-health-grdn-routes-impl-auth-api
- description: The grdn.routes.impl.bookable-entities API from Eden Health — 1 operation(s) for grdn.routes.impl.bookable-entities.
  name: Eden Health grdn.routes.impl.bookable-entities API
  slug: eden-health-grdn-routes-impl-bookable-entities-api
- description: The grdn.routes.impl.brad API from Eden Health — 3 operation(s) for grdn.routes.impl.brad.
  name: Eden Health grdn.routes.impl.brad API
  slug: eden-health-grdn-routes-impl-brad-api
- description: Bug Report handler
  name: Eden Health grdn.routes.impl.bug API
  slug: eden-health-grdn-routes-impl-bug-api
- description: The grdn.routes.impl.care-pods API from Eden Health — 1 operation(s) for grdn.routes.impl.care-pods.
  name: Eden Health grdn.routes.impl.care-pods API
  slug: eden-health-grdn-routes-impl-care-pods-api
- description: The grdn.routes.impl.careteam API from Eden Health — 2 operation(s) for grdn.routes.impl.careteam.
  name: Eden Health grdn.routes.impl.careteam API
  slug: eden-health-grdn-routes-impl-careteam-api
- description: Contains handlers for routes related to Channels.
  name: Eden Health grdn.routes.impl.channel API
  slug: eden-health-grdn-routes-impl-channel-api
- description: The grdn.routes.impl.chat API from Eden Health — 1 operation(s) for grdn.routes.impl.chat.
  name: Eden Health grdn.routes.impl.chat API
  slug: eden-health-grdn-routes-impl-chat-api
- description: The grdn.routes.impl.configuration API from Eden Health — 1 operation(s) for grdn.routes.impl.configuration.
  name: Eden Health grdn.routes.impl.configuration API
  slug: eden-health-grdn-routes-impl-configuration-api
- description: The grdn.routes.impl.consent API from Eden Health — 2 operation(s) for grdn.routes.impl.consent.
  name: Eden Health grdn.routes.impl.consent API
  slug: eden-health-grdn-routes-impl-consent-api
- description: The grdn.routes.impl.demographics API from Eden Health — 1 operation(s) for grdn.routes.impl.demographics.
  name: Eden Health grdn.routes.impl.demographics API
  slug: eden-health-grdn-routes-impl-demographics-api
- description: The grdn.routes.impl.document API from Eden Health — 12 operation(s) for grdn.routes.impl.document.
  name: Eden Health grdn.routes.impl.document API
  slug: eden-health-grdn-routes-impl-document-api
- description: Route implementation for all things eligibility
  name: Eden Health grdn.routes.impl.eligibility API
  slug: eden-health-grdn-routes-impl-eligibility-api
- description: Route implementation for our various event posting endpoints.
  name: Eden Health grdn.routes.impl.event API
  slug: eden-health-grdn-routes-impl-event-api
- description: Contains handlers for routes related to Appointments, Cases, Encounters etc.
  name: Eden Health grdn.routes.impl.feedback API
  slug: eden-health-grdn-routes-impl-feedback-api
- description: Handlers for image upload and download.
  name: Eden Health grdn.routes.impl.images API
  slug: eden-health-grdn-routes-impl-images-api
- description: The grdn.routes.impl.insurance API from Eden Health — 3 operation(s) for grdn.routes.impl.insurance.
  name: Eden Health grdn.routes.impl.insurance API
  slug: eden-health-grdn-routes-impl-insurance-api
- description: Simple CRUD operations for macros.
  name: Eden Health grdn.routes.impl.macros API
  slug: eden-health-grdn-routes-impl-macros-api
- description: Handlers for sponsor roster members
  name: Eden Health grdn.routes.impl.member API
  slug: eden-health-grdn-routes-impl-member-api
- description: Handlers for membership, invites, codes
  name: Eden Health grdn.routes.impl.membership API
  slug: eden-health-grdn-routes-impl-membership-api
- description: Contains handlers for routes related to Patients.
  name: Eden Health grdn.routes.impl.next-step API
  slug: eden-health-grdn-routes-impl-next-step-api
- description: Contains handlers for routes related to Patients.
  name: Eden Health grdn.routes.impl.patients API
  slug: eden-health-grdn-routes-impl-patients-api
- description: The grdn.routes.impl.pediatric API from Eden Health — 7 operation(s) for grdn.routes.impl.pediatric.
  name: Eden Health grdn.routes.impl.pediatric API
  slug: eden-health-grdn-routes-impl-pediatric-api
- description: Simple CRUD operations for popups.
  name: Eden Health grdn.routes.impl.popup API
  slug: eden-health-grdn-routes-impl-popup-api
- description: Handlers to get general info about providers and departments.
  name: Eden Health grdn.routes.impl.provider API
  slug: eden-health-grdn-routes-impl-provider-api
- description: The grdn.routes.impl.provider-groups API from Eden Health — 1 operation(s) for grdn.routes.impl.provider-groups.
  name: Eden Health grdn.routes.impl.provider-groups API
  slug: eden-health-grdn-routes-impl-provider-groups-api
- description: Handlers for screener fetching and submission.
  name: Eden Health grdn.routes.impl.screener-response API
  slug: eden-health-grdn-routes-impl-screener-response-api
- description: Handlers for screener fetching and submission.
  name: Eden Health grdn.routes.impl.screeners API
  slug: eden-health-grdn-routes-impl-screeners-api
- description: Handlers for sendbird webhooks.
  name: Eden Health grdn.routes.impl.sendbird API
  slug: eden-health-grdn-routes-impl-sendbird-api
- description: Handlers for sponsor data.
  name: Eden Health grdn.routes.impl.sponsor API
  slug: eden-health-grdn-routes-impl-sponsor-api
- description: Handlers for sponsor_user endpoints
  name: Eden Health grdn.routes.impl.sponsor-user API
  slug: eden-health-grdn-routes-impl-sponsor-user-api
- description: The grdn.routes.impl.ticklers API from Eden Health — 5 operation(s) for grdn.routes.impl.ticklers.
  name: Eden Health grdn.routes.impl.ticklers API
  slug: eden-health-grdn-routes-impl-ticklers-api
- description: The grdn.routes.impl.tools API from Eden Health — 1 operation(s) for grdn.routes.impl.tools.
  name: Eden Health grdn.routes.impl.tools API
  slug: eden-health-grdn-routes-impl-tools-api
- description: The grdn.routes.impl.validation API from Eden Health — 1 operation(s) for grdn.routes.impl.validation.
  name: Eden Health grdn.routes.impl.validation API
  slug: eden-health-grdn-routes-impl-validation-api
- description: Scheduling calls and querying call metadata
  name: Eden Health grdn.routes.impl.video API
  slug: eden-health-grdn-routes-impl-video-api
- description: Handlers for getting and creating Video Visits.
  name: Eden Health grdn.routes.impl.video-visit API
  slug: eden-health-grdn-routes-impl-video-visit-api
- description: Handlers for sponsor visitors
  name: Eden Health grdn.routes.impl.visitor API
  slug: eden-health-grdn-routes-impl-visitor-api
artifact_total: 45
common:
- group: company
  title: ''
  type: Website
  url: https://edenhealth.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eden-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eden-health-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eden-health-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eden-health-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eden-health-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eden-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eden-health-llms.txt
created: '2026-07-17'
description: Eden Health was a primary and virtual care company that delivered app-based medical care, behavioral health, and care navigation to employers and their employees, integrating with health systems and insurers (backed by Insight Partners). It was surfaced as an Insight Partners portfolio company and added to the API Evangelist network for enrichment. Its public marketing site is no longer reachable over TLS, but its primary backend service — the "Grdn" (Guardian) API at api.edenhealth.com — still serves a Swagger 2.0 description covering patients, appointments, membership, documents, care teams, and clinician tooling.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eden-health.png
layout: provider
modified: '2026-07-19'
name: Eden Health
nav: Providers
network: true
overview: Eden Health publishes 43 APIs on the [APIs.io](https://apis.io/) network, including grdn.handler API, grdn.routes.impl.addons API, grdn.routes.impl.app API, and 40 more. Tagged areas include Company, Healthcare, Primary Care, Virtual Care, and Telehealth.
random_paper: 16
score:
  band: emerging
  composite: 20.1
  delta: 0.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 37.7
    developer_ergonomics: 0.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.4
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Eden Health Domain Security
  slug: eden-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eden-health
tags:
- Company
- Healthcare
- Primary Care
- Virtual Care
- Telehealth
- Digital Health
- Patient
- Appointments
website: https://edenhealth.com/
---
