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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hike
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hike-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hike-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Hike Private Limited wound down in September 2025 after India's real-money gaming ban; hike.in now returns a Google Front End HTTP 502 behind a wildcard certificate that expired 2026-07-01, and every developer host that ever appeared in Certificate Transparency (platform.hike.in, hub.hike.in, im.hike.in, api.hike.in, developer.hike.in) is NXDOMAIN.
  evidence:
  - status: 502
    url: https://hike.in/
  - status: 502
    url: https://hike.in/openapi.json
  - status: 502
    url: https://hike.in/.well-known/agent-card.json
  - status: 200
    url: https://github.com/hike
  - status: 403
    url: https://forgeglobal.com/hike_stock/
  reason: defunct
  state: none
created: '2026-08-22'
description: Hike Private Limited is a New Delhi consumer internet company founded in 2011 by Kavin Bharti Mittal. It is best known for Hike Messenger, launched in December 2012 and at its peak one of India's largest homegrown messaging apps, which the company retired in January 2021 to pivot into the Rush Gaming Universe — a mobile-first skill-gaming platform that layered Web3 ownership and play-to-earn mechanics over roughly fourteen casual titles. Hike raised approximately $261M across seven rounds from investors including SoftBank, Tencent, Tiger Global and Polygon, and reached unicorn valuation in 2021. In September 2025, after India's Promotion and Regulation of Online Gaming Act banned real-money gaming, the founder announced a complete wind-down of the company and of Rush. As of August 2026 hike.in still resolves but serves an HTTP 502 behind an expired certificate, and every developer-facing subdomain is NXDOMAIN; the company publishes no API, developer portal, or machine-readable
  contract.
image: https://avatars.githubusercontent.com/u/1162265?v=4
layout: provider
modified: '2026-08-22'
name: Hike
nav: Providers
network: true
overview: Hike is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, Social, Gaming, and Mobile.
random_paper: 18
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 6.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Hike Domain Security
  slug: hike-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hike
tags:
- Company
- Messaging
- Social
- Gaming
- Mobile
- Consumer
- Web3
- India
- Defunct
---
