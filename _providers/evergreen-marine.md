---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Evergreen Marine Agentic Access
  operation_count: 22
  slug: evergreen-marine-agentic-access
  summary_line: 22 operations · 13 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Endpoints implemented by the adopters who publish arrival notices
  name: Evergreen Marine Corp. AN Publisher Endpoints API
  slug: evergreen-marine-an-publisher-endpoints-api
- description: Endpoints implemented by the adopters who receive arrival notices
  name: Evergreen Marine Corp. AN Subscriber Endpoints API
  slug: evergreen-marine-an-subscriber-endpoints-api
- description: Booking endPoints to be implemented by **providers** of the Booking API
  name: Evergreen Marine Corp. Booking API
  slug: evergreen-marine-booking-api
- description: Event Service Controller
  name: Evergreen Marine Corp. Events API
  slug: evergreen-marine-events-api
- description: Issuance Response **implemented** by carrier
  name: Evergreen Marine Corp. Issuance Response API
  slug: evergreen-marine-issuance-response-api
- description: Notifications to be implemented by the **consumers** of the Booking API
  name: Evergreen Marine Corp. Notifications API
  slug: evergreen-marine-notifications-api
- description: ''
  name: Evergreen Marine Corp. Point To Point API
  slug: evergreen-marine-point-to-point-api
- description: ''
  name: Evergreen Marine Corp. Port Schedule API
  slug: evergreen-marine-port-schedule-api
- description: The Shipping Instructions endPoints to be implemented by **providers** of the Bill of Lading API
  name: Evergreen Marine Corp. Shipping Instructions API
  slug: evergreen-marine-shipping-instructions-api
- description: Subscriptions Service Controller
  name: Evergreen Marine Corp. Subscriptions API
  slug: evergreen-marine-subscriptions-api
- description: The Surrender Requests **implemented** by carrier
  name: Evergreen Marine Corp. Surrender Requests API
  slug: evergreen-marine-surrender-requests-api
- description: The Transport Document endPoints to be implemented by **providers** of the Bill of Lading API
  name: Evergreen Marine Corp. Transport Document API
  slug: evergreen-marine-transport-document-api
- description: ''
  name: Evergreen Marine Corp. Vessel Schedule API
  slug: evergreen-marine-vessel-schedule-api
artifact_total: 44
common:
- group: agent
  href: https://artifacts.apis.io/evergreen-marine/agentic-access/evergreen-marine-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/evergreen-marine-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/evergreen-marine/plans/evergreen-marine-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/evergreen-marine-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/evergreen-marine/rules/evergreen-marine-rules.yml
  title: ''
  type: Spectral
  url: rules/evergreen-marine-rules.yml
- group: design
  href: https://artifacts.apis.io/evergreen-marine/json-ld/evergreen-marine-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/evergreen-marine-context.jsonld
- group: design
  href: https://artifacts.apis.io/evergreen-marine/vocabulary/evergreen-marine-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/evergreen-marine-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/evergreen-marine/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/evergreen-marine/data-model/evergreen-marine-data-model.yml
  title: ''
  type: DataModel
  url: data-model/evergreen-marine-data-model.yml
- group: design
  href: https://artifacts.apis.io/evergreen-marine/conventions/evergreen-marine-conventions.yml
  title: ''
  type: Conventions
  url: conventions/evergreen-marine-conventions.yml
- group: start
  href: https://artifacts.apis.io/evergreen-marine/sandbox/evergreen-marine-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/evergreen-marine-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/evergreen-marine/authentication/evergreen-marine-authentication.yml
  title: ''
  type: Authentication
  url: authentication/evergreen-marine-authentication.yml
- group: operate
  href: https://artifacts.apis.io/evergreen-marine/lifecycle/evergreen-marine-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/evergreen-marine-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/evergreen-marine/lifecycle/evergreen-marine-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/evergreen-marine-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/evergreen-marine/errors/evergreen-marine-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/evergreen-marine-problem-types.yml
- group: design
  href: https://artifacts.apis.io/evergreen-marine/conformance/evergreen-marine-conformance.yml
  title: ''
  type: Conformance
  url: conformance/evergreen-marine-conformance.yml
- group: other
  href: https://artifacts.apis.io/evergreen-marine/overlays/evergreen-marine-arrival-notice-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/evergreen-marine-arrival-notice-overlay.yaml
- group: other
  href: https://artifacts.apis.io/evergreen-marine/hosts/evergreen-marine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evergreen-marine-hosts.yml
- group: auth
  href: https://artifacts.apis.io/evergreen-marine/security/evergreen-marine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evergreen-marine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.evergreen-marine.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.shipmentlink.com/_ec/APIPORTAL_Home
- group: docs
  title: ''
  type: Documentation
  url: https://www.shipmentlink.com/_ec/APIPORTAL_APIServiceCategory
- group: operate
  title: ''
  type: FAQ
  url: https://www.shipmentlink.com/_ec/APIPORTAL_FAQ
- group: start
  title: ''
  type: Login
  url: https://www.shipmentlink.com/tam1/jsp/TAM1_Login.jsp?lang=en
- group: operate
  title: ''
  type: Support
  url: https://www.evergreen-marine.com/emc/aboutevergreen/jsp/EMC_ContactUs.jsp?lang=en
