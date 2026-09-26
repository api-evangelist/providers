---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 2
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SynapseFI
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/synapsefi/refs/heads/main/packages/synapsefi-packages.yml
  title: ''
  type: Packages
  url: packages/synapsefi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/synapsefi/refs/heads/main/packages/synapsefi-packages.yml
  title: ''
  type: SDKs
  url: packages/synapsefi-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/synapsefi/refs/heads/main/lifecycle/synapsefi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/synapsefi-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/synapsefi/refs/heads/main/plans/synapsefi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/synapsefi-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/synapsefi/refs/heads/main/rate-limits/synapsefi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/synapsefi-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/synapsefi/refs/heads/main/llms/synapsefi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/synapsefi-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Synapse Financial Technologies filed Chapter 11 on 2024-04-22, no buyer took the platform, and the entire synapsefi.com zone has since been withdrawn — synapsefi.com, api.synapsefi.com and docs.synapsefi.com all fail DNS resolution with NXDOMAIN, so there is no host left to serve a contract, a portal or a .well-known document.
  evidence:
  - note: 'curl: (6) Could not resolve host — NXDOMAIN'
    status: 0
    url: https://synapsefi.com/
  - note: 'curl: (6) Could not resolve host — NXDOMAIN'
    status: 0
    url: https://api.synapsefi.com/openapi.json
  - note: 'curl: (6) Could not resolve host — NXDOMAIN'
    status: 0
    url: https://docs.synapsefi.com/
  - note: Organization is live with 11 public repositories, but every git tree was walked and none contains an OpenAPI, Swagger, AsyncAPI, GraphQL SDL, protobuf, WSDL or Postman collection.
    status: 200
    url: https://github.com/SynapseFI
  reason: defunct
  state: none
created: '2026-08-29'
description: 'Synapse Financial Technologies was a San Francisco banking-as-a-service platform, founded 2014-04-14 by Sankaet Pathak and Bryan Keltner, that sold a REST API letting fintech companies open and operate deposit accounts, move money over ACH and wires, issue cards and run KYC/CIP checks through partner banks including Evolve Bank & Trust, AMG National Trust, American Bank North America and Lineage Bank. At its peak it served roughly 100 fintech platforms reaching about 10 million end customers, and it published first-party client libraries for Node.js, Python, Ruby, Go and PHP against its v3.1 REST API. Synapse filed for Chapter 11 bankruptcy on 2024-04-22 with a $65-96 million shortfall between its records and its partner banks''; the sale of its technology assets drew no qualified bids and the case was later dismissed. The company is defunct: as of 2026-08-29 every synapsefi.com host returns NXDOMAIN, so the API, its documentation and its developer portal are all permanently
  unreachable. This profile records what survives — the first-party SDKs still published on npm, PyPI, RubyGems and the Go module proxy, and the public GitHub organization.'
image: https://avatars.githubusercontent.com/u/21111011?v=4
layout: provider
modified: '2026-08-29'
name: Synapse
nav: Providers
network: true
overview: Synapse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Banking as a Service, Fintech, and Payments.
plans:
- name: Synapsefi Plans Pricing
  plan_count: 0
  slug: synapsefi-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Synapsefi Rate Limits
  slug: synapsefi-rate-limits
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 6
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
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: synapsefi
tags:
- Company
- Banking
- Banking as a Service
- Fintech
- Payments
- ACH
- Deposit Accounts
- KYC
- Defunct
---
