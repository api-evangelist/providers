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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 12
apis:
- description: Free public REST API that returns whether a given crypto address is identified as sanctioned by OFAC or other major sanctions authorities. No commercial licence required; widely embedded by wallets, d
  name: Chainalysis Sanctions Screening API
  slug: sanctions-screening
- description: 'Enterprise REST API for real-time anti-money-laundering monitoring of crypto transactions - register deposits, withdrawals, and transfers, and receive risk scoring, alerts, and exposure breakdowns by '
  name: Chainalysis KYT API
  slug: kyt-api
- description: 'Enterprise REST API for assessing a wallet''s risk exposure - returns categorised exposure (e.g. darknet markets, sanctions, scams) and a risk score for a given address. Used to gate counterparties at '
  name: Chainalysis Address Screening API
  slug: address-screening
- description: Enterprise REST API exposing Chainalysis's labelled-entity dataset - look up the entity behind a given address (exchange, mixer, sanctioned actor, scam, etc.) and retrieve entity metadata for complian
  name: Chainalysis Entities API
  slug: entities-api
- description: Investigation product for tracing funds across blockchains - graph explorer, address clustering, and case management used by law enforcement, government, and private investigators. Web UI plus complem
  name: Chainalysis Reactor
  slug: reactor
- description: Managed investigation service where Chainalysis analysts conduct or assist with crypto-related investigations on behalf of customers, including expert testimony, asset recovery support, and intelligen
  name: Chainalysis Crypto Investigations
  slug: crypto-investigations
- description: AI-powered triage product for instant assessment of crypto addresses and transactions - surfaces key risk and entity context to speed up investigations and compliance reviews.
  name: Chainalysis Rapid
  slug: rapid
- description: Tool for scanning recovered seed phrases against the blockchain to identify wallets holding seizable cryptocurrency, used in law-enforcement asset-seizure workflows.
  name: Chainalysis Wallet Scan
  slug: wallet-scan
- description: Risk-profile product for Virtual Asset Service Providers - assesses exchanges and other VASPs against AML, sanctions, and counterparty risk criteria for use in correspondent and partnership decisions.
  name: Chainalysis VASP Risking
  slug: vasp-risking
- description: Stablecoin-focused risk product that evaluates the risk profile of individual stablecoins, their issuers, and circulation patterns.
  name: Chainalysis Sentinel
  slug: sentinel
- description: Web3 security product (acquired by Chainalysis) that monitors smart contracts and on-chain activity in real time to detect and prevent exploits, governance attacks, and protocol risk events.
  name: Hexagate (Chainalysis)
  slug: hexagate
- description: AI-powered fraud prevention product (acquired by Chainalysis) that identifies scams and fraud-victim relationships to help exchanges and payment platforms intervene before funds are sent to bad actors
  name: Alterya (Chainalysis)
  slug: alterya
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chainalysis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chainalysis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chainalysis.com/
- group: operate
  title: ''
  type: Support
  url: https://support.chainalysis.com/
- group: other
  title: ''
  type: Sanctions
  url: https://go.chainalysis.com/chainalysis-oracle-docs.html
- group: company
  title: ''
  type: Blog
  url: https://www.chainalysis.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chainalysis/
- group: other
  title: ''
  type: X
  url: https://x.com/chainalysis
created: '2026-05-23'
description: Chainalysis is a blockchain analysis company providing data, software, and research to government agencies, exchanges, banks, and crypto businesses for compliance, investigation, and risk management. Core products include KYT (real-time transaction monitoring), Address Screening, the publicly hosted Sanctions API, Reactor (investigations and fund tracing), Crypto Investigations, Wallet Scan, Rapid (AI-assisted triage), VASP Risking, and Sentinel (stablecoin risk). Security-side products include Hexagate (web3 threat prevention) and Alterya (fraud prevention). Most APIs are REST-based and gated behind enterprise contracts, except the free public Sanctions Screening API.
finops:
- name: Chainalysis Finops
  service_category: API
  slug: chainalysis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chainalysis.png
layout: provider
modified: '2026-05-23'
name: Chainalysis
nav: Providers
network: true
overview: 'Chainalysis publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, AML, KYT, Sanctions, and Investigations.


  Chainalysis'' developer surface includes documentation, support, engineering blog, and 5 more developer resources.'
plans:
- name: Chainalysis Plans Pricing
  plan_count: 1
  slug: chainalysis-plans-pricing
random_paper: 133
rate_limits:
- limit_count: 2
  name: Chainalysis Rate Limits
  slug: chainalysis-rate-limits
score:
  band: emerging
  composite: 19.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chainalysis/refs/heads/main/screenshots/chainalysis-2026-06-20T174208.png
security:
- kind: domain-security
  name: Chainalysis Domain Security
  slug: chainalysis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chainalysis
tags:
- Compliance
- AML
- KYT
- Sanctions
- Investigations
- Blockchain Analytics
- Risk
- Crypto
website: https://www.chainalysis.com/
---
