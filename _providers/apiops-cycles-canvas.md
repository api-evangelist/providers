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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Apiops Cycles Canvas Agentic Access
  operation_count: 6
  slug: apiops-cycles-canvas-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: Placing and managing of products placed for products.
  name: APIOps Cycles Canvas Products API
  slug: apiops-cycles-canvas-products-api
artifact_total: 12
collections:
- collection_type: open
  name: Products API
  slug: open-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apiops-cycles-canvas-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apiops-cycles-canvas-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apiops-cycles-canvas-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/APIOpsCycles
- group: company
  title: ''
  type: Website
  url: https://www.apiopscycles.com/
- group: other
  title: ''
  type: APIOpsBusinessModelCanvas
  url: canvases/Canvas_apiBusinessModelCanvas_en-US.json
- group: other
  title: ''
  type: APIOpsValuePropositionCanvas
  url: canvases/Canvas_apiValuePropositionCanvas_en-US.json
- group: other
  title: ''
  type: APIOpsBusinessImpactCanvas
  url: canvases/Canvas_businessImpactCanvas_en-US.json
- group: other
  title: ''
  type: APIOpsCapacityCanvas
  url: canvases/Canvas_capacityCanvas_en-US.json
- group: other
  title: ''
  type: APIOpsCustomerJourneyCanvas
  url: canvases/Canvas_customerJourneyCanvas_en-US.json
- group: other
  title: ''
  type: APIOpsDomainCanvas
  url: canvases/Canvas_domainCanvas_en-US.json
- group: other
  title: ''
  type: APIOpsEventCanvas
  url: canvases/Canvas_eventCanvas_en-US.json
- group: other
  title: ''
  type: APIOpsInteractionCanvas
  url: canvases/Canvas_interactionCanvas_en-US.json
- group: other
  title: ''
  type: APIOpsLocationsCanvas
  url: canvases/Canvas_locationsCanvas_en-US.json
- group: other
  title: ''
  type: APIOpsRestCanvas
  url: canvases/Canvas_restCanvas_en-US.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/apiops-canvas-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apiops-context.jsonld
created: '2024-12-29'
description: APIOps Cycles Canvases are structured workshop tools for API strategy, design, and business modeling. The collection includes 10 canvas types covering API business models, value propositions, capacity planning, customer journeys, domain design, event modeling, interaction design, location analysis, and REST API design, enabling teams to collaborate and align on API decisions using visual canvas methodologies.
finops:
- name: Apiops Cycles Canvas Finops
  service_category: API
  slug: apiops-cycles-canvas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apiops-cycles-canvas.png
json_schemas:
- name: APIOps Canvas
  property_count: 3
  slug: apiops-canvas
json_structures:
- name: Apiops Canvas Structure
  property_count: 3
  slug: apiops-canvas-structure
jsonld:
- class_count: 10
  name: Apiops Context
  property_count: 2
  slug: apiops-context
layout: provider
modified: '2026-05-19'
name: APIOps Cycles Canvas
nav: Providers
network: true
overview: 'APIOps Cycles Canvas publishes 1 API on the [APIs.io](https://apis.io/) network: Products API. Tagged areas include API Design, API Strategy, Business Model, Canvas, and Workshop.


  The APIOps Cycles Canvas catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIOps Cycles Canvas'' developer surface includes authentication and 16 more developer resources.'
plans:
- name: Apiops Cycles Canvas Plans Pricing
  plan_count: 1
  slug: apiops-cycles-canvas-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 2
  name: Apiops Cycles Canvas Rate Limits
  slug: apiops-cycles-canvas-rate-limits
rules:
- name: APIOps Cycles Canvas API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apiops-cycles-canvas-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apiops-cycles-canvas/refs/heads/main/screenshots/apiops-cycles-canvas-2026-06-20T172250.png
security:
- kind: authentication
  name: Apiops Cycles Canvas Authentication
  slug: apiops-cycles-canvas-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apiops Cycles Canvas Domain Security
  slug: apiops-cycles-canvas-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apiops-cycles-canvas
tags:
- API Design
- API Strategy
- Business Model
- Canvas
- Workshop
website: https://www.apiopscycles.com/
---
