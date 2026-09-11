---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/energy-transfer
- group: other
  title: ''
  type: Successor
  url: https://www.energytransfer.com
- group: start
  title: ''
  type: Successor Developer Portal
  url: https://dev.messenger.energytransfer.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/energy-transfer-equity-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/energy-transfer-equity-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/energy-transfer-equity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/energy-transfer-equity-rate-limits.yml
coverage:
  checked: '2026-09-06'
  detail: Energy Transfer Equity, L.P. was dissolved into Energy Transfer LP in October 2018 and serves no host of its own; its legacy corporate domain energytransferequity.com now answers from GoDaddy NameFind parking nameservers with a 114-byte for-sale lander on every path, including a negative-control path that cannot exist.
  evidence:
  - status: 200
    url: https://energytransferequity.com/.well-known/ete-negative-control-7f3ab91c.json
  - status: 200
    url: https://energytransferequity.com/llms.txt
  - status: 404
    url: https://dev.messenger.energytransfer.com/openapi.json
  - status: 403
    url: https://www.energytransfer.com/.well-known/agent-card.json
  reason: defunct
  state: none
created: '2026-03-24'
description: 'Energy Transfer Equity, L.P. (ETE) was a master limited partnership that owned and operated a diverse portfolio of midstream energy assets. In October 2018, ETE merged with its operating subsidiary Energy Transfer Partners (ETP) to form a single publicly traded partnership, Energy Transfer LP (NYSE: ET). All developer resources, including the Messenger+ API for pipeline messaging and gas scheduling, are now provided under the Energy Transfer LP brand.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energy-transfer-equity.png
layout: provider
modified: '2026-09-06'
name: Energy Transfer Equity
nav: Providers
network: true
overview: Energy Transfer Equity is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Pipelines, Midstream, Defunct Entity, and Fortune 100.
plans:
- name: Energy Transfer Equity Plans Pricing
  plan_count: 0
  slug: energy-transfer-equity-plans-pricing
press:
- date: '2026-05-25'
  title: WILLIAMS RIDES AI GAS BOOM America's race to build artificial ...
  url: https://www.facebook.com/tribunephl/posts/williams-rides-ai-gas-boomamericas-race-to-build-artificial-intelligence-is-now-/1388683783308038/
- date: '2026-05-25'
  title: Energy Transfer details vast midstream network in 10-K
  url: https://www.stocktitan.net/sec-filings/ET/10-k-energy-transfer-lp-files-annual-report-92d1558c35ce.html
- date: '2026-05-25'
  title: Energy Transfer LP Common Units (ET) Stock Price, Quote ...
  url: https://seekingalpha.com/symbol/ET
- date: '2026-05-25'
  title: Energy Transfer Equity LP files to offer up to $1 billion of ...
  url: https://www.reuters.com/article/idUSFWN1FT10C/
- date: '2026-05-25'
  title: Power demand is skyrocketing from AI, electrification and ...
  url: https://www.facebook.com/WilliamsEnergyCo/posts/power-demand-is-skyrocketing-from-ai-electrification-and-industrial-reshoring-bu/904918505241219/
random_paper: 14
rate_limits:
- limit_count: 0
  name: Energy Transfer Equity Rate Limits
  slug: energy-transfer-equity-rate-limits
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 4.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/energy-transfer-equity/refs/heads/main/screenshots/energy-transfer-equity-2026-06-20T180709.png
security:
- kind: domain-security
  name: Energy Transfer Equity Domain Security
  slug: energy-transfer-equity-domain-security
  summary_line: TLSv1.3
slug: energy-transfer-equity
tags:
- Energy
- Pipelines
- Midstream
- Defunct Entity
- Fortune 100
---
