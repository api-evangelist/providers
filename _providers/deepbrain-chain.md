---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation not publicly machine-readable; site is a JS shell with no readable spec.
  name: DeepBrain Chain API
  slug: deepbrain-chain-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/deepbrain-chain/hosts/deepbrain-chain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepbrain-chain-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepbrain-chain/vendors/deepbrain-chain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepbrain-chain-vendors.yml
- group: build
  href: https://artifacts.apis.io/deepbrain-chain/packages/deepbrain-chain-packages.yml
  title: ''
  type: SDKs
  url: packages/deepbrain-chain-packages.yml
- group: build
  href: https://artifacts.apis.io/deepbrain-chain/packages/deepbrain-chain-packages.yml
  title: ''
  type: Packages
  url: packages/deepbrain-chain-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DeepBrainChain
- group: auth
  href: https://artifacts.apis.io/deepbrain-chain/security/deepbrain-chain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepbrain-chain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepbrainchain.org
coverage:
  checked: '2026-10-22'
  detail: The homepage returns a JavaScript shell with no machine-readable API specification.
  evidence:
  - status: 200
    url: https://deepbrainchain.org
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: DeepBrain Chain is an AI computing platform that leverages blockchain technology to provide decentralized, low-cost, and secure AI model training and inference services. The company aims to democratize AI by allowing developers and enterprises to access powerful computational resources without the high costs associated with traditional cloud providers. Their platform offers a marketplace for AI models, data, and computing power, fostering collaboration across the AI ecosystem.
layout: provider
modified: '2026-10-22'
name: DeepBrain Chain
nav: Providers
network: true
overview: DeepBrain Chain is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Blockchain, Decentralized, Compute, and Marketplace.
random_paper: 10
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deepbrain Chain Domain Security
  slug: deepbrain-chain-domain-security
  summary_line: TLSv1.3 · HSTS
slug: deepbrain-chain
tags:
- Artificial Intelligence
- Blockchain
- Decentralized
- Compute
- Marketplace
website: https://deepbrainchain.org
---
