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
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 49
  human_in_the_loop: 11
  name: Rachio Agentic Access
  operation_count: 79
  slug: rachio-agentic-access
  summary_line: 79 operations · 49 acting · 11 human-in-the-loop
api_count: 10
apis:
- baseURL: https://api.rach.io/1
  baseurl_source: declared
  description: 'REST API for Rachio smart irrigation controllers, Smart Hose Timers and lighting controllers: read people, devices and zones; start/stop watering; manage schedules and rain delays; subscribe to webhoo'
  name: Rachio Public API
  slug: rachio-public-api
- baseURL: https://api.rach.io/1
  baseurl_source: declared
  description: The LightingService API from Rachio — 28 operation(s) for lightingservice.
  name: Rachio Lighting Service API
  slug: rachio-lightingservice-api
- baseURL: https://api.rach.io/1
  baseurl_source: declared
  description: The ProgramService API from Rachio — 11 operation(s) for programservice.
  name: Rachio Program Service API
  slug: rachio-programservice-api
- baseURL: https://api.rach.io/1
  baseurl_source: declared
  description: The PropertyService API from Rachio — 3 operation(s) for propertyservice.
  name: Rachio Property Service API
  slug: rachio-propertyservice-api
- baseURL: https://api.rach.io/1
  baseurl_source: declared
  description: The Public API from Rachio — 21 operation(s) for public.
  name: Rachio Public API
  slug: rachio-public-api
- baseURL: https://api.rach.io/1
  baseurl_source: declared
  description: The SummaryService API from Rachio — 1 operation(s) for summaryservice.
  name: Rachio Summary Service API
  slug: rachio-summaryservice-api
- baseURL: https://api.rach.io/1
  baseurl_source: declared
  description: The ValveService API from Rachio — 7 operation(s) for valveservice.
  name: Rachio Valve Service API
  slug: rachio-valveservice-api
- baseURL: https://api.rach.io/1
  baseurl_source: declared
  description: The WebhookService API from Rachio — 7 operation(s) for webhookservice.
  name: Rachio Webhook Service API
  slug: rachio-webhookservice-api
artifact_total: 36
asyncapis:
- description: ''
  name: Rachio Webhooks
  slug: rachio-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/agentic-access/rachio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rachio-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/rules/rachio-rules.yml
  title: ''
  type: Spectral
  url: rules/rachio-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/json-ld/rachio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rachio-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/vocabulary/rachio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rachio-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/hosts/rachio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rachio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/vendors/rachio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rachio-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://rachio.statuspage.io/
- group: start
  title: ''
  type: SignUp
  url: https://rachio.com/pro/signup
- group: company
  title: ''
  type: Newsroom
  url: https://rachio.com/newsroom
- group: company
  title: ''
  type: Website
  url: https://rachio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rachio.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://rachio.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://rachio.readme.io/reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://rachio.readme.io/reference/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.rachio.com
- group: company
  title: ''
  type: Blog
  url: https://rachio.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://rachio.com/products
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rachio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rachio.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/authentication/rachio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rachio-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/conventions/rachio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rachio-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/rate-limits/rachio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rachio-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/asyncapi/rachio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rachio-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/errors/rachio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rachio-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/data-model/rachio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rachio-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/lifecycle/rachio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rachio-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/conformance/rachio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rachio-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/mcp/rachio-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rachio-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/llms/rachio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rachio-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/security/rachio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rachio-domain-security.yml
created: '2026-07-17'
description: Rachio makes smart, WiFi-connected irrigation controllers, Smart Hose Timers and lighting controllers for homes and landscapes. The Rachio Public API lets developers read a person's account, controllers (devices) and irrigation zones, start and stop watering, manage fixed and Flex (weather-adjusted) schedules, set rain delays, and subscribe to real-time webhook events for schedule and zone activity. Requests authenticate with an OAuth2 bearer token retrieved from the Rachio mobile app; the Controller and User API is served at https://api.rach.io/1 and newer product surfaces at https://cloud-rest.rach.io, with a quota of 3,500 requests per day per token.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rachio.png
json_schemas:
- name: CreateLightingProgramRequest
  property_count: 8
  slug: rachio-create-lighting-program-request
- name: CreateLightingSceneRequest
  property_count: 3
  slug: rachio-create-lighting-scene-request
- name: CreatePlannedRunSkipOverridesResponse
  property_count: 3
  slug: rachio-create-planned-run-skip-overrides-response
- name: CreateProgramV2Request
  property_count: 9
  slug: rachio-create-program-v2-request
- name: CreateSkipOverridesResponse
  property_count: 3
  slug: rachio-create-skip-overrides-response
- name: CreateWebhookRequest
  property_count: 4
  slug: rachio-create-webhook-request
- name: CreateWebhookResponse
  property_count: 1
  slug: rachio-create-webhook-response
- name: DeleteSkipOverridesRequest
  property_count: 2
  slug: rachio-delete-skip-overrides-request
- name: FindPropertyByEntityResponse
  property_count: 1
  slug: rachio-find-property-by-entity-response
- name: GetPropertyResponse
  property_count: 1
  slug: rachio-get-property-response
- name: GetValveDayViewsRequest
  property_count: 3
  slug: rachio-get-valve-day-views-request
- name: GetWebhookResponse
  property_count: 1
  slug: rachio-get-webhook-response
- name: ListPropertiesResponse
  property_count: 1
  slug: rachio-list-properties-response
- name: ListWebhookEventTypesResponse
  property_count: 1
  slug: rachio-list-webhook-event-types-response
- name: ListWebhooksResponse
  property_count: 1
  slug: rachio-list-webhooks-response
- name: UpdateLightingProgramRequest
  property_count: 9
  slug: rachio-update-lighting-program-request
- name: UpdateLightingSceneRequest
  property_count: 3
  slug: rachio-update-lighting-scene-request
- name: UpdateLightingZoneGroupRequest
  property_count: 3
  slug: rachio-update-lighting-zone-group-request
- name: UpdateLightingZoneRequest
  property_count: 5
  slug: rachio-update-lighting-zone-request
- name: UpdateProgramV2Request
  property_count: 11
  slug: rachio-update-program-v2-request
- name: UpdateWebhookRequest
  property_count: 5
  slug: rachio-update-webhook-request
jsonld:
- class_count: 120
  name: Rachio Context
  property_count: 176
  slug: rachio-context
layout: provider
modified: '2026-07-20'
name: Rachio
nav: Providers
network: true
overview: 'Rachio publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Public API, Lighting Service API, Program Service API, and 5 more. Tagged areas include Company, Smart Home, IoT, Irrigation, and Home Automation.


  The Rachio catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Rachio''s developer surface includes signup flow, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 1
  name: Rachio Rate Limits
  slug: rachio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Rachio API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: rachio-rules
score:
  band: strong
  composite: 57.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 17.0
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 68.5
    developer_ergonomics: 58.9
    discoverability: 80.4
    operational_transparency: 44.7
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/rachio/refs/heads/main/screenshots/rachio-2026-08-17T081438.png
security:
- kind: authentication
  name: Rachio Authentication
  slug: rachio-authentication
  summary_line: oauth2/http · 1 scheme
- kind: domain-security
  name: Rachio Domain Security
  slug: rachio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rachio
tags:
- Company
- Smart Home
- IoT
- Irrigation
- Home Automation
- Water Management
- Webhook
website: https://rachio.com
---
