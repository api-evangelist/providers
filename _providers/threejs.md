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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.6
  scored_at: '2026-08-06'
api_count: 6
apis:
- description: 'The Three.js core library provides the scene graph, cameras, lights, geometries, materials, textures, loaders, and animation primitives used to build interactive 3D applications in the browser and on '
  name: Three.js Core
  slug: threejs-core
- description: WebGLRenderer (default, ships in the main bundle) and the newer WebGPURenderer (under `three/webgpu`) draw the scene graph to a canvas. The Node Material System (TSL — Three.js Shading Language) provi
  name: Three.js Renderers (WebGL and WebGPU)
  slug: threejs-renderers
- description: 'A family of asset loaders consumed via `three/addons/loaders/*` covering glTF/GLB (recommended), OBJ, FBX, Collada, STL, PLY, 3MF, USDZ, DRACO, KTX2, Basis, and HDR/EXR environment maps. Loaders read '
  name: Three.js Loaders
  slug: threejs-loaders
- description: Camera and object controls shipped as addons (`three/addons/controls/*`) including OrbitControls, MapControls, TrackballControls, FirstPersonControls, FlyControls, PointerLockControls, TransformContro
  name: Three.js Controls and Helpers
  slug: threejs-controls
- description: EffectComposer plus a passes library — RenderPass, ShaderPass, UnrealBloomPass, BloomPass, SSAOPass, SSRPass, SAOPass, OutlinePass, SMAAPass, FXAAPass, TAARenderPass, BokehPass, GlitchPass — for chain
  name: Three.js Post-Processing
  slug: threejs-postprocessing
- description: Browser-based scene editor for assembling Three.js scenes, importing assets, editing materials and lights, and exporting to the documented Three.js JSON object format. Useful as a no-code starting poi
  name: Three.js Editor
  slug: threejs-editor
artifact_total: 34
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/threejs-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://threejs.org
- group: docs
  title: ''
  type: Documentation
  url: https://threejs.org/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://threejs.org/manual/
- group: build
  title: ''
  type: CodeExamples
  url: https://threejs.org/examples/
- group: start
  title: ''
  type: Sandbox
  url: https://threejs.org/editor/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mrdoob/three.js
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mrdoob
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/mrdoob/three.js/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/mrdoob/three.js/blob/dev/LICENSE
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/mrdoob/three.js/blob/dev/CONTRIBUTING.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/mrdoob/three.js/blob/dev/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/mrdoob/three.js/wiki
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/mrdoob/three.js/wiki/Migration-Guide
- group: operate
  title: ''
  type: Issues
  url: https://github.com/mrdoob/three.js/issues
- group: other
  title: ''
  type: PullRequests
  url: https://github.com/mrdoob/three.js/pulls
- group: operate
  title: ''
  type: Forums
  url: https://github.com/mrdoob/three.js/discussions
- group: operate
  title: ''
  type: Forums
  url: https://discourse.threejs.org/
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/56GBJwAnUS
- group: operate
  title: ''
  type: Support
  url: https://stackoverflow.com/questions/tagged/three.js
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/three
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/@types/three
- group: build
  title: ''
  type: SDKs
  url: https://github.com/three-types/three-ts-types
- group: other
  title: ''
  type: CDN
  url: https://cdn.jsdelivr.net/npm/three/
- group: other
  title: ''
  type: CDN
  url: https://unpkg.com/three/
- group: build
  title: ''
  type: Tools
  url: https://github.com/mrdoob/stats.js
- group: build
  title: ''
  type: Tools
  url: https://github.com/threejs/three-devtools
- group: other
  title: ''
  type: X
  url: https://x.com/threejs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/mrdoob/three.js/blob/dev/README.md
created: '2026-05-25T00:00:00.000Z'
description: Three.js is an open-source JavaScript 3D library originally created by Ricardo Cabello (mrdoob) in 2010 and now maintained by a broad community of contributors. It abstracts WebGL and WebGPU behind a clean object-oriented API — Scenes, Cameras, Lights, Geometries, Materials, Textures, Loaders, Controls, Animation, and Post-Processing — to make interactive 3D in the browser practical for games, product configurators, data visualization, generative art, GIS, scientific visualization, simulations, AR/VR (WebXR), and creative coding. The library ships as the `three` npm package under MIT license with a rich addon ecosystem (`three/addons/*`) including dozens of loaders for industry asset formats (glTF, OBJ, FBX, USDZ, KTX2, DRACO), controls, helpers, post-processing passes, and a node-based shading language (TSL) that targets both WebGL and WebGPU. A browser-based editor at threejs.org/editor produces scenes in a documented JSON object format. Three.js has become the de-facto foundation
  for the JavaScript 3D ecosystem and underpins higher-level projects including React Three Fiber, A-Frame, model-viewer, Threlte, and TroisJS.
