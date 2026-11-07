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
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 4
  name: Moondream Agentic Access
  operation_count: 6
  slug: moondream-agentic-access
  summary_line: 6 operations · 5 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.moondream.ai/v1
  baseurl_source: declared
  description: OpenAI-compatible chat completions endpoint.
  name: Moondream OpenAI Compatibility API
  slug: moondream-openai-compatibility-api
- baseURL: https://api.moondream.ai/v1
  baseurl_source: declared
  description: Moondream vision Skills — query, caption, detect, point, segment.
  name: Moondream Skills API
  slug: moondream-skills-api
artifact_total: 14
collections:
- collection_type: open
  name: Moondream Cloud OpenAI Compatibility API
  slug: open-moondream-openai-compatibility-api
- collection_type: open
  name: Moondream Cloud OpenAI Compatibility Skills API
  slug: open-moondream-skills-api
common:
- group: commercial
  href: https://artifacts.apis.io/moondream/plans/moondream-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moondream-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/moondream/authentication/moondream-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moondream-authentication.yml
- group: design
  href: https://artifacts.apis.io/moondream/conventions/moondream-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moondream-conventions.yml
- group: design
  href: https://artifacts.apis.io/moondream/errors/moondream-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moondream-problem-types.yml
- group: design
  href: https://artifacts.apis.io/moondream/lifecycle/moondream-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moondream-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/moondream/conformance/moondream-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moondream-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://moondream.ai/pricing
- group: design
  href: https://artifacts.apis.io/moondream/data-model/moondream-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moondream-data-model.yml
- group: other
  href: https://artifacts.apis.io/moondream/overlays/moondream-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moondream-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/moondream/packages/moondream-packages.yml
  title: ''
  type: Packages
  url: packages/moondream-packages.yml
- group: build
  href: https://artifacts.apis.io/moondream/packages/moondream-packages.yml
  title: ''
  type: SDKs
  url: packages/moondream-packages.yml
- group: agent
  href: https://artifacts.apis.io/moondream/mcp/moondream-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/moondream-mcp.yml
- group: agent
  href: https://artifacts.apis.io/moondream/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/moondream/llms/moondream-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moondream-llms.txt
- group: agent
  href: https://artifacts.apis.io/moondream/well-known/moondream-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moondream-well-known.yml
- group: operate
  href: https://artifacts.apis.io/moondream/changelog/moondream-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/moondream-changelog.yml
- group: auth
  href: https://artifacts.apis.io/moondream/security/moondream-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moondream-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/moondream/agentic-access/moondream-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moondream-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://moondream.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.moondream.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moondream.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moondream.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moondream.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://moondream.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://moondream.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://moondream.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moondream.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moondream.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/m87-labs
- group: start
  title: ''
  type: Sandbox
  url: https://moondream.ai/c/playground
- group: operate
  title: ''
  type: Support
  url: mailto:sales@moondream.ai
created: '2026-07-17'
description: Moondream is a fast, efficient open vision language model (VLM) from M87 Labs. The Moondream Cloud API turns images into structured output through five Skills — Query (visual question answering), Caption, Detect (bounding boxes), Point (center coordinates), and Segment (SVG path masks) — plus an OpenAI-compatible chat endpoint, an asynchronous Batch API, and cloud finetuning (Lens). Model weights are open and downloadable from Hugging Face; hosted inference is pay-per-token with HIPAA and SOC 2 available. Official Python and Node.js SDKs are published.
finops:
- has_sources: true
  method: derived
  name: Moondream Finops
  primary_unit: 1m output tokens
  service_category: ''
  slug: moondream-finops
  template: false
image: https://moondream.ai/apple-touch-icon.png
layout: provider
modified: '2026-07-20'
name: Moondream
nav: Providers
network: true
overview: 'Moondream publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: OpenAI Compatibility API and Skills API. Tagged areas include Company, Artificial Intelligence, Machine Learning, Computer Vision, and Vision Language Model.


  The Moondream catalog on APIs.io includes 1 Spectral governance ruleset.


  Moondream''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Moondream Plans Pricing
  plan_count: 13
  slug: moondream-plans-pricing
- name: Moondream Price Estimates
  plan_count: 0
  slug: moondream-price-estimates
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Moondream API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: moondream-rules
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 14.5
    developer_ergonomics: 69.6
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/moondream/moondream-2026-08-07T184237.png
security:
- kind: authentication
  name: Moondream Authentication
  slug: moondream-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Moondream Domain Security
  slug: moondream-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Caption an image
  slug: moondream-caption-image
- name: Detect and locate objects in an image
  slug: moondream-detect-and-point
- name: Ask questions about an image
  slug: moondream-visual-qa
slug: moondream
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Computer Vision
- Vision Language Model
- Object Detection
- Image Captioning
- OCR
- Developer Tools
website: https://moondream.ai
---
