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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openbazaar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openbazaar.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenBazaar
created: '2026-07-17'
description: OpenBazaar is an open-source, decentralized peer-to-peer marketplace protocol that let buyers and sellers trade goods and services directly with one another using cryptocurrency, with no central company, listing fees, or intermediaries taking a cut. Trades were coordinated over a distributed network built on IPFS and libp2p, settled with Bitcoin and other cryptocurrencies, and secured with multisignature escrow and third-party moderation. The project originated from the DarkMarket proof-of-concept and was developed and funded by the company OB1 (backed by a16z, Union Square Ventures, and others). The OpenBazaar server daemon exposed a local JSON REST API on the node that desktop, mobile, and web clients used to manage listings, orders, wallets, and profiles. OB1 wound down commercial operations and the hosted services in early 2021, and the code was open-sourced to the community. The openbazaar.org site now advertises an in-development "OpenBazaar 3.0" successor, and the GitHub
  organization hosts the legacy Python (1.0) and Go (2.0) daemons alongside newer Rust and browser-based clients.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openbazaar.png
layout: provider
modified: '2026-07-20'
name: OpenBazaar
nav: Providers
network: true
overview: OpenBazaar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Decentralized, Peer-to-Peer, and Cryptocurrency.
random_paper: 9
score:
  band: minimal
  composite: 5.3
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openbazaar/refs/heads/main/screenshots/openbazaar-2026-08-07T190534.png
security:
- kind: domain-security
  name: Openbazaar Domain Security
  slug: openbazaar-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openbazaar
tags:
- Company
- Marketplace
- Decentralized
- Peer-to-Peer
- Cryptocurrency
- Bitcoin
- E-Commerce
- Open-Source
- Blockchain
website: https://openbazaar.org
---
