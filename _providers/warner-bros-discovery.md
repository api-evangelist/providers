---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Warner Bros Discovery Agentic Access
  operation_count: 7
  slug: warner-bros-discovery-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- description: Media asset management
  name: Warner Bros. Discovery Assets API
  slug: warner-bros-discovery-assets-api
- description: Media content delivery management
  name: Warner Bros. Discovery Deliveries API
  slug: warner-bros-discovery-deliveries-api
- description: Content metadata and manifest submission
  name: Warner Bros. Discovery Metadata API
  slug: warner-bros-discovery-metadata-api
- description: Delivery and validation status tracking
  name: Warner Bros. Discovery Status API
  slug: warner-bros-discovery-status-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Warner Bros. Discovery Content Partner Assets API
  slug: open-warner-bros-discovery-assets-api
- collection_type: open
  name: Warner Bros. Discovery Content Partner API
  slug: open-warner-bros-discovery-content-partner
- collection_type: open
  name: Warner Bros. Discovery Content Partner Assets Deliveries API
  slug: open-warner-bros-discovery-deliveries-api
- collection_type: open
  name: Warner Bros. Discovery Content Partner Assets Metadata API
  slug: open-warner-bros-discovery-metadata-api
- collection_type: open
  name: Warner Bros. Discovery Content Partner Assets Status API
  slug: open-warner-bros-discovery-status-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/warner-bros-discovery-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/warner-bros-discovery-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/warner-bros-discovery-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/warner-bros-discovery-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/warner-bros-discovery
- group: company
  title: ''
  type: Website
  url: https://www.wbd.com/
- group: start
  title: ''
  type: Portal
  url: https://partnerhub.warnermedia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://partnerhub.warnermedia.com/specifications-and-guides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WarnerMedia
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/warnerbros
- group: company
  title: ''
  type: Website
  url: https://www.max.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.wbd.com/
created: '2026-03-21'
description: Warner Bros. Discovery is a leading global media and entertainment company that creates and distributes the world's most differentiated and complete portfolio of branded content across television, film, and streaming. WBD operates the Max streaming platform, Warner Bros. film studio, HBO, CNN, Discovery, TNT, TBS, and many other brands. The company provides content partner APIs for media supply chain integration and maintains open source projects through its engineering teams.
examples:
- key_count: 2
  name: Warner Bros Discovery Listdeliveries Example
  slug: warner-bros-discovery-listDeliveries-example
finops:
- name: Warner Bros Discovery Finops
  service_category: Entertainment / Media
  slug: warner-bros-discovery-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/warner-bros-discovery.png
json_schemas:
- name: Warner Bros. Discovery Content Delivery
  property_count: 8
  slug: warner-bros-discovery-content
json_structures:
- name: Warner Bros Discovery Content Structure
  property_count: 0
  slug: warner-bros-discovery-content-structure
jsonld:
- class_count: 6
  name: Warner Bros Discovery Context
  property_count: 11
  slug: warner-bros-discovery-context
layout: provider
modified: '2026-05-19'
name: Warner Bros. Discovery
nav: Providers
network: true
overview: 'Warner Bros. Discovery publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Deliveries API, Metadata API, and 1 more. Tagged areas include Entertainment, Media, Streaming, Content, and Television.


  The Warner Bros. Discovery catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Warner Bros. Discovery''s developer surface includes authentication, developer portal, documentation, and 9 more developer resources.'
plans:
- name: Warner Bros Discovery Plans Pricing
  plan_count: 1
  slug: warner-bros-discovery-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Warner Bros Discovery Rate Limits
  slug: warner-bros-discovery-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Warner Bros. Discovery API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: warner-bros-discovery-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Warner Bros. Discovery API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 4
  slug: warner-bros-discovery-rules
scopes:
- name: Warner Bros Discovery Scopes
  scope_count: 4
  slug: warner-bros-discovery-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 69.8
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/warner-bros-discovery/refs/heads/main/screenshots/warner-bros-discovery-2026-06-20T201227.png
security:
- kind: authentication
  name: Warner Bros Discovery Authentication
  slug: warner-bros-discovery-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Warner Bros Discovery Domain Security
  slug: warner-bros-discovery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: warner-bros-discovery
tags:
- Entertainment
- Media
- Streaming
- Content
- Television
- Film
website: https://www.wbd.com/
---
