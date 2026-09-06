---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Steelcase Agentic Access
  operation_count: 7
  slug: steelcase-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- baseURL: https://roomwizard.local/api
  baseurl_source: declared
  description: Manage conference room reservations including creating, retrieving, updating, and cancelling bookings.
  name: Steelcase Bookings API
  slug: steelcase-bookings-api
- baseURL: https://roomwizard.local/api
  baseurl_source: declared
  description: Retrieve room information including availability, capacity, and equipment details.
  name: Steelcase Rooms API
  slug: steelcase-rooms-api
- baseURL: https://roomwizard.local/api
  baseurl_source: declared
  description: Monitor the connectivity and health status of RoomWizard devices and the connector service.
  name: Steelcase Status API
  slug: steelcase-status-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Steelcase RoomWizard Bookings API
  slug: open-steelcase-bookings-api
- collection_type: open
  name: Steelcase RoomWizard Bookings Rooms API
  slug: open-steelcase-rooms-api
- collection_type: open
  name: Steelcase RoomWizard API
  slug: open-steelcase-roomwizard-api
- collection_type: open
  name: Steelcase RoomWizard Bookings Status API
  slug: open-steelcase-status-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/steelcase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steelcase-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/steelcase
- group: company
  title: ''
  type: Website
  url: https://www.steelcase.com
- group: operate
  title: ''
  type: TechSupport
  url: https://www.steelcase.com/techsupport/
- group: other
  title: ''
  type: Downloads
  url: https://www.steelcase.com/techsupport/downloads/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/steelcase-booking-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/steelcase-room-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/steelcase-booking-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/steelcase-room-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/steelcase-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/steelcase-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/steelcase-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.steelcase.com/feed/
created: '2025-03-01'
description: Steelcase is a global leader in the office furniture and workplace design industry, providing furniture, technology, and research-based insights to help organizations create effective work environments. Steelcase offers the RoomWizard API for integrating room scheduling and conference room reservation systems with enterprise calendaring platforms. The API enables developers to manage room bookings, retrieve availability, and synchronize reservations with Microsoft Exchange, Office 365, and Google Calendar.
examples:
- key_count: 2
  name: Steelcase Create Booking Example
  slug: steelcase-create-booking-example
- key_count: 2
  name: Steelcase Get Bookings Example
  slug: steelcase-get-bookings-example
- key_count: 2
  name: Steelcase Get Room Availability Example
  slug: steelcase-get-room-availability-example
finops:
- name: Steelcase Finops
  service_category: API
  slug: steelcase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/steelcase.png
json_schemas:
- name: Steelcase Room Booking
  property_count: 12
  slug: steelcase-booking
- name: Steelcase Room
  property_count: 9
  slug: steelcase-room
json_structures:
- name: Steelcase Booking Structure
  property_count: 0
  slug: steelcase-booking-structure
- name: Steelcase Room Structure
  property_count: 0
  slug: steelcase-room-structure
jsonld:
- class_count: 28
  name: Steelcase Context
  property_count: 0
  slug: steelcase-context
layout: provider
modified: '2026-05-19'
name: Steelcase
nav: Providers
network: true
overview: 'Steelcase publishes 3 APIs on the [APIs.io](https://apis.io/) network: Bookings API, Rooms API, and Status API. Tagged areas include Office Furniture, Workplace, Room Scheduling, Facilities Management, and IoT.


  The Steelcase catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Steelcase''s developer surface includes engineering blog and 13 more developer resources.'
plans:
- name: Steelcase Plans Pricing
  plan_count: 3
  slug: steelcase-plans-pricing
press:
- date: '2026-05-25'
  title: Working With AI Assistants
  url: https://www.steelcase.com/research/articles/topics/ai/onboarding-ai/
- date: '2026-05-25'
  title: Office Design Ideas to Support AI in the Workplace
  url: https://www.steelcase.com/research/articles/topics/learning/four-new-designs-for-ai-ready-workplaces/
- date: '2026-05-25'
  title: 'The Transhuman Future: AI in the Workplace'
  url: https://www.steelcase.com/asia-en/research/articles/topics/culture-talent/translating-transhuman-code/
- date: '2026-05-25'
  title: AI Needs a Human-Centered Workplace
  url: https://www.steelcase.com/research/articles/topics/ai/ai-needs-a-human-centered-workplace/
- date: '2026-05-25'
  title: Steelcase and Frank Lloyd Wright Foundation Launch New ...
  url: https://www.prnewswire.com/news-releases/steelcase-and-frank-lloyd-wright-foundation-launch-new-collaborative-collection-301730763.html
- date: '2026-01-21'
  title: Steelcase Recognized as One of the World’s Most Admired Companies for the 20th Year
  url: https://www.steelcase.com/press-releases/steelcase-recognized-as-one-of-the-worlds-most-admired-companies-for-the-20th-year/
- date: '2025-12-10'
  title: HNI Corporation Completes Acquisition of Steelcase Inc.
  url: https://www.steelcase.com/press-releases/hni-corporation-completes-acquisition-of-steelcase-inc/
- date: '2025-09-30'
  title: Steelcase 2025 Impact Report Highlights the Strength of Community and Progress Toward a Net-Zero Future
  url: https://www.steelcase.com/press-releases/steelcase-2025-impact-report-highlights-the-strength-of-community-and-progress-toward-a-net-zero-future/
random_paper: 8
rate_limits:
- limit_count: 5
  name: Steelcase Rate Limits
  slug: steelcase-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Steelcase API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: steelcase-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Steelcase API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: steelcase-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 53.5
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Steelcase Domain Security
  slug: steelcase-domain-security
  summary_line: TLSv1.3 · DMARC
slug: steelcase
tags:
- Office Furniture
- Workplace
- Room Scheduling
- Facilities Management
- IoT
- Smart Office
- Fortune 1000
website: https://www.steelcase.com
---
