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
api_count: 1
apis:
- description: API reference for Canton Wiki providing data about the Canton Network ecosystem.
  name: Canton Wiki API
  slug: canton-wiki-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/canton-wiki/llms/canton-wiki-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canton-wiki-llms.txt
- group: other
  href: https://artifacts.apis.io/canton-wiki/hosts/canton-wiki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canton-wiki-hosts.yml
- group: other
  href: https://artifacts.apis.io/canton-wiki/vendors/canton-wiki-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canton-wiki-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canton.wiki/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canton.wiki/privacy
- group: auth
  href: https://artifacts.apis.io/canton-wiki/security/canton-wiki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canton-wiki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canton.wiki/
created: '2026-11-04'
description: CANTON.WIKI is the comprehensive knowledge base for the Canton Network ecosystem. It provides detailed information, comparisons, and reviews of projects modernizing decentralized institutional finance on Canton, covering topics such as blockchain, tokenized treasuries, RWA tokenization, and validator economics. The site serves as a central wiki for developers, investors, and community members seeking authoritative data and resources about the Canton Network and its associated tools.
image: https://canton.wiki/opengraph-image
layout: provider
modified: '2026-11-04'
name: CANTON.WIKI
nav: Providers
network: true
overview: CANTON.WIKI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Canton Network, Decentralized Finance, Blockchain, Tokenization, and Institutional Finance.
random_paper: 20
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canton Wiki Domain Security
  slug: canton-wiki-domain-security
  summary_line: TLSv1.3 · HSTS
slug: canton-wiki
tags:
- Canton Network
- Decentralized Finance
- Blockchain
- Tokenization
- Institutional Finance
website: https://canton.wiki/
---
