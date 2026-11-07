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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Sandbox API for BrainKB providing access to neuroscience data during platform upgrade.
  name: BrainKB API
  slug: brainkb-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/brainkb-org/hosts/brainkb-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainkb-org-hosts.yml
- group: build
  href: https://artifacts.apis.io/brainkb-org/packages/brainkb-org-packages.yml
  title: ''
  type: SDKs
  url: packages/brainkb-org-packages.yml
- group: build
  href: https://artifacts.apis.io/brainkb-org/packages/brainkb-org-packages.yml
  title: ''
  type: Packages
  url: packages/brainkb-org-packages.yml
- group: auth
  href: https://artifacts.apis.io/brainkb-org/security/brainkb-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainkb-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainkb.org/
created: '2026-11-02'
description: BrainKB is a platform providing a sandbox for researchers to explore and build on a growing knowledge base of brain-related data. The service is currently undergoing an upgrade, offering a sandbox environment where users can experiment with data access, APIs, and tools while the new platform is finalized. It aims to support faster discovery, expanded datasets, and improved researcher collaboration across neuroscience domains.
image: https://brainkb.org/brainkb_logo.png
layout: provider
modified: '2026-11-02'
name: BrainKB
nav: Providers
network: true
overview: BrainKB is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Brain, Neuroscience, Data, Research, and Platform.
random_paper: 22
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainkb Org Domain Security
  slug: brainkb-org-domain-security
  summary_line: TLSv1.3
slug: brainkb-org
tags:
- Brain
- Neuroscience
- Data
- Research
- Platform
website: https://brainkb.org/
---
