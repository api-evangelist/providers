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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/carbonitex-dev/llms/carbonitex-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carbonitex-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/carbonitex-dev/hosts/carbonitex-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbonitex-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/carbonitex-dev/vendors/carbonitex-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbonitex-dev-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Carbonitex
- group: auth
  href: https://artifacts.apis.io/carbonitex-dev/security/carbonitex-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbonitex-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbonitex.dev/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://carbonitex.dev/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Carbonitex is a creative web experiments platform hosting a collection of interactive projects, including the original Discord bot list, AI side‑effects tools, QR‑code art, tabletop RPG utilities, and various browser‑based utilities. Established in 2015, it showcases experimental web technologies, open‑source tools, and community‑driven applications across multiple domains. The site aggregates projects like carbonitex.net, thinkwith.pictures, qart.uk, and more, offering users innovative digital experiences.
image: https://carbonitex.dev/videoeffects/src/img/motion.webp
layout: provider
modified: '2026-11-03'
name: Carbonitex
nav: Providers
network: true
overview: Carbonitex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Creative, Web, Experiments, Open Source, and Community.
random_paper: 19
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 2.6
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
  name: Carbonitex Dev Domain Security
  slug: carbonitex-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: carbonitex-dev
tags:
- Creative
- Web
- Experiments
- Open Source
- Community
website: https://carbonitex.dev/
---
