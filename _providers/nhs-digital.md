---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Nhs Digital Agentic Access
  operation_count: 52
  slug: nhs-digital-agentic-access
  summary_line: 52 operations · 25 acting
api_count: 23
apis:
- description: Access the national NHS patient demographic database. Supports search, retrieval, and update of patient records including names, addresses, dates of birth, registered GPs, nominated pharmacies, and NH
  name: Personal Demographics Service - FHIR API
  slug: personal-demographics-service-fhir-api
- description: Transmit electronic prescriptions between prescribers and community dispensers. Prescribers can create, encode, and cancel prescriptions; dispensers can download prescriptions, manage dispense notific
  name: Electronic Prescription Service - FHIR API
  slug: electronic-prescription-service-fhir-api
- description: Access a patient's Summary Care Record (SCR), a national electronic record of key clinical information derived from GP records. Also provides access to the Access Control Service (ACS) for managing pa
  name: Summary Care Record - FHIR API
  slug: summary-care-record-fhir-api
- description: Locate and access patient information shared by other NHS healthcare organisations to support direct patient care. Supports both producer and consumer roles, enabling providers to publish record point
  name: National Record Locator - FHIR API
  slug: national-record-locator-fhir-api
- description: Send booking and referral information between NHS service providers following the NHS Booking and Referral Standard (BaRS). Enables interoperable bookings and referrals across urgent and emergency car
  name: Booking and Referral - FHIR API
  slug: booking-and-referral-fhir-api
- description: Manage appointments across GP practices. Enables third-party systems to search for available slots, book appointments, amend or cancel bookings, and retrieve appointment details via a FHIR STU3 API ho
  name: GP Connect Appointment Management - FHIR API
  slug: gp-connect-appointment-management-fhir-api
- description: Interact with the NHS e-Referral Service (e-RS), the national paperless referral system for primary and secondary care. Supports creating and managing referrals, retrieving available service slots, an
  name: e-Referral Service - FHIR API
  slug: e-referral-service-fhir-api
- description: Retrieve a patient's immunisation history recorded in NHS national systems. Supports clinical decision-making, care continuity, and patient-facing applications by providing structured vaccination reco
  name: Immunisation History - FHIR API
  slug: immunisation-history-fhir-api
- description: Engage with users of the NHS App, enabling healthcare organisations and suppliers to send in-app messages, manage notifications, and trigger communications to patients who have the NHS App installed o
  name: NHS App API
  slug: nhs-app-api
- description: Search for NHS healthcare services across England including GPs, dentists, opticians, hospitals, pharmacies, and other care settings. Returns structured service information, location data, opening hou
  name: Directory of Healthcare Services (Service Search) API
  slug: directory-of-healthcare-services-service-search-api
- description: Authenticate patients and members of the public using NHS login, the national identity service for patient-facing digital health services in England. Implements OpenID Connect and OAuth 2.0 supporting
  name: NHS Login API
  slug: nhs-login-api
- description: Query the Spine Directory Service (SDS) to look up endpoint information, organisation codes, and service metadata for NHS organisations and systems registered on the NHS Spine. Supports routing decisi
  name: Spine Directory Service - FHIR API
  slug: spine-directory-service-fhir-api
- description: Retrieve metadata about NHS health datasets suitable for publication in health research catalogues. Enables researchers and data controllers to discover available NHS datasets, their coverage, data cu
  name: Health Research Data Catalogue API
  slug: health-research-data-catalogue-api
- description: Pull content from the NHS.UK website about health conditions, medications, live well guidance, mental health, care and support, and the NHS system. Returns structured JSON content suitable for integra
  name: NHS Website Content API
  slug: nhs-website-content-api
- description: Exchange messages and data files between NHS organisations using MESH, the national messaging infrastructure. Supports sending and receiving structured clinical messages, bulk data transfers, and real
  name: Message Exchange for Social Care and Health (MESH) API
  slug: message-exchange-for-social-care-and-health-mesh-api
- description: The Booking API from NHS Digital — 2 operation(s) for booking.
  name: NHS Digital Booking API
  slug: nhs-digital-booking-api
