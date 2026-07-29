---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sketchfab Agentic Access
  operation_count: 4
  slug: sketchfab-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 5
apis:
- description: REST API for reading and writing Sketchfab data. Upload, list, update, and delete 3D models; manage collections, comments, likes, and bookmarks; search the public model catalog; and manage user, organ
  name: Sketchfab Data API
  slug: sketchfab-data-api
- description: Client-side JavaScript library for controlling an embedded Sketchfab 3D viewer. Exposes camera control, screenshot capture, annotation, material and texture manipulation, post-processing filters, anim
  name: Sketchfab Viewer API
  slug: sketchfab-viewer-api
- description: Programmatic download of 3D models from Sketchfab's library in glTF, GLB, and USDZ formats. Requires end-user OAuth authentication. Source formats (FBX, OBJ, etc.) are not exposed through the public A
  name: Sketchfab Download API
  slug: sketchfab-download-api
- description: oEmbed-protocol endpoint at https://sketchfab.com/oembed that returns JSON containing an HTML <iframe> snippet for any Sketchfab model or playlist URL. Supports maxwidth and maxheight parameters; alwa
  name: Sketchfab oEmbed API
  slug: sketchfab-oembed-api
- description: OAuth 2.0 authorization server for the Sketchfab platform. Supports Authorization Code, Implicit, and Resource Owner Password Credentials grant types plus refresh-token rotation. Authorize endpoint at
  name: Sketchfab OAuth 2.0 API
  slug: sketchfab-oauth-api
artifact_total: 35
collections:
- collection_type: postman
  name: Sketchfab Download API
  slug: postman-sketchfab-download-api
- collection_type: postman
  name: Sketchfab Download OAuth API
  slug: postman-sketchfab-oauth-api
- collection_type: postman
  name: Sketchfab Download oEmbed API
  slug: postman-sketchfab-oembed-api
- collection_type: open
  name: Sketchfab Download API
  slug: open-sketchfab-download-api
- collection_type: open
  name: Sketchfab OAuth 2.0 API
  slug: open-sketchfab-oauth-api
- collection_type: open
  name: Sketchfab oEmbed API
  slug: open-sketchfab-oembed-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sketchfab/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sketchfab-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sketchfab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sketchfab-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sketchfab-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://sketchfab.com
- group: start
  title: ''
  type: Portal
  url: https://sketchfab.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://sketchfab.com/developers/data-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sketchfab.com/data-api/v3/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://sketchfab.com/developers/viewer
- group: docs
  title: ''
  type: Documentation
  url: https://sketchfab.com/developers/download-api
- group: docs
  title: ''
  type: Documentation
  url: https://sketchfab.com/developers/oembed
- group: docs
  title: ''
  type: Documentation
  url: https://sketchfab.com/developers/oauth
- group: docs
  title: ''
  type: Documentation
  url: https://sketchfab.com/developers/guidelines
- group: start
  title: ''
  type: GettingStarted
  url: https://sketchfab.com/developers
- group: start
  title: ''
  type: Signup
  url: https://sketchfab.com/signup
- group: start
  title: ''
  type: Login
  url: https://sketchfab.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sketchfab.com/terms
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sketchfab.com/developers/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sketchfab.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://sketchfab.com/plans
- group: commercial
  title: ''
  type: Plans
  url: plans/sketchfab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sketchfab-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sketchfab-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sketchfab.com/blogs/community
- group: operate
  title: ''
  type: Forums
  url: https://forum.sketchfab.com/
- group: operate
  title: ''
  type: Support
  url: https://support.fab.com/s/?ProductOrigin=Sketchfab
- group: other
  title: ''
  type: Labs
  url: https://labs.sketchfab.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sketchfab
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sketchfab/viewer-api
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/sketchfab-viewer
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sketchfab/sketchfab-oauth2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sketchfab/node-sketchfab
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/blender-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/unity-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/unreal-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/godot-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/c4d-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/maya-exporter
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/modo-exporter
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/3dsmax-exporter
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/lightwave-exporter
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/wordpress-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/ckeditor-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/sketchfab/phpbb-plugin
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/sketchfab/experiments
- group: build
  title: ''
  type: CodeExamples
  url: https://labs.sketchfab.com/experiments/configurator/
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/sketchfab/configurator-framework
- group: build
  title: ''
  type: Tools
  url: https://github.com/sketchfab/UnityGLTF