- group: company
  title: ''
  type: News
  url: https://www.evergreen-marine.com/emc/latestnews/jsp/EMC_NoticesAndNews.jsp?lang=en
- group: company
  title: ''
  type: About
  url: https://www.evergreen-marine.com/emc/aboutevergreen/jsp/EMC_CorporateProfile.jsp?lang=en
- group: other
  title: ''
  type: Sustainability
  url: https://csr.evergreen-marine.com/?en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evergreen-marine.com/emc/common/jsp/EMC_TermsOfUse.jsp?lang=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evergreen-marine.com/emc/common/jsp/EMC_PrivacyPolicy.jsp?lang=en
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC0CfeZUHFm7w5A6c4rGhU4Q
created: '2026-10-18'
description: 'Evergreen Marine Corp. (Taiwan) Ltd. (TWSE: 2603) is a worldwide container shipping company founded by Dr. Yung-Fa Chang in 1968; since 2007 its group carriers have operated under the Evergreen Line brand. Through its ShipmentLink e-commerce platform it offers online cargo tracking, vessel schedules, booking, e-B/L, VGM submission, EDI services and an API Developer Portal with a catalogue of APIs such as shipment Track & Trace, available to customers after an application and registration process.'
image: https://www.evergreen-marine.com/emc/common/images/logo/emc_logo.svg
json_schemas:
- name: Approve Transport Document
  property_count: 1
  slug: evergreen-marine-approve-transport-document
- name: Booking Notification
  property_count: 8
  slug: evergreen-marine-booking-notification
- name: Booking
  property_count: 51
  slug: evergreen-marine-booking
- name: Cancel Booking Request
  property_count: 1
  slug: evergreen-marine-cancel-booking-request
- name: Create Booking Response
  property_count: 1
  slug: evergreen-marine-create-booking-response
- name: Create Booking
  property_count: 38
  slug: evergreen-marine-create-booking
- name: Create Shipping Instructions Response
  property_count: 1
  slug: evergreen-marine-create-shipping-instructions-response
- name: Create Shipping Instructions
  property_count: 32
  slug: evergreen-marine-create-shipping-instructions
- name: GetArrivalNoticesResponse
  property_count: 2
  slug: evergreen-marine-get-arrival-notices-response
- name: Issuance Response
  property_count: 5
  slug: evergreen-marine-issuance-response
- name: PostArrivalNoticeNotificationsRequest
  property_count: 1
  slug: evergreen-marine-post-arrival-notice-notifications-request
- name: PostArrivalNoticesRequest
  property_count: 1
  slug: evergreen-marine-post-arrival-notices-request
- name: PostArrivalNoticesResponse
  property_count: 1
  slug: evergreen-marine-post-arrival-notices-response
- name: Surrender Request Details
  property_count: 7
  slug: evergreen-marine-surrender-request-details
- name: Transport Document
  property_count: 46
  slug: evergreen-marine-transport-document
- name: Update Booking
  property_count: 40
  slug: evergreen-marine-update-booking
- name: Update Shipping Instructions
  property_count: 33
  slug: evergreen-marine-update-shipping-instructions
jsonld:
- class_count: 120
  name: Evergreen Marine Context
  property_count: 336
  slug: evergreen-marine-context
layout: provider
modified: '2026-10-18'
name: Evergreen Marine Corp.
nav: Providers
network: true
overview: 'Evergreen Marine Corp. publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including AN Publisher Endpoints API, AN Subscriber Endpoints API, Booking API, and 10 more. Tagged areas include Company, Container Shipping, Logistics, Maritime, and Shipping.


  The Evergreen Marine Corp. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Evergreen Marine Corp.''s developer surface includes sandbox, authentication, documentation, FAQ, support, product news, YouTube channel, and 22 more developer resources.'
plans:
- name: Evergreen Marine Plans Pricing
  plan_count: 1
  slug: evergreen-marine-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Evergreen Marine Rate Limits
  slug: evergreen-marine-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Evergreen Marine Corp. API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: evergreen-marine-rules
scopes:
- name: Evergreen Marine Scopes
  scope_count: 0
  slug: evergreen-marine-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 38.2
    contract_governance: 35.6
    contract_quality: 54.2
    developer_ergonomics: 32.7
    discoverability: 63.4
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/evergreen-marine/evergreen-marine-2026-11-03T131658.png
security:
- kind: authentication
  name: Evergreen Marine Authentication
  slug: evergreen-marine-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Evergreen Marine Domain Security
  slug: evergreen-marine-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 6
skills:
- name: evergreen-marine-book-a-shipment
  slug: evergreen-marine-book-a-shipment
- name: evergreen-marine-find-sailing-schedules
  slug: evergreen-marine-find-sailing-schedules
- name: evergreen-marine-retrieve-arrival-notices
  slug: evergreen-marine-retrieve-arrival-notices
- name: evergreen-marine-submit-shipping-instructions-and-approve-draft-bl
  slug: evergreen-marine-submit-shipping-instructions-and-approve-draft-bl
- name: evergreen-marine-surrender-an-ebl
  slug: evergreen-marine-surrender-an-ebl
- name: evergreen-marine-track-shipment-events
  slug: evergreen-marine-track-shipment-events
slug: evergreen-marine
tags:
- Company
- Container Shipping
- Logistics
- Maritime
- Shipping
- Supply Chain
- Track and Trace
- Taiwan
website: https://www.evergreen-marine.com/
---
