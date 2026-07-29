---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rijksmuseum Agentic Access
  operation_count: 5
  slug: rijksmuseum-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: Standards-based bulk harvesting endpoint implementing the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH 2.0). Supports ListRecords, GetRecord, ListMetadataFormats, ListSets, and L
  name: OAI-PMH Harvesting API
  slug: oai-pmh-harvesting-api
- description: Search and browse the Rijksmuseum collection.
  name: Rijksmuseum Collection API
  slug: rijksmuseum-collection-api
- description: Deep-zoom tile pyramids for object web images.
  name: Rijksmuseum Images API
  slug: rijksmuseum-images-api
- description: Retrieve the full record for a single object.
  name: Rijksmuseum Object Details API
  slug: rijksmuseum-object-details-api
- description: Rijksstudio sets curated by Rijksmuseum's online community.
  name: Rijksmuseum User Generated Content API
  slug: rijksmuseum-user-generated-content-api
artifact_total: 30
collections:
- collection_type: open
  name: Rijksmuseum Collection API
  slug: open-rijksmuseum-collection
- collection_type: open
  name: Rijksmuseum Usersets API
  slug: open-rijksmuseum-user-sets
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rijksmuseum-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rijksmuseum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rijksmuseum-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.rijksmuseum.nl/en
- group: docs
  title: ''
  type: Documentation
  url: https://data.rijksmuseum.nl/
- group: docs
  title: Legacy API Documentation (Archived)
  type: Documentation
  url: https://rijksmuseum.github.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rijksmuseum
- group: start
  title: Rijksstudio Account For API Key
  type: Signup
  url: https://www.rijksmuseum.nl/en/rijksstudio
- group: auth
  title: ''
  type: Authentication
  url: https://data.rijksmuseum.nl/object-metadata/api/#access-to-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/rijksmuseum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rijksmuseum-rate-limits.yml
- group: commercial
  title: Information And Data Policy
  type: TermsOfService
  url: https://www.rijksmuseum.nl/en/data/policy
- group: commercial
  title: Public Domain Mark For Most Object Images
  type: License
  url: https://creativecommons.org/publicdomain/mark/1.0/
- group: commercial
  title: CC-BY For Photography Of The Building And Modern Works
  type: License
  url: https://creativecommons.org/licenses/by/4.0/
- group: other
  title: Open Data Policy
  type: Knowledge
  url: https://www.rijksmuseum.nl/en/data/policy
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rijksmuseum-vocabulary.yml
- group: other
  title: Controlled Vocabularies (Actors, Places, Concepts, Events)
  type: Discovery
  url: https://data.rijksmuseum.nl/controlled-vocabularies/
- group: other
  title: SRU Bibliographic Catalogue
  type: Discovery
  url: https://data.rijksmuseum.nl/bibliographic-data/
- group: build
  title: aio_oai_repo — Configurable OAI-PMH Repository Library (Python)
  type: Tools
  url: https://github.com/Rijksmuseum/aio_oai_repo
- group: build
  title: MCP Server (Community — Artwork Exploration And Analysis)
  type: Tools
  url: https://github.com/r-huijts/rijksmuseum-mcp
- group: build
  title: MCP Server (Community — Semantic Search, Provenance, Similarity, Spatial Reasoning)
  type: Tools
  url: https://github.com/kintopp/rijksmuseum-mcp-plus
- group: build
  title: MCP Client (Community — Web Client For MCP+ Server)
  type: Tools
  url: https://github.com/kintopp/rijksmuseum-mcp-client
- group: build
  title: MCP Server (Community — OAI-PMH Harvesting)
  type: Tools
  url: https://github.com/lwsinclair/rijksmuseum-mcp-oaipmh
- group: build
  title: MCP Server (Community — Iconclass Semantic Search)
  type: Tools
  url: https://github.com/kintopp/rijksmuseum-iconclass-mcp
- group: build
  title: MCP Server (Community — Multi-Museum Imagery, Includes Rijksmuseum)
  type: Tools
  url: https://github.com/chandhoke/archival-imagery-mcp
- group: build
  title: PHP Client (Community)
  type: SDKs
  url: https://github.com/hay/rijksmuseumapi
- group: build
  title: Python Client (Community)
  type: SDKs
  url: https://github.com/yutongquan/rijksmuseum_py
