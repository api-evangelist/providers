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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/varadaio
- group: build
  title: ''
  type: Packages
  url: packages/varada-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/varada-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/varada-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/varada-domain-security.yml
created: '2026-07-17'
description: Varada was a Tel Aviv-based data lake analytics accelerator that used proprietary, patented adaptive indexing to dramatically speed up Trino/Presto queries directly on data lake storage. Backed by Lightspeed Venture Partners, Varada was acquired by Starburst Data on June 23, 2022, and its indexing technology and engineering team were folded into Starburst's query engine. The company published developer tooling (the vtm cluster-management CLI, a Presto/Trino workload analyzer, and a PowerBI Presto connector) on GitHub but no public API; the varada.io domain is now parked and its GitHub organization has been dormant since the acquisition.
image: https://avatars.githubusercontent.com/u/50166579?v=4
layout: provider
modified: '2026-07-21'
name: Varada
nav: Providers
network: true
overview: 'Varada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Data Lakes, Analytics, and Trino.


  Varada''s developer surface includes CLI and 4 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Varada Domain Security
  slug: varada-domain-security
  summary_line: no transport/DNS hardening detected
slug: varada
tags:
- Company
- Data
- Data Lakes
- Analytics
- Trino
- Presto
- Query Acceleration
- Acquired
---