- group: build
  title: ''
  type: Tools
  url: https://github.com/sketchfab/Unity-glTF-Exporter
- group: other
  title: ''
  type: Acquirer
  url: https://www.epicgames.com/site/en-US/news/sketchfab-is-joining-epic-games
- group: other
  title: ''
  type: SuccessorPlatform
  url: https://www.fab.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sketchfab/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Sketchfab
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/Sketchfab
created: '2026-05-25'
description: Sketchfab is the largest dedicated platform for publishing, sharing, discovering, buying, and embedding interactive 3D content on the web. Founded in Paris in 2012 by Cedric Pinson and Alban Denoyel and acquired by Epic Games on July 21, 2021, Sketchfab hosts millions of 3D models from artists, museums, scanning rigs, and studios — much of it Creative Commons licensed. The platform exposes a public REST Data API for programmatic upload and content management, a JavaScript Viewer API for controlling the embedded WebGL/WebXR viewer, a Download API delivering glTF/GLB/USDZ, an oEmbed endpoint, and OAuth 2.0 authentication, alongside native exporters for every major 3D / DCC tool. Following the Fab.com launch in 2024 the Sketchfab Store has been retired into Epic's unified content marketplace while the publishing, viewing, and developer APIs remain on sketchfab.com.
features:
- REST Data API v3 at https://api.sketchfab.com/v3/ — models, users, collections, comments, likes, bookmarks, search, organizations, projects
- OAuth 2.0 with Authorization Code, Implicit, and Password grants plus refresh-token rotation; bearer access tokens expire after one month
- Personal API tokens for server-to-server access (issued from account settings)
- JavaScript Viewer API for embedded 3D viewer control — camera, materials, textures, annotations, animation, post-processing, screenshot capture, event stream
- Download API exposing glTF, GLB, and USDZ formats; source formats (FBX, OBJ) reserved for direct contracts
- oEmbed endpoint at /oembed for one-call iframe embedding (16:9 viewer aspect)
- Public model search covering Sketchfab's library of millions of 3D models, much of it Creative Commons licensed
- Native plugins / exporters for Blender, Unity, Unreal, Godot, Cinema 4D, Maya, Modo, 3ds Max, Lightwave, ZBrush, SketchUp, KSP, Minecraft (Mineways)
- WordPress, CKEditor, phpBB, NodeBB, and Vanilla Forums content plugins for embedding models in CMS and forum platforms
- VR / AR / WebXR-ready viewer with USDZ Quick Look support for iOS Safari
- Labs experiments (annotations sync, configurator, watch configurator, screenshot generator, viewer sharing)
- Configurator framework for building product configurators on the Sketchfab viewer
- Owned by Epic Games since July 21, 2021; commerce surface migrating to Fab.com (Epic's unified marketplace launched 2024)
- Free, Plus, Premium, Premium Pro, and Enterprise plans for creators; separate Store buyer surface
finops:
- name: Sketchfab Finops
  service_category: Media and Content
  slug: sketchfab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sketchfab.png
json_schemas:
- name: Sketchfab Model
  property_count: 24
  slug: sketchfab-model
jsonld:
- class_count: 0
  name: Sketchfab Context
  property_count: 6
  slug: sketchfab-context
layout: provider
modified: '2026-05-25'
name: Sketchfab
nav: Providers
network: true
overview: 'Sketchfab publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data API, Download API, oEmbed API, and 1 more. Tagged areas include 3D, Models, Marketplace, Viewer, and WebGL.


  The Sketchfab catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sketchfab''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 48 more developer resources.'
plans:
- name: Sketchfab Plans Pricing
  plan_count: 5
  slug: sketchfab-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Sketchfab Rate Limits
  slug: sketchfab-rate-limits
rules:
- name: Sketchfab API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sketchfab-jsonschema-spectral-rules
scopes:
- name: Sketchfab Scopes
  scope_count: 1
  slug: sketchfab-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 65.6
  delta: -3.5
  facets:
    commercial_clarity: 84.2
    contract_quality: 69.8
    developer_ergonomics: 65.2
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sketchfab/refs/heads/main/screenshots/sketchfab-2026-06-20T194108.png
security:
- kind: authentication
  name: Sketchfab Authentication
  slug: sketchfab-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sketchfab Domain Security
  slug: sketchfab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sketchfab
tags:
- 3D
- Models
- Marketplace
- Viewer
- WebGL
- glTF
- AR
- VR
- Creative
- Epic Games
website: https://sketchfab.com
---
