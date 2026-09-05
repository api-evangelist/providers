---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.9
  scored_at: '2026-09-04'
api_count: 3
apis:
- baseURL: https://api.sommelier.finance
  baseurl_source: declared
  description: Integration-specific datasets (Kelp, ether.fi).
  name: Sommelier Integrations API
  slug: sommelier-integrations-api
- baseURL: https://api.sommelier.finance
  baseurl_source: declared
  description: Protocol-wide metrics such as total value locked.
  name: Sommelier Protocol API
  slug: sommelier-protocol-api
- baseURL: https://api.sommelier.finance
  baseurl_source: declared
  description: Daily and hourly performance snapshots of Sommelier vaults (cellars).
  name: Sommelier Vault Data API
  slug: sommelier-vault-data-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sommelier Finance Integrations API
  slug: open-sommelier-integrations-api
- collection_type: open
  name: Sommelier Finance Integrations Protocol API
  slug: open-sommelier-protocol-api
- collection_type: open
  name: Sommelier Finance Integrations Vault Data API
  slug: open-sommelier-vault-data-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.somm.finance
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.sommelier.finance/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sommelier-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sommelier-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sommelier-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sommelier-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sommelier-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sommelier-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sommelier-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sommelier-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Sommelier (rebranding to "Somm") is a decentralized asset-management and DeFi vault protocol whose smart-contract "cellars" run automated yield strategies on Ethereum. It publishes a public, read-only HTTP API that exposes on-chain vault performance data — daily and hourly snapshots (APY, TVL, share price, total assets), protocol-wide total value locked, per-cellar snapshots, and integration datasets for Kelp and ether.fi points and balances. All endpoints are unauthenticated GET requests with path-based parameters and a { "Response": ... } envelope; the API currently serves the ethereum network. Backed by Multicoin Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sommelier.png
layout: provider
modified: '2026-07-21'
name: Sommelier
nav: Providers
network: true
overview: 'Sommelier publishes 3 APIs on the [APIs.io](https://apis.io/) network: Integrations API, Protocol API, and Vault Data API. Tagged areas include Company, Crypto Web3, DeFi, Blockchain, and Ethereum.


  Sommelier''s developer surface includes authentication and 10 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 48.1
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 28.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sommelier/refs/heads/main/screenshots/sommelier-2026-09-02T160153.png
security:
- kind: authentication
  name: Sommelier Authentication
  slug: sommelier-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Sommelier Domain Security
  slug: sommelier-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: sommelier
tags:
- Company
- Crypto Web3
- DeFi
- Blockchain
- Ethereum
- Vault
- Yield
- Analytics
website: https://www.somm.finance
---
