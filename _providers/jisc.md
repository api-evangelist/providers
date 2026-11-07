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
api_count: 1
apis:
- description: Documentation guides for Jisc services
  name: Jisc Guides API
  slug: jisc-guides-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/jisc/security/jisc-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/jisc-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/jisc/hosts/jisc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jisc-hosts.yml
- group: other
  href: https://artifacts.apis.io/jisc/vendors/jisc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jisc-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jisc.ac.uk/website/privacy-notice
- group: docs
  title: ''
  type: Documentation
  url: https://www.jisc.ac.uk/guides
- group: company
  title: ''
  type: Blog
  url: https://www.jisc.ac.uk/blog/do-you-really-know-how-secure-your-organisation-is
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Jisc
- group: auth
  href: https://artifacts.apis.io/jisc/security/jisc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jisc-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jisc/security/jisc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jisc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jisc.ac.uk/
coverage:
  checked: '2026-10-13'
  detail: Jisc provides documentation guides but no machine‑readable API specifications were found.
  evidence:
  - status: 200
    url: https://www.jisc.ac.uk/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Jisc is the UK’s digital services and technology agency for education and research. It provides digital solutions, advice, and support to further learning, teaching, and research across the United Kingdom. Jisc offers services ranging from cloud consultancy, connectivity, cyber‑security, data analytics, digital learning resources, and licensed content, helping institutions innovate and improve outcomes for students and researchers.
layout: provider
modified: '2026-10-13'
name: Jisc
nav: Providers
network: true
overview: 'Jisc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Technology, Digital Services, Research, and United Kingdom.


  Jisc''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 53.6
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 11.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jisc/jisc-2026-11-03T134146.png
security:
- kind: domain-security
  name: Jisc Domain Security
  slug: jisc-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Jisc Vulnerability Disclosure
  slug: jisc-vulnerability-disclosure
  summary_line: no policy recorded
slug: jisc
tags:
- Education
- Technology
- Digital Services
- Research
- United Kingdom
website: https://www.jisc.ac.uk/
---
