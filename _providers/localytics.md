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
  - sandbox
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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Localytics Agentic Access
  operation_count: 13
  slug: localytics-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 2
apis:
- baseURL: https://dashboard.localytics.com/api/v6
  baseurl_source: declared
  description: Requests relating to audiences
  name: Localytics Audiences API
  slug: localytics-audiences-api
- baseURL: https://dashboard.localytics.com/api/v6
  baseurl_source: declared
  description: Requests relating to all channel campaigns
  name: Localytics Campaigns API
  slug: localytics-campaigns-api
- baseURL: https://dashboard.localytics.com/api/v6
  baseurl_source: declared
  description: Requests relating to push-channel campaigns
  name: Localytics Push Campaigns API
  slug: localytics-push-campaigns-api
- description: HAL+JSON reporting and analytics API. Run queries over apps, events, sessions, users, profiles and attribution data with metrics, dimensions and conditions; the service root at https://api.localytics.
  name: Localytics Query API
  slug: localytics-query-api
- description: Read, create, update and delete user profile attributes used for targeting and segmentation, addressed by customer_id at the org, app or customer scope. No machine-readable specification is published.
  name: Localytics Profile API
  slug: localytics-profile-api
- description: Server-side event ingestion for in-app activity that completes off-device (purchases, fulfilment, backend conversions). Accepts JSON or gzipped JSON up to 256 KB per POST, validated against a publishe
  name: Localytics Events API
  slug: localytics-events-api
- description: Bulk export of audiences, profiles and raw analytics logs. Requests return a 302 redirect to a generated export file; audiences must be enabled for export in the dashboard first. No machine-readable s
  name: Localytics Export APIs
  slug: localytics-export-apis
- description: Bulk import of user profiles and audience lists built in external systems (CRM, marketing cloud) into Localytics for targeting and campaign use, with an asynchronous status endpoint per import job. No
  name: Localytics Import APIs
  slug: localytics-import-apis
- description: Point-of-interest sync for location-triggered messaging — upload and manage the geofence/POI set an app monitors. Rate limited to 20 requests per hour and 50 per day per app. No machine-readable speci
  name: Localytics Places API
  slug: localytics-places-api
- baseURL: https://dashboard.localytics.com/api/v6
  baseurl_source: declared
  description: Health and documentation endpoints
  name: Localytics Meta API
  slug: localytics-meta-api
- baseURL: https://dashboard.localytics.com/api/v6
  baseurl_source: declared
  description: Transactional push send endpoints
  name: Localytics Push API
  slug: localytics-push-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Localytics Campaigns And Audience Audiences API
  slug: open-localytics-audiences-api
- collection_type: open
  name: Localytics And Audience Audiences Campaigns API
  slug: open-localytics-campaigns-api
- collection_type: open
  name: Localytics Campaigns And Audience Audiences Push Campaigns API
  slug: open-localytics-push-campaigns-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/localytics-send-transactional-push.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.localytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.localytics.com/dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.localytics.com/campaigns_audiences_api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.localytics.com/docs/resources/developer-documentation
- group: operate
  title: ''
  type: Support
  url: https://www.localytics.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.localytics.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.localytics.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.localytics.com/terms
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/localytics-campaigns-audiences-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/localytics-campaigns-audiences-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/localytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/localytics-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/localytics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/localytics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/localytics-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/localytics-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/localytics-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/localytics-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/localytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/localytics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/localytics-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/localytics-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/localytics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/localytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.localytics.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/localytics-transactional-push-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/localytics-transactional-push-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/localytics-push.proto
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/localytics-events-api-v1-schema.json
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/localytics-tool-crosswalk.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/localytics-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/localytics-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/localytics-plans-pricing.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.localytics.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/localytics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.localytics.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/localytics
- group: start
  title: ''
  type: Login
  url: https://dashboard.localytics.com/login
created: '2026-07-17'
description: 'Localytics is a mobile analytics and customer-engagement platform that turns the behavioral signals a mobile app already produces into real-time analytics and personalized, data-driven campaigns across push notifications, in-app messages, and inbox messaging. It serves product, marketing, and engineering teams with segmentation, audience building, and campaign management. Its developer surface is broad but unevenly specified: two real OpenAPI 3.0.3 documents (a Campaigns & Audience API and a Transactional Push API served live at messaging.localytics.com/swagger.json), an MIT-licensed proto3 definition for a bidirectional streaming gRPC push service, and a published JSON Schema for Events API requests — alongside six further production REST APIs (Query/Reporting in HAL+JSON, Profile, Events, Exports, Imports, Places) that are documented only in prose. Everything authenticates with one organization-level API key and secret over HTTP Basic; there is no OAuth, no scopes and no
  rate-limit response headers anywhere. First-party SDKs cover iOS, Android, Web, Maui, Flutter, React Native, tvOS, Xamarin, Unity, Cordova and Windows. Localytics is an Upland Software product.'
image: https://localytics.com/og-image.png
json_schemas:
- name: Events API Request V1
  property_count: 8
  slug: localytics-events-api-v1
layout: provider
modified: '2026-08-13'
name: Localytics
nav: Providers
network: true
overview: 'Localytics publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Audiences API, Campaigns API, Push Campaigns API, and 2 more. Tagged areas include Company, MarTech, Mobile Analytics, Push Notifications, and Customer Engagement.


  Localytics'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 33 more developer resources.'
plans:
- name: Localytics Plans Pricing
  plan_count: 0
  slug: localytics-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Localytics Rate Limits
  slug: localytics-rate-limits
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 53.6
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 60.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/localytics/refs/heads/main/screenshots/localytics-2026-07-25T225426.png
security:
- kind: authentication
  name: Localytics Authentication
  slug: localytics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Localytics Domain Security
  slug: localytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Localytics Vulnerability Disclosure
  slug: localytics-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: localytics
tags:
- Company
- MarTech
- Mobile Analytics
- Push Notifications
- Customer Engagement
- Marketing Automation
- Mobile
- Segmentation
- Audiences
- Event Ingestion
- gRPC
website: https://www.localytics.com/
---
