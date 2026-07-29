---
access_model:
  confidence: high
  label: Partner-only PMS integrations · no public developer API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - review
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/healthengine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthengine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://healthengine.com.au/
- group: company
  title: ''
  type: About
  url: https://about.healthengine.com.au/
- group: start
  title: ''
  type: Portal
  url: https://practices.healthengine.com.au/
- group: company
  title: ''
  type: Blog
  url: https://practices.healthengine.com.au/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/healthengine
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://healthengine.com.au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://healthengine.com.au/terms
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/healthengine-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/healthengine-well-known.yml
- group: auth
  title: ''
  type: Security
  url: security/healthengine-vulnerability-disclosure.yml
created: '2026-07-24'
description: HealthEngine is Australia's largest consumer healthcare marketplace and patient-engagement platform, founded in 2006 and headquartered in Perth, Western Australia. Its consumer app and website let millions of Australians search a national directory of primary-care providers and book, manage, and attend appointments (including telehealth) across GP, dental, allied-health, and specialist practices. For practices, HealthEngine sells a SaaS suite - GP Complete, Patient Connect, Online Booking, Appointment Reminders and Recalls, Featured Listings, online payments, patient reviews, and Scripts - that plugs into the practice's existing software. It maintains private, real-time integrations into 25+ Australian practice management systems (Best Practice / Bp Premier, MedicalDirector Pracsoft, Zedmed, Cliniko, Genie, Gentu, Medtech, Nookal, PracSuite, Dental4Windows, and others) so appointment availability and bookings sync directly with the front desk. Home market is Australia. HealthEngine
  does NOT publish a public developer portal, REST OpenAPI, or HL7 FHIR endpoint - its API surface is a set of gated, partner-only PMS integrations rather than a self-serve developer program, so this profile is an honest identity stub with no public machine-readable contract to harvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: HealthEngine
nav: Providers
network: true
overview: 'HealthEngine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Australia, Patient Engagement, and Appointment Booking.


  HealthEngine''s developer surface includes developer portal, engineering blog, and 10 more developer resources.'
random_paper: 45
score:
  band: emerging
  composite: 15.5
  delta: -3.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthengine/refs/heads/main/screenshots/healthengine-2026-07-25T220836.png
security:
- kind: domain-security
  name: Healthengine Domain Security
  slug: healthengine-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Healthengine Vulnerability Disclosure
  slug: healthengine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: healthengine
tags:
- Company
- Healthcare
- Australia
- Patient Engagement
- Appointment Booking
- Scheduling
- Telehealth
- Practice Management
- Digital Health
- Healthcare Marketplace
- Interoperability
website: https://healthengine.com.au/
---
