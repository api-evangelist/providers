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
api_count: 1
apis:
- description: Partner order-booking API used by Thyrocare's DSA (Direct Selling Agent) franchise network for booking diagnostic tests and retrieving reports. A Swashbuckle (.NET) Swagger UI is publicly reachable, b
  name: Thyrocare TechSo Partner API (BTS)
  slug: thyrocare-techso-partner-api-bts
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thyrocare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thyrocare.com
- group: operate
  title: ''
  type: Support
  url: https://thyrocare.freshdesk.com/support/solutions
- group: start
  title: ''
  type: Login
  url: https://client.thyrocare.com/
- group: start
  title: ''
  type: SignUp
  url: https://lead.thyrocare.com/dsa-affiliate/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://b2capi.thyrocare.com/privacy_policy.html
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thyrocare-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thyrocare-llms.txt
created: '2026-07-17'
description: Thyrocare Technologies Limited is an Indian chain of diagnostic and preventive-care laboratories headquartered in Navi Mumbai, founded in 1996. Built around a centralized, highly automated laboratory model, it focuses on affordable preventive health checkups, thyroid and pathology testing, and sells through a nationwide network of DSA (Direct Selling Agent) franchise partners. Norwest Venture Partners invested pre-IPO, and PharmEasy (API Holdings) acquired a majority stake in 2021. Its partner order-booking API (TechSo/BTS) is gated behind the DSA program and publishes no public OpenAPI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thyrocare.png
layout: provider
modified: '2026-07-21'
name: Thyrocare
nav: Providers
network: true
overview: 'Thyrocare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Diagnostics, Laboratory, and Pathology.


  Thyrocare''s developer surface includes support, signup flow, and 6 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 12.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thyrocare/refs/heads/main/screenshots/thyrocare-2026-09-02T163657.png
security:
- kind: domain-security
  name: Thyrocare Domain Security
  slug: thyrocare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: thyrocare
tags:
- Company
- Healthcare
- Diagnostics
- Laboratory
- Pathology
- Preventive Care
- India
website: https://thyrocare.com
---
