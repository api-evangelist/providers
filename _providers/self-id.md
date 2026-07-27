---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Self Id Agentic Access
  operation_count: 10
  slug: self-id-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 8
apis:
- description: Read and write DID identity records in browser environments. Exports WebClient and SelfID classes enabling Ethereum-based authentication via 3ID Connect, then get/set/merge operations on records (basi
  name: Self.ID Web API
  slug: selfid-web-api
- description: React hooks and utilities for Ceramic-based DID authentication and record interactions. Provides useViewerRecord, usePublicRecord, useViewerConnection, and related hooks so React applications can conn
  name: Self.ID React API
  slug: selfid-react-api
- description: Highest-level React framework abstraction for decentralized identity apps built on Ceramic. Wraps the core, web, and react packages into a single Provider + hooks surface (useViewerConnection, useView
  name: Self.ID Framework API
  slug: selfid-framework-api
- description: Apply commits to existing streams and retrieve stream commit history
  name: Self.ID Commits API
  slug: self-id-commits-api
- description: Batch-load multiple streams in a single request
  name: Self.ID Multiqueries API
  slug: self-id-multiqueries-api
- description: Node health and configuration information
  name: Self.ID Node API
  slug: self-id-node-api
- description: Manage persistent pinning of streams on the local node
  name: Self.ID Pins API
  slug: self-id-pins-api
- description: Create and load Ceramic streams by StreamID or CommitID
  name: Self.ID Streams API
  slug: self-id-streams-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/self-id-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/self-id-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.ceramic.network/feed/
description: Self.ID is a Ceramic-based decentralized identity framework providing SDK packages and REST-compatible APIs for managing DID profiles, verifiable credentials, and self-sovereign identity data on the Ceramic network. It supports Ethereum-based authentication via 3ID Connect and enables reading and writing identity records such as basic profiles, linked crypto accounts, and linked Web2 accounts. The SDK is organized in layered packages (core, web, react, framework) targeting both Node.js and browser environments.
examples:
- key_count: 10
  name: Basic Profile Example
  slug: basic-profile-example
- key_count: 3
  name: Create Stream Request
  slug: create-stream-request
- key_count: 1
  name: Multiquery Request
  slug: multiquery-request
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://self.id/favicon.ico
json_schemas:
- name: AlsoKnownAs
  property_count: 1
  slug: also-known-as
- name: BasicProfile
  property_count: 11
  slug: basic-profile
- name: CryptoAccounts
  property_count: 0
  slug: crypto-accounts
jsonld:
- class_count: 0
  name: Self Id Context
  property_count: 7
  slug: self-id-context
layout: provider
modified: '2026-06-14'
name: Self.ID
nav: Providers
network: true
overview: 'Self.ID publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Commits API, Multiqueries API, Node API, and 2 more. Tagged areas include Decentralized Identity, DID, Ceramic, Self-Sovereign Identity, and Web3.


  The Self.ID catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Self.ID''s developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 64
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Self.ID API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: self-id-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.5
    developer_ergonomics: 2.2
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 39.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/self-id/refs/heads/main/screenshots/self-id-2026-06-20T193640.png
security:
- kind: domain-security
  name: Self Id Domain Security
  slug: self-id-domain-security
  summary_line: TLSv1.3
slug: self-id
tags:
- Decentralized Identity
- DID
- Ceramic
- Self-Sovereign Identity
- Web3
- Verifiable Credentials
- Blockchain
website: https://self.id
---
