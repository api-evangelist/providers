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
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/datumo/refs/heads/main/changelog/datumo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/datumo-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datumo/refs/heads/main/llms/datumo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datumo-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/datumo/refs/heads/main/well-known/datumo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datumo-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datumo/refs/heads/main/hosts/datumo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datumo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/datumo/refs/heads/main/vendors/datumo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datumo-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.datumo.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.datumo.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datumo.com/documentation/readme/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/datumo/refs/heads/main/security/datumo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datumo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datumo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.datumo.com/en/
- group: company
  title: ''
  type: Blog
  url: https://datumo.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://datumo.com/contact_datumo/
- group: commercial
  title: ''
  type: Pricing
  url: https://datumo.com/paid-dataset/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stump-shark-f56.notion.site/DATUMO-Privacy-Policy-7eeb73c3d8044a058dce8e3057a4df2b
coverage:
  checked: '2026-10-16'
  detail: Documentation is served as a JavaScript‑rendered GitBook site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.datumo.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Datumo provides an advanced LLM evaluation platform that offers automated generation of golden question sets, custom metric support, and comprehensive red‑team testing for AI models. Their services include Datumo Eval for model benchmarking, AI Red Team for adversarial analysis, and a dataset store with premium and open datasets for training and evaluation. The platform aims to help developers and researchers improve LLM performance, safety, and reliability through detailed analytics and actionable insights.
image: https://datumo.com/wp-content/uploads/2024/08/back_3.webp
layout: provider
modified: '2026-10-16'
name: Datumo
nav: Providers
network: true
overview: 'Datumo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Evaluation, LLM, and Platform.


  Datumo''s developer surface includes changelog, getting-started guide, documentation, engineering blog, support, pricing, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 55.4
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datumo Domain Security
  slug: datumo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datumo
tags:
- Company
- Artificial Intelligence
- Evaluation
- LLM
- Platform
website: https://datumo.com/
---
