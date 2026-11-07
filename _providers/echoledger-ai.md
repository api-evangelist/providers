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
- group: other
  href: https://artifacts.apis.io/echoledger-ai/hosts/echoledger-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/echoledger-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/echoledger-ai/vendors/echoledger-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/echoledger-ai-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/defipy-devs
- group: auth
  href: https://artifacts.apis.io/echoledger-ai/security/echoledger-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/echoledger-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://echoledger.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.echoledger.ai/
coverage:
  checked: '2026-11-06'
  detail: No machine‑readable API contract (OpenAPI, AsyncAPI, GraphQL, gRPC, WSDL) was found on the provider’s documented sites.
  evidence:
  - status: 200
    url: https://www.echoledger.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: EchoLedger provides quantitative on-chain analysis tools that are open by design. Leveraging the open-source DeFi analytics library defipy, the platform offers transparent, reproducible research on Uniswap V2/V3, Balancer, and Curve pools. It emphasizes open methodology, detailed risk decomposition, and verifiable results, aiming to make DeFi analytics accessible and trustworthy for researchers and practitioners alike.
layout: provider
modified: '2026-11-06'
name: EchoLedger
nav: Providers
network: true
overview: 'EchoLedger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeFi, Analytics, Open Source, and Research.


  EchoLedger''s developer surface includes documentation and 5 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Echoledger Ai Domain Security
  slug: echoledger-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: echoledger-ai
tags:
- Company
- DeFi
- Analytics
- Open Source
- Research
website: https://echoledger.ai/
---
