---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Argilla Agentic Access
  operation_count: 73
  slug: argilla-agentic-access
  summary_line: 73 operations · 44 acting
api_count: 15
apis:
- description: The Authentication API from Argilla — 4 operation(s) for authentication.
  name: Argilla Authentication API
  slug: argilla-authentication-api
- description: The datasets API from Argilla — 19 operation(s) for datasets.
  name: Argilla datasets API
  slug: argilla-datasets-api
- description: The fields API from Argilla — 1 operation(s) for fields.
  name: Argilla fields API
  slug: argilla-fields-api
- description: The info API from Argilla — 2 operation(s) for info.
  name: Argilla info API
  slug: argilla-info-api
- description: The jobs API from Argilla — 1 operation(s) for jobs.
  name: Argilla jobs API
  slug: argilla-jobs-api
- description: The metadata properties API from Argilla — 2 operation(s) for metadata properties.
  name: Argilla metadata properties API
  slug: argilla-metadata-properties-api
- description: The questions API from Argilla — 1 operation(s) for questions.
  name: Argilla questions API
  slug: argilla-questions-api
- description: The records API from Argilla — 3 operation(s) for records.
  name: Argilla records API
  slug: argilla-records-api
- description: The responses API from Argilla — 2 operation(s) for responses.
  name: Argilla responses API
  slug: argilla-responses-api
- description: The settings API from Argilla — 1 operation(s) for settings.
  name: Argilla settings API
  slug: argilla-settings-api
- description: The suggestions API from Argilla — 1 operation(s) for suggestions.
  name: Argilla suggestions API
  slug: argilla-suggestions-api
- description: The users API from Argilla — 4 operation(s) for users.
  name: Argilla users API
  slug: argilla-users-api
- description: The vectors-settings API from Argilla — 1 operation(s) for vectors-settings.
  name: Argilla vectors-settings API
  slug: argilla-vectors-settings-api
- description: The webhooks API from Argilla — 3 operation(s) for webhooks.
  name: Argilla webhooks API
  slug: argilla-webhooks-api
- description: The workspaces API from Argilla — 5 operation(s) for workspaces.
  name: Argilla workspaces API
  slug: argilla-workspaces-api
artifact_total: 37
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/argilla-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argilla-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/argilla-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://argilla.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.argilla.io/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/argilla-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/argilla-io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/argilla_io
- group: company
  title: ''
  type: Blog
  url: https://argilla.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://argilla.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/argilla-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/argilla-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/argilla-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/argilla-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/argilla-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: 2026-06-12
description: Argilla is an open-source data annotation and curation platform designed for AI engineers and domain experts building high-quality datasets for LLMs and NLP models. The platform provides a FastAPI-based REST API for managing workspaces, datasets, records, responses, suggestions, and vectors, enabling RLHF and preference tuning pipelines. Developers interact with Argilla through a Python SDK (pip install argilla) or directly via REST using API key authentication. Argilla supports deployment on Hugging Face Spaces, Docker, and self-hosted environments, and is licensed under Apache-2.0. The platform recently joined Hugging Face, deepening its integration with the broader open ML ecosystem.
examples:
- key_count: 4
  name: Argilla Add Records Example
  slug: argilla-add-records-example
- key_count: 4
  name: Argilla Create Dataset Example
  slug: argilla-create-dataset-example
- key_count: 4
  name: Argilla Submit Response Example
  slug: argilla-submit-response-example
finops:
- name: Argilla Finops
  service_category: ''
  slug: argilla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argilla.png
json_schemas:
- name: Dataset
  property_count: 11
  slug: argilla-dataset
- name: Field
  property_count: 8
  slug: argilla-field
- name: MetadataProperty
  property_count: 8
  slug: argilla-metadataproperty
- name: Question
  property_count: 9
  slug: argilla-question
- name: Record
  property_count: 11
  slug: argilla-record
- name: Response
  property_count: 7
  slug: argilla-response
- name: Suggestion
  property_count: 8
  slug: argilla-suggestion
- name: User
  property_count: 8
  slug: argilla-user
- name: VectorSettings
  property_count: 7
  slug: argilla-vectorsettings
- name: Webhook
  property_count: 8
  slug: argilla-webhook
- name: Workspace
  property_count: 4
  slug: argilla-workspace
jsonld:
- class_count: 13
  name: Argilla Context
  property_count: 25
  slug: argilla-context
layout: provider
modified: 2026-06-12
name: Argilla
nav: Providers
network: true
overview: 'Argilla publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, datasets API, fields API, and 12 more. Tagged areas include data annotation, LLM, NLP, RLHF, and machine learning.


  The Argilla catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Argilla''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Argilla Plans Pricing
  plan_count: 2
  slug: argilla-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 2
  name: Argilla Rate Limits
  slug: argilla-rate-limits
rules:
- name: Argilla API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: argilla-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/argilla/refs/heads/main/screenshots/argilla-2026-06-20T172416.png
security:
- kind: authentication
  name: Argilla Authentication
  slug: argilla-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Argilla Domain Security
  slug: argilla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: argilla
tags:
- data annotation
- LLM
- NLP
- RLHF
- machine learning
- datasets
- open source
- human feedback
- fine-tuning
- Hugging Face
website: https://argilla.io/
---
