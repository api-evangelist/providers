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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unbound-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unbound.finance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unbound-finance
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unbound-llms.txt
created: '2026-07-17'
description: 'Unbound (Unbound Finance) was a DeFi protocol describing itself as "The DeFi Treasury for Liquidity Pool Tokens," enabling liquidity providers to collateralize LP tokens on Ethereum. It is a Pantera Capital portfolio company (sector: crypto). As of 2026-07-21 the project appears inactive: unbound.finance returns HTTP 404, its documentation host (wiki.unbound.finance) no longer resolves, and its GitHub organization contains only forked repositories - no public API surface, developer portal, or first-party packages were found.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unbound.png
layout: provider
modified: '2026-07-21'
name: Unbound
nav: Providers
network: true
overview: Unbound is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, DeFi, Liquidity, and Ethereum.
random_paper: 7
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Unbound Domain Security
  slug: unbound-domain-security
  summary_line: TLSv1.3 · DMARC
slug: unbound
tags:
- Company
- Crypto
- DeFi
- Liquidity
- Ethereum
- Venture Portfolio
website: https://www.unbound.finance/
---
