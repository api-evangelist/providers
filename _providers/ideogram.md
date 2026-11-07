---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Ideogram Agentic Access
  operation_count: 23
  slug: ideogram-agentic-access
  summary_line: 23 operations · 19 acting
api_count: 1
apis:
- baseURL: https://api.ideogram.ai
  baseurl_source: declared
  description: The subpackage_datasets API from Ideogram — 3 operation(s) for subpackage_datasets.
  name: Ideogram Subpackage Datasets API
  slug: ideogram-subpackage-datasets-api
- baseURL: https://api.ideogram.ai
  baseurl_source: declared
  description: The subpackage_generate API from Ideogram — 15 operation(s) for subpackage_generate.
  name: Ideogram Subpackage Generate API
  slug: ideogram-subpackage-generate-api
- baseURL: https://api.ideogram.ai
  baseurl_source: declared
  description: The subpackage_models API from Ideogram — 3 operation(s) for subpackage_models.
  name: Ideogram Subpackage Models API
  slug: ideogram-subpackage-models-api
- baseURL: https://api.ideogram.ai
  baseurl_source: declared
  description: The subpackage_vision API from Ideogram — 1 operation(s) for subpackage_vision.
  name: Ideogram Subpackage Vision API
  slug: ideogram-subpackage-vision-api
artifact_total: 17
collections:
- collection_type: open
  name: API Reference subpackage_datasets API
  slug: open-ideogram-subpackage-datasets-api
- collection_type: open
  name: API Reference subpackage_datasets subpackage_generate API
  slug: open-ideogram-subpackage-generate-api
- collection_type: open
  name: API Reference subpackage_datasets subpackage_models API
  slug: open-ideogram-subpackage-models-api
- collection_type: open
  name: API Reference subpackage_datasets subpackage_vision API
  slug: open-ideogram-subpackage-vision-api
- collection_type: open
  name: API Reference
  slug: open-ideogram
common:
- group: company
  title: ''
  type: Blog
  url: https://ideogram.ai/blog/
- group: other
  href: https://artifacts.apis.io/ideogram/capabilities/ideogram-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ideogram-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/ideogram/agentic-access/ideogram-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ideogram-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ideogram/security/ideogram-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ideogram-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ideogram/authentication/ideogram-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ideogram-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ideogram-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ideogram-ai
- group: company
  title: ''
  type: Website
  url: https://ideogram.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ideogram.ai/
- group: docs
  href: https://artifacts.apis.io/ideogram/openapi/_original/ideogram-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/ideogram-openapi.yml
- group: commercial
  href: https://artifacts.apis.io/ideogram/plans/ideogram-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ideogram-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ideogram/rate-limits/ideogram-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ideogram-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ideogram/finops/ideogram-finops.yml
  title: ''
  type: FinOps
  url: finops/ideogram-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.ideogram.ai/llms.txt
created: '2026-05-08'
description: Ideogram is an image generation platform notable for industry-leading text-in-image rendering. The Ideogram API (3.0 and beyond) supports generation, edit, inpaint, remix, reframe, replace background, layerize text, upscale, describe, and remove background, plus custom model training with dataset and asset management. Authenticated REST API with published OpenAPI 3.1 spec.
finops:
- has_sources: true
  method: generated
  name: Ideogram Finops
  primary_unit: ''
  service_category: AI
  slug: ideogram-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ideogram.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.ideogram.ai over HTTP.
  name: Ideogram MCP Server
  slug: ideogram
modified: '2026-10-06'
name: Ideogram
nav: Providers
network: true
overview: 'Ideogram publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Subpackage Datasets API, Subpackage Generate API, Subpackage Models API, and 1 more. Tagged areas include Artificial Intelligence, Image Generation, Text, Realistic, and Editing.


  The Ideogram catalog on APIs.io includes 1 Spectral governance ruleset.


  Ideogram''s developer surface includes engineering blog, authentication, documentation, and 11 more developer resources.'
plans:
- name: Ideogram Plans Pricing
  plan_count: 2
  slug: ideogram-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Ideogram Rate Limits
  slug: ideogram-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Ideogram API Rules
  rule_count: 58
  severity_counts:
    error: 41
    hint: 0
    info: 2
    warn: 15
  slug: ideogram-rules
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 30.5
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 7.9
  previous_composite: 26.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 15.4
      total: 26
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ideogram/ideogram-2026-06-20T183206.png
security:
- kind: authentication
  name: Ideogram Authentication
  slug: ideogram-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ideogram Domain Security
  slug: ideogram-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ideogram
tags:
- Artificial Intelligence
- Image Generation
- Text
- Realistic
- Editing
website: https://ideogram.ai/
---
