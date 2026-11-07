---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 4.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/skalelabs-com/vendors/skalelabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skalelabs-com-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/skalelabs-com/plans/skalelabs-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skalelabs-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/skalelabs-com/cli/skalelabs-com-cli.yml
  title: ''
  type: CLI
  url: cli/skalelabs-com-cli.yml
- group: agent
  href: https://artifacts.apis.io/skalelabs-com/llms/skalelabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skalelabs-com-llms.txt
- group: other
  href: https://artifacts.apis.io/skalelabs-com/a2a/skalelabs-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/skalelabs-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/skalelabs-com/well-known/skalelabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skalelabs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/skalelabs-com/hosts/skalelabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skalelabs-com-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skale.space/get-started/quick-start/skale-on-base
- group: docs
  title: ''
  type: Documentation
  url: https://developers.skalelabs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.skale.space/llms-full.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skalelabs
- group: auth
  href: https://artifacts.apis.io/skalelabs-com/security/skalelabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skalelabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skalelabs.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://skalelabs.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: SKALE Labs is a blockchain scaling platform that provides elastic sidechains for high‑throughput, low‑cost decentralized applications. Backed by multicoin‑capital, the company focuses on enabling developers to deploy scalable dApps without compromising security, offering tools for rapid deployment, monitoring, and governance across multiple networks.
layout: provider
modified: '2026-10-22'
name: SKALE Labs
nav: Providers
network: true
overview: 'SKALE Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Scaling, Decentralized, and Infrastructure.


  SKALE Labs'' developer surface includes CLI, getting-started guide, documentation, API reference, and 9 more developer resources.'
plans:
- name: Skalelabs Com Plans Pricing
  plan_count: 2
  slug: skalelabs-com-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 51.8
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.7
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
screenshot: https://apis.io/screenshots/skalelabs-com/skalelabs-com-2026-11-03T143314.png
security:
- kind: domain-security
  name: Skalelabs Com Domain Security
  slug: skalelabs-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: skalelabs-com
tags:
- Company
- Blockchain
- Scaling
- Decentralized
- Infrastructure
website: https://skalelabs.com
---
