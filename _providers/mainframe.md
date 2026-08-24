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
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The Graph subgraph that indexes the Hifi fixed-rate, fixed-term lending protocol — vaults, collateral and debt positions, listed bonds and collaterals, AMM pools and swaps — and serves them over Graph
  name: Hifi Protocol Subgraph
  slug: hifi-subgraph
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mainframe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mainframe.co/
- group: build
  title: ''
  type: Packages
  url: packages/mainframe-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mainframe-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mainframe-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hifi.finance/protocol/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hifi-finance
created: '2026-07-17'
description: Mainframe (Mainframe Group, Inc.) is a software development and marketing services company building products for the decentralized finance (DeFi) ecosystem. It offers three service areas — Risk Management (protocol parameter optimization and stability), Development (DeFi and blockchain financial solutions), and Marketing (brand reach and audience engagement) — and has produced projects including Hifi, Pooled NFT, Sheet Heads, and Crown Ribbon. It was surfaced as a portfolio company of a16z and Techstars and added to the API Evangelist network. Mainframe itself publishes only a three-page Webflow marketing site, with no API host and no developer portal (api., docs. and developer.mainframe.co do not resolve), and its MainframeHQ GitHub organization has zero public repositories. Its developer surface lives under its Hifi product instead — the docs.hifi.finance protocol documentation (footer copyright "Mainframe Group Inc."), the github.com/hifi-finance organization, five first-party
  npm packages in the @hifi scope, and a GraphQL subgraph schema for the Hifi lending protocol. That surface is a smart-contract SDK rather than an HTTP API — there is no REST API and no OpenAPI anywhere — and it has gone quiet, with the newest package release dated 2024-01-12 and the documented GraphQL endpoint on The Graph's retired hosted service returning HTTP 404.
graphqls:
- description: 'generated: ''2026-08-13'''
  name: Mainframe / Hifi Protocol GraphQL
  slug: mainframe-hifi-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mainframe.png
layout: provider
modified: '2026-08-13'
name: Mainframe
nav: Providers
network: true
overview: 'Mainframe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeFi, Blockchain, Web3, and NFT.


  Mainframe''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Mainframe Plans Pricing
  plan_count: 0
  slug: mainframe-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Mainframe Rate Limits
  slug: mainframe-rate-limits
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.8
    developer_ergonomics: 16.7
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 21.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mainframe/refs/heads/main/screenshots/mainframe-2026-07-25T225915.png
security:
- kind: domain-security
  name: Mainframe Domain Security
  slug: mainframe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mainframe
tags:
- Company
- DeFi
- Blockchain
- Web3
- NFT
- Software Development
- Marketing
- Lending
- GraphQL
- Smart Contracts
- Subgraph
- Ethereum
website: https://mainframe.co/
---
