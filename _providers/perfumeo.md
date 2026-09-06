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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/perfumeo
coverage:
  checked: '2026-08-26'
  detail: The domain Perfumeo itself publishes as its website, perfumeo-ai.com, was re-registered on 2026-06-12 behind a Dynadot privacy proxy on domain-parking nameservers and now answers a JS bot-challenge and then a "Coming Soon" holding page, with wildcard DNS and an HTTP catch-all that returns an identical 200 HTML shell for every path and every subdomain including invented ones.
  evidence:
  - status: 200
    url: https://perfumeo-ai.com/
  - status: 200
    url: https://perfumeo-ai.com/openapi.json
  - status: 200
    url: https://perfumeo-ai.com/.well-known/agent-card.json
  - status: 404
    url: https://github.com/perfumeo
  - status: 404
    url: https://registry.npmjs.org/perfumeo
  - status: 200
    url: https://www.linkedin.com/company/perfumeo
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Perfumeo (Perfumeo(R)) is a consumer-hardware startup that built an AI-driven smart-home fragrance diffuser — a connected device holding scent capsules that its companion mobile app uses to adapt diffusion to the user''s mood. The company describes itself as combining AI, data science, "green mechatronics" and green chemistry, and states it was founded in Paris in July 2021 and relocated to Cupertino, California in April 2023. It is an end-user product company: no public API, SDK, developer portal, webhook surface or machine-readable contract has ever been published, and none was found in this pass. As of 2026-08-26 the domain the company itself lists as its website, www.perfumeo-ai.com, no longer belongs to it — WHOIS shows the domain was created 2026-06-12 under a Dynadot privacy proxy on domain-parking nameservers, and it now serves a bot-challenge interstitial followed by a "Coming Soon" holding page. The company''s LinkedIn page remains up and lists a headcount of one.'
layout: provider
modified: '2026-08-26'
name: Perfumeo
nav: Providers
network: true
overview: Perfumeo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Hardware, Internet of Things, Smart Home, and Artificial Intelligence.
random_paper: 6
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 4.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
slug: perfumeo
tags:
- Company
- Consumer Hardware
- Internet of Things
- Smart Home
- Artificial Intelligence
- Fragrance
- Consumer Products
- Mobile Apps
- No API Surface
---
