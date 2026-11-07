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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/emergentcf-cloud/security/emergentcf-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emergentcf-cloud-domain-security.yml
coverage:
  checked: '2026-09-19'
  detail: emergentcf.cloud has no A record (it is Emergent's wildcard preview-cluster domain, not a company site), the //HERE agent card the registry recorded at oversight-hub-12.preview.emergentagent.com returns 404, and its cluster origin answers 403 on every path - the agent surface is gone and the dead Website pointer was removed rather than left as a claim.
  evidence:
  - status: 0
    url: https://emergentcf.cloud/
  - status: 404
    url: https://oversight-hub-12.preview.emergentagent.com/api/.well-known/agent-card.json
  - status: 403
    url: https://oversight-hub-12.cluster-12.preview.emergentcf.cloud/.well-known/here-agent.json
  reason: defunct
  state: none
created: '2026-09-19'
description: //HERE is an A2A agent listed on a2aregistry.org (registered 2026-09-17) that describes itself as an "autonomous machine-native economy" in which agents register, take paid work, own finite land, trade resources and settle in USDC on Base via x402. It was deployed to a preview slot on Emergent (emergent.sh), an AI app-building platform; emergentcf.cloud is Emergent's wildcard preview/deploy cluster domain and has no website of its own. The agent card the registry recorded now returns 404 and the cluster origin answers 403, so no public API surface is reachable.
layout: provider
modified: '2026-09-19'
name: //HERE
nav: Providers
network: true
overview: //HERE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agents, A2A, Agentic Commerce, and x402.
random_paper: 4
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
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
      reason: not_a_repo
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 0.0
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
security:
- kind: domain-security
  name: Emergentcf Cloud Domain Security
  slug: emergentcf-cloud-domain-security
  summary_line: DNSSEC · DMARC
slug: emergentcf-cloud
tags:
- Company
- Agents
- A2A
- Agentic Commerce
- x402
- Stablecoins
---
