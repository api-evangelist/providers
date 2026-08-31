---
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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinshift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coinshift.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coinshift.xyz/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coinshift.xyz/business/primer-and-peaks/first-steps
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/coinshift
- group: start
  title: ''
  type: SignUp
  url: https://coinshift.global/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinshift.xyz/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coinshift-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.coinshift.xyz/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/coinshift-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coinshift-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coinshift-conformance.yml
coverage:
  checked: '2026-08-09'
  detail: Coinshift ships only end-user software — docs.coinshift.xyz publishes a complete, crawlable llms.txt index of 136 pages and every one of them is a product walkthrough or a csUSDL/csUSDC asset explainer, with no developer portal, API reference, SDK or webhook page anywhere in it; the only HTTP backend behind the app, uspc-prod.up.railway.app, is undocumented and answers 404 NOT_FOUND to /openapi.json, /graphql, /mcp and every other discovery path.
  evidence:
  - status: 200
    url: https://docs.coinshift.xyz/llms.txt
  - status: 404
    url: https://docs.coinshift.xyz/openapi.json
  - status: 404
    url: https://uspc-prod.up.railway.app/openapi.json
  - status: 404
    url: https://uspc-prod.up.railway.app/graphql
  - status: 404
    url: https://uspc-prod.up.railway.app/mcp
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'Coinshift is a non-custodial, multi-chain onchain treasury management platform for startups, DAOs and crypto-native organisations, founded in 2021 as MultiSafe and built on top of Safe (Gnosis Safe) multisig accounts. The application unifies portfolio tracking across ERC-20 tokens and NFTs, multi-signature proposal and transaction workflows, mass and recurring payouts, contact and label management, CSV transaction export and cash-flow reporting, plus embedded dApp integrations for Aave, CoW Swap, 1inch, LI.FI, ParaSwap, Hedgey, Request Finance and Superfluid money streams, with Slack and Discord signing notifications. Coinshift also issues onchain yield assets — csUSDL, an ERC-4626 vault receipt token for USDL deposited into the Coinshift USDL Morpho Vault, csUSDC, the SHIFT governance token, and the iUSPC institutional credit product. Coinshift publishes no public developer API: the documentation at docs.coinshift.xyz is entirely end-user product and asset guidance, with no
  developer portal, API reference, OpenAPI, GraphQL schema or webhook catalog.'
image: https://app.coinshift.xyz/images/logo.svg
layout: provider
modified: '2026-08-09'
name: Coinshift
nav: Providers
network: true
overview: 'Coinshift is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, crypto-treasury-management, digital-assets, decentralized-finance, and stablecoins.


  Coinshift''s developer surface includes documentation, getting-started guide, support, signup flow, and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 10.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Coinshift Domain Security
  slug: coinshift-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: coinshift
tags:
- Company
- crypto-treasury-management
- digital-assets
- decentralized-finance
- stablecoins
- multisig
- Payments
- Payouts
- accounting
- Web3
- ethereum
- daos
website: https://www.coinshift.xyz/
---
