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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pharmeasy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pharmeasy.in/
- group: company
  title: ''
  type: Blog
  url: https://pharmeasy.in/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pharmeasy.in/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pharmeasy.in/legal/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://pharmeasy.in/customer-support-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://pharmeasy.in/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: Security
  url: https://pharmeasy.in/vulnerability-disclosure-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pharmeasy-well-known.yml
created: '2026-07-17'
description: 'PharmEasy is one of India''s largest digital healthcare platforms, operating a consumer online pharmacy and health marketplace at pharmeasy.in. It lets users order prescription and over-the-counter medicines (with prescription upload and verification), buy health and wellness products, book diagnostic lab tests and health checkup packages, and consult doctors via telemedicine, plus a PLUS subscription for recurring savings. Surfaced as a portfolio company of Bessemer Venture Partners and Prosus Ventures and added to the API Evangelist network for enrichment. PharmEasy runs an internal API at api.pharmeasy.in but publishes no public developer program, API documentation, SDKs, or OpenAPI; it does operate a responsible-disclosure security program (infosec@pharmeasy.in). Sector: healthcare / e-pharmacy.'
image: https://pharmeasy.in/pe_logo_2x.png
layout: provider
modified: '2026-07-20'
name: Pharmeasy
nav: Providers
network: true
overview: 'Pharmeasy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Pharmacy, E-Pharmacy, and Diagnostics.


  Pharmeasy''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.0
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pharmeasy/refs/heads/main/screenshots/pharmeasy-2026-09-02T151136.png
security:
- kind: domain-security
  name: Pharmeasy Domain Security
  slug: pharmeasy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pharmeasy Vulnerability Disclosure
  slug: pharmeasy-vulnerability-disclosure
  summary_line: contact published
slug: pharmeasy
tags:
- Company
- Healthcare
- Pharmacy
- E-Pharmacy
- Diagnostics
- Telemedicine
- India
- E-Commerce
website: https://www.pharmeasy.in/
---
