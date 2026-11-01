---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/ontaurus-com/hosts/ontaurus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ontaurus-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ontaurus-com/vendors/ontaurus-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ontaurus-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ontaurus-com/security/ontaurus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ontaurus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ontaurus.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ontaurus.com/blog/
coverage:
  checked: '2026-10-24'
  detail: The company website provides no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://www.ontaurus.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Taurus is a technology company specializing in advanced data analytics and cloud-based solutions for enterprise customers. Founded with a focus on delivering scalable, secure, and high-performance platforms, Taurus provides a suite of APIs that enable integration of data pipelines, real-time monitoring, and AI-driven insights. The company emphasizes robust security practices, comprehensive documentation, and developer-friendly tools to accelerate innovation across industries. Backed by General Catalyst, Taurus continues to expand its product offerings and partner ecosystem, aiming to empower businesses to harness the full potential of their data assets.
image: https://ontaurus.com/opengraph-image?e9656b5ee5698778
layout: provider
modified: '2026-10-24'
name: Taurus
nav: Providers
network: true
overview: 'Taurus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, Cloud Services, Enterprise APIs, and Security.


  Taurus'' developer surface includes engineering blog and 4 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ontaurus Com Domain Security
  slug: ontaurus-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ontaurus-com
tags:
- Company
- Data Analytics
- Cloud Services
- Enterprise APIs
- Security
website: https://www.ontaurus.com/
---
