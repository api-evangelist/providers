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
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: 'Xact via SWIFT delivers settlement, custody, asset servicing and reporting messages over the SWIFTNet FIN network. The interface uses ISO 15022 MT messages today and is being migrated to ISO 20022 MX '
  name: Clearstream Xact via SWIFT
  slug: xact-via-swift
- description: 'Xact File Transfer offers bulk and report-style exchange of settlement, custody, and collateral messages over SWIFTNet FileAct. Files may be delivered in ISO 15022, ISO 20022, PDF, XML or XLS formats '
  name: Clearstream Xact File Transfer
  slug: xact-file-transfer
- description: Xact Web Portal is the browser-based interface to ClearstreamXact for instructing settlement, custody and collateral activity, monitoring status, and reviewing reports. It complements the SWIFT and Fi
  name: Clearstream Xact Web Portal
  slug: xact-web-portal
- description: CASCADE is the German central securities depository (CSD) settlement platform. CASCADE is reachable via SWIFT FIN/FileAct messages and via MQ-based host-to-host connectivity for instructing domestic a
  name: Clearstream CASCADE (CSD)
  slug: cascade
- description: Vestima is Clearstream's investment fund processing platform. It routes subscription, redemption, switch and transfer orders for mutual funds, ETFs, hedge funds and alternatives, and integrates with S
  name: Clearstream Vestima
  slug: vestima
- description: CmaX is Clearstream's triparty collateral management platform. It automates collateral allocation, optimisation, margining and substitution across repo, securities lending, and OTC derivatives exposur
  name: Clearstream CmaX (Triparty Collateral)
  slug: cmax
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearstream-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clearstream
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearstream
- group: company
  title: ''
  type: Website
  url: https://www.clearstream.com/
- group: start
  title: ''
  type: Portal
  url: https://www.clearstream.com/clearstream-en/products-and-services
- group: docs
  title: ''
  type: Documentation
  url: https://www.clearstream.com/clearstream-en/keydocuments-1-/icsd-1-/connectivity-manuals
- group: operate
  title: ''
  type: Support
  url: https://www.clearstream.com/clearstream-en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearstream.com/clearstream-en/legal-and-regulatory
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clearstream-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clearstream-rules.yml
created: '2024-01-15'
description: Clearstream is a leading provider of post-trade infrastructure services for international securities transactions. They offer settlement, custody, and collateral management services for bonds, equities, and investment funds. The Clearstream developer surface is built on regulated post-trade messaging rather than a public REST API. Clients connect through ClearstreamXact (Web Portal, File Transfer via SWIFTNet FileAct, and Xact via SWIFT FIN), CASCADE via SWIFT and MQ, the CreationOnline / CreationDirect channels, Vestima for fund order routing, and the CmaX triparty collateral platform. Messages follow ISO 15022 and ISO 20022 standards, with ongoing migration toward ISO 20022 driven by the SWIFT CBPR+ programme.
finops:
- name: Clearstream Finops
  service_category: API
  slug: clearstream-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearstream.png
jsonld:
- class_count: 0
  name: Clearstream Context
  property_count: 6
  slug: clearstream-context
layout: provider
modified: '2026-04-23'
name: Clearstream
nav: Providers
network: true
overview: 'Clearstream publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Capital Markets, Collateral Management, Custody, Financial Services, and ISO 15022.


  The Clearstream catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clearstream''s developer surface includes developer portal, documentation, support, and 7 more developer resources.'
plans:
- name: Clearstream Plans Pricing
  plan_count: 3
  slug: clearstream-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Clearstream Rate Limits
  slug: clearstream-rate-limits
rules:
- name: Clearstream API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 8
  slug: clearstream-rules
score:
  band: thin
  composite: 30.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 30.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 35.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clearstream/refs/heads/main/screenshots/clearstream-2026-06-20T174506.png
security:
- kind: domain-security
  name: Clearstream Domain Security
  slug: clearstream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearstream
tags:
- Capital Markets
- Collateral Management
- Custody
- Financial Services
- ISO 15022
- ISO 20022
- Post-Trade Infrastructure
- Securities
- Settlement
- SWIFT
website: https://www.clearstream.com/
---
