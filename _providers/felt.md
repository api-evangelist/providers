---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Felt Agentic Access
  operation_count: 51
  slug: felt-agentic-access
  summary_line: 51 operations · 34 acting
api_count: 13
apis:
- description: 'JavaScript SDK for embedding, controlling, and extending Felt maps in external web applications. Supports two integration modes: Extensions (custom code inside Felt) and Embed (Felt maps inside extern'
  name: Felt JavaScript SDK
  slug: felt-javascript-sdk
- description: Official Python client for the Felt REST API providing convenient wrappers for map creation, file and DataFrame uploads, layer styling and refreshing, and element management. Supports Pandas and GeoPa
  name: Felt Python SDK
  slug: felt-python-sdk
- description: Comments bring conversations to mapping. With these APIs, you can export, resolve, and delete map comments and collaboration threads.
  name: Felt Comments API
  slug: felt-comments-api
- description: Elements enable you to annotate maps with custom shapes, text, and markers. With these APIs, you can create, update, and delete map elements.
  name: Felt Elements API
  slug: felt-elements-api
- description: Embed tokens enable safely sharing your private maps. With these APIs, you can generate secure tokens for embedding maps.
  name: Felt Embed Tokens API
  slug: felt-embed-tokens-api
- description: With these APIs, you can export data to CSV, GeoJSON, and other formats.
  name: Felt Layer Exports API
  slug: felt-layer-exports-api
- description: With these APIs, you can publish your layers to your workspace library.
  name: Felt Layer Library API
  slug: felt-layer-library-api
- description: With these APIs, you can upload your data to create new layers.
  name: Felt Layer Uploads API
  slug: felt-layer-uploads-api
- description: Layers enable you to visualize, style and interact with your spatial data. With these APIs, you can upload data, manage layer styling, publish and refresh live data layers.
  name: Felt Layers API
  slug: felt-layers-api
- description: Maps are the centerpiece of Felt. With these APIs, you can create, retrieve, update, delete, move, and duplicate maps programmatically.
  name: Felt Maps API
  slug: felt-maps-api
- description: Projects help you organize maps and manage team permissions. With these APIs, you can manage the projects in your workspace.
  name: Felt Projects API
  slug: felt-projects-api
- description: Sources connect your databases to Felt. With these APIs, you can configure data source connections, credentials, and sync settings to create live maps.
  name: Felt Sources API
  slug: felt-sources-api
- description: Users represent the people in your workspace. With these APIs, you can retrieve user profile information.
  name: Felt Users API
  slug: felt-users-api
artifact_total: 31
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/felt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/felt-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/felt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/felt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/felt-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://felt.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.felt.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/felt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/feltmaps
- group: company
  title: ''
  type: Blog
  url: https://felt.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://felt.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/felt
- group: commercial
  title: ''
  type: Plans
  url: plans/felt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/felt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/felt-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/felt-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/felt-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: https://felt.com/blog/rss.xml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-12'
description: Felt is a collaborative mapping platform with a REST API for creating and managing maps, layers, elements, and sharing settings programmatically. The Enterprise-tier REST API and JavaScript SDK enable developers to build custom mapping applications, automate geospatial workflows, embed maps, and integrate with data pipelines using Bearer token authentication against the https://felt.com/api/v2 base URL.
examples:
- key_count: 1
  name: Felt Api Examples
  slug: felt-api-examples
finops:
- name: Felt Finops
  service_category: ''
  slug: felt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/felt.png
json_schemas:
- name: EmbedToken
  property_count: 2
  slug: felt-embedtoken
- name: Layer
  property_count: 23
  slug: felt-layer
- name: LayerGroup
  property_count: 10
  slug: felt-layergroup
- name: Map
  property_count: 18
  slug: felt-map
- name: Project
  property_count: 6
  slug: felt-project
- name: Source
  property_count: 13
  slug: felt-source
- name: User
  property_count: 3
  slug: felt-user
jsonld:
- class_count: 25
  name: Felt Context
  property_count: 9
  slug: felt-context
layout: provider
modified: '2026-06-12'
name: Felt
nav: Providers
network: true
overview: 'Felt publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Comments API, Elements API, Embed Tokens API, and 8 more. Tagged areas include Maps, GIS, Geospatial, Collaborative, and Mapping.


  The Felt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Felt''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Felt Plans Pricing
  plan_count: 3
  slug: felt-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Felt Rate Limits
  slug: felt-rate-limits
rules:
- name: Felt API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: felt-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.3
  delta: -5.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 71.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/felt/refs/heads/main/screenshots/felt-2026-06-20T181135.png
security:
- kind: authentication
  name: Felt Authentication
  slug: felt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Felt Domain Security
  slug: felt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Felt Vulnerability Disclosure
  slug: felt-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Felt Trust Center
  slug: felt-trust-center
  summary_line: SOC 2, GDPR
slug: felt
tags:
- Maps
- GIS
- Geospatial
- Collaborative
- Mapping
- Layers
- Embedding
website: https://felt.com
---
