---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 1
  name: Flock Safety Agentic Access
  operation_count: 43
  slug: flock-safety-agentic-access
  summary_line: 43 operations · 26 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The Alerts API from Flock Safety — 3 operation(s) for alerts.
  name: Flock Safety Alerts API
  slug: flock-safety-alerts-api
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The CAD Events API from Flock Safety — 7 operation(s) for cad events.
  name: Flock Safety CAD Events API
  slug: flock-safety-cad-events-api
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The Custom Hotlists API from Flock Safety — 5 operation(s) for custom hotlists.
  name: Flock Safety Custom Hotlists API
  slug: flock-safety-custom-hotlists-api
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The Devices API from Flock Safety — 3 operation(s) for devices.
  name: Flock Safety Devices API
  slug: flock-safety-devices-api
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The LPR Hotlist Alert Subscriptions API from Flock Safety — 2 operation(s) for lpr hotlist alert subscriptions.
  name: Flock Safety LPR Hotlist Alert Subscriptions API
  slug: flock-safety-lpr-hotlist-alert-subscriptions-api
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The Plate Reads API from Flock Safety — 2 operation(s) for plate reads.
  name: Flock Safety Plate Reads API
  slug: flock-safety-plate-reads-api
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The Tracked Subject Types API from Flock Safety — 2 operation(s) for tracked subject types.
  name: Flock Safety Tracked Subject Types API
  slug: flock-safety-tracked-subject-types-api
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The Tracked Subjects API from Flock Safety — 2 operation(s) for tracked subjects.
  name: Flock Safety Tracked Subjects API
  slug: flock-safety-tracked-subjects-api
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The Vehicle Images API from Flock Safety — 1 operation(s) for vehicle images.
  name: Flock Safety Vehicle Images API
  slug: flock-safety-vehicle-images-api
- baseURL: https://api.flocksafety.com/api/v3
  baseurl_source: declared
  description: The OAuth2 API from Flock Safety — 1 operation(s) for oauth2.
  name: Flock Safety O Auth2 API
  slug: flock-safety-oauth2-api
