---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: Sprite AI provides a REST API for generating pixel‑art sprites, with endpoints such as /api/me, /api/sprites, and MCP server for AI generation.
  name: Sprite AI API
  slug: sprite-ai-api-2
- description: The Cancel API from Sprite AI — 1 operation(s) for cancel.
  name: Sprite AI Cancel API
  slug: sprite-ai-cancel-api
- description: The Palettes API from Sprite AI — 1 operation(s) for palettes.
  name: Sprite AI Palettes API
  slug: sprite-ai-palettes-api
- description: The Sprite AI API API from Sprite AI — 2 operation(s) for sprite ai api.
  name: Sprite AI Sprite AI API
  slug: sprite-ai-sprite-ai-api-api
- description: The Sprites API from Sprite AI — 1 operation(s) for sprites.
  name: Sprite AI Sprites API
  slug: sprite-ai-sprites-api
artifact_total: 16
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/plans/sprite-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sprite-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/rules/sprite-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/sprite-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/json-ld/sprite-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sprite-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/vocabulary/sprite-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sprite-ai-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/data-model/sprite-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sprite-ai-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/authentication/sprite-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sprite-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/conformance/sprite-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sprite-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/llms/sprite-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sprite-ai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/well-known/sprite-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sprite-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/hosts/sprite-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sprite-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/vendors/sprite-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sprite-ai-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.sprite-ai.art/docs/api-reference
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sprite-ai/refs/heads/main/security/sprite-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sprite-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sprite-ai.art
- group: docs
  title: ''
  type: Documentation
  url: https://www.sprite-ai.art/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sprite-ai.art/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sprite-ai.art/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://www.sprite-ai.art/contact
- group: company
  title: ''
  type: Blog
  url: https://www.sprite-ai.art/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sprite-ai.art/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.sprite-ai.art/signup
- group: start
  title: ''
  type: Login
  url: https://www.sprite-ai.art/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sprite-ai.art/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sprite-ai.art/privacy
coverage:
  checked: '2026-10-11'
  detail: Documentation lists endpoints but no OpenAPI or other machine‑readable contract is available.
  evidence:
  - status: 200
    url: https://www.sprite-ai.art/docs/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-11'
description: Sprite AI provides a REST API for generating pixel-art sprites using AI, targeting game developers and designers. The service lets users describe characters, items, or creatures in natural language and receive clean, ready‑to‑use sprite images instantly. Features include sprite sheet and GIF export, animation generation, and integration with popular tools like Aseprite. With a free tier offering thousands of generated sprites and paid plans for higher volume, Sprite AI aims to accelerate 2D game asset creation through fast, affordable AI‑powered art.
image: https://www.sprite-ai.art/og/og.jpg
json_schemas:
- name: GetApiApiidIdResponse
  property_count: 7
  slug: sprite-ai-get-api-apiid-id-response
- name: GetApiApiidResponse
  property_count: 7
  slug: sprite-ai-get-api-apiid-response
- name: PostApiApiidRequest
  property_count: 3
  slug: sprite-ai-post-api-apiid-request
- name: PostApiApiidResponse
  property_count: 7
  slug: sprite-ai-post-api-apiid-response
- name: PostApiPalettesGenerateRequest
  property_count: 3
  slug: sprite-ai-post-api-palettes-generate-request
- name: PostApiSpritesSpriteidResponse
  property_count: 3
  slug: sprite-ai-post-api-sprites-spriteid-response
jsonld:
- class_count: 9
  name: Sprite Ai Context
  property_count: 15
  slug: sprite-ai-context
layout: provider
modified: '2026-10-11'
name: Sprite AI
nav: Providers
network: true
overview: 'Sprite AI is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Cancel API, Palettes API, Sprite AI API, and 2 more. Tagged areas include Company, Artificial Intelligence, Gaming, Graphics, and REST API.


  The Sprite AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sprite AI''s developer surface includes authentication, API reference, documentation, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Sprite Ai Plans Pricing
  plan_count: 7
  slug: sprite-ai-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Sprite AI API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: sprite-ai-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 57.1
    discoverability: 69.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Sprite Ai Authentication
  slug: sprite-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sprite Ai Domain Security
  slug: sprite-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sprite-ai
tags:
- Company
- Artificial Intelligence
- Gaming
- Graphics
- REST API
website: https://www.sprite-ai.art
---
