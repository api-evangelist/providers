---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Defillama Agentic Access
  operation_count: 31
  slug: defillama-agentic-access
  summary_line: 31 operations
api_count: 1
apis:
- description: Free, no-auth REST API exposing 31+ endpoints for protocol TVL, chain TVL, coin prices, stablecoin metrics, yield pools, DEX volumes, and fees. Underpins thousands of dashboards and integrations.
  name: DefiLlama Public API
  slug: public-api
- description: Paid REST API ($300/month) with higher rate limits and 38 exclusive endpoints covering token unlocks, cross-chain bridges, digital-asset treasury data, and other advanced datasets. Authenticated via A
  name: DefiLlama Pro API
  slug: pro-api
- baseURL: https://api.llama.fi
  baseurl_source: declared
  description: The Coins API from DefiLlama — 7 operation(s) for coins.
  name: DefiLlama Coins API
  slug: defillama-coins-api
- baseURL: https://api.llama.fi
  baseurl_source: declared
  description: The Fees API from DefiLlama — 3 operation(s) for fees.
  name: DefiLlama Fees API
  slug: defillama-fees-api
- baseURL: https://api.llama.fi
  baseurl_source: declared
  description: The Stablecoins API from DefiLlama — 6 operation(s) for stablecoins.
  name: DefiLlama Stablecoins API
  slug: defillama-stablecoins-api
- baseURL: https://api.llama.fi
  baseurl_source: declared
  description: The TVL API from DefiLlama — 6 operation(s) for tvl.
  name: DefiLlama TVL API
  slug: defillama-tvl-api
- baseURL: https://api.llama.fi
  baseurl_source: declared
  description: The Volumes API from DefiLlama — 7 operation(s) for volumes.
  name: DefiLlama Volumes API
  slug: defillama-volumes-api
- baseURL: https://api.llama.fi
  baseurl_source: declared
  description: The Yields API from DefiLlama — 2 operation(s) for yields.
  name: DefiLlama Yields API
  slug: defillama-yields-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DefiLlama Public Coins API
  slug: open-defillama-coins-api
- collection_type: open
  name: DefiLlama Public Coins Fees API
  slug: open-defillama-fees-api
- collection_type: open
  name: DefiLlama Public Coins Stablecoins API
  slug: open-defillama-stablecoins-api
- collection_type: open
  name: DefiLlama Public Coins TVL API
  slug: open-defillama-tvl-api
- collection_type: open
  name: DefiLlama Public Coins Volumes API
  slug: open-defillama-volumes-api
- collection_type: open
  name: DefiLlama Public Coins Yields API
  slug: open-defillama-yields-api
- collection_type: open
  name: DefiLlama Public API
  slug: open-defillama
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/defillama-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defillama-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/defillama-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defillama
- group: start
  title: ''
  type: Portal
  url: https://defillama.com/
- group: docs
  title: ''
  type: Documentation
  url: https://defillama.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://defillama.com/pro-api
- group: build
  title: ''
  type: GitHub
  url: https://github.com/DefiLlama
- group: commercial
  title: ''
  type: Plans
  url: plans/defillama-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/defillama-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/defillama-finops.yml
created: '2026-05-08'
description: DefiLlama is the largest open-source DeFi TVL and yield aggregator. It publishes a free public REST API (api.llama.fi) and a Pro API (pro-api.llama.fi) that adds higher rate limits and exclusive endpoints for token unlocks, bridges, digital-asset treasuries, and other advanced datasets. Free API requires no authentication; Pro is $300/month.
finops:
- name: Defillama Finops
  service_category: Crypto Analytics
  slug: defillama-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defillama.png
layout: provider
modified: '2026-05-08'
name: DefiLlama
nav: Providers
network: true
overview: 'DefiLlama publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Coins API, Fees API, Stablecoins API, and 3 more. Tagged areas include Web3, DeFi, TVL, Crypto, and Stablecoins.


  DefiLlama''s developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, and 6 more developer resources.'
plans:
- name: Defillama Plans Pricing
  plan_count: 2
  slug: defillama-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Defillama Rate Limits
  slug: defillama-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 46.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defillama/refs/heads/main/screenshots/defillama-2026-06-20T175849.png
security:
- kind: authentication
  name: Defillama Authentication
  slug: defillama-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Defillama Domain Security
  slug: defillama-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: defillama
tags:
- Web3
- DeFi
- TVL
- Crypto
- Stablecoins
- Yields
- Bridges
- Aggregator
- Open-Source
website: https://defillama.com/
---
