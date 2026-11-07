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
  href: https://artifacts.apis.io/zup/well-known/zup-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zup-www-security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://zup.com.br/security/
- group: agent
  href: https://artifacts.apis.io/zup/llms/zup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zup-llms.txt
- group: agent
  href: https://artifacts.apis.io/zup/well-known/zup-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zup-well-known.yml
- group: other
  href: https://artifacts.apis.io/zup/hosts/zup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zup-hosts.yml
- group: other
  href: https://artifacts.apis.io/zup/vendors/zup-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zup-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZupIT
- group: operate
  title: ''
  type: ChangeLog
  url: https://zup.com.br/releases/
- group: auth
  href: https://artifacts.apis.io/zup/security/zup-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zup-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zup/security/zup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zup.com.br/
- group: company
  title: ''
  type: Blog
  url: https://zup.com.br/blog/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://zup.com.br/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: ZUP Innovation is a Brazilian technology company that provides digital transformation solutions, focusing on software development, cloud services, and automation. It helps enterprises modernize their processes, build custom applications, and adopt innovative platforms to stay competitive in a fast‑changing market. The firm emphasizes agile methodologies, AI integration, and end‑to‑end delivery, serving clients across various industries such as finance, retail, and manufacturing.
image: https://zupinnovation.com/wp-content/uploads/2021/03/zup-logo-1-e1626185300293.jpg
layout: provider
modified: '2026-10-21'
name: ZUP INNOVATION
nav: Providers
network: true
overview: 'ZUP INNOVATION is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Digital Transformation, Software Development, and Cloud Services.


  ZUP INNOVATION''s developer surface includes changelog, engineering blog, and 10 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 8.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zup Domain Security
  slug: zup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zup Trust Center
  slug: zup-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: zup
tags:
- Company
- Technology
- Digital Transformation
- Software Development
- Cloud Services
website: https://zup.com.br/
---
