---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Visteon Agentic Access
  operation_count: 18
  slug: visteon-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 7
apis:
- description: The Phoenix Software Development Kit provides development tools for building automotive infotainment applications targeting Visteon hardware. Phoenix Studio 2.0 is a PC-based IDE that enables app deve
  name: Visteon Phoenix SDK
  slug: phoenix-sdk
- description: Audio playback, volume, and source management
  name: Visteon Audio API
  slug: visteon-audio-api
- description: Media library browsing, playback, and device management
  name: Visteon Media API
  slug: visteon-media-api
- description: Route planning, turn-by-turn guidance, and POI search
  name: Visteon Navigation API
  slug: visteon-navigation-api
- description: Phone call management, contacts, and call history
  name: Visteon Phone API
  slug: visteon-phone-api
- description: Display and screen configuration for multi-screen cockpit
  name: Visteon Screen Management API
  slug: visteon-screen-management-api
- description: Vehicle data including speed, fuel, HVAC, and door status
  name: Visteon Vehicle API
  slug: visteon-vehicle-api
artifact_total: 22
collections:
- collection_type: open
  name: Visteon Phoenix API
  slug: open-visteon-phoenix
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/visteon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/visteon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/visteon-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/visteon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/visteon
- group: company
  title: ''
  type: Website
  url: https://www.visteon.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.visteon.com/phoenix/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/visteon-phoenix-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/visteon-vehicle-data-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/visteon-audio-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/visteon-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/visteon-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/visteon-rules.yml
created: '2026-03-24'
description: Visteon Corporation is a global automotive electronics supplier providing innovative cockpit electronics products and connected car solutions to vehicle manufacturers worldwide. The Visteon Phoenix platform offers a JavaScript API for building HTML5-based automotive infotainment applications covering audio control, phone integration, media playback, navigation, screen management, remote UI, and vehicle data access. Phoenix Studio enables third-party app development targeting Visteon's SmartCore and display audio infotainment systems.
examples:
- key_count: 2
  name: Visteon Phoenix Getvehicledata Example
  slug: visteon-phoenix-getVehicleData-example
- key_count: 2
  name: Visteon Phoenix Startnavigation Example
  slug: visteon-phoenix-startNavigation-example
finops:
- name: Visteon Finops
  service_category: Automotive Tier-1
  slug: visteon-finops
image: https://www.visteon.com/wp-content/themes/visteon/images/visteon-logo.png
json_schemas:
- name: Visteon Audio Status
  property_count: 5
  slug: visteon-audio
- name: Visteon Vehicle Data
  property_count: 6
  slug: visteon-vehicle-data
json_structures:
- name: Visteon Vehicle Data Structure
  property_count: 0
  slug: visteon-vehicle-data-structure
jsonld:
- class_count: 39
  name: Visteon Context
  property_count: 2
  slug: visteon-context
layout: provider
modified: '2026-05-19'
name: Visteon
nav: Providers
network: true
overview: 'Visteon publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Media API, Navigation API, and 3 more. Tagged areas include Automotive, Connected Car, Infotainment, IoT, and Fortune 500.


  The Visteon catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Visteon''s developer surface includes authentication and 12 more developer resources.'
plans:
- name: Visteon Plans Pricing
  plan_count: 1
  slug: visteon-plans-pricing
press:
- date: '2026-05-25'
  title: Visteon Launches Flexible Compute Solution with NVIDIA ...
  url: https://www.prnewswire.com/news-releases/visteon-launches-flexible-compute-solution-with-nvidia-ai-to-accelerate-smart-cockpit-and-adas-development-302652616.html
- date: '2026-05-25'
  title: Flexibility meets innovation. Visteon's new AI-ADAS ...
  url: https://www.facebook.com/VisteonCorporation/posts/flexibility-meets-innovation-visteons-new-ai-adas-compute-module-powered-by-nvid/1488985699901215/
- date: '2026-05-25'
  title: Visteon Presents Its Most Comprehensive CES Showcase ...
  url: https://www.prnewswire.com/news-releases/visteon-presents-its-most-comprehensive-ces-showcase-yet-bringing-software-defined-mobility-to-life-302652609.html
- date: '2026-05-25'
  title: How To Scale AI Across Global Manufacturing Operations
  url: https://www.visteon.com/resources-insights/automotive-intellect-blog/automotive-intellect-blog-details/2025/How-To-Scale-AI-Across-Global-Manufacturing-Operations/default.aspx
- date: '2026-05-25'
  title: Technology
  url: https://www.visteon.com/products-technology/technology/default.aspx
random_paper: 80
rate_limits:
- limit_count: 1
  name: Visteon Rate Limits
  slug: visteon-rate-limits
rules:
- name: Visteon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: visteon-jsonschema-spectral-rules
- name: Visteon API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 2
    info: 0
    warn: 5
  slug: visteon-rules
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Visteon Authentication
  slug: visteon-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Visteon Domain Security
  slug: visteon-domain-security
  summary_line: TLSv1.3 · HSTS
slug: visteon
tags:
- Automotive
- Connected Car
- Infotainment
- IoT
- Fortune 500
website: https://www.visteon.com
---
