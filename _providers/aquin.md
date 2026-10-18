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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquin/refs/heads/main/hosts/aquin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquin-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquin/refs/heads/main/vendors/aquin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aquin-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aquin/refs/heads/main/packages/aquin-packages.yml
  title: ''
  type: SDKs
  url: packages/aquin-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aquin/refs/heads/main/packages/aquin-packages.yml
  title: ''
  type: Packages
  url: packages/aquin-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.aquin.app/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AquinF03
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aquin/refs/heads/main/security/aquin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aquin.app/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aquin.app/aq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aquin.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aquin.app/privacy-policy
- group: commercial
  title: ''
  type: License
  url: https://www.aquin.app/license
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.aquin.app/acceptable-use-policy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.aquin.app/security-policy
- group: company
  title: ''
  type: Careers
  url: https://www.aquin.app/careers
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://aquin.app/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Aquin Labs provides a developer environment for foundation models, offering libraries, frameworks, and tools to build, train, and interpret large AI models. Their platform supports applied machine learning across physics, life sciences, industrial and frontier verticals, emphasizing safety, precision, and open-source tooling. Backed by programs like Emergent Ventures, NVIDIA Inception, and Founders Inc, Aquin aims to accelerate ML development with reproducible, responsible AI workflows.
image: https://www.aquin.app/logo.png
layout: provider
modified: '2026-10-16'
name: Aquin
nav: Providers
network: true
overview: 'Aquin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine Learning, Foundation Models, Open Source, and Research.


  Aquin''s developer surface includes documentation and 14 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aquin Domain Security
  slug: aquin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aquin
tags:
- Artificial Intelligence
- Machine Learning
- Foundation Models
- Open Source
- Research
website: https://aquin.app/
---
