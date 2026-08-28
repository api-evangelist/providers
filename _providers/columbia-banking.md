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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: First-party commercial and treasury-management API product from Columbia Bank, providing programmatic access to banking data and operations for integration with financial software and ERP platforms. D
  name: Columbia API Banking
  slug: columbia-api-banking
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/columbia-banking-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/columbia-banking-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.columbiabank.com/commercial/api-banking/
- group: company
  title: ''
  type: Website
  url: https://www.columbiabank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.columbiabank.com/commercial/api-banking/
- group: company
  title: ''
  type: Blog
  url: https://www.columbiabank.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.columbiabank.com/help-center/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/umpqua-bank
created: '2026-07-23'
description: 'Columbia Bank is an Oregon state-chartered commercial bank and the principal banking subsidiary of Columbia Banking System, Inc. (NASDAQ: COLB), a West Coast regional bank holding company headquartered in Tacoma, Washington with more than $50 billion in assets. The bank took the legal name "Columbia Bank" effective July 1, 2025, having previously operated as Umpqua Bank following the 2023 merger of Columbia Banking System and Umpqua Holdings Corporation. On the open-finance front, Columbia is one of the relatively few US regional banks to run a first-party developer surface: Columbia API Banking, a commercial and treasury-management integration product exposing capabilities such as book transfers, ACH file imports, positive pay, stop-payment and NSF management, lockbox management, transaction and statement search, check images, and real-time account balances in JSON and XML, backed by a production-ready SDK and the gated Columbia API Portal. That surface is commercial/ERP-oriented
  rather than a self-serve public developer portal, and consumer-permissioned data access is instead delivered through the Plaid aggregator. No documented FDX participation or published CFPB Section 1033 posture was found.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Columbia Bank
nav: Providers
network: true
overview: 'Columbia Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Regional Bank, and Commercial Banking.


  Columbia Bank''s developer surface includes documentation, engineering blog, support, and 5 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 8.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/columbia-banking/refs/heads/main/screenshots/columbia-banking-2026-07-25T210116.png
security:
- kind: domain-security
  name: Columbia Banking Domain Security
  slug: columbia-banking-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: columbia-banking
tags:
- Financial-Services
- Banking
- United States
- Regional Bank
- Commercial Banking
- Treasury Management
- Open Finance
- Data Aggregation
website: https://www.columbiabank.com/
---
