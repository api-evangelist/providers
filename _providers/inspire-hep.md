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
- group: other
  href: https://artifacts.apis.io/inspire-hep/hosts/inspire-hep-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inspire-hep-hosts.yml
- group: build
  href: https://artifacts.apis.io/inspire-hep/packages/inspire-hep-packages.yml
  title: ''
  type: SDKs
  url: packages/inspire-hep-packages.yml
- group: build
  href: https://artifacts.apis.io/inspire-hep/packages/inspire-hep-packages.yml
  title: ''
  type: Packages
  url: packages/inspire-hep-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inspirehep
- group: auth
  href: https://artifacts.apis.io/inspire-hep/security/inspire-hep-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inspire-hep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inspirehep.net
- group: docs
  title: ''
  type: Documentation
  url: https://help.inspirehep.net
- group: docs
  title: ''
  type: APIReference
  url: https://help.inspirehep.net/knowledge-base/about-inspire
- group: company
  title: ''
  type: Blog
  url: https://blog.inspirehep.net
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.inspirehep.net/knowledge-base/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.inspirehep.net/knowledge-base/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.inspirehep.net/knowledge-base/contact-us
coverage:
  checked: '2026-10-14'
  detail: The main site https://inspirehep.net serves a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://inspirehep.net
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: INSPIRE HEP is a community-driven portal for high‑energy physics literature, data, and author information. It provides searchable access to millions of records, including papers, authors, conferences, jobs, and datasets, supporting researchers worldwide. The platform offers APIs for programmatic access to its rich metadata, enabling integration with scholarly tools and services.
layout: provider
modified: '2026-10-14'
name: INSPIRE HEP
nav: Providers
network: true
overview: 'INSPIRE HEP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HighEnergyPhysics, Research, Data, and Open Science.


  INSPIRE HEP''s developer surface includes documentation, API reference, engineering blog, support, and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 2.6
  previous_composite: 15.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/inspire-hep/inspire-hep-2026-11-03T133852.png
security:
- kind: domain-security
  name: Inspire Hep Domain Security
  slug: inspire-hep-domain-security
  summary_line: TLSv1.3
slug: inspire-hep
tags:
- Company
- HighEnergyPhysics
- Research
- Data
- Open Science
website: https://inspirehep.net
---
