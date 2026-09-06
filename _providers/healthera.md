---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthera-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthera-llms.txt
- group: company
  title: ''
  type: Website
  url: https://healthera.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://healthera.co.uk/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://healthera.co.uk/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://healthera.co.uk/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/healthera
- group: commercial
  title: ''
  type: TermsOfService
  url: https://healthera.co.uk/pharmacy-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://healthera.co.uk/privacy
- group: other
  title: ''
  type: Cookies
  url: https://healthera.co.uk/cookies
created: '2026-07-24'
description: Healthera is a United Kingdom digital-health and patient-engagement company, founded in 2015 by Cambridge University students and headquartered in Cambridge, England. It runs a patient-facing pharmacy app and website for ordering NHS prescriptions and medicines online and booking pharmacy services (Pharmacy First, treatments, vaccinations), alongside a pharmacy-facing SaaS "Patient Experience Platform" used by 1,700+ community pharmacies to manage repeat prescriptions, bookings, marketing, and delivery. In November 2022 Healthera became the first pharmacy app to integrate with the NHS Electronic Prescription Service (EPS), and it connects to NHS Digital / NHS England systems plus third-party platforms such as myGP, eConsult, Cegedim Rx Pharmacy Manager, Medpoint, Royal Mail, and Uber for same-hour delivery. Healthera markets custom integration APIs to pharmacy and brand partners, but as of this review it publishes no public developer portal, no self-serve API documentation,
  and no machine-readable contract; its api.healthera.co.uk "Healthera Core" host is a private backend and exposes no FHIR CapabilityStatement. Integration is partner-gated rather than self-serve.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Healthera
nav: Providers
network: true
overview: 'Healthera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United Kingdom, Pharmacy, Patient Engagement, and e-Prescribing.


  Healthera''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 11.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthera/refs/heads/main/screenshots/healthera-2026-07-25T220840.png
security:
- kind: domain-security
  name: Healthera Domain Security
  slug: healthera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: healthera
tags:
- Healthcare
- United Kingdom
- Pharmacy
- Patient Engagement
- e-Prescribing
- NHS
- Electronic Prescription Service
- Digital Health
- Telehealth
website: https://healthera.co.uk/
---
