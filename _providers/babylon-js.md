---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 18
apis:
- description: The core Babylon.js engine and scene graph. Provides the Engine and Scene abstractions, cameras, lights, meshes, materials, textures, animation, post-processing, particle systems, physics integration,
  name: Babylon.js Core
  slug: babylonjs-core
- description: 2D and 3D GUI library for Babylon.js — buttons, sliders, panels, input boxes, color pickers, and 3D holographic controls — rendered through a dynamic texture or as 3D meshes. Authored visually via the
  name: Babylon.js GUI
  slug: babylonjs-gui
- description: 'Asset importers for Babylon.js — glTF 2.0 (with KHR extensions), OBJ, STL, USDZ, SPLAT (Gaussian splats), and others. Loaders parse external assets into the Babylon scene graph and are tree-shakeable '
  name: Babylon.js Loaders
  slug: babylonjs-loaders
- description: Library of advanced and specialty materials — water, lava, fire, fur, terrain, cell, mix, gradient, sky, grid, normal, shadow-only, and others — built on top of Babylon's Standard and PBR materials. D
  name: Babylon.js Materials
  slug: babylonjs-materials
- description: Additional post-processing effects beyond core — including ASCII art, anaglyph, digital rain, ocean, and other stylized image pipelines. Composes on top of the core post-process chain via the `@babylo
  name: Babylon.js Post-Processes
  slug: babylonjs-post-processes
- description: GPU-generated procedural textures — brick, cloud, fire, grass, marble, normal-map, perlin-noise, road, starfield, and wood — packaged separately as `@babylonjs/procedural-textures` so applications can
  name: Babylon.js Procedural Textures
  slug: babylonjs-procedural-textures
- description: Scene exporters that serialize a live Babylon.js scene to glTF 2.0, OBJ, STL, or .babylon JSON. Used by Sandbox, the Editor, and the Playground export flow, and available as the `@babylonjs/serializer
  name: Babylon.js Serializers
  slug: babylonjs-serializers
- description: Embeddable developer tool that overlays a live tree of every Babylon scene object — nodes, materials, textures, cameras, lights, animations, particles, and physics bodies — with property editing, gizm
  name: Babylon.js Inspector
  slug: babylonjs-inspector
- description: Visual node-graph authoring tools — Node Material Editor (NME), Node Geometry Editor (NGE), Node Particle Editor (NPE), and Node Render Graph Editor — that produce serializable JSON graphs which the c
  name: Babylon.js Node Editors
  slug: babylonjs-node-editors
- description: Hosted browser-based IDE for writing and sharing Babylon.js scenes as TypeScript snippets. Backed by the Babylon Snippet Server which assigns shareable snippet IDs and a public read API at `snippet.ba
  name: Babylon.js Playground
  slug: babylonjs-playground
- description: Drop-in browser viewer for 3D assets — glTF/GLB, OBJ, STL, USDZ, SPLAT, and .babylon files — with Inspector integration, environment/IBL configuration, and animation playback. Used as the reference gl
  name: Babylon.js Sandbox
  slug: babylonjs-sandbox
- description: Public REST endpoint hosted at `https://snippet.babylonjs.com/` that stores and serves serialized JSON snippets for the Playground, Node Material Editor, Node Geometry Editor, Node Particle Editor, an
  name: Babylon.js Snippet API
  slug: babylonjs-snippet-server
- description: C++ host that runs the Babylon.js engine on top of native graphics APIs (DirectX, Metal, Vulkan, OpenGL, OpenGL ES) without a browser. Targets Windows, macOS, Linux, Android, and iOS. Used as the foun
  name: Babylon Native
  slug: babylon-native
