---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/comfyui/hosts/comfyui-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comfyui-hosts.yml
- group: other
  href: https://artifacts.apis.io/comfyui/vendors/comfyui-vendors.yml
  title: ''
  type: Vendors
  url: vendors/comfyui-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://comfyui.org/en/collections/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jiangsi
- group: auth
  href: https://artifacts.apis.io/comfyui/security/comfyui-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comfyui-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://comfy.org
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.comfyui.org
  - status: 200
    url: https://forgeglobal.com/comfyui_stock/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: ComfyUI is an open-source, node-based stable diffusion UI that enables users to create complex image generation workflows through a visual programming interface. It provides a modular architecture, extensive community-contributed nodes, and integration with various AI models, making it a powerful tool for artists, developers, and researchers to prototype and produce high-quality AI-generated visuals. The platform supports custom extensions, real-time preview, and collaborative sharing of workflows, fostering an active ecosystem of contributors and users.
image: https://image.edgecd.com/logo512512.jpg
layout: provider
modified: '2026-10-09'
name: ComfyUI
nav: Providers
network: true
overview: ComfyUI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Open Source, Image Generation, Workflows, and Community.
random_paper: 20
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 2.6
  previous_composite: 3.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/comfyui/comfyui-2026-11-03T125019.png
security:
- kind: domain-security
  name: Comfyui Domain Security
  slug: comfyui-domain-security
  summary_line: TLSv1.3 · DMARC
slug: comfyui
tags:
- Artificial Intelligence
- Open Source
- Image Generation
- Workflows
- Community
website: https://comfy.org
---
