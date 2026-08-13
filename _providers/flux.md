---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Flux Agentic Access
  operation_count: 9
  slug: flux-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 3
apis:
- description: Endpoints for submitting image editing requests using FLUX.1 Kontext models. Accepts an input image and a text instruction to produce a transformed output image.
  name: Flux Editing API
  slug: flux-editing-api
- description: Endpoints for submitting image generation requests using FLUX models. Each endpoint targets a specific model variant and returns a task ID for polling.
  name: Flux Generation API
  slug: flux-generation-api
- description: Endpoints for polling the status and retrieving completed image editing results.
  name: Flux Results API
  slug: flux-results-api
artifact_total: 18
collections:
- collection_type: postman
  name: Flux Image Editing API
  slug: postman-flux-editing-api
- collection_type: postman
  name: Flux Image Editing Generation API
  slug: postman-flux-generation-api
- collection_type: postman
  name: Flux Image Editing Results API
  slug: postman-flux-results-api
- collection_type: open
  name: Flux Image Editing API
  slug: open-flux-image-editing
- collection_type: open
  name: Flux Image Generation API
  slug: open-flux-image-generation
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/black-forest-labs/flux/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/black-forest-labs/flux/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/flux/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flux-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flux-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flux-authentication.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/flux-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/flux-generation-request-schema.json
- group: company
  title: ''
  type: Website
  url: https://bfl.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bfl.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bfl.ml/quick_start/generating_images
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/black-forest-labs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/black-forest-labs/flux
- group: company
  title: ''
  type: Blog
  url: https://bfl.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bfl.ai/release-notes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bfl.ai/legal/flux-api-service-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bfl.ai/legal/privacy-policy
- group: start
  title: ''
  type: Signup
  url: https://auth.bfl.ai/register
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/black-forest-labs/flux-mcp
created: '2025-01-01'
description: An open-source text-to-image AI model developed by Black Forest Labs that generates high-quality images from text prompts with improved prompt following and visual quality.
finops:
- name: Flux Finops
  service_category: API
  slug: flux-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flux.png
json_schemas:
- name: Flux Image Generation Request
  property_count: 11
  slug: flux-generation-request
jsonld:
- class_count: 0
  name: Flux Context
  property_count: 5
  slug: flux-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Flux
nav: Providers
network: true
overview: 'Flux publishes 3 APIs on the [APIs.io](https://apis.io/) network: Editing API, Generation API, and Results API. Tagged areas include AI, Image Generation, Machine Learning, Open Source, and Text to Image.


  The Flux catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Flux''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, signup flow, and 13 more developer resources.'
plans:
- name: Flux Plans Pricing
  plan_count: 3
  slug: flux-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 5
  name: Flux Rate Limits
  slug: flux-rate-limits
rules:
- name: Flux API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: flux-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.9
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flux/refs/heads/main/screenshots/flux-2026-06-20T181418.png
security:
- kind: authentication
  name: Flux Authentication
  slug: flux-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flux Domain Security
  slug: flux-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flux
tags:
- AI
- Image Generation
- Machine Learning
- Open Source
- Text to Image
website: https://bfl.ai/
---
