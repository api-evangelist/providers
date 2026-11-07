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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/shaip/llms/shaip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shaip-llms.txt
- group: agent
  href: https://artifacts.apis.io/shaip/well-known/shaip-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shaip-well-known.yml
- group: other
  href: https://artifacts.apis.io/shaip/hosts/shaip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shaip-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shaip.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shaip.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/shaip/security/shaip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shaip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shaip.com/
- group: company
  title: ''
  type: Blog
  url: https://www.shaip.com/blog/
coverage:
  checked: '2026-10-21'
  detail: Shaip does not provide a public developer program or API documentation.
  evidence:
  - status: 301
    url: https://www.shaip.com/api-docs/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Shaip provides a data platform for AI and machine learning, offering services such as data collection, annotation, labeling, and model evaluation. Their solutions help enterprises build high‑quality training datasets, accelerate AI development, and ensure data security and compliance across industries. Shaip’s platform supports custom workflows, expert review, and scalable pipelines for both image and text data, catering to sectors like healthcare, automotive, and finance.
image: https://c0a6be58.delivery.rocketcdn.me/wp-content/uploads/2024/12/Homepage_SM.jpg
layout: provider
modified: '2026-10-21'
name: Shaip
nav: Providers
network: true
overview: 'Shaip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data Annotation, Machine Learning, and Platform.


  Shaip''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shaip/shaip-2026-11-03T143106.png
security:
- kind: domain-security
  name: Shaip Domain Security
  slug: shaip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shaip
tags:
- Company
- Artificial Intelligence
- Data Annotation
- Machine Learning
- Platform
website: https://www.shaip.com/
---
