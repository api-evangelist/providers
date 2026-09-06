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
- group: company
  title: ''
  type: Website
  url: https://www.unohealth.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unohealth.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unohealth.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://members.unohealth.com/login
- group: start
  title: ''
  type: SignUp
  url: https://members.unohealth.com/public-eligibility
- group: operate
  title: ''
  type: Support
  url: mailto:info@hiuno.com
- group: company
  title: ''
  type: Careers
  url: https://boards.greenhouse.io/unohealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uno-health/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/uno_health
- group: auth
  title: ''
  type: TrustCenter
  url: security/uno-health-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uno-health-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uno-health-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uno-health-llms.txt
created: '2026-07-17'
description: Uno Health is a New York-based healthcare technology company that helps Medicare members enroll in the government assistance programs they are eligible for — such as SNAP and utility assistance — saving members an average of $4,500 per year. Medicare Advantage health plans partner with Uno's technology-driven member engagement platform to simplify eligibility checks, subsidy enrollment, plan optimization, and benefits matching, increasing Part C revenue, member retention, and star ratings. Members run a 5-minute savings check, upload enrollment documents, and track recurring monthly savings through the Uno Health Member Portal. Backed by Cowboy Ventures and General Catalyst. Uno Health publishes no public developer program; its API (api.unohealth.com, AWS API Gateway) is private and partner-facing.
image: https://cdn.prod.website-files.com/655827fc6ec4f39efa885fd1/65c3a8dab371aebc7d9da316_256.png
layout: provider
modified: '2026-07-21'
name: Uno Health
nav: Providers
network: true
overview: 'Uno Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medicare, Benefits, and Enrollment.


  Uno Health''s developer surface includes signup flow, support, and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uno-health/refs/heads/main/screenshots/uno-health-2026-09-02T164940.png
security:
- kind: domain-security
  name: Uno Health Domain Security
  slug: uno-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Uno Health Trust Center
  slug: uno-health-trust-center
  summary_line: trust center published
slug: uno-health
tags:
- Company
- Healthcare
- Medicare
- Benefits
- Enrollment
- Health Plans
- Government Programs
website: https://www.unohealth.com
---
