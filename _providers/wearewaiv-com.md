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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/wearewaiv-com/hosts/wearewaiv-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wearewaiv-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/wearewaiv-com/vendors/wearewaiv-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wearewaiv-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://waiv.com/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://waiv.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://waiv.com/news
- group: other
  title: ''
  type: Leadership
  url: https://waiv.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://waiv.com/blog/towards-tumor-agnostic-ihc-ai
- group: auth
  href: https://artifacts.apis.io/wearewaiv-com/security/wearewaiv-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wearewaiv-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waiv.com/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite probing known API hosts.
  evidence:
  - status: 0
    url: https://api.wearewaiv.com/openapi.json
  - status: 0
    url: https://api.waiv.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Waiv is an AI-driven precision testing company focused on digital pathology and oncology. It develops AI biomarkers and companion diagnostics to accelerate clinical trials and co-develop AI tests for biopharma and clinicians. The platform offers products such as RlapsRisk, MSIntuit Suite, BRCAura, and Destra, aiming to turn routine pathology slides into clinical-grade precision tests for cancer patients, improving care through advanced AI models.
image: https://cdn.prod.website-files.com/693aa5958f830a8ecab1c1eb/69aef2dbc9e80a879ba31dc1_open-graph-waiv-home.jpg
layout: provider
modified: '2026-10-29'
name: Waiv
nav: Providers
network: true
overview: 'Waiv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Pathology, Oncology, Diagnostics, and PrecisionMedicine.


  Waiv''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.5
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
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wearewaiv Com Domain Security
  slug: wearewaiv-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wearewaiv-com
tags:
- AI
- Pathology
- Oncology
- Diagnostics
- PrecisionMedicine
- Company
website: https://waiv.com/
---
