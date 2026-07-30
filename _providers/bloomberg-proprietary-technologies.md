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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Bloomberg's proprietary socket-based API protocol for accessing Bloomberg data, providing a high-performance connectivity layer between client applications and Bloomberg's data infrastructure.
  name: Bloomberg Open API (BLPAPI)
  slug: blpapi
- description: The Financial Instrument Global Identifier (FIGI) is Bloomberg's open standard for identifying financial instruments. The OpenFIGI API allows free mapping of tickers, ISINs, CUSIPs, and other identifi
  name: Bloomberg FIGI API
  slug: figi-api
- description: Bloomberg's proprietary query language enabling flexible data requests with filtering, aggregation, and calculated field capabilities across Bloomberg's data universe.
  name: Bloomberg Query Language (BQL)
  slug: bql
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-proprietary-technologies-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bloomberg.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg Proprietary Technologies encompasses the internally developed technology innovations that power Bloomberg's products and services. This includes Bloomberg's proprietary data network, the BLPAPI connectivity protocol, BQL query language, B-PIPE data distribution technology, FIGI (Financial Instrument Global Identifier) system, and the Bloomberg Generative AI capabilities integrated into its financial data platform.
features:
- description: Proprietary socket protocol for high-performance Bloomberg data connectivity.
  name: BLPAPI Protocol
- description: Proprietary query language for flexible financial data requests.
  name: Bloomberg Query Language
- description: Open standard financial instrument identifier with free API access.
  name: FIGI Identifier System
- description: Proprietary managed data distribution technology for enterprise.
  name: B-PIPE Distribution
- description: Machine learning and AI capabilities integrated into Bloomberg data products.
  name: Bloomberg AI/ML
- description: Cloud-native infrastructure enabling Bloomberg data access from major cloud platforms.
  name: Bloomberg Cloud Infrastructure
finops:
- name: Bloomberg Proprietary Technologies Finops
  service_category: API
  slug: bloomberg-proprietary-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-proprietary-technologies.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Proprietary Technologies
nav: Providers
network: true
overview: 'Bloomberg Proprietary Technologies publishes 1 API on the [APIs.io](https://apis.io/) network: Bloomberg FIGI API. Tagged areas include Proprietary Technology, BLPAPI, BQL, FIGI, and B-PIPE.


  Bloomberg Proprietary Technologies'' developer surface includes developer portal, documentation, support, and 4 more developer resources.'
plans:
- name: Bloomberg Proprietary Technologies Plans Pricing
  plan_count: 3
  slug: bloomberg-proprietary-technologies-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Bloomberg Proprietary Technologies Rate Limits
  slug: bloomberg-proprietary-technologies-rate-limits
score:
  band: thin
  composite: 35.8
  delta: -3.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.3
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-proprietary-technologies/refs/heads/main/screenshots/bloomberg-proprietary-technologies-2026-06-20T173458.png
security:
- kind: domain-security
  name: Bloomberg Proprietary Technologies Domain Security
  slug: bloomberg-proprietary-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-proprietary-technologies
tags:
- Proprietary Technology
- BLPAPI
- BQL
- FIGI
- B-PIPE
- Financial Technology
- Bloomberg
use_cases:
- description: Map and resolve financial instrument identifiers using FIGI.
  name: Instrument Identification
- description: Build custom data requests using Bloomberg Query Language.
  name: Custom Data Queries
- description: Connect enterprise systems to Bloomberg data via BLPAPI.
  name: System Integration
  url: https://bloomberg.github.io/blpapi-docs/
website: https://www.bloomberg.com/professional/
---
