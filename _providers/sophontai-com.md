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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for SophontAI medical AI platform, as documented on the developer portal.
  name: SophontAI API
  slug: sophontai-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/sophontai-com/hosts/sophontai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sophontai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sophontai-com/vendors/sophontai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sophontai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sophont.med/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sophont.med/privacy/
- group: company
  title: ''
  type: Blog
  url: https://sophont.med/blog/
- group: auth
  href: https://artifacts.apis.io/sophontai-com/security/sophontai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sophontai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sophont.med/
coverage:
  checked: '2026-10-26'
  detail: Documentation is only available via a JavaScript‑rendered portal at https://sophont.med/docs, which yields no machine‑readable spec.
  evidence:
  - status: 200
    url: https://sophont.med/docs
  - status: 0
    url: https://api.sophontai.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Sophont builds medical AI, including Holon‑S1 for spatial gene‑expression prediction from routine pathology, open foundation models, and benchmarks. The company focuses on open medical superintelligence, offering research, tools, and collaborations to advance healthcare AI.
image: https://sophont.med/assets/generated/hero-medical-ai-bg.webp
layout: provider
modified: '2026-10-25'
name: Sophontai
nav: Providers
network: true
overview: 'Sophontai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Medical, Healthcare, OpenSource, and Superintelligence.


  Sophontai''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sophontai Com Domain Security
  slug: sophontai-com-domain-security
  summary_line: TLSv1.3
slug: sophontai-com
tags:
- AI
- Medical
- Healthcare
- OpenSource
- Superintelligence
website: https://sophont.med/
---
