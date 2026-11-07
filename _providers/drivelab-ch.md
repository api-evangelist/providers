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
    mcp_server: documented
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
  score: 17.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/drivelab-ch/llms/drivelab-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drivelab-ch-llms.txt
- group: agent
  href: https://artifacts.apis.io/drivelab-ch/well-known/drivelab-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drivelab-ch-well-known.yml
- group: other
  href: https://artifacts.apis.io/drivelab-ch/hosts/drivelab-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drivelab-ch-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://drivelab.ch/support/
- group: company
  title: ''
  type: Blog
  url: https://drivelab.ch/blog/
- group: auth
  href: https://artifacts.apis.io/drivelab-ch/security/drivelab-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drivelab-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drivelab.ch/
coverage:
  checked: '2026-11-06'
  detail: The main site returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://drivelab.ch/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DriveLab is the Swiss marketplace for comparing driving instructors and booking driving lessons online. It offers car, motorcycle, first aid and trailer courses with transparent pricing and real user reviews, enabling users to find and schedule lessons conveniently across Switzerland.
image: https://i0.wp.com/drivelab.ch/wp-content/uploads/2022/11/Fahrschule-Luzern-Frau.jpg?fit=2063%2C1547&ssl=1
layout: provider
modified: '2026-11-05'
name: DriveLab
nav: Providers
network: true
overview: 'DriveLab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Swiss and First‑Aid Course.


  DriveLab''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Drivelab Ch Domain Security
  slug: drivelab-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: drivelab-ch
tags:
- Swiss
- First‑Aid Course
website: https://drivelab.ch/
---
