---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daz-3d-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.daz3d.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.daz3d.com/start
- group: docs
  title: ''
  type: APIReference
  url: https://docs.daz3d.com/public/software/dazstudio/4/referenceguide/scripting/api_reference/start
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.daz3d.com/public/software/dazstudio/4/referenceguide/scripting/start
- group: build
  title: ''
  type: SDK
  url: https://www.daz3d.com/daz-studio-4-5-sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daz3d
- group: company
  title: ''
  type: Blog
  url: https://blog.daz3d.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.daz3d.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.daz3d.com/help
- group: operate
  title: ''
  type: Community
  url: https://www.daz3d.com/forums
- group: commercial
  title: ''
  type: Pricing
  url: https://www.daz3d.com/daz-plus
- group: start
  title: ''
  type: SignUp
  url: https://www.daz3d.com/customer/account/create/
- group: start
  title: ''
  type: Login
  url: https://www.daz3d.com/customer/account/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.daz3d.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.daz3d.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/daz-3d-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/daz-3d-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/daz-3d-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/daz-3d-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/daz-3d-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/daz-3d-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/daz-3d-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/daz-3d-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: Daz 3D publishes a complete, public DAZ Script API reference and its own DSON JSON file format spec as human-readable DokuWiki pages, but ships no OpenAPI, GraphQL SDL, AsyncAPI, Postman collection or JSON Schema anywhere — and api.daz3d.com, the only API-shaped hostname it owns, 302s every path to the marketing site root.
  evidence:
  - status: 302
    url: https://api.daz3d.com/openapi.json
  - status: 404
    url: https://www.daz3d.com/openapi.json
  - status: 404
    url: https://www.daz3d.com/rest/all/schema?services=all
  - status: 200
    url: https://docs.daz3d.com/public/dson_spec/start
  - status: 404
    url: https://www.daz3d.com/.well-known/agent-card.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-08-12'
description: 'Daz 3D is a Salt Lake City based 3D content and software company best known for Daz Studio, a free figure posing, morphing and rendering application, and for the Genesis line of morphable 3D human figures. The company runs a large first-party and marketplace store of 3D characters, clothing, props and environments, publishes the DSON (Daz Scene Object Notation) JSON-based scene file format, and licenses synthetic 3D character datasets for AI training through the surface that was formerly the Tafi brand. Its developer surface is an application SDK rather than a web API: a free C++ plug-in SDK, the DAZ Script ECMAScript scripting API documented in the public Daz Documentation Center, and open-source Daz-to-Blender / Unity / Unreal / Maya / Cinema 4D / 3ds Max bridge plug-ins published on GitHub. No public REST, GraphQL or event API is published.'
image: https://www.daz3d.com/static/images/logo/share.png
layout: provider
modified: '2026-08-12'
name: DAZ 3D
nav: Providers
network: true
overview: 'DAZ 3D is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, 3D Content, Digital Assets, Graphics, and Rendering.


  DAZ 3D''s developer surface includes documentation, API reference, getting-started guide, SDKs, engineering blog, support, pricing, and 17 more developer resources.'
plans:
- name: Daz 3D Plans Pricing
  plan_count: 3
  slug: daz-3d-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Daz 3D Rate Limits
  slug: daz-3d-rate-limits
score:
  band: thin
  composite: 33.4
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 33.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Daz 3D Domain Security
  slug: daz-3d-domain-security
  summary_line: TLSv1.3 · DMARC
slug: daz-3d
tags:
- 3D
- 3D Content
- Digital Assets
- Graphics
- Rendering
- Avatars
- Game Development
- AI Training Data
- Marketplace
- SDK
- Desktop Software
- Creator Tools
website: https://www.daz3d.com/
---
