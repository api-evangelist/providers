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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fabcom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.epicgames.com/documentation/en-us/fab/fab-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.epicgames.com/documentation/fab/publisher-get-started-in-fab
- group: operate
  title: ''
  type: Support
  url: https://support.fab.com/s/?ProductOrigin=FabSupport
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fabcom-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fabcom-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fabcom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/epicgames
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fabcom-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.epicgames.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fabcom-llms.txt
created: '2026-07-17'
description: Fab.com is a digital content marketplace operated by Epic Games, where creators buy and sell 3D models, materials, environments, VFX, audio, and game-ready assets. Launched in October 2024, Fab consolidated four of Epic's prior storefronts — the Unreal Engine Marketplace, the Sketchfab Store, Quixel, and the ArtStation Marketplace — into a single catalog with unified licensing, and integrates into Unreal Engine, UEFN, and the Epic Games Launcher. The fabcom entry was originally added to the API Evangelist network as an a16z portfolio lead for the earlier, unrelated Fab.com flash-sale design-commerce company (2011–2015), which wound down before the domain passed to Epic Games; see x-identity-note. Fab publishes no public developer API, developer portal, or machine-readable specification as of this pass — the surface captured here is its documentation, support, and security-disclosure posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fabcom.png
layout: provider
modified: '2026-07-20'
name: Fab.com
nav: Providers
network: true
overview: 'Fab.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Digital Assets, 3D Content, and Game Development.


  Fab.com''s developer surface includes documentation, getting-started guide, support, and 9 more developer resources.'
random_paper: 49
score:
  band: emerging
  composite: 15.0
  delta: 0.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 14.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fabcom/refs/heads/main/screenshots/fabcom-2026-07-25T214107.png
security:
- kind: domain-security
  name: Fabcom Domain Security
  slug: fabcom-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Fabcom Vulnerability Disclosure
  slug: fabcom-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: fabcom
tags:
- Company
- Marketplace
- Digital Assets
- 3D Content
- Game Development
- Creator Economy
- Ecommerce
- Unreal Engine
- Epic Games
website: https://www.fab.com/
---
