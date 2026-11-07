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
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/being-health/conformance/being-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/being-health-conformance.yml
- group: other
  href: https://artifacts.apis.io/being-health/hosts/being-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/being-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/being-health/vendors/being-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/being-health-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.beinghealth.co/press
- group: start
  title: ''
  type: GettingStarted
  url: https://help.beinghealth.co/collection/1-getting-started-at-being-health
- group: docs
  title: ''
  type: Documentation
  url: https://help.beinghealth.co/
- group: auth
  href: https://artifacts.apis.io/being-health/security/being-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/being-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beinghealth.co/
- group: company
  title: ''
  type: Blog
  url: https://www.beinghealth.co/blog
- group: company
  title: ''
  type: About
  url: https://www.beinghealth.co/about
- group: operate
  title: ''
  type: Contact
  url: https://www.beinghealth.co/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beinghealth.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beinghealth.co/privacy-policy
coverage:
  checked: '2026-09-27'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable contract could be retrieved.
  evidence:
  - status: 200
    url: https://www.beinghealth.co/get-started
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Being Health is a modern psychiatry practice that provides psychiatry, Spravato® treatment, psychotherapy, functional medicine and wellness services—all in one place. It offers integrated mental health care with in‑network insurance plans, virtual and in‑person appointments, and a focus on coordinated treatment for conditions such as anxiety, depression, PTSD, and more. Founded in 2023 and based in New York, Being Health aims to improve mental wellbeing through comprehensive, evidence‑based care.
image: https://cdn.prod.website-files.com/64c0d111a0343d5ffc92d3e7/6988c5bf0c0e9fd1888104c1_Screenshot%202026-02-08%20121945.jpg
layout: provider
modified: '2026-09-27'
name: Being Health
nav: Providers
network: true
overview: 'Being Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Psychiatry, Wellness, and Telehealth.


  Being Health''s developer surface includes getting-started guide, documentation, engineering blog, and 10 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 16.6
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/being-health/being-health-2026-10-11T101819.png
security:
- kind: domain-security
  name: Being Health Domain Security
  slug: being-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: being-health
tags:
- Company
- Mental Health
- Psychiatry
- Wellness
- Telehealth
- New York
website: https://www.beinghealth.co/
---
