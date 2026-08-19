---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: 'GDScript is Godot''s first-class scripting language, a high-level dynamically typed (and gradually statically typed) language with Python-like syntax and tight integration with the engine, the editor, '
  name: Godot GDScript API
  slug: godot-gdscript-api
- description: Godot's .NET build ships C# bindings over the engine API, letting developers write game logic and editor tooling in C# against the same class library that GDScript and C++ see. C# support targets .NET
  name: Godot C# / .NET Bindings
  slug: godot-csharp-bindings
- description: 'GDExtension is Godot 4''s mechanism for binding native C++ (or any language with a C ABI) into the engine without recompiling Godot itself. GDExtension libraries register their own classes against the '
  name: Godot GDExtension (C++ Bindings)
  slug: godot-gdextension
- description: Godot's editor can be extended in-place with EditorPlugin scripts that add docks, inspector plugins, import plugins, export plugins, gizmos, and custom tool windows. Editor plugins use the same engine
  name: Godot Editor Plugin API
  slug: godot-editor-plugin-api
- description: The Godot Asset Library REST API powers the community asset browser inside the Godot editor (AssetLib tab) and the website at godotengine.org/asset-library. It exposes endpoints to search and filter a
  name: Godot Asset Library API
  slug: godot-asset-library-api
artifact_total: 10
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/godotengine/godot/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/godotengine/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/godotengine/godot/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/godot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/godot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://godotengine.org
- group: other
  title: ''
  type: Download
  url: https://godotengine.org/download/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.godotengine.org/en/stable/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.godotengine.org/en/stable/classes/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.godotengine.org/en/stable/getting_started/introduction/
- group: other
  title: ''
  type: Marketplace
  url: https://godotengine.org/asset-library
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/godotengine/godot
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/godotengine
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/godotengine/godot/issues
- group: other
  title: ''
  type: Proposals
  url: https://github.com/godotengine/godot-proposals
- group: operate
  title: ''
  type: Community
  url: https://godotengine.org/community/
- group: operate
  title: ''
  type: Forums
  url: https://forum.godotengine.org
- group: other
  title: ''
  type: Chat
  url: https://chat.godotengine.org
- group: operate
  title: ''
  type: Contact
  url: https://godotengine.org/contact/
- group: company
  title: ''
  type: Blog
  url: https://godotengine.org/blog/
- group: other
  title: ''
  type: ParentOrganization
  url: https://godot.foundation
- group: commercial
  title: ''
  type: License
  url: https://godotengine.org/license/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://godotengine.org/code-of-conduct/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://godotengine.org/privacy-policy/
- group: other
  title: ''
  type: Donate
  url: https://godotengine.org/donate/
- group: other
  title: ''
  type: X
  url: https://x.com/godotengine
- group: company
  title: ''
  type: Mastodon
  url: https://mastodon.gamedev.place/@godotengine
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Godotengineofficial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/godot-foundation
created: '2024-01-01'
description: 'Godot Engine is a free and open-source community-driven 2D and 3D game engine released under the MIT License and stewarded by the Godot Foundation. Godot ships an integrated editor plus a deep scripting and extension surface across three primary languages: GDScript (Godot''s own typed scripting language), C# (via .NET 8 / Mono in the .NET build), and C++ (via GDExtension, the modern successor to GDNative, which lets native shared libraries register their own classes against the same API the built-in classes use). The engine API is documented per-class at docs.godotengine.org. In addition, the Godot Asset Library at godotengine.org/asset-library/api exposes a public REST API used by the in-editor AssetLib browser to list, search, fetch, and download community plugins, templates, tools, and demos. The Godot project source lives at github.com/godotengine/godot.'
finops:
- name: Godot Finops
  service_category: API
  slug: godot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/godot.png
layout: provider
modified: '2026-05-23'
name: Godot Engine
nav: Providers
network: true
overview: 'Godot Engine publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 2D, 3D, C#, C++, and Game Development.


  Godot Engine''s developer surface includes documentation, API reference, getting-started guide, engineering blog, YouTube channel, and 24 more developer resources.'
plans:
- name: Godot Plans Pricing
  plan_count: 1
  slug: godot-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 2
  name: Godot Rate Limits
  slug: godot-rate-limits
score:
  band: thin
  composite: 28.7
  delta: 0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 28.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/godot/refs/heads/main/screenshots/godot-2026-06-20T181943.png
security:
- kind: domain-security
  name: Godot Domain Security
  slug: godot-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Godot Vulnerability Disclosure
  slug: godot-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: godot
tags:
- 2D
- 3D
- C#
- C++
- Game Development
- Game Engine
- GDExtension
- GDScript
- Godot
- Open Source
- Plugin
- SDK
website: https://godotengine.org
---
