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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/careerbhavan-com/security/careerbhavan-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/careerbhavan-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/careerbhavan-com/llms/careerbhavan-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/careerbhavan-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/careerbhavan-com/well-known/careerbhavan-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/careerbhavan-com-security.txt
- group: auth
  href: https://artifacts.apis.io/careerbhavan-com/well-known/careerbhavan-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/careerbhavan-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/careerbhavan-com/well-known/careerbhavan-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/careerbhavan-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/careerbhavan-com/hosts/careerbhavan-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/careerbhavan-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/careerbhavan-com/vendors/careerbhavan-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/careerbhavan-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://careerbhavan.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://careerbhavan.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://careerbhavan.com/nirf-ranking/management
- group: company
  title: ''
  type: Blog
  url: https://careerbhavan.com/blog
- group: auth
  href: https://artifacts.apis.io/careerbhavan-com/security/careerbhavan-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/careerbhavan-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/careerbhavan-com/security/careerbhavan-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/careerbhavan-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://careerbhavan.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://careerbhavan.com/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Looking for admission consultants near you? Career Bhavan provides university admission consulting services, application support, and higher education guidance. We assist students with university admissions, application support, and higher education counseling across India, offering expert guidance to secure admissions to top institutions.
image: https://careerbhavan.com/assets/og-image.webp
layout: provider
modified: '2026-11-03'
name: Career Bhavan
nav: Providers
network: true
overview: 'Career Bhavan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Admissions, Consulting, India, and Careers.


  Career Bhavan''s developer surface includes engineering blog and 13 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Careerbhavan Com Domain Security
  slug: careerbhavan-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Careerbhavan Com Vulnerability Disclosure
  slug: careerbhavan-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: careerbhavan-com
tags:
- Education
- Admissions
- Consulting
- India
- Careers
website: https://careerbhavan.com/
---
