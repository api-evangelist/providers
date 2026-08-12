---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Terrain Discovery Environment Api Agentic Access
  operation_count: 27
  slug: terrain-discovery-environment-api-agentic-access
  summary_line: 27 operations · 13 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Job submission, monitoring, and management
  name: Terrain Discovery Environment API Analyses API
  slug: terrain-discovery-environment-api-analyses-api
- description: Application metadata, discovery, and management
  name: Terrain Discovery Environment API Apps API
  slug: terrain-discovery-environment-api-apps-api
- description: Token and authentication management
  name: Terrain Discovery Environment API Authentication API
  slug: terrain-discovery-environment-api-authentication-api
- description: iRODS filesystem operations - browse, create, move, delete files and directories
  name: Terrain Discovery Environment API Filesystem API
  slug: terrain-discovery-environment-api-filesystem-api
- description: Permanent identifier (DOI) requests
  name: Terrain Discovery Environment API Identifiers API
  slug: terrain-discovery-environment-api-identifiers-api
- description: File and data metadata annotation
  name: Terrain Discovery Environment API Metadata API
  slug: terrain-discovery-environment-api-metadata-api
- description: User notification management
  name: Terrain Discovery Environment API Notifications API
  slug: terrain-discovery-environment-api-notifications-api
- description: Full-text search across data and apps
  name: Terrain Discovery Environment API Search API
  slug: terrain-discovery-environment-api-search-api
- description: Data sharing and permissions
  name: Terrain Discovery Environment API Sharing API
  slug: terrain-discovery-environment-api-sharing-api
artifact_total: 22
collections:
- collection_type: open
  name: Terrain Discovery Environment API
  slug: open-terrain
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/terrain-discovery-environment-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terrain-discovery-environment-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/terrain-discovery-environment-api-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://cyverse.org/Science-APIs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cyverse.org
- group: other
  title: ''
  type: Repository
  url: https://github.com/cyverse-de/terrain
- group: start
  title: ''
  type: Portal
  url: https://de.cyverse.org
- group: learn
  title: ''
  type: Webinar
  url: https://cyverse.org/webinar_TerrainAPI
- group: auth
  title: ''
  type: Authentication
  url: https://docs.cyverse.org/services/getting_started/
created: '2026-03-16'
description: Terrain is the primary REST API gateway for CyVerse's Discovery Environment (DE), an open-source data science workbench. Terrain validates user authentication via Keycloak/JWT and orchestrates calls to backend microservices covering filesystem operations, application management, data analysis, metadata annotation, notifications, and persistent identifier management.
examples:
- key_count: 2
  name: Terrain List Directory Example
  slug: terrain-list-directory-example
finops:
- name: Terrain Discovery Environment Api Finops
  service_category: API
  slug: terrain-discovery-environment-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terrain-discovery-environment-api.png
json_schemas:
- name: Terrain Analysis
  property_count: 11
  slug: terrain-analysis
json_structures:
- name: Terrain Filesystem Structure
  property_count: 0
  slug: terrain-filesystem-structure
jsonld:
- class_count: 29
  name: Terrain Discovery Environment Api Context
  property_count: 0
  slug: terrain-discovery-environment-api-context
layout: provider
modified: '2026-05-19'
name: Terrain Discovery Environment API
nav: Providers
network: true
overview: 'Terrain Discovery Environment API publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Analyses API, Apps API, Authentication API, and 6 more. Tagged areas include Bioinformatics, Data Science, Life Sciences, Filesystem, and Cloud Computing.


  The Terrain Discovery Environment API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Terrain Discovery Environment API''s developer surface includes authentication, developer portal, documentation, and 6 more developer resources.'
plans:
- name: Terrain Discovery Environment Api Plans Pricing
  plan_count: 3
  slug: terrain-discovery-environment-api-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Terrain Discovery Environment Api Rate Limits
  slug: terrain-discovery-environment-api-rate-limits
rules:
- name: Terrain Discovery Environment API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: terrain-discovery-environment-api-jsonschema-spectral-rules
- name: Terrain Discovery Environment API API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 5
  slug: terrain-rules
score:
  band: thin
  composite: 37.8
  delta: -7.2
  facets:
    commercial_clarity: 15.8
    contract_quality: 65.7
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 7.9
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/terrain-discovery-environment-api/refs/heads/main/screenshots/terrain-discovery-environment-api-2026-06-20T195131.png
security:
- kind: authentication
  name: Terrain Discovery Environment Api Authentication
  slug: terrain-discovery-environment-api-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Terrain Discovery Environment Api Domain Security
  slug: terrain-discovery-environment-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: terrain-discovery-environment-api
tags:
- Bioinformatics
- Data Science
- Life Sciences
- Filesystem
- Cloud Computing
- Open Source
website: https://cyverse.org/Science-APIs
---
