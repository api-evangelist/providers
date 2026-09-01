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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The OpenUSD C++ API is the primary interface for working with Universal Scene Description data. Provides access to USD core (scene composition and asset management), UsdImaging and Hydra (rendering in
  name: OpenUSD C++ API
  slug: openusd-c-api
- description: OpenUSD provides comprehensive Python bindings for all major C++ modules, enabling scripting and pipeline integration in Python-based DCC workflows. Python bindings cover the full USD API including px
  name: OpenUSD Python Bindings
  slug: openusd-python-bindings
artifact_total: 29
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/PixarAnimationStudios/OpenUSD/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/PixarAnimationStudios/OpenUSD/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/PixarAnimationStudios/OpenUSD/blob/dev/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/PixarAnimationStudios/OpenUSD/blob/dev/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/PixarAnimationStudios/OpenUSD/blob/dev/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aousd-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allianceopenusd
- group: start
  title: ''
  type: Portal
  url: https://aousd.org
- group: docs
  title: ''
  type: Documentation
  url: https://openusd.org/release/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://openusd.org/release/tut_usd_tutorials.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PixarAnimationStudios
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/PixarAnimationStudios/OpenUSD
- group: docs
  title: USD Layer Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/aousd/refs/heads/main/json-schema/aousd-usd-layer-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/aousd/refs/heads/main/vocabulary/aousd-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://aousd.org/feed/
created: '2026-03-16'
description: The Alliance for OpenUSD (AOUSD) is a Linux Foundation project dedicated to promoting interoperability of 3D content through Universal Scene Description (OpenUSD). Founded by Pixar, Adobe, Apple, Autodesk, and NVIDIA, AOUSD standardizes 3D content ecosystems for film, gaming, architecture, industrial design, and the metaverse. OpenUSD provides a high-performance extensible software platform for collaboratively constructing animated 3D scenes with schemas for geometry, shading, lighting, physics, and volume rendering.
examples:
- key_count: 12
  name: Aousd Usd Layer Example
  slug: aousd-usd-layer-example
- key_count: 10
  name: Aousd Usd Prim Example
  slug: aousd-usd-prim-example
features:
- description: USD's composition arcs (references, payloads, variants, instancing, and specializes) enable non-destructive scene assembly from multiple asset layers with override workflows.
  name: Scene Composition
- description: OpenUSD's schema system allows studios and tool vendors to extend the core specification with domain-specific schemas for physics, simulation, characters, and environments.
  name: Schema-Driven Extensibility
- description: The Hydra rendering delegate architecture enables pluggable render backends including Storm (OpenGL), Arnold, RenderMan, and others.
  name: Hydra Rendering Architecture
- description: OpenUSD supports human-readable ASCII (.usda), binary (.usdb), and packaged archive (.usdz) file formats for different use cases.
  name: Multiple File Formats
- description: The ArResolver system enables customizable asset path resolution for integrating USD with studio asset management systems.
  name: Asset Resolution
finops:
- name: Aousd Finops
  service_category: API
  slug: aousd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aousd.png
integrations:
- description: Import and export USD files via Autodesk's official USD plugins for Maya and 3ds Max, enabling OpenUSD-based pipelines.
  name: Autodesk Maya / 3ds Max
- description: Native USD integration in Houdini via LOPs (Layout Object Primitives) for creating and editing USD scenes and assets.
  name: SideFX Houdini
- description: Apple's spatial computing tools use .usdz as the primary format for augmented reality and visionOS content.
  name: Apple Reality Composer Pro
- description: NVIDIA Omniverse is built on OpenUSD, using it as the foundation for collaborative 3D design and industrial digital twin workflows.
  name: NVIDIA Omniverse
- description: RenderMan natively reads USD scenes, making it the primary production renderer for USD-based feature film pipelines.
  name: Pixar RenderMan
json_schemas:
- name: USDLayer
  property_count: 12
  slug: aousd-usd-layer
- name: USDPrim
  property_count: 10
  slug: aousd-usd-prim
json_structures:
- name: Aousd Usd Layer Structure
  property_count: 12
  slug: aousd-usd-layer-structure
- name: Aousd Usd Prim Structure
  property_count: 10
  slug: aousd-usd-prim-structure
jsonld:
- class_count: 5
  name: Aousd Context
  property_count: 18
  slug: aousd-context
layout: provider
modified: '2026-04-19'
name: Alliance for OpenUSD
nav: Providers
network: true
overview: 'Alliance for OpenUSD publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, Interoperability, Linux Foundation, Metaverse, and OpenUSD.


  The Alliance for OpenUSD catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Alliance for OpenUSD''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Aousd Plans Pricing
  plan_count: 3
  slug: aousd-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Aousd Rate Limits
  slug: aousd-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Alliance for OpenUSD API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aousd-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 14.7
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 37.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aousd/refs/heads/main/screenshots/aousd-2026-06-20T172036.png
security:
- kind: domain-security
  name: Aousd Domain Security
  slug: aousd-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aousd
tags:
- 3D
- Interoperability
- Linux Foundation
- Metaverse
- OpenUSD
- Specification
- Standards
- USD
- Visual Effects
use_cases:
- description: Exchange complex animated scenes between DCC tools (Maya, Houdini, Blender, Katana) and render farms using OpenUSD as the common format.
  name: Film and Visual Effects Production
- description: Use OpenUSD as an interchange format between game engines like Unreal Engine and Unity and DCC content creation tools.
  name: Game Development
- description: Share 3D building models, materials, and lighting between architectural design tools and real-time visualization platforms.
  name: Architecture and Design Visualization
- description: Enable interoperability of 3D assets and scenes across XR platforms, spatial computing devices, and virtual world applications.
  name: Metaverse and XR
- description: Represent complex mechanical assemblies and simulation environments for industrial digital twin applications using USD schemas.
  name: Industrial Digital Twins
website: https://aousd.org
---
