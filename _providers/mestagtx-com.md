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
  href: https://artifacts.apis.io/mestagtx-com/hosts/mestagtx-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mestagtx-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/mestagtx-com/vendors/mestagtx-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mestagtx-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mestagtherapeutics.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.mestagtherapeutics.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mestagtx
- group: auth
  href: https://artifacts.apis.io/mestagtx-com/security/mestagtx-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mestagtx-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mestagtherapeutics.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://mestagtx.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Mestag Therapeutics is a biotechnology company focused on developing bispecific antibody therapeutics that harness fibroblast‑immune interactions to treat cancer and inflammatory diseases. Their pipeline includes MST‑0312, a bispecific antibody targeting tertiary lymphoid structures, and M402, an agonist antibody for stromal inhibition. The firm aims to advance novel immunotherapies from preclinical through clinical trials, addressing unmet needs in oncology and autoimmune conditions.
image: https://www.mestagtherapeutics.com/wp-content/uploads/2022/12/yoast-metstag-logo.jpg
layout: provider
modified: '2026-10-22'
name: Mestag Therapeutics
nav: Providers
network: true
overview: Mestag Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Immunotherapy, Oncology, Autoimmune, and Antibodies.
random_paper: 17
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mestagtx Com Domain Security
  slug: mestagtx-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mestagtx-com
tags:
- Biotechnology
- Immunotherapy
- Oncology
- Autoimmune
- Antibodies
- Company
website: https://www.mestagtherapeutics.com
---
