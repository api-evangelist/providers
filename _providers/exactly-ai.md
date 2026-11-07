---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Exactly Ai Agentic Access
  operation_count: 20
  slug: exactly-ai-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.exactly.ai
  baseurl_source: declared
  description: The Images v1 API from Exactly Ai — 6 operation(s) for images v1.
  name: Exactly Ai Images v1 API
  slug: exactly-ai-images-v1-api
- baseURL: https://api.exactly.ai
  baseurl_source: declared
  description: The Models v1 API from Exactly Ai — 9 operation(s) for models v1.
  name: Exactly Ai Models v1 API
  slug: exactly-ai-models-v1-api
arazzos:
- description: Generate an image from an existing style model, then upscale, vectorize, and remove its background.
  name: Exactly.ai — generate and post-process an image
  slug: exactly-ai-generate-and-postprocess
- description: Create a custom style model, train it on brand images, then generate on-brand images once ready.
  name: Exactly.ai — train a style model and generate images
  slug: exactly-ai-train-and-generate
artifact_total: 15
collections:
- collection_type: open
  name: Exactly Public Images v1 API
  slug: open-exactly-ai-images-v1-api
- collection_type: open
  name: Exactly Public Images v1 Models v1 API
  slug: open-exactly-ai-models-v1-api
common:
- group: company
  title: ''
  type: Blog
  url: https://exactly.ai/community/blog
- group: commercial
  href: https://artifacts.apis.io/exactly-ai/plans/exactly-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/exactly-ai-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.exactly.ai/
- group: other
  href: https://artifacts.apis.io/exactly-ai/capabilities/exactly-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/exactly-ai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/exactly-ai/agentic-access/exactly-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/exactly-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/exactly-ai/security/exactly-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/exactly-ai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.exactly.ai/public/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.exactly.ai/public/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.exactly.ai/public/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://exactly.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://exactly.ai/help-center
- group: start
  title: ''
  type: SignUp
  url: https://exactly.ai/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exactly.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exactly.ai/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://exactly.ai/help-center/collections/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exactly-ai
- group: auth
  title: ''
  type: Compliance
  url: https://exactly.ai/help-center/data-protection-privacy-ico-registered-private-by-default
- group: auth
  href: https://artifacts.apis.io/exactly-ai/authentication/exactly-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/exactly-ai-authentication.yml
- group: docs
  href: https://artifacts.apis.io/exactly-ai/openapi/_original/exactly-ai-public-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/exactly-ai-public-openapi-original.json
- group: agent
  href: https://artifacts.apis.io/exactly-ai/llms/exactly-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/exactly-ai-llms.txt
- group: design
  href: https://artifacts.apis.io/exactly-ai/errors/exactly-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/exactly-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/exactly-ai/conventions/exactly-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/exactly-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/exactly-ai/data-model/exactly-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/exactly-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/exactly-ai/lifecycle/exactly-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/exactly-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/exactly-ai/conformance/exactly-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/exactly-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/exactly-ai/mcp/exactly-ai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/exactly-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/exactly-ai/overlays/exactly-ai-public-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/exactly-ai-public-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/exactly-ai/skills/exactly-ai-train-style-model.md
  title: ''
  type: AgentSkill
  url: skills/exactly-ai-train-style-model.md
- group: agent
  href: https://artifacts.apis.io/exactly-ai/skills/exactly-ai-generate-images.md
  title: ''
  type: AgentSkill
  url: skills/exactly-ai-generate-images.md
- group: design
  href: https://artifacts.apis.io/exactly-ai/arazzo/exactly-ai-train-and-generate.yml
  title: ''
  type: Arazzo
  url: arazzo/exactly-ai-train-and-generate.yml
- group: design
  href: https://artifacts.apis.io/exactly-ai/arazzo/exactly-ai-generate-and-postprocess.yml
  title: ''
  type: Arazzo
  url: arazzo/exactly-ai-generate-and-postprocess.yml
created: '2026-07-17'
description: Exactly.ai is a private, brand-safe AI image generation platform for brands, agencies, and creative teams. It trains custom AI "style" models from as few as ten brand images, then generates hundreds of on-brand image variations with consistent look and feel. Beyond generation the platform edits and animates images, pins characters, upscales to 8K, vectorizes to SVG, and removes backgrounds, with outputs fully licensed for commercial use and original artists compensated when their styles are used. Exactly.ai exposes an enterprise Public API (bearer-token authenticated) for programmatic model creation and training, image generation, upscaling, vectorization, and background removal, alongside the e.studio web product. The company is a portfolio company of Speedinvest and is tracked in the API Evangelist network.
finops:
- has_sources: true
  method: derived
  name: Exactly Ai Finops
  primary_unit: 1 license & 50 credits
  service_category: ''
  slug: exactly-ai-finops
  template: false
image: https://framerusercontent.com/images/WlAkvz0GvPEt7p9O61w5Zp9WtY.png
layout: provider
modified: '2026-10-06'
name: Exactly Ai
nav: Providers
network: true
overview: 'Exactly Ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Images v1 API and Models v1 API. Tagged areas include Company, Artificial Intelligence, Image Generation, Generative AI, and Creative Tools.


  The Exactly Ai catalog on APIs.io includes 1 Spectral governance ruleset.


  Exactly Ai''s developer surface includes engineering blog, documentation, API reference, pricing, support, signup flow, getting-started guide, and 24 more developer resources.'
plans:
- name: Exactly Ai Plans Pricing
  plan_count: 8
  slug: exactly-ai-plans-pricing
- name: Exactly Ai Price Estimates
  plan_count: 0
  slug: exactly-ai-price-estimates
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Exactly Ai API Rules
  rule_count: 52
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 6
  slug: exactly-ai-rules
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 51.0
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/exactly-ai/exactly-ai-2026-07-25T213837.png
security:
- kind: authentication
  name: Exactly Ai Authentication
  slug: exactly-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Exactly Ai Domain Security
  slug: exactly-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Generate on-brand images from a style model
  slug: exactly-ai-generate-images
- name: Train a custom exactly.ai style model
  slug: exactly-ai-train-style-model
slug: exactly-ai
tags:
- Company
- Artificial Intelligence
- Image Generation
- Generative AI
- Creative Tools
- Brands
- Machine Learning
- Media
website: https://www.exactly.ai/
---
