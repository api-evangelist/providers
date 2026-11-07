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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cloudnc.com/
- group: agent
  href: https://artifacts.apis.io/cloudnc/well-known/cloudnc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudnc-well-known.yml
- group: other
  href: https://artifacts.apis.io/cloudnc/hosts/cloudnc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudnc-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloudnc/vendors/cloudnc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudnc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudnc.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.cloudnc.com/help-center
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudnc.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.cloudnc.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.cloudnc.com/blog
- group: auth
  href: https://artifacts.apis.io/cloudnc/security/cloudnc-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cloudnc-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cloudnc/security/cloudnc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudnc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudnc.com
coverage:
  checked: '2026-10-09'
  detail: CloudNC's website provides product information but no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.cloudnc.com
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CloudNC is a London‑based technology company founded in 2015 that builds AI‑driven CAM (Computer‑Aided Manufacturing) software to automate CNC machining programming. Its platform integrates with major CAM packages to generate toolpaths, reduce programming time and increase factory output. Backed by investors such as Atomico and Episode 1 Ventures, CloudNC offers a suite of AI CAM Assist products for Fusion, Mastercam, Siemens NX, GibbsCAM, SolidCAM, Creo and more, targeting manufacturers seeking faster, more efficient machining workflows.
image: https://cdn.prod.website-files.com/64246cfb160f6643a8080605/6a632158a30beefe75ab9aa7_6656f3da159b8b0d7656ada5_Cover%20(1).png
layout: provider
modified: '2026-10-09'
name: CloudNC
nav: Providers
network: true
overview: 'CloudNC is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Manufacturing, CAM, and Automation.


  CloudNC''s developer surface includes support, pricing, engineering blog, and 9 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 13.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cloudnc/cloudnc-2026-11-03T124533.png
security:
- kind: domain-security
  name: Cloudnc Domain Security
  slug: cloudnc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cloudnc Trust Center
  slug: cloudnc-trust-center
  summary_line: SOC 2, ISO 27001
slug: cloudnc
tags:
- Company
- Artificial Intelligence
- Manufacturing
- CAM
- Automation
website: https://www.cloudnc.com
---
