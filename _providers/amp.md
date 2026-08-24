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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amp.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amp.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amp.xyz/api-reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amptoken
- group: operate
  title: ''
  type: Support
  url: https://docs.amp.xyz/community-and-resources
- group: company
  title: ''
  type: Blog
  url: https://amptoken.substack.com
- group: other
  title: ''
  type: WhitePaper
  url: https://docs.amp.xyz/whitepaper
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amp-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amp-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amp-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/amp-packages.yml
created: '2026-07-17'
description: Amp is an Ethereum-based digital collateral token (an ERC-20 fungible token extended with ERC-1400-style partitions and ERC-777-style operator semantics) designed to collateralize and instantly settle value transfer worldwide, most notably as the collateral layer behind Flexa payments. The AMP contract (0xff20817765cb7f73d4bde2e66e067e58d11095c2) supports partitioned staking, registered collateral managers, and operator authorization, and has been independently audited by ConsenSys Diligence (June 2020) and Trail of Bits (August 2020). Amp is smart-contract-only and exposes no REST/HTTP API; its published "API reference" documents the on-chain contract interface. The project is stewarded by the Acronym Foundation and was backed by Pantera Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amp.png
layout: provider
modified: '2026-07-17'
name: Amp
nav: Providers
network: true
overview: 'Amp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, Ethereum, and Collateral Token.


  Amp''s developer surface includes documentation, API reference, support, engineering blog, and 8 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 10.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amp/refs/heads/main/screenshots/amp-2026-07-25T200109.png
security:
- kind: domain-security
  name: Amp Domain Security
  slug: amp-domain-security
  summary_line: TLSv1.3 · HSTS
slug: amp
tags:
- Company
- Crypto
- Blockchain
- Ethereum
- Collateral Token
- Payments
- DeFi
- Smart Contracts
- Tokenization
website: https://amp.xyz/
---