- description: React Native binding that runs Babylon Native on iOS and Android with a React component (`EngineView`) for embedding Babylon scenes in cross-platform mobile applications. Published as `@babylonjs/reac
  name: Babylon React Native
  slug: babylon-react-native
- description: Community-maintained visual editor for authoring Babylon.js scenes — scene graph, materials, animations, GUI, scripting, post-processing, and asset pipeline — exporting to runnable Babylon.js projects
  name: Babylon.js Editor
  slug: babylonjs-editor
- description: Community-maintained Unity and Unreal exporters and a runtime scripting layer that lets engines author scenes in Unity / Unreal and export them to Babylon.js for web delivery.
  name: Babylon Toolkit
  slug: babylon-toolkit
- description: First-party DCC exporters for 3ds Max, Maya, and Blender that emit .babylon and glTF 2.0 assets compatible with the Babylon.js runtime, Sandbox, and Editor pipelines.
  name: Babylon.js Exporters
  slug: babylonjs-exporters
- description: Browser extension and embeddable library that captures and inspects WebGL / WebGPU frames — every draw call, state change, shader, texture, and uniform — for any 3D web application, not only Babylon.j
  name: Spector.js
  slug: spectorjs
artifact_total: 41
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/babylon-js-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.babylonjs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.babylonjs.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.babylonjs.com/setup/frameworkPackages/firstApp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BabylonJS
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/BabylonJS/Babylon.js
- group: commercial
  title: ''
  type: License
  url: https://github.com/BabylonJS/Babylon.js/blob/master/license.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/BabylonJS/Babylon.js/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributingGuide
  url: https://github.com/BabylonJS/Babylon.js/blob/master/contributing.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://doc.babylonjs.com/setup/support/whatsNew
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/BabylonJS/Babylon.js/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/BabylonJS/Babylon.js/issues
- group: operate
  title: ''
  type: Forums
  url: https://forum.babylonjs.com/
- group: company
  title: ''
  type: Blog
  url: https://babylonjs.medium.com/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@BabylonJSEngine
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/babylonjs
- group: other
  title: ''
  type: TypeDoc
  url: https://doc.babylonjs.com/typedoc/modules/BABYLON
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/core
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/gui
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/loaders
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/materials
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/post-processes
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/procedural-textures
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/serializers
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/inspector
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/node-editor
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/babylonjs
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@babylonjs/react-native
- group: start
  title: ''
  type: Sandbox
  url: https://playground.babylonjs.com/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.babylonjs.com/
- group: start
  title: ''
  type: Sandbox
  url: https://nme.babylonjs.com/
- group: start
  title: ''
  type: Sandbox
  url: https://nge.babylonjs.com/
- group: start
  title: ''
  type: Sandbox
  url: https://npe.babylonjs.com/
- group: start
  title: ''
  type: Sandbox
  url: https://gui.babylonjs.com/
- group: other
  title: ''
  type: API
  url: https://snippet.babylonjs.com/
- group: build
  title: ''
  type: Tools
  url: https://spector.babylonjs.com/
- group: build
  title: ''
  type: Tools
  url: https://editor.babylonjs.com/
- group: build
  title: ''
  type: Tools
  url: https://github.com/BabylonJS/BabylonNative
- group: build
  title: ''
  type: Tools
  url: https://github.com/BabylonJS/BabylonReactNative
- group: build
  title: ''
  type: Tools
  url: https://github.com/BabylonJS/BabylonToolkit
- group: build
  title: ''
  type: Tools
  url: https://github.com/BabylonJS/Exporters
- group: docs
  title: ''
  type: Documentation
  url: https://doc.babylonjs.com/features/featuresDeepDive/physics
- group: docs
  title: ''
  type: Documentation
  url: https://doc.babylonjs.com/features/featuresDeepDive/webXR
created: '2026-05-25'
description: Babylon.js is an Apache-2.0 licensed, TypeScript-first open-source 3D engine and rendering framework sponsored by Microsoft and developed in the public BabylonJS GitHub organization. It targets WebGL, WebGPU, and WebXR in the browser, and DirectX, Metal, Vulkan, OpenGL, and OpenGL ES natively through Babylon Native — including a Babylon React Native binding for mobile. The framework ships as a family of scoped npm packages (`@babylonjs/core`, `gui`, `loaders`, `materials`, `inspector`, `serializers`, `post-processes`, `procedural-textures`, `node-editor`) plus a rich tooling surface — the Playground IDE, Sandbox asset viewer, Inspector, Spector.js, the Node Material / Geometry / Particle / Render-Graph editors, a community Editor, the Babylon Toolkit (Unity / Unreal exporters), and DCC exporters for 3ds Max, Maya, and Blender — all backed by the public Snippet API at `snippet.babylonjs.com` that powers shareable Playground and node-editor assets.
features:
- Cross-platform 3D engine — WebGL2, WebGPU, and (via Babylon Native) DirectX / Metal / Vulkan / OpenGL / OpenGL ES
- TypeScript-first SDK published as scoped `@babylonjs/*` ES modules with tree-shakeable imports
- Scene graph with cameras, lights, meshes, materials, textures, animations, particles, audio, and physics
- PBR materials with OpenPBR support, clustered and textured area lighting, and volumetric lighting (v9)
- Frame Graph, Dynamic IBL Shadows, and Render Graph-driven pipelines (v9)
- Node Material Editor, Node Geometry Editor, Node Particle Editor, and Node Render Graph Editor
- Procedural geometry with Node Geometry — runtime-evaluated graphs serialized as JSON
- Gaussian Splat rendering and 3D Tiles geospatial pipeline with PBR atmosphere (v9)
- glTF 2.0 first-class import and export with full KHR extension coverage
- GUI library with Inspector-driven authoring and 3D holographic controls
- WebXR / VR / AR support including hand tracking, controllers, anchors, and pass-through
- Physics integration with Havok (recommended), Ammo.js, Cannon.js, Oimo.js, and Recast
- Babylon Native — C++ host for running Babylon on Windows, macOS, Linux, Android, and iOS
- Babylon React Native (`@babylonjs/react-native`) for embedding Babylon scenes in mobile apps
- Inspector — runtime scene debugger with property editing, gizmos, and shader editing
- Spector.js — frame-by-frame WebGL / WebGPU capture and inspection tool
- Hosted Playground IDE and Sandbox asset viewer with shareable snippet IDs
- Snippet API at `snippet.babylonjs.com` powering shareable Playground / NME / NGE / GUI assets
- Babylon.js Editor — community-maintained visual scene editor
- Babylon Toolkit — Unity and Unreal exporters for the Babylon runtime
- First-party DCC exporters for 3ds Max, Maya, and Blender
- Apache-2.0 licensed, Microsoft-sponsored, community-governed via forum.babylonjs.com
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/babylon-js.png
layout: provider
modified: '2026-05-25'
name: Babylon.js
nav: Providers
network: true
overview: 'Babylon.js publishes 18 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, Game Engine, Rendering, WebGL, and WebGPU.


  Babylon.js'' developer surface includes developer portal, documentation, getting-started guide, changelog, release notes, engineering blog, YouTube channel, and 36 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/babylon-js/refs/heads/main/screenshots/babylon-js-2026-06-20T172915.png
security:
- kind: domain-security
  name: Babylon Js Domain Security
  slug: babylon-js-domain-security
  summary_line: TLSv1.3
slug: babylon-js
tags:
- 3D
- Game Engine
- Rendering
- WebGL
- WebGPU
- WebXR
- TypeScript
- glTF
- Open-Source
- Microsoft
website: https://www.babylonjs.com/
---
