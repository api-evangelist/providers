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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: 'Python API for scripting and extending Maya functionality, providing access to Maya''s scene graph and node architecture. Includes Python API 2.0 with a more Pythonic workflow and improved performance '
  name: Maya Python API
  slug: maya-python-api
- description: C++ API providing low-level access to Maya's core functionality for creating plugins, custom nodes, and high-performance tools. The API is organized into functional libraries including OpenMaya, OpenM
  name: Maya C++ API
  slug: maya-cpp-api
- description: Maya Embedded Language (MEL) scripting interface for automating tasks and customizing Maya workflows. MEL provides direct access to Maya commands and is the foundation of Maya's scripting capabilities
  name: Maya Commands (MEL)
  slug: maya-mel-commands
- description: Universal Scene Description (USD) integration for Maya, enabling exchange of 3D content between applications. Provides tools for importing, exporting, and working with USD stages and layers within May
  name: Maya USD API
  slug: maya-usd-api
- description: Bifrost is Maya's visual programming environment for creating simulation and procedural effects. It provides a node-based graph editor for building complex effects including fluids, particles, destruc
  name: Maya Bifrost API
  slug: maya-bifrost-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autodesk-maya-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.autodesk.com/developer-network/platform-technologies/maya
- group: docs
  title: ''
  type: Documentation
  url: https://help.autodesk.com/view/MAYADEV/2026/ENU/
- group: operate
  title: ''
  type: Support
  url: https://forums.autodesk.com/t5/maya-programming/bd-p/area-c-maya-programming
- group: company
  title: ''
  type: Blog
  url: https://www.autodesk.com/blogs/maya/
- group: learn
  title: ''
  type: Tutorials
  url: https://tutorials.autodesk.io/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://help.autodesk.com/view/MAYAUL/2026/ENU/?guid=MAYA_RELEASENOTES_2026_RELEASE_NOTES_HTML
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autodesk-platform-services
created: '2025-01-01'
description: Autodesk Maya is a comprehensive 3D computer graphics application used for creating interactive 3D applications including video games, animated films, TV series, and visual effects. Maya provides multiple programming APIs including a Python API, C++ plugin API, MEL scripting language, USD integration, and Bifrost visual programming environment for extending and automating Maya workflows and creating custom tools and plugins.
features:
- description: Modern Pythonic API with improved performance and a cleaner interface for accessing Maya's node architecture and scene graph via maya.api.OpenMaya.
  name: Python API 2.0
- description: Low-level C++ API for high-performance plugin development with access to Maya's full internal architecture through OpenMaya functional libraries.
  name: C++ Plugin SDK
- description: Maya Embedded Language for command-line scripting, UI automation, and batch processing of Maya scenes and assets.
  name: MEL Scripting
- description: Universal Scene Description support for importing, exporting, and working with USD assets within Maya for cross-application 3D content pipelines.
  name: USD Integration
- description: Node-based visual programming environment for creating procedural effects, simulations, and custom workflows without traditional coding.
  name: Bifrost Visual Programming
- description: Create custom dependency graph nodes, deformers, and shape nodes that integrate natively into Maya's scene graph and evaluation system.
  name: Custom Node Development
finops:
- name: Autodesk Maya Finops
  service_category: API
  slug: autodesk-maya-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autodesk-maya.png
integrations:
- description: Integration with Arnold renderer via the MtoA (Maya to Arnold) plugin for photorealistic rendering of Maya scenes.
  name: Autodesk Arnold
- description: USD-based pipeline integration with Unreal Engine for game asset export and visualization workflows.
  name: Unreal Engine
- description: Integration with Autodesk ShotGrid for production tracking, asset management, and review workflows in film and TV production.
  name: ShotGrid (Flow Production Tracking)
- description: Interoperability with SideFX Houdini via USD and Alembic for visual effects simulation and procedural content pipelines.
  name: Houdini
layout: provider
modified: '2026-04-19'
name: Autodesk Maya
nav: Providers
network: true
overview: 'Autodesk Maya publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Graphics, Animation, Game Development, Modeling, and Rendering.


  Autodesk Maya''s developer surface includes developer portal, documentation, support, engineering blog, release notes, and 4 more developer resources.'
plans:
- name: Autodesk Maya Plans Pricing
  plan_count: 3
  slug: autodesk-maya-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Autodesk Maya Rate Limits
  slug: autodesk-maya-rate-limits
score:
  band: thin
  composite: 28.1
  delta: -2.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 30.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autodesk-maya/refs/heads/main/screenshots/autodesk-maya-2026-06-20T172637.png
security:
- kind: domain-security
  name: Autodesk Maya Domain Security
  slug: autodesk-maya-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: autodesk-maya
tags:
- 3D Graphics
- Animation
- Game Development
- Modeling
- Rendering
- Visual Effects
- VFX
- CAD
use_cases:
- description: Integrating Maya into visual effects production pipelines with custom tools, asset management systems, and render farm automation.
  name: VFX Pipeline Integration
- description: Automating game asset creation, optimization, and export workflows for game engines like Unreal Engine and Unity through Maya scripting.
  name: Game Asset Automation
- description: Building custom rigging systems, animation controls, and workflow tools to accelerate character animation production for film and TV.
  name: Animation Workflow Tools
- description: Using Bifrost and Python APIs to generate procedural geometry, textures, and scene content for games, visualization, and architectural projects.
  name: Procedural Content Generation
- description: Developing studio pipeline tools that automate scene assembly, asset tracking, and data interchange between Maya and other DCC applications.
  name: DCC Pipeline Development
website: https://www.autodesk.com/developer-network/platform-technologies/maya
---
