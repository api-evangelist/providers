---
access_model:
  confidence: high
  label: Free developer tier · Enterprise contract for production
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://dashboard.validic.com/register
  - https://dashboard.validic.com/validic-developer-signup.txt
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Validic Agentic Access
  operation_count: 21
  slug: validic-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 3
apis:
- baseURL: https://api.v2.validic.com
  baseurl_source: declared
  description: Cellular-enabled health device activation and suspension.
  name: Validic Devices API
  slug: validic-devices-api
- baseURL: https://api.v2.validic.com
  baseurl_source: declared
  description: Hosted Marketplace tokens and connection (connect/disconnect) event history.
  name: Validic Marketplace & Connections API
  slug: validic-marketplace-connections-api
- baseURL: https://api.v2.validic.com
  baseurl_source: declared
  description: Standardized health observations recorded by connected apps and devices.
  name: Validic Observations & Data API
  slug: validic-observations-data-api
- baseURL: https://api.v2.validic.com
  baseurl_source: declared
  description: Event-based webhook delivery to a customer endpoint.
  name: Validic Push Service API
  slug: validic-push-service-api
- baseURL: https://streams.v2.validic.com
  baseurl_source: declared
  description: Server-Sent Events stream of organization-wide health events.
  name: Validic Streaming API
  slug: validic-streaming-api
- baseURL: https://api.v2.validic.com
  baseurl_source: declared
  description: Provision and manage users within an organization.
  name: Validic Users API
  slug: validic-users-api
- description: Self-serve registration, email verification, login and organization provisioning for the free Validic developer tier. Returns the organization_id and organization_token that every Inform API call requ
  name: Validic Developer Signup API
  slug: validic-developer-signup-api
- baseURL: https://api.v2.validic.com
  baseurl_source: declared
  description: The Measurements API from Validic — 1 operation(s) for measurements.
  name: Validic Measurements API
  slug: validic-measurements-api
- baseURL: https://api.v2.validic.com
  baseurl_source: declared
  description: The Organizations API from Validic — 15 operation(s) for organizations.
  name: Validic Organizations API
  slug: validic-organizations-api
- baseURL: https://api.v2.validic.com
  baseurl_source: declared
  description: The Streams API from Validic — 1 operation(s) for streams.
  name: Validic Streams API
  slug: validic-streams-api
- baseURL: https://api.v2.validic.com
  baseurl_source: declared
  description: The Streams?token={token} API from Validic — 1 operation(s) for streams?token={token}.
  name: Validic Streams?token={token} API
  slug: validic-streams-token-token-api
artifact_total: 28
asyncapis:
- description: ''
  name: Validic Events Webhooks
  slug: validic-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Validic Inform Devices API
  slug: open-validic-devices-api
- collection_type: open
  name: Validic Inform Devices Marketplace & Connections API
  slug: open-validic-marketplace-connections-api
- collection_type: open
  name: Validic Inform Devices Observations & Data API
  slug: open-validic-observations-data-api
- collection_type: open
  name: Validic Inform Devices Push Service API
  slug: open-validic-push-service-api
- collection_type: open
  name: Validic Inform Devices Streaming API
  slug: open-validic-streaming-api
- collection_type: open
  name: Validic Inform Devices Users API
  slug: open-validic-users-api
- collection_type: open
  name: Validic Inform API
  slug: open-validic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/validic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/validic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/validic-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/validic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/validic
- group: company
  title: ''
  type: Website
  url: https://validic.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.validic.com
- group: commercial
  title: ''
  type: Plans
  url: plans/validic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/validic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/validic-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://validic.com/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.validic.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.validic.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.validic.com/docs/using-this-guide
- group: operate
  title: ''
  type: Support
  url: https://help.validic.com/portal/2
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.validic.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://validic.com/online-service-agreement-inform/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://validic.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.validic.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/validic-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/validic-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/validic-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/validic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/validic-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/validic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/validic-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/validic-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/validic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/validic-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/validic-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/validic-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/validic-events-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/validic-inform-data-resources-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/validic-streaming-resources-overlay.yaml
created: '2026-07-05'
description: Validic is an enterprise health-data platform that connects patient-recorded data from digital health applications, medical devices, and wearables to healthcare organizations. Its Inform API and Mobile SDK provision users against an organization, present a hosted Marketplace for connecting API/cloud and Bluetooth sources, and return standardized health observations - CGM, intraday activity, point-in-time measurements, nutrition, sleep, daily summaries, and workouts. Validic also manages cellular-enabled devices, exposes connection-event history, and delivers data in real time through a Server-Sent Events Streaming API and a webhook Push Service. The platform is HITRUST-certified and HIPAA-compliant. Requests authenticate with an organization access token passed as the token query parameter over HTTPS.
finops:
- name: Validic Finops
  service_category: Health Data Platform
  slug: validic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/validic.png
layout: provider
modified: '2026-08-15'
name: Validic
nav: Providers
network: true
overview: 'Validic publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Marketplace & Connections API, Observations & Data API, and 7 more. Tagged areas include Health Data, Digital Health, Wearables, Remote Patient Monitoring, and Health IoT.


  The Validic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Validic''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, signup flow, and 28 more developer resources.'
plans:
- name: Validic Plans Pricing
  plan_count: 4
  slug: validic-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Validic Rate Limits
  slug: validic-rate-limits
score:
  band: strong
  composite: 62.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 73.7
  previous_composite: 64.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 53.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/validic/refs/heads/main/screenshots/validic-2026-08-17T082707.png
security:
- kind: authentication
  name: Validic Authentication
  slug: validic-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Validic Domain Security
  slug: validic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Validic Vulnerability Disclosure
  slug: validic-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Validic Trust Center
  slug: validic-trust-center
  summary_line: HITRUST CSF, ISO/IEC 27001, HIPAA
slug: validic
tags:
- Health Data
- Digital Health
- Wearables
- Remote Patient Monitoring
- Health IoT
- Interoperability
- HIPAA
website: https://validic.com
---
