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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/youdao/well-known/youdao-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/youdao-well-known.yml
- group: other
  href: https://artifacts.apis.io/youdao/hosts/youdao-hosts.yml
  title: ''
  type: Hosts
  url: hosts/youdao-hosts.yml
- group: build
  href: https://artifacts.apis.io/youdao/packages/youdao-packages.yml
  title: ''
  type: SDKs
  url: packages/youdao-packages.yml
- group: build
  href: https://artifacts.apis.io/youdao/packages/youdao-packages.yml
  title: ''
  type: Packages
  url: packages/youdao-packages.yml
- group: auth
  href: https://artifacts.apis.io/youdao/security/youdao-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/youdao-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://youdao.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://youdao.com/
  reason: no-developer-program
  state: none
created: '2026-10-27'
description: NetEase Youdao, a leading Chinese intelligent learning company, offers a suite of language and education services including the popular Youdao Dictionary, translation tools, premium courses, cloud note‑taking, AI hardware, and enterprise education platforms. Founded in 2006, it has expanded into AI‑driven learning products and went public on the NYSE in 2019, positioning itself as a key player in digital education and language technology.
image: https://ydlunacommon-cdn.nosdn.127.net/cb776e6995f1c703706cf8c4c39a7520.png
layout: provider
modified: '2026-10-27'
name: NetEase Youdao
nav: Providers
network: true
overview: NetEase Youdao is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Language, Artificial Intelligence, and Cloud.
random_paper: 9
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/youdao/youdao-2026-11-03T150442.png
security:
- kind: domain-security
  name: Youdao Domain Security
  slug: youdao-domain-security
  summary_line: TLSv1.3
slug: youdao
tags:
- Company
- Education
- Language
- Artificial Intelligence
- Cloud
- Enterprise
website: https://youdao.com/
---
