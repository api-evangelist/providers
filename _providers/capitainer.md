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
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/capitainer/well-known/capitainer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/capitainer-well-known.yml
- group: other
  href: https://artifacts.apis.io/capitainer/hosts/capitainer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/capitainer-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capitainer.com/wp-content/uploads/2025/11/TERMS-AND-CONDITIONS-US.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capitainer.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://capitainer.com/news/
- group: company
  title: ''
  type: Blog
  url: https://capitainer.com/category/blog/
- group: auth
  href: https://artifacts.apis.io/capitainer/security/capitainer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/capitainer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://capitainer.com
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at api.capitainer.com.
  evidence:
  - status: 0
    url: https://api.capitainer.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Capitainer provides microsampling solutions for laboratory and biotechnology applications. Their product portfolio includes the Capitainer®B10, B50, B10Vanadate, SEP10, DIP70 instruments, accessories, and lab services such as sampling kit instructions and kitting support. The company focuses on enabling precise low-volume sampling for research and clinical use, offering request pricing and sample services through their website.
layout: provider
modified: '2026-10-06'
name: Capitainer
nav: Providers
network: true
overview: 'Capitainer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Microsampling, Biotechnology, Laboratory, and Instruments.


  Capitainer''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 10.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/capitainer/capitainer-2026-11-03T123207.png
security:
- kind: domain-security
  name: Capitainer Domain Security
  slug: capitainer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: capitainer
tags:
- Company
- Microsampling
- Biotechnology
- Laboratory
- Instruments
website: https://capitainer.com
---