examples:
- key_count: 6
  name: Threejs Gltf Scene Example
  slug: threejs-gltf-scene-example
features:
- WebGLRenderer — production WebGL 2 renderer with PBR materials, shadows, instancing, and morph targets
- WebGPURenderer — next-generation WebGPU backend with the Node Material System (TSL) authoring model
- TSL — Three.js Shading Language, a node-based shader graph that compiles to both GLSL and WGSL
- Scene graph based on Object3D with Groups, LOD, Bones, Skinned meshes, InstancedMesh, and BatchedMesh
- Cameras — PerspectiveCamera, OrthographicCamera, ArrayCamera, StereoCamera, CubeCamera
- Lights — Ambient, Directional, Point, Spot, Hemisphere, Rect Area, plus shadow maps and light probes
- Materials — MeshStandard, MeshPhysical (clearcoat, sheen, iridescence, transmission), MeshBasic, MeshLambert, MeshPhong, MeshToon, Shader, Raw, Sprite, Line, Points
- Geometry primitives — Box, Sphere, Plane, Cylinder, Cone, Torus, TorusKnot, Tetra/Octa/Icosa/Dodecahedron, Capsule, Lathe, Extrude, Tube
- Loaders — glTF/GLB (with KHR_draco_mesh_compression, KHR_mesh_quantization, KHR_texture_basisu, EXT_meshopt_compression), OBJ, FBX, Collada, STL, PLY, 3MF, USDZ
- Texture pipeline — KTX2/Basis Universal, HDR/EXR/RGBE, video textures, canvas textures, compressed textures
- Animation system — AnimationMixer, AnimationClip, KeyframeTrack, morph target and skeletal animation
- Controls addons — OrbitControls, MapControls, TrackballControls, PointerLockControls, TransformControls, ArcballControls, DragControls
- Post-processing — EffectComposer with RenderPass, Bloom, SSAO, SSR, SMAA, FXAA, TAA, DOF, Outline, Glitch
- XR — WebXR support for VR and AR via `renderer.xr` and XR controllers/hands
- Physics integrations — Cannon.js, Ammo.js, Rapier (community)
- Browser-based Editor at threejs.org/editor for visual scene authoring and JSON export/import
- Three.js JSON Object format — documented serialization via `Object3D.toJSON()` and `ObjectLoader.parse()`
- Distributed as `three` on npm, ES modules in `three/build/three.module.js`, addons in `three/addons/*`
- TypeScript types via `@types/three` on DefinitelyTyped, mirrored in three-types/three-ts-types
- Monthly release cadence — current release r184 (April 2026), 47k+ commits, 113k+ GitHub stars
- MIT licensed, no required runtime dependencies, runs in browser, Node.js, Electron, Tauri, Deno, and React Native
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/threejs.png
json_schemas:
- name: THREE.Object3D
  property_count: 15
  slug: threejs-object3d
- name: Three.js JSON Object Scene
  property_count: 6
  slug: threejs-scene
- name: THREE.Vector3
  property_count: 3
  slug: threejs-vector3
jsonld:
- class_count: 58
  name: Threejs Context
  property_count: 5
  slug: threejs-context
layout: provider
modified: '2026-05-25'
name: Three.js
nav: Providers
network: true
overview: 'Three.js publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, Graphics, WebGL, WebGPU, and JavaScript.


  The Three.js catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Three.js'' developer surface includes developer portal, documentation, code examples, sandbox, changelog, support, tooling, and 22 more developer resources.'
random_paper: 79
rules:
- name: Three.js API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: threejs-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 29.0
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 30.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/threejs/refs/heads/main/screenshots/threejs-2026-06-20T195317.png
security:
- kind: domain-security
  name: Threejs Domain Security
  slug: threejs-domain-security
  summary_line: TLSv1.3
slug: threejs
tags:
- 3D
- Graphics
- WebGL
- WebGPU
- JavaScript
- Rendering
- Open Source
- Game Development
- Visualization
website: https://threejs.org
---
