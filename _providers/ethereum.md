---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ethereum Agentic Access
  operation_count: 1
  slug: ethereum-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Ethereum JSON RPC API API from Ethereum — 1 operation(s) for ethereum json rpc api.
  name: Ethereum Ethereum JSON RPC API API
  slug: ethereum-ethereum-json-rpc-api-api
artifact_total: 11
collections:
- collection_type: open
  name: Ethereum JSON-RPC API
  slug: open-ethereum-json-rpc
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ethereum-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ethereum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ethereum-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ethereum-foundation
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ethereum-json-rpc-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ethereum-json-rpc-context.jsonld
- group: company
  title: ''
  type: Website
  url: https://ethereum.org
- group: docs
  title: ''
  type: Documentation
  url: https://ethereum.org/en/developers/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://ethereum.org/en/developers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ethereum
- group: agent
  title: ''
  type: LlmsText
  url: https://ethereum.org/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.ethereum.org/feed.xml
created: '2025-01-01'
description: Ethereum is a decentralized, open-source blockchain platform that supports smart contracts - self-executing programs that run on its distributed network. It is the foundation for a vast ecosystem of decentralized applications (dApps), tokens, DeFi protocols, and NFTs, and uses a proof-of-stake consensus mechanism.
finops:
- name: Ethereum Finops
  service_category: API
  slug: ethereum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ethereum.png
json_schemas:
- name: Ethereum Data Models
  property_count: 0
  slug: ethereum-json-rpc
jsonld:
- class_count: 0
  name: Ethereum Json Rpc Context
  property_count: 8
  slug: ethereum-json-rpc-context
layout: provider
modified: '2026-05-19'
name: Ethereum
nav: Providers
network: true
overview: 'Ethereum publishes 1 API on the [APIs.io](https://apis.io/) network: Ethereum JSON RPC API API. Tagged areas include Blockchain, DeFi, Ethereum, JSON-RPC, and Smart Contracts.


  The Ethereum catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ethereum''s developer surface includes documentation, getting-started guide, engineering blog, and 9 more developer resources.'
plans:
- name: Ethereum Plans Pricing
  plan_count: 3
  slug: ethereum-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Ethereum Rate Limits
  slug: ethereum-rate-limits
rules:
- name: Ethereum API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: ethereum-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.7
  delta: -2.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.9
    developer_ergonomics: 21.7
    discoverability: 66.7
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ethereum/refs/heads/main/screenshots/ethereum-2026-06-20T180835.png
security:
- kind: domain-security
  name: Ethereum Domain Security
  slug: ethereum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ethereum Vulnerability Disclosure
  slug: ethereum-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ethereum
tags:
- Blockchain
- DeFi
- Ethereum
- JSON-RPC
- Smart Contracts
- Web3
website: https://ethereum.org
---
