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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://github.com/ukncsc/Vulnerability-Disclosure/blob/master/UK-Government-Vulnerability-Disclosure-Policy.md
- group: auth
  href: https://artifacts.apis.io/aston-university/well-known/aston-university-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aston-university-security.txt
- group: agent
  href: https://artifacts.apis.io/aston-university/well-known/aston-university-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aston-university-well-known.yml
- group: other
  href: https://artifacts.apis.io/aston-university/hosts/aston-university-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aston-university-hosts.yml
- group: other
  href: https://artifacts.apis.io/aston-university/vendors/aston-university-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aston-university-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aston.ac.uk/staff-public/procurement/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.aston.ac.uk/support
- group: start
  title: ''
  type: SignUp
  url: https://www.aston.ac.uk/clearing/guide/parents/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aston.ac.uk/about/statutes-ordinances-regulations/publication-scheme/policies-regulations/data-protection/privacy-notices
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aston.ac.uk/latest-news/plans-new-landmark-building-aston-university-are-approved-birmingham-city-council
- group: company
  title: ''
  type: Newsroom
  url: https://www.aston.ac.uk/sport/news
- group: other
  title: ''
  type: Leadership
  url: https://www.aston.ac.uk/sro/team
- group: auth
  href: https://artifacts.apis.io/aston-university/security/aston-university-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aston-university-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aston-university/security/aston-university-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aston-university-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.aston.ac.uk/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.aston.ac.uk/
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Aston University is a public research university located in Birmingham, United Kingdom. It offers a wide range of undergraduate, postgraduate and research programmes across engineering, business, health, and the arts. The university is known for its strong industry links, innovative teaching methods, and contributions to scientific research. As an educational institution, it provides various digital services and resources for students, staff, and partners, though it does not expose a public API for its core systems.
layout: provider
modified: '2026-10-23'
name: Aston University
nav: Providers
network: true
overview: 'Aston University is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, University, Research, United Kingdom, and Higher Education.


  Aston University''s developer surface includes support, signup flow, pricing, and 12 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aston-university/aston-university-2026-11-03T121228.png
security:
- kind: domain-security
  name: Aston University Domain Security
  slug: aston-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aston University Vulnerability Disclosure
  slug: aston-university-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aston-university
tags:
- Education
- University
- Research
- United Kingdom
- Higher Education
- Public
website: http://www.aston.ac.uk/
---
