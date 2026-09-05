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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Self Id Agentic Access
  operation_count: 10
  slug: self-id-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
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
- baseURL: https://gateway.ceramic.network
  baseurl_source: declared
  description: Apply commits to existing streams and retrieve stream commit history
  name: Self.ID Commits API
  slug: self-id-commits-api
- baseURL: https://gateway.ceramic.network
  baseurl_source: declared
  description: Batch-load multiple streams in a single request
  name: Self.ID Multiqueries API
  slug: self-id-multiqueries-api
- baseURL: https://gateway.ceramic.network
  baseurl_source: declared
  description: Node health and configuration information
  name: Self.ID Node API
  slug: self-id-node-api
- baseURL: https://gateway.ceramic.network
  baseurl_source: declared
  description: Manage persistent pinning of streams on the local node
  name: Self.ID Pins API
  slug: self-id-pins-api
- baseURL: https://gateway.ceramic.network
  baseurl_source: declared
  description: Create and load Ceramic streams by StreamID or CommitID
  name: Self.ID Streams API
  slug: self-id-streams-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ceramic HTTP Commits API
  slug: open-self-id-commits-api
- collection_type: open
  name: Ceramic HTTP Commits Multiqueries API
  slug: open-self-id-multiqueries-api
- collection_type: open
  name: Ceramic HTTP Commits Node API
  slug: open-self-id-node-api
- collection_type: open
  name: Ceramic HTTP Commits Pins API
  slug: open-self-id-pins-api
- collection_type: open
  name: Ceramic HTTP Commits Streams API
  slug: open-self-id-streams-api
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
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Self.ID API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: self-id-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 56.3
    catalog_earned_first_party: 0.0
    catalog_gap: 58.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 53.1
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
