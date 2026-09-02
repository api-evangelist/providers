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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Blender Python API (bpy) provides Python access to Blender's internal data, operators, and UI components. It enables developers to automate tasks, create addons, build custom tools, manipulate sce
  name: Blender Python API
  slug: blender-python-api
- description: The Blender Extensions Platform (extensions.blender.org) provides a curated repository of addons, themes, and node presets for Blender. The platform supports structured addon packaging, versioning, an
  name: Blender Extensions Platform
  slug: blender-extensions
artifact_total: 32
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blender-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blender-foundation
- group: company
  title: ''
  type: Website
  url: https://www.blender.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blender.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blender.org/api/current/info_quickstart.html
- group: operate
  title: ''
  type: Community
  url: https://www.blender.org/community/
- group: operate
  title: ''
  type: Support
  url: https://www.blender.org/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blender
- group: build
  title: ''
  type: GitHub
  url: https://github.com/blender/blender
- group: company
  title: ''
  type: Blog
  url: https://www.blender.org/news/
- group: learn
  title: ''
  type: Training
  url: https://www.blender.org/training/
- group: operate
  title: ''
  type: FAQ
  url: https://www.blender.org/support/faq/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.blender.org/docs/release_notes/
- group: commercial
  title: GPL-2.0-or-later
  type: License
  url: https://www.blender.org/about/license/
- group: start
  title: ''
  type: PackageRegistry
  url: https://extensions.blender.org
- group: design
  title: ''
  type: SpectralRules
  url: rules/blender-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/blender-vocabulary.yaml
created: '2024-01-01'
description: Blender is the free and open source 3D creation suite supporting the entirety of the 3D pipeline including modeling, rigging, animation, simulation, rendering, compositing, motion tracking, video editing, and game creation. Blender's Python API provides extensive scripting capabilities for automation, tool development, and addon creation, enabling developers to extend Blender with custom functionality. The project is governed by the Blender Foundation and maintained at blender.org.
examples:
- key_count: 11
  name: Blender Addon Manifest Example
  slug: blender-addon-manifest-example
- key_count: 6
  name: Blender Bpy Operator Example
  slug: blender-bpy-operator-example
features:
- description: The bpy module provides access to Blender's internal data model, allowing Python scripts to create, read, update, and delete scene objects, materials, animations, constraints, and render settings.
  name: Python Scripting (bpy)
- description: Blender's operator system allows Python developers to create custom operators (commands) accessible from menus, panels, keyboard shortcuts, and scripts.
  name: Operator Framework
- description: Blender addons are Python packages extending functionality across modeling, rigging, animation, rendering, import/export, and UI. Distributed via the Extensions Platform or bundled directly.
  name: Addon Development
- description: Geometry Nodes and Shader Nodes provide visual programming for procedural modeling and materials, scriptable via the Python API.
  name: Node Groups and Geometry Nodes
- description: Python API integrates with Blender's Cycles and EEVEE render engines for batch rendering, render farm integration, and custom render pipeline control.
  name: Render Pipeline Integration
- description: Blender can be invoked headlessly via CLI for batch rendering, script execution, and pipeline automation without a GUI.
  name: Command-Line Interface
- description: Blender 3.x+ includes an asset library system with Python API support for managing and accessing reusable 3D assets across projects.
  name: Asset Library System
finops:
- name: Blender Finops
  service_category: API
  slug: blender-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blender.png
integrations:
- description: Blender's built-in path-tracing render engine with Python API access for controlling render settings, passes, and denoising.
  name: Cycles X Render Engine
- description: Blender supports import and export of Pixar USD scenes, enabling pipeline integration with VFX and game development workflows.
  name: USD (Universal Scene Description)
- description: Blender has built-in glTF 2.0 import/export support with Python API access, enabling web, AR/VR, and game engine pipelines.
  name: glTF 2.0
- description: Blender supports OpenVDB for volumetric simulation and rendering, with Python API access to volume data and simulation parameters.
  name: OpenVDB
- description: Blender integrates with OpenColorIO for ACES and professional color pipeline support in VFX productions.
  name: ACES Color Management
json_schemas:
- name: Blender Addon Manifest
  property_count: 12
  slug: blender-addon-manifest
- name: Blender bpy Operator
  property_count: 6
  slug: blender-bpy-operator
json_structures:
- name: Blender Addon Manifest Structure
  property_count: 0
  slug: blender-addon-manifest-structure
- name: Blender Bpy Operator Structure
  property_count: 0
  slug: blender-bpy-operator-structure
jsonld:
- class_count: 11
  name: Blender Context
  property_count: 0
  slug: blender-context
layout: provider
modified: '2026-04-21'
name: Blender
nav: Providers
network: true
overview: 'Blender publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, Animation, Game Development, Modeling, and Open-Source.


  The Blender catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Blender''s developer surface includes documentation, getting-started guide, support, GitHub presence, engineering blog, training material, FAQ, and 10 more developer resources.'
plans:
- name: Blender Plans Pricing
  plan_count: 3
  slug: blender-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Blender Rate Limits
  slug: blender-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Blender API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: blender-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Blender API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: blender-spectral-rules
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 30.7
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 30.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blender/refs/heads/main/screenshots/blender-2026-06-20T173348.png
security:
- kind: domain-security
  name: Blender Domain Security
  slug: blender-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blender
tags:
- 3D
- Animation
- Game Development
- Modeling
- Open-Source
- Python
- Rendering
- VFX
use_cases:
- description: VFX and animation studios automate Blender production pipelines using Python scripts for batch rendering, asset processing, and scene assembly.
  name: Pipeline Automation
- description: Developers create custom tools and plugins extending Blender's functionality for modeling, rigging, simulation, and export workflows.
  name: Addon Development
- description: Blender is used for headless server-side rendering via CLI and Python scripts in cloud rendering pipelines and automated content generation workflows.
  name: Headless Rendering
- description: Python scripts and Geometry Nodes enable procedural generation of 3D assets for games, VFX, and architectural visualization.
  name: Procedural Content Generation
- description: Universities, research labs, and educators use Blender's Python API for 3D visualization, scientific rendering, and computer graphics research.
  name: Education and Research
website: https://www.blender.org/
---
