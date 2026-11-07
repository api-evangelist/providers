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
  href: https://artifacts.apis.io/dsp-concepts/hosts/dsp-concepts-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dsp-concepts-hosts.yml
- group: other
  href: https://artifacts.apis.io/dsp-concepts/vendors/dsp-concepts-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dsp-concepts-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dspconcepts.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dspconcepts.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://dspconcepts.com/news
- group: auth
  href: https://artifacts.apis.io/dsp-concepts/security/dsp-concepts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dsp-concepts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dspconcepts.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dochub.dspconcepts.com/latest/
- group: company
  title: ''
  type: Blog
  url: https://dspconcepts.com/blog
coverage:
  checked: '2026-10-24'
  detail: Documentation is provided as HTML pages without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://dochub.dspconcepts.com/latest/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: DSP Concepts provides embedded audio processing software and the Audio Weaver platform, enabling developers to integrate advanced audio algorithms into automotive, consumer, and professional audio products. Their solutions include AI‑enhanced audio processing, customizable DSP blocks, and tools for rapid development and deployment across a range of industries. The company emphasizes modular, scalable designs and offers extensive documentation, training, and support for engineers building audio‑centric applications.
layout: provider
modified: '2026-10-24'
name: DSP Concepts
nav: Providers
network: true
overview: 'DSP Concepts is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Embedded, DSP, Software, and Automotive.


  DSP Concepts'' developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 11.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dsp-concepts/dsp-concepts-2026-11-03T131108.png
security:
- kind: domain-security
  name: Dsp Concepts Domain Security
  slug: dsp-concepts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dsp-concepts
tags:
- Audio
- Embedded
- DSP
- Software
- Automotive
website: https://dspconcepts.com/
---