- group: build
  title: SimpleOAIHarvester — Reference Harvester Script
  type: CodeExamples
  url: https://github.com/Q42/SimpleOAIHarvester
created: '2026-05-28'
description: Rijksmuseum is the Dutch national museum dedicated to Dutch arts and history, located in Amsterdam. Its RijksData open-data programme exposes more than 800,000 collection object metadata records, 600,000+ public-domain images, 320,000 bibliographic records, 160,000 actor / institution records, and 70,000 controlled-vocabulary terms through a family of JSON-based REST APIs, an OAI-PMH harvesting endpoint, IIIF tile services, and linked-data dumps.
examples:
- key_count: 3
  name: Rijksmuseum Get Collection Object Example
  slug: rijksmuseum-get-collection-object-example
- key_count: 3
  name: Rijksmuseum Get Collection Object Tiles Example
  slug: rijksmuseum-get-collection-object-tiles-example
- key_count: 3
  name: Rijksmuseum Get User Set Example
  slug: rijksmuseum-get-user-set-example
- key_count: 3
  name: Rijksmuseum List User Sets Example
  slug: rijksmuseum-list-user-sets-example
- key_count: 3
  name: Rijksmuseum Search Collection Example
  slug: rijksmuseum-search-collection-example
image: https://www.rijksmuseum.nl/assets/site/img/logo.png
json_schemas:
- name: Rijksmuseum Art Object
  property_count: 46
  slug: rijksmuseum-art-object
- name: Rijksmuseum Art Object Summary
  property_count: 12
  slug: rijksmuseum-art-object-summary
- name: Rijksmuseum Image Tiles
  property_count: 1
  slug: rijksmuseum-image-tiles
- name: Rijksstudio User Set
  property_count: 11
  slug: rijksmuseum-user-set
- name: Rijksstudio User Set Summary
  property_count: 10
  slug: rijksmuseum-user-set-summary
json_structures:
- name: Rijksmuseum Art Object Structure
  property_count: 46
  slug: rijksmuseum-art-object-structure
- name: Rijksmuseum Art Object Summary Structure
  property_count: 12
  slug: rijksmuseum-art-object-summary-structure
- name: Rijksmuseum Image Tiles Structure
  property_count: 1
  slug: rijksmuseum-image-tiles-structure
- name: Rijksmuseum User Set Structure
  property_count: 11
  slug: rijksmuseum-user-set-structure
- name: Rijksmuseum User Set Summary Structure
  property_count: 10
  slug: rijksmuseum-user-set-summary-structure
jsonld:
- class_count: 51
  name: Rijksmuseum Context
  property_count: 17
  slug: rijksmuseum-context
layout: provider
modified: '2026-05-29'
name: Rijksmuseum
nav: Providers
network: true
overview: 'Rijksmuseum publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Collection API, Images API, Object Details API, and 1 more. Tagged areas include Art And Design, Museums, Cultural Heritage, Open Data, and Linked Data.


  The Rijksmuseum catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rijksmuseum''s developer surface includes authentication, documentation, signup flow, tooling, code examples, and 23 more developer resources.'
plans:
- name: Rijksmuseum Plans Pricing
  plan_count: 1
  slug: rijksmuseum-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Rijksmuseum Rate Limits
  slug: rijksmuseum-rate-limits
rules:
- name: Rijksmuseum API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: rijksmuseum-jsonschema-spectral-rules
- name: Rijksmuseum API Rules
  rule_count: 15
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 6
  slug: rijksmuseum-rules
score:
  band: developing
  composite: 44.8
  delta: -6.9
  facets:
    commercial_clarity: 31.6
    contract_quality: 68.6
    developer_ergonomics: 26.1
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rijksmuseum/refs/heads/main/screenshots/rijksmuseum-2026-06-20T193120.png
security:
- kind: authentication
  name: Rijksmuseum Authentication
  slug: rijksmuseum-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rijksmuseum Domain Security
  slug: rijksmuseum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rijksmuseum
tags:
- Art And Design
- Museums
- Cultural Heritage
- Open Data
- Linked Data
- OAI-PMH
- IIIF
- Dutch Heritage
- Public APIs
website: https://www.rijksmuseum.nl/en
---
