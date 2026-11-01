---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Coram Ai Agentic Access
  operation_count: 26
  slug: coram-ai-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: The alerts API from Coram Ai — 5 operation(s) for alerts.
  name: Coram Ai Alerts API
  slug: coram-ai-alerts-api
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: Organize cameras into logical collections for easier management. Camera groups allow you to categorize cameras by location, purpose, or any custom criteria. Use these endpoints to create, update, list
  name: Coram Ai Camera Groups API
  slug: coram-ai-camera-groups-api
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: Manage individual cameras within your organization. Use these endpoints to register new cameras, update camera settings, retrieve camera information and status, move cameras between locations, and del
  name: Coram Ai Cameras API
  slug: coram-ai-cameras-api
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: List access control doors and trigger momentary remote unlocks. The same per-door permission checks the in-app unlock flow runs apply here — a key whose creator cannot unlock a door in the UI cannot u
  name: Coram Ai Doors API
  slug: coram-ai-doors-api
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: Query access control device events (card scans, REX presses, forced-open / held-open alarms, battery alerts, …) and fetch the MP4 video clip recorded by the door's primary camera around an event's tim
  name: Coram Ai Events API
  slug: coram-ai-events-api
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: Manage physical site configurations where cameras and NVRs are deployed. Locations represent your facilities, buildings, or areas. Use these endpoints to create, update, list, and delete locations.
  name: Coram Ai Locations API
  slug: coram-ai-locations-api
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: Control and monitor Network Video Recorders (NVRs) in your infrastructure. NVRs are hardware devices that record and store video from connected cameras. Use these endpoints to register NVRs, update th
  name: Coram Ai Nvrs API
  slug: coram-ai-nvrs-api
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: Bulk-import your school reunification roster — schools, students (with guardians), teachers, staff, and class sections — programmatically, the API equivalent of the in-app CSV upload. Each import is a
  name: Coram Ai Reunification API
  slug: coram-ai-reunification-api
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: View user credentials and assign or remove cards.
  name: Coram Ai Credentials API
  slug: coram-ai-credentials-api
- baseURL: https://api.coram.ai/developer-api
  baseurl_source: declared
  description: Choose which doors users can unlock and when.
  name: Coram Ai Permissions API
  slug: coram-ai-permissions-api
artifact_total: 24
collections:
- collection_type: open
  name: Coram alerts API
  slug: open-coram-ai-alerts-api
- collection_type: open
  name: Coram alerts camera-groups API
  slug: open-coram-ai-camera-groups-api
- collection_type: open
  name: Coram alerts cameras API
  slug: open-coram-ai-cameras-api
- collection_type: open
  name: Coram alerts doors API
  slug: open-coram-ai-doors-api
- collection_type: open
  name: Coram alerts events API
  slug: open-coram-ai-events-api
- collection_type: open
  name: Coram alerts locations API
  slug: open-coram-ai-locations-api
- collection_type: open
  name: Coram alerts nvrs API
  slug: open-coram-ai-nvrs-api
- collection_type: open
  name: Coram alerts reunification API
  slug: open-coram-ai-reunification-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.coram.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.coram.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.coram.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.coram.ai/
- group: auth
  href: https://artifacts.apis.io/coram-ai/authentication/coram-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coram-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/coram-ai/mcp/coram-ai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/coram-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/coram-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/coram-ai/agentic-access/coram-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coram-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/coram-ai/conventions/coram-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coram-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/coram-ai/errors/coram-ai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/coram-ai-error-codes.yml
- group: design
  href: https://artifacts.apis.io/coram-ai/data-model/coram-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coram-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/coram-ai/conformance/coram-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coram-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/coram-ai/overlays/coram-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/coram-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/coram-ai/llms/coram-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coram-ai-llms.txt
- group: design
  href: https://artifacts.apis.io/coram-ai/lifecycle/coram-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coram-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coram.ai
- group: operate
  href: https://artifacts.apis.io/coram-ai/changelog/coram-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/coram-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/coram-ai/security/coram-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coram-ai-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.coram.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://help.coram.ai/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.coram.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coram.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coram.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://coram.ai
created: '2026-07-17'
description: Coram AI is an AI-native unified physical security platform that brings video surveillance, access control, emergency management, and visitor verification into a single cloud system that works with existing IP cameras. Its Developer API offers programmatic access to cameras, camera groups, NVRs, locations, access-control doors and events, and firearm-detection alerts, plus bulk school-reunification roster imports. Features include natural-language AI video search, firearm and fall detection, license plate and facial recognition, tailgating alerts, and remote door unlock. Coram is backed by 8VC and Battery Ventures.
image: https://cdn.prod.website-files.com/630e00312de75c578a95ebfb/6a1ed1f27828fd211e840fd7_Open%20Graph.png
layout: provider
modified: '2026-07-18'
name: Coram Ai
nav: Providers
network: true
overview: 'Coram Ai publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Camera Groups API, Cameras API, and 7 more. Tagged areas include Company, Physical Security, Video Surveillance, Access Control, and Artificial Intelligence.


  Coram Ai''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 17 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 49.5
    developer_ergonomics: 58.9
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coram-ai/coram-ai-2026-07-25T210425.png
security:
- kind: authentication
  name: Coram Ai Authentication
  slug: coram-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Coram Ai Domain Security
  slug: coram-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Respond to an access-control event
  slug: coram-ai-access-control-response
- name: Manage the firearm alert lifecycle
  slug: coram-ai-firearm-alert-lifecycle
- name: Onboard Coram camera infrastructure
  slug: coram-ai-onboard-camera-infrastructure
slug: coram-ai
tags:
- Company
- Physical Security
- Video Surveillance
- Access Control
- Artificial Intelligence
- Security Cameras
- Emergency Management
- Computer Vision
website: https://coram.ai
---