artifact_total: 35
asyncapis:
- description: Real-time webhook that delivers Flock Safety LPR (license plate recognition) hotlist alert events. An alert fires when a plate captured by a Flock LPR camera (owned by, or shared within the First Resp
  name: Flock Safety LPR Hotlist Alerts Webhook
  slug: flock-safety-lpr-alerts-asyncapi
collections:
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts API
  slug: open-flock-safety-alerts-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts CAD Events API
  slug: open-flock-safety-cad-events-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Custom Hotlists API
  slug: open-flock-safety-custom-hotlists-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Devices API
  slug: open-flock-safety-devices-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts LPR Hotlist Alert Subscriptions API
  slug: open-flock-safety-lpr-hotlist-alert-subscriptions-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts OAuth2 API
  slug: open-flock-safety-oauth2-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Plate Reads API
  slug: open-flock-safety-plate-reads-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Tracked Subject Types API
  slug: open-flock-safety-tracked-subject-types-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Tracked Subjects API
  slug: open-flock-safety-tracked-subjects-api
- collection_type: open
  name: Flock Safety API Platform (v3) Alerts Vehicle Images API
  slug: open-flock-safety-vehicle-images-api
common:
- group: commercial
  href: https://artifacts.apis.io/flock-safety/plans/flock-safety-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flock-safety-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/flock-safety/capabilities/flock-safety-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/flock-safety-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/flock-safety/overlays/flock-safety-api-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/flock-safety-api-platform-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/flock-safety/security/flock-safety-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/flock-safety-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://flocksafety.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flocksafety.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flocksafety.com/developer-hub/docs/flock-developer-platform-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flocksafety.com/developer-hub/reference/post_oauth-token
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flocksafety.com/developer-hub/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.flocksafety.com/s/
- group: company
  title: ''
  type: Blog
  url: https://flocksafety.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flocksafety.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.flocksafety.com/developer-hub/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://flocksafety.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flocksafety.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flocksafety.com/legal/privacy-notice
- group: auth
  title: ''
  type: Compliance
  url: https://security.flocksafety.com/
- group: operate
  href: https://artifacts.apis.io/flock-safety/rate-limits/flock-safety-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flock-safety-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Flock-Safety
- group: auth
  href: https://artifacts.apis.io/flock-safety/authentication/flock-safety-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flock-safety-authentication.yml
- group: auth
  href: https://artifacts.apis.io/flock-safety/scopes/flock-safety-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/flock-safety-scopes.yml
- group: design
  href: https://artifacts.apis.io/flock-safety/conventions/flock-safety-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flock-safety-conventions.yml
- group: design
  href: https://artifacts.apis.io/flock-safety/conventions/flock-safety-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/flock-safety-conventions.yml
- group: design
  href: https://artifacts.apis.io/flock-safety/errors/flock-safety-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/flock-safety-problem-types.yml
- group: design
  href: https://artifacts.apis.io/flock-safety/lifecycle/flock-safety-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flock-safety-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/flock-safety/lifecycle/flock-safety-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/flock-safety-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/flock-safety/conformance/flock-safety-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flock-safety-conformance.yml
- group: design
  href: https://artifacts.apis.io/flock-safety/data-model/flock-safety-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flock-safety-data-model.yml
- group: build
  href: https://artifacts.apis.io/flock-safety/packages/flock-safety-packages.yml
  title: ''
  type: Packages
  url: packages/flock-safety-packages.yml
- group: agent
  href: https://artifacts.apis.io/flock-safety/mcp/flock-safety-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/flock-safety-mcp.yml
- group: agent
  href: https://artifacts.apis.io/flock-safety/llms/flock-safety-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flock-safety-llms.txt
- group: auth
  href: https://artifacts.apis.io/flock-safety/security/flock-safety-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flock-safety-domain-security.yml
- group: docs
  href: https://artifacts.apis.io/flock-safety/asyncapi/flock-safety-lpr-alerts-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/flock-safety-lpr-alerts-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/flock-safety/asyncapi/flock-safety-lpr-alerts-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/flock-safety-lpr-alerts-asyncapi.yml
- group: operate
  href: https://artifacts.apis.io/flock-safety/changelog/flock-safety-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flock-safety-changelog.yml
- group: agent
  href: https://artifacts.apis.io/flock-safety/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/flock-safety/agentic-access/flock-safety-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flock-safety-agentic-access.yml
created: '2026-07-17'
description: Flock Safety is a public safety technology company whose platform connects communities, businesses, and law enforcement through crime detection, investigation, and response tools built around license plate recognition (LPR) cameras, audio detection, video, and the FlockOS situational-awareness platform. Its v3 API Platform (api.flocksafety.com) lets approved customer organizations and third-party developers build "Flock Apps" that bring data in (register hardware as devices, ingest vehicle images for detection, push CAD events, alerts, and geolocation telemetry, manage custom hotlists) and connect Flock data out (retrieve devices, look up license plate reads, and subscribe to real-time LPR hotlist alert webhooks). The APIs use OAuth 2.0 with machine-level (client_credentials) and recommended user-level (authorization_code) flows, role-based access control, audit logging, and data-stewardship requirements.
finops:
- has_sources: true
  method: derived
  name: Flock Safety Finops
  primary_unit: ''
  service_category: ''
  slug: flock-safety-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flock-safety.png
layout: provider
modified: '2026-07-19'
name: Flock Safety
nav: Providers
network: true
overview: 'Flock Safety publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, CAD Events API, Custom Hotlists API, and 7 more. Tagged areas include Company, American Dynamism, Public Safety, Law Enforcement, and License Plate Recognition.


  The Flock Safety catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Flock Safety''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 30 more developer resources.'
plans:
- name: Flock Safety Plans Pricing
  plan_count: 0
  slug: flock-safety-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Flock Safety Rate Limits
  slug: flock-safety-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Flock Safety API Rules
  rule_count: 60
  severity_counts:
    error: 48
    hint: 0
    info: 3
    warn: 9
  slug: flock-safety-rules
scopes:
- name: Flock Safety Scopes
  scope_count: 5
  slug: flock-safety-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.2
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 57.8
    developer_ergonomics: 55.4
    discoverability: 73.2
    operational_transparency: 50.0
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/flock-safety/flock-safety-2026-07-25T214812.png
security:
- kind: authentication
  name: Flock Safety Authentication
  slug: flock-safety-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Flock Safety Domain Security
  slug: flock-safety-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Flock Safety Trust Center
  slug: flock-safety-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018
skill_count: 5
skills:
- name: Get a Flock Safety API access token
  slug: flock-safety-authenticate
- name: Create a custom hotlist and add plate entries
  slug: flock-safety-manage-custom-hotlist
- name: Look up license plate reads
  slug: flock-safety-plate-lookup
- name: Upsert a CAD event and append a narrative
  slug: flock-safety-push-cad-event
- name: Subscribe to real-time LPR hotlist alert webhooks
  slug: flock-safety-subscribe-lpr-alerts
slug: flock-safety
tags:
- Company
- American Dynamism
- Public Safety
- Law Enforcement
- License Plate Recognition
- LPR
- Physical Security
- Surveillance
- Computer Vision
- Webhook
- Geolocation
- CAD
website: https://flocksafety.com
---
