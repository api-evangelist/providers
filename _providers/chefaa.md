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
artifact_total: 2
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chefaa-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/chefaa-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chefaa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://chefaa.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chefaa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chefaa.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chefaa.com/eg-en/become-partner-pharmacy
- group: company
  title: ''
  type: Blog
  url: https://chefaa.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://chefaa.com/eg-en/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chefaa.com/eg-en/page/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chefaa.com/eg-en/page/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://chefaa.com/eg-en
created: '2026-07-17'
description: Chefaa is Egypt's leading digital pharmacy and pharmacy-benefits platform, founded in 2017 and headquartered in Cairo. Its GPS-enabled, AI-powered consumer app connects more than 1.5 million monthly users with a nationwide network of over 1,500 partner pharmacies, letting patients upload, order, schedule, and refill both insured and non-insured prescriptions with home delivery, medication reminders, and pharmacist chat support. On the B2B side Chefaa operates a full-stack supply layer for pharmacies and corporates — including Chefaa Supply (direct procurement with deferred payment and consolidated delivery) and the Makhazen pharmacy-supply app — plus the Chefaa Prime subscription for SMEs and consumers. Chefaa is a 500 Global portfolio company. This profile is maintained by the API Evangelist network; Chefaa publishes consumer and B2B web/mobile products but does not expose a public developer API program, so the enrichment below is limited to its public web, security, and domain
  surface.
image: https://chefaa.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Chefaa
nav: Providers
network: true
overview: 'Chefaa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmacy, Healthcare, Digital Health, and Pharmacy Benefits.


  Chefaa''s developer surface includes engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
    - middle-east
  previous_composite: 16.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chefaa/refs/heads/main/screenshots/chefaa-2026-07-25T205140.png
security:
- kind: domain-security
  name: Chefaa Domain Security
  slug: chefaa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chefaa Vulnerability Disclosure
  slug: chefaa-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chefaa
tags:
- Company
- Pharmacy
- Healthcare
- Digital Health
- Pharmacy Benefits
- E-Commerce
- Delivery
- Egypt
- Middle East
website: https://chefaa.com
---
