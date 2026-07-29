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
    agentic_access: derived
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Singularity Net Agentic Access
  operation_count: 9
  slug: singularity-net-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 5
apis:
- description: 'The SingularityNET AI Marketplace REST API provides service discovery, organization management, and metadata access for the decentralized AI network. Allows consumers to browse available AI services, '
  name: SingularityNET Marketplace API
  slug: singularitynet-marketplace-api
- description: Payment channel management for service access
  name: SingularityNET Channels API
  slug: singularity-net-channels-api
- description: AI service provider organization management
  name: SingularityNET Organizations API
  slug: singularity-net-organizations-api
- description: Service endpoint group management
  name: SingularityNET Service Groups API
  slug: singularity-net-service-groups-api
- description: AI service discovery and metadata
  name: SingularityNET Services API
  slug: singularity-net-services-api
artifact_total: 17
collections:
- collection_type: open
  name: SingularityNET Marketplace API
  slug: open-singularitynet-marketplace
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/singularity-net-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/singularity-net-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.singularitynet.io/feed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/singularitynet
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/singnet
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.singularitynet.io
- group: docs
  title: ''
  type: Documentation
  url: https://dev.singularitynet.io/docs/products/DecentralizedAIPlatform/
- group: other
  title: ''
  type: AIMarketplace
  url: https://marketplace.singularitynet.io
- group: other
  title: ''
  type: Whitepaper
  url: https://public.singularitynet.io/whitepaper.pdf
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/singnet/snet-sdk-python
- group: build
  title: ''
  type: DaemonGitHub
  url: https://github.com/singnet/snet-daemon
- group: commercial
  title: ''
  type: TermsOfService
  url: https://singularitynet.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://singularitynet.io/privacy-policy
created: '2026-05-02'
description: SingularityNET is a decentralized AI services marketplace built on blockchain. Developers can publish AI services to the network and consumers can access them using the ASI (FET) token. The platform uses a daemon (snetd) that exposes AI applications as gRPC APIs accessible through the SingularityNET Network, with a REST API for marketplace interaction and service discovery.
examples:
- key_count: 4
  name: Singularitynet List Services Example
  slug: singularitynet-list-services-example
finops:
- name: Singularity Net Finops
  service_category: API
  slug: singularity-net-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/singularity-net.png
json_schemas:
- name: SingularityNET Service
  property_count: 12
  slug: singularitynet-service
json_structures:
- name: Singularitynet Service Structure
  property_count: 0
  slug: singularitynet-service-structure
jsonld:
- class_count: 33
  name: Singularitynet Context
  property_count: 0
  slug: singularitynet-context
layout: provider
modified: '2026-05-02'
name: SingularityNET
nav: Providers
network: true
overview: 'SingularityNET publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Organizations API, Service Groups API, and 1 more. Tagged areas include Artificial Intelligence, Blockchain, Decentralized AI, AI Marketplace, and Web3.


  The SingularityNET catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SingularityNET''s developer surface includes engineering blog, documentation, and 11 more developer resources.'
plans:
- name: Singularity Net Plans Pricing
  plan_count: 3
  slug: singularity-net-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Singularity Net Rate Limits
  slug: singularity-net-rate-limits
rules:
- name: SingularityNET API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: singularity-net-jsonschema-spectral-rules
- name: SingularityNET API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: singularitynet-rules
score:
  band: developing
  composite: 49.8
  delta: -4.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/singularity-net/refs/heads/main/screenshots/singularity-net-2026-06-20T193947.png
security:
- kind: domain-security
  name: Singularity Net Domain Security
  slug: singularity-net-domain-security
  summary_line: TLSv1.3 · DMARC
slug: singularity-net
tags:
- Artificial Intelligence
- Blockchain
- Decentralized AI
- AI Marketplace
- Web3
website: https://dev.singularitynet.io
---
