---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  url: security/ultralight-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ultralight-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.ultralighthealth.com/platform
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ultralight-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ultralighthealth.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ultralighthealth.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ultralighthealth.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ultralighthealth.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.ultralighthealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ultralighthealth.com/resources
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vibrantpractice/
created: '2026-07-17'
description: Ultralight is an AI-native electronic health record (EHR) and operating system for functional, integrative, and longevity medicine practices. The platform brings clinical data, workflows, and intelligence into a single system, synthesizing wearable data, longitudinal symptoms, labs, and treatment history with a built-in, clinician-reviewed clinical intelligence layer, alongside a consumer-grade patient app, automated workflows, and HIPAA-compliant infrastructure. Ultralight is headquartered in San Francisco and backed by Anthemis through its Female Innovators Lab. The company publishes no public developer or API surface today.
image: https://cdn.prod.website-files.com/6995e2fab9583dcbfef5676c/69a1b5d7465a1b66aa29e040_favicon-256.png
layout: provider
modified: '2026-07-21'
name: Ultralight
nav: Providers
network: true
overview: 'Ultralight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, EHR, Artificial Intelligence, and Functional Medicine.


  Ultralight''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ultralight/refs/heads/main/screenshots/ultralight-2026-09-02T164832.png
security:
- kind: domain-security
  name: Ultralight Domain Security
  slug: ultralight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ultralight
tags:
- Company
- Healthcare
- EHR
- Artificial Intelligence
- Functional Medicine
- Integrative Medicine
- Longevity Medicine
- Clinical Intelligence
- Patient Experience
website: https://www.ultralighthealth.com/
---
