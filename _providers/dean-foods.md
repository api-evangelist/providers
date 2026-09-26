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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dean-foods
- group: other
  title: ''
  type: Acquirer
  url: https://www.dfamilk.com/
- group: other
  title: ''
  type: ShutdownNotice
  url: https://www.prnewswire.com/news-releases/dean-foods-company-initiates-voluntary-reorganization-with-new-financial-support-from-existing-lenders-300956285.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dean-foods/refs/heads/main/security/dean-foods-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dean-foods-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dean-foods/refs/heads/main/llms/dean-foods-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dean-foods-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Dean Foods filed Chapter 11 on 2019-11-12 and its plants and brands were sold to Dairy Farmers of America in May 2020; the company has no operating surface left to profile — deanfoods.com is now registered to Dairy Farmers of America, Inc., serves no HTTPS at all (the TLS handshake to port 443 aborts with "tlsv1 alert internal error", so every https probe returns 0 rather than a status code), and over plain HTTP answers 301 to https://www.dfamilk.com/ for every path including /openapi.json, /llms.txt and all seven /.well-known/ paths, while no api., developer., docs. or portal. subdomain resolves on either deanfoods.com or dfamilk.com and no GitHub organization exists under any spelling of the name.
  evidence:
  - status: 0
    url: https://deanfoods.com/openapi.json
  - status: 0
    url: https://deanfoods.com/.well-known/agent-card.json
  - status: 301
    url: http://deanfoods.com/
  - status: 404
    url: https://www.dfamilk.com/.well-known/agent-card.json
  - status: 404
    url: https://www.dfamilk.com/zzz-soft404-control-probe
  - status: 404
    url: https://api.github.com/orgs/deanfoods
  reason: defunct
  state: none
created: '2025-01-01'
description: Dean Foods was a leading U.S. food and beverage company and one of the largest processors and direct-to-store distributors of fresh fluid milk and other dairy products. After filing for Chapter 11 bankruptcy in 2019, most of Dean Foods' assets were acquired by Dairy Farmers of America (DFA) in 2020. Dean Foods no longer operates as an independent company and does not publish a public developer API; surviving brands are now managed under DFA. This profile is retained for historical reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dean-foods.png
layout: provider
modified: '2026-09-05'
name: Dean Foods
nav: Providers
network: true
overview: Dean Foods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, Beverages, Dairy, Defunct, and Food and Beverage.
press:
- date: ''
  title: Dean Foods
  url: https://greenamerica.org/dean-foods
- date: ''
  title: Dean Foods opts for internal transformation plan after ...
  url: https://www.just-food.com/news/dean-foods-opts-for-internal-transformation-plan-after-strategic-review/
- date: ''
  title: Dean Foods Completes Sale to DFA | Dairy News
  url: https://www.lancasterfarming.com/farming-news/dairy/dean-foods-completes-sale-to-dfa/article_cc082519-cf62-522d-8841-bb0b497557c0.html
- date: ''
  title: 'Dean Foods goes bust thanks to a fatal error: shying away ...'
  url: https://agfundernews.com/dean-foods-goes-bust-thanks-to-a-fatal-error-shying-away-from-alt-milk
- date: ''
  title: Dean Foods Company Initiates Voluntary Reorganization ...
  url: https://www.prnewswire.com/news-releases/dean-foods-company-initiates-voluntary-reorganization-with-new-financial-support-from-existing-lenders-300956285.html
random_paper: 2
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 7
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
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/dean-foods/refs/heads/main/screenshots/dean-foods-2026-06-20T175743.png
security:
- kind: domain-security
  name: Dean Foods Domain Security
  slug: dean-foods-domain-security
  summary_line: DNSSEC · DMARC
slug: dean-foods
tags:
- Acquired
- Beverages
- Dairy
- Defunct
- Food and Beverage
- Milk
- Fortune 500
---
