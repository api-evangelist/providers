---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
- group: commercial
  href: https://artifacts.apis.io/deepdyve/plans/deepdyve-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/deepdyve-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/deepdyve/hosts/deepdyve-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepdyve-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepdyve/vendors/deepdyve-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepdyve-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.deepdyve.com/category/7-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.deepdyve.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepdyve
- group: auth
  href: https://artifacts.apis.io/deepdyve/security/deepdyve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepdyve-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deepdyve.com
created: '2026-10-22'
description: DeepDyve provides a literature management platform that offers AI‑powered search, reference management, and full‑text access to millions of research papers and ebooks. Users can discover, annotate, and cite scholarly content, integrate with tools like PubMed and Google Scholar, and collaborate via shared libraries. Pricing starts under $2 per day, targeting individuals and businesses seeking affordable, comprehensive research solutions.
layout: provider
modified: '2026-10-22'
name: Deepdyve
nav: Providers
network: true
overview: 'Deepdyve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Literature, Research, Artificial Intelligence, and Software-as-a-Service.


  Deepdyve''s developer surface includes getting-started guide, documentation, and 6 more developer resources.'
plans:
- name: Deepdyve Plans Pricing
  plan_count: 2
  slug: deepdyve-plans-pricing
random_paper: 14
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 44.6
    operational_transparency: 2.6
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/deepdyve/deepdyve-2026-11-03T130434.png
security:
- kind: domain-security
  name: Deepdyve Domain Security
  slug: deepdyve-domain-security
  summary_line: TLSv1.3 · DMARC
slug: deepdyve
tags:
- Company
- Literature
- Research
- Artificial Intelligence
- Software-as-a-Service
website: https://www.deepdyve.com
---
