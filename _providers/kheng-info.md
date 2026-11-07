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
  href: https://artifacts.apis.io/kheng-info/hosts/kheng-info-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kheng-info-hosts.yml
- group: auth
  href: https://artifacts.apis.io/kheng-info/security/kheng-info-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kheng-info-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kheng.info/
- group: company
  title: ''
  type: About
  url: https://kheng.info/about/
coverage:
  checked: '2026-10-28'
  detail: The site provides no API documentation or developer program.
  evidence:
  - status: 200
    url: https://kheng.info/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Kheng.info provides an online tool for Khmer word segmentation and annotation. It accepts Khmer text input and returns a clickable document where each word is segmented, defined, and linked to audio recordings. The service helps language learners and researchers explore Khmer language structure, offering definitions, pronunciations, and linguistic data for each token in the submitted text.
image: https://kheng.info/static/kheng_info/css/img/favicon.ico
layout: provider
modified: '2026-10-28'
name: Kheng.info
nav: Providers
network: true
overview: Kheng.info is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Language, Natural Language Processing, Khmer, and Tool.
random_paper: 14
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
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
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 3.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kheng-info/kheng-info-2026-11-03T134404.png
security:
- kind: domain-security
  name: Kheng Info Domain Security
  slug: kheng-info-domain-security
  summary_line: TLSv1.2
slug: kheng-info
tags:
- Company
- Language
- Natural Language Processing
- Khmer
- Tool
website: https://kheng.info/
---
