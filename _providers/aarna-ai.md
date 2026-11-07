---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
api_count: 1
apis:
- description: Aarna protocol is building the Agentic Onchain Treasury (AOT), a fully autonomous onchain system that allocates, rotates, and secures assets through programmable, transparent agent governance.
  name: Aarna Protocol
  slug: aarna-protocol
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/aarna-ai/llms/aarna-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aarna-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/aarna-ai/well-known/aarna-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aarna-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/aarna-ai/hosts/aarna-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aarna-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/aarna-ai/packages/aarna-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/aarna-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/aarna-ai/packages/aarna-ai-packages.yml
  title: ''
  type: Packages
  url: packages/aarna-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/aarna-ai/security/aarna-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aarna-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aarna.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://iyp-handbook.aarna.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://iyp-handbook.aarna.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://iyp-handbook.aarna.ai/#/introduction
- group: operate
  title: ''
  type: Support
  url: https://iyp-handbook.aarna.ai/#/resources
- group: company
  title: ''
  type: Blog
  url: https://aarna.ai/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aarna.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aarna.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aarna-ai
- group: operate
  title: ''
  type: Roadmap
  url: https://iyp-handbook.aarna.ai/#/roadmap
coverage:
  checked: '2026-10-31'
  detail: Public documentation exists but no OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://docs.aarna.ai/aarna-protocol.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Aarna AI operates the Tokenization Bridge for India's Capital Markets, building regulated on-chain infrastructure to tokenise Indian financial assets. Based in GIFT City, it offers permissioned digital tokens backed by Category II alternative investment funds, settled in USD or USDC, targeting accredited investors worldwide. The platform provides APIs for subscription, redemption, reporting, and compliance, leveraging ERC-3643 standards and ONCHAINID identity. It is approved in the IFSCA FinTech Sandbox (Stage 1) with Stage 2 under review, aiming for launch Q4 2026.
image: https://aarna.ai/static/logo.png
layout: provider
modified: '2026-10-31'
name: Aarna AI
nav: Providers
network: true
overview: 'Aarna AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Tokenization, Blockchain, Capital Markets, and India.


  Aarna AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 11 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 57.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 19.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aarna Ai Authentication
  slug: aarna-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aarna Ai Domain Security
  slug: aarna-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aarna-ai
tags:
- Fintech
- Tokenization
- Blockchain
- Capital Markets
- India
- RegTech
website: https://aarna.ai/
---
