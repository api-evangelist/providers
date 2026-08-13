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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: API Harmony was an intelligent API matchmaking service that used graph technology and machine learning to search public APIs, reveal relationships between them, make recommendations, and identify gaps
  name: API Harmony Service
  slug: api-harmony-service
artifact_total: 16
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/api-harmony-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-harmony-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.ibm.com/apiharmony/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ibm.com/api/view/apiharmony-prod:apih-product:title-API_Harmony
- group: other
  title: ''
  type: Research
  url: https://research.ibm.com/publications/api-harmony-graph-based-search-and-selection-of-apis-in-the-cloud
- group: other
  title: ''
  type: Article
  url: https://www.linuxjournal.com/node/1338947
created: '2026-03-26'
description: API Harmony was an API discovery and recommendation tool from IBM Research that used graph-based search, machine learning, and cognitive technologies to help developers find, compare, and select compatible APIs. It was offered as a cloud service on IBM Bluemix and has since been discontinued.
features:
- description: Graph-based search across public APIs to reveal relationships and connections between services.
  name: API Graph Search
- description: Machine learning-powered recommendations for compatible APIs based on developer intent and context.
  name: API Recommendation
- description: Tooling to help developers compose multiple APIs into unified applications.
  name: API Composition Support
- description: Unified catalog and discovery interface for cloud-hosted and public APIs.
  name: API Discovery
- description: Tools for API providers to publish and promote their APIs to the ecosystem.
  name: API Publishing
- description: Identifies gaps in the API ecosystem where no existing API satisfies a developer need.
  name: Gap Identification
finops:
- name: Api Harmony Finops
  service_category: API
  slug: api-harmony-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-harmony.png
layout: provider
modified: '2026-04-19'
name: API Harmony
nav: Providers
network: true
overview: 'API Harmony publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Aggregation, API Discovery, API Recommendation, Graph Technology, and IBM.


  API Harmony''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Api Harmony Plans Pricing
  plan_count: 3
  slug: api-harmony-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Api Harmony Rate Limits
  slug: api-harmony-rate-limits
score:
  band: minimal
  composite: 11.9
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-harmony/refs/heads/main/screenshots/api-harmony-2026-06-20T172217.png
security:
- kind: domain-security
  name: Api Harmony Domain Security
  slug: api-harmony-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Api Harmony Vulnerability Disclosure
  slug: api-harmony-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: api-harmony
tags:
- API Aggregation
- API Discovery
- API Recommendation
- Graph Technology
- IBM
- Machine Learning
use_cases:
- description: Help developers find the right APIs for cloud-based application development on IBM Bluemix.
  name: Cloud API Discovery
- description: Identify which APIs can be combined for a given use case without conflicts or duplication.
  name: API Compatibility Analysis
- description: API providers could publish and promote their services to the broader developer ecosystem.
  name: API Portfolio Management
- description: Support microservices architectures by identifying optimal third-party API combinations.
  name: Microservices Integration
website: https://developer.ibm.com/apiharmony/
---
