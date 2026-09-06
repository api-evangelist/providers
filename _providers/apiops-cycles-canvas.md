---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Apiops Cycles Canvas Agentic Access
  operation_count: 6
  slug: apiops-cycles-canvas-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.example.com
  baseurl_source: spec
  description: Placing and managing of products placed for products.
  name: APIOps Cycles Canvas Products API
  slug: apiops-cycles-canvas-products-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Products API
  slug: open-apiops-cycles-canvas-products-api
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
random_paper: 5
rate_limits:
- limit_count: 2
  name: Apiops Cycles Canvas Rate Limits
  slug: apiops-cycles-canvas-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: APIOps Cycles Canvas API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apiops-cycles-canvas-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 66.9
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
