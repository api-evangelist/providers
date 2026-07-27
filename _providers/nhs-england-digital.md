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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: The NHS England API platform hosts a catalogue of national APIs for health and care, including FHIR and REST APIs covering patient demographics, prescriptions, appointments, records, screening, and cl
  name: NHS England API Platform
  slug: api-platform
- description: The Personal Demographics Service is the national electronic database of NHS patient demographic details such as name, address, date of birth and NHS Number. The PDS FHIR API allows authorised systems
  name: Personal Demographics Service (PDS) FHIR API
  slug: personal-demographics-service
- description: The Electronic Prescription Service enables prescribers to send prescriptions electronically to a dispenser of the patient's choice. The EPS FHIR API allows clinical systems to create, retrieve, relea
  name: Electronic Prescription Service (EPS) FHIR API
  slug: electronic-prescription-service
- description: The NHS e-Referral Service combines electronic booking with a choice of place, date and time for first hospital or clinic appointments. The e-RS FHIR API enables clinical systems to integrate referral
  name: e-Referral Service (e-RS) FHIR API
  slug: e-referral-service
- description: The Summary Care Record holds essential patient information from the GP record. The SCR API enables authorised health and care professionals to retrieve a patient's medication, allergies and adverse r
  name: Summary Care Record (SCR) API
  slug: summary-care-record
- description: GP Connect APIs allow authorised clinical systems to view and book GP services. The APIs provide structured access to GP records including medications, allergies, immunisations, observations, problems
  name: GP Connect API
  slug: gp-connect
- description: NHS login provides a single, secure way for citizens to access NHS digital services. The NHS login API enables relying parties to authenticate users, verify identity to a known level of assurance, and
  name: NHS Login API
  slug: nhs-login
artifact_total: 23
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nhs-england-digital-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nhs-england-digital-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nhs-digital
- group: company
  title: ''
  type: Website
  url: https://digital.nhs.uk
- group: docs
  title: ''
  type: Documentation
  url: https://digital.nhs.uk/developer
- group: docs
  title: ''
  type: APIReference
  url: https://digital.nhs.uk/developer/api-catalogue
- group: start
  title: ''
  type: GettingStarted
  url: https://digital.nhs.uk/developer/guides-and-documentation
- group: company
  title: ''
  type: Blog
  url: https://digital.nhs.uk/blog
- group: company
  title: ''
  type: News
  url: https://digital.nhs.uk/news
- group: operate
  title: ''
  type: Support
  url: https://digital.nhs.uk/about-nhs-digital/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.digital.nhs.uk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NHSDigital
- group: commercial
  title: ''
  type: TermsOfService
  url: https://digital.nhs.uk/about-nhs-digital/terms-and-conditions
- group: commercial
  title: ''
  type: Privacy
  url: https://digital.nhs.uk/about-nhs-digital/privacy-and-cookies
- group: other
  title: ''
  type: X
  url: https://x.com/NHSEngland
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/NHSDigital
created: '2025-03-01'
description: NHS England (incorporating the former NHS Digital and NHSX) provides national digital, data, and technology services for the NHS in England. The organization operates the Spine, the Personal Demographics Service, the Electronic Prescription Service, the Summary Care Record, e-Referral Service, NHS App, NHS.uk, and an extensive API platform of FHIR and REST APIs used by health and care providers, developers, and researchers across England.
features:
- description: HL7 FHIR-based APIs for patient records, prescriptions, referrals, and clinical data exchange.
  name: National FHIR APIs
- description: Free, anonymous sandbox endpoints for testing API integrations before production access.
  name: Sandbox Environments
- description: Production authentication via OAuth 2.0 user-restricted access and application-restricted signed JWT.
  name: OAuth 2.0 and Signed JWT
- description: Structured onboarding pathway from sandbox to integration test to production via Apigee developer portal.
  name: Developer Onboarding
- description: Citizen-facing OpenID Connect identity provider for NHS digital services.
  name: NHS Login Identity Provider
- description: National secure messaging and data backbone underlying the major NHS APIs.
  name: Spine Connectivity
finops:
- name: Nhs England Digital Finops
  service_category: API
  slug: nhs-england-digital-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nhs-england-digital.png
layout: provider
modified: '2026-04-28'
name: NHS England Digital
nav: Providers
network: true
overview: 'NHS England Digital publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Clinical, Demographics, FHIR, Government, and Health.


  NHS England Digital''s developer surface includes documentation, API reference, getting-started guide, engineering blog, product news, support, privacy policy, and 9 more developer resources.'
plans:
- name: Nhs England Digital Plans Pricing
  plan_count: 3
  slug: nhs-england-digital-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 5
  name: Nhs England Digital Rate Limits
  slug: nhs-england-digital-rate-limits
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 35.6
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 43.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Nhs England Digital Domain Security
  slug: nhs-england-digital-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Nhs England Digital Vulnerability Disclosure
  slug: nhs-england-digital-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: nhs-england-digital
tags:
- Clinical
- Demographics
- FHIR
- Government
- Health
- Healthcare
- NHS
- Open Data
- Patient Records
- Prescriptions
- UK
use_cases:
- description: Integrate EHR and clinical systems with national patient demographics, prescriptions, and records.
  name: Clinical System Integration
- description: Build apps that authenticate citizens with NHS login and surface their NHS data.
  name: Citizen-Facing Apps
- description: Receive, release, dispense, and claim electronic prescriptions through the EPS API.
  name: Pharmacy Workflow
- description: Integrate appointment booking and referral workflows via the e-Referral Service.
  name: Referral Management
- description: View structured GP record data across federated systems via GP Connect.
  name: GP Record Access
website: https://digital.nhs.uk
---
