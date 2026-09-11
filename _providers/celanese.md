---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-10'
api_count: 1
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Celanese API
  slug: open-celanese
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celanese-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/celanese
- group: company
  title: ''
  type: Website
  url: https://www.celanese.com
- group: other
  title: ''
  type: Digital Assistant
  url: https://materials.celanese.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/celanese-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Celanese
coverage:
  checked: '2026-09-06'
  detail: 'Celanese sells polymers and acetyl chemicals, not software: there is no developer program to find — developer.celanese.com and developers.celanese.com do not resolve, api.celanese.com presents no matching certificate, the real github.com/Celanese organization publishes zero public repositories, seven package registries return zero first-party libraries, and the only digital product (the Chemille material-selection assistant at materials.celanese.com) is a browser app for engineers that ships no API, no llms.txt and no .well-known document.'
  evidence:
  - status: 404
    url: https://www.celanese.com/llms.txt
  - status: 404
    url: https://www.celanese.com/.well-known/security.txt
  - status: 404
    url: https://materials.celanese.com/.well-known/security.txt
  - status: 200
    url: https://api.github.com/orgs/Celanese/repos
  reason: not-a-software-company
  state: none
created: '2024-01-15'
description: Celanese Corporation is a global chemical and specialty materials company that produces high-performance engineered polymers and acetyl products used across automotive, medical, consumer, and industrial applications. Celanese has no publicly documented developer API; digital engagement is delivered through the Chemille digital materials assistant for product search and selection, and a Cognite Data Fusion based manufacturing data platform for internal operations.
finops:
- name: Celanese Finops
  service_category: API
  slug: celanese-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/celanese.png
layout: provider
modified: '2026-09-06'
name: Celanese
nav: Providers
network: true
overview: Celanese publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Chemicals, Engineered Polymers, Materials, Specialty Materials, and Fortune 500.
plans:
- name: Celanese Plans Pricing
  plan_count: 0
  slug: celanese-plans-pricing
press:
- date: '2026-05-25'
  title: Celanese Designing the Future at K 2025
  url: https://www.celanese.com/news-and-media/2025/october/celanese-designing-the-future-at-k-2025
- date: '2026-05-25'
  title: Telecom Polymers
  url: https://www.celanese.com/industries/telecom
- date: '2026-05-25'
  title: Radix and Celanese Partnership Leverages AI to Harness the ...
  url: https://www.radixeng.com/post/radix-and-celanese-partnership-leverages-ai-to-harness-the-power-of-industrial-data
- date: '2026-05-25'
  title: Fourth Quarter 2025 Earnings Prepared Comments
  url: https://www.sec.gov/Archives/edgar/data/1306830/000130683026000017/q420258-kex991a.htm
- date: '2026-05-25'
  title: Celanese's Chemille AI Assistant Revolutionizes Material ...
  url: https://www.linkedin.com/posts/useready_materialsscience-enterpriseai-chemicalindustry-activity-7433474582881259520-V9F8
random_paper: 13
rate_limits:
- limit_count: 0
  name: Celanese Rate Limits
  slug: celanese-rate-limits
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.7
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/celanese/refs/heads/main/screenshots/celanese-2026-06-20T174110.png
security:
- kind: domain-security
  name: Celanese Domain Security
  slug: celanese-domain-security
  summary_line: TLSv1.3 · DMARC
slug: celanese
tags:
- Chemicals
- Engineered Polymers
- Materials
- Specialty Materials
- Fortune 500
website: https://www.celanese.com
---