- description: The communication API from NHS Digital — 4 operation(s) for communication.
  name: NHS Digital communication API
  slug: nhs-digital-communication-api
- description: The Message API from NHS Digital — 1 operation(s) for message.
  name: NHS Digital Message API
  slug: nhs-digital-message-api
- description: The Metadata API from NHS Digital — 2 operation(s) for metadata.
  name: NHS Digital Metadata API
  slug: nhs-digital-metadata-api
- description: The R4 API from NHS Digital — 6 operation(s) for r4.
  name: NHS Digital R4 API
  slug: nhs-digital-r4-api
- description: The Referral API from NHS Digital — 2 operation(s) for referral.
  name: NHS Digital Referral API
  slug: nhs-digital-referral-api
- description: The Slots API from NHS Digital — 1 operation(s) for slots.
  name: NHS Digital Slots API
  slug: nhs-digital-slots-api
- description: The STU3 API from NHS Digital — 32 operation(s) for stu3.
  name: NHS Digital STU3 API
  slug: nhs-digital-stu3-api
artifact_total: 31
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nhs-digital-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nhs-digital-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nhs-digital-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nhs-digital-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: https://digital.nhs.uk/developer/api-catalogue
- group: operate
  title: ''
  type: RateLimits
  url: https://digital.nhs.uk/developer/guides-and-documentation
- group: auth
  title: ''
  type: Authentication
  url: https://digital.nhs.uk/developer/guides-and-documentation/security-and-authorisation
- group: start
  title: ''
  type: GettingStarted
  url: https://digital.nhs.uk/developer/guides-and-documentation/onboarding-process
- group: start
  title: ''
  type: digital-onboarding
  url: https://digital.nhs.uk/developer/guides-and-documentation/digital-onboarding
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.api.service.nhs.uk
- group: start
  title: ''
  type: DeveloperPortal
  url: https://digital.nhs.uk/developer
- group: other
  title: ''
  type: api-catalogue
  url: https://digital.nhs.uk/developer/api-catalogue
- group: operate
  title: ''
  type: help
  url: https://digital.nhs.uk/developer/help-and-support
- group: operate
  title: ''
  type: developer-community
  url: https://developer.community.nhs.uk
- group: build
  title: ''
  type: github
  url: https://github.com/NHSDigital
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onboarding.prod.api.platform.nhs.uk/PolicyPages/TermsOfUsePolicy
- group: other
  title: ''
  type: api-platform
  url: https://digital.nhs.uk/services/api-platform
description: NHS England Digital is the national provider of digital health technology for the NHS in England. It delivers a comprehensive suite of REST and FHIR APIs covering patient demographic services, personal demographics, electronic prescriptions, summary care records, referrals and bookings, GP Connect, vaccination records, and national clinical data services. APIs are hosted on the NHS API platform at api.service.nhs.uk with sandbox and production environments, supporting OAuth 2.0 / private-key JWT, NHS CIS2 Care Identity, NHS login, and API-key authentication patterns.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://digital.nhs.uk/binaries/content/gallery/website/about-nhs-digital/nhs-digital-og.png
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: NHS Digital
nav: Providers
network: true
overview: 'NHS Digital publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Booking API, communication API, Message API, and 5 more. Tagged areas include NHS, health, FHIR, UK, and patient demographics.


  The NHS Digital catalog on APIs.io includes 1 JSON-LD context.


  NHS Digital''s developer surface includes authentication, getting-started guide, sandbox, GitHub presence, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 68
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 39.8
  delta: -4.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.2
    developer_ergonomics: 37.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 33.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nhs Digital Authentication
  slug: nhs-digital-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nhs Digital Domain Security
  slug: nhs-digital-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Nhs Digital Vulnerability Disclosure
  slug: nhs-digital-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: nhs-digital
tags:
- NHS
- health
- FHIR
- UK
- patient demographics
- prescriptions
- referrals
- clinical data
- digital health
- government
website: https://digital.nhs.uk/developer
---
