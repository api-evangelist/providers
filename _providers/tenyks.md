---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Tenyks Agentic Access
  operation_count: 8
  slug: tenyks-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 1
apis:
- baseURL: https://dashboard.tenyks.ai
  baseurl_source: declared
  description: Obtain a Bearer access token from an API key and secret.
  name: Tenyks Auth API
  slug: tenyks-auth-api
- baseURL: https://dashboard.tenyks.ai
  baseurl_source: declared
  description: Upload and ingest annotations, models and predictions from cloud storage.
  name: Tenyks Data Upload API
  slug: tenyks-data-upload-api
- baseURL: https://dashboard.tenyks.ai
  baseurl_source: declared
  description: Create and retrieve datasets.
  name: Tenyks Datasets API
  slug: tenyks-datasets-api
artifact_total: 16
collections:
- collection_type: open
  name: Tenyks Auth API
  slug: open-tenyks-auth-api
- collection_type: open
  name: Tenyks Auth Data Upload API
  slug: open-tenyks-data-upload-api
- collection_type: open
  name: Tenyks Auth Datasets API
  slug: open-tenyks-datasets-api
common:
- group: commercial
  href: https://artifacts.apis.io/tenyks/plans/tenyks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tenyks-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/tenyks/capabilities/tenyks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tenyks-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.tenyks.ai/
- group: auth
  href: https://artifacts.apis.io/tenyks/security/tenyks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tenyks-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/tenyks/agentic-access/tenyks-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tenyks-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tenyks.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tenyks.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tenyks.ai/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tenyks.ai/docs/the-foundations
- group: company
  title: ''
  type: Blog
  url: https://www.tenyks.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tenyks.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sandbox.tenyks.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/tenyks
- group: auth
  href: https://artifacts.apis.io/tenyks/authentication/tenyks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tenyks-authentication.yml
- group: agent
  href: https://artifacts.apis.io/tenyks/llms/tenyks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tenyks-llms.txt
- group: agent
  href: https://artifacts.apis.io/tenyks/well-known/tenyks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tenyks-well-known.yml
- group: agent
  href: https://artifacts.apis.io/tenyks/mcp/tenyks-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tenyks-mcp.yml
- group: build
  href: https://artifacts.apis.io/tenyks/packages/tenyks-packages.yml
  title: ''
  type: Packages
  url: packages/tenyks-packages.yml
- group: build
  href: https://artifacts.apis.io/tenyks/packages/tenyks-packages.yml
  title: ''
  type: SDKs
  url: packages/tenyks-packages.yml
- group: build
  href: https://artifacts.apis.io/tenyks/cli/tenyks-cli.yml
  title: ''
  type: CLI
  url: cli/tenyks-cli.yml
- group: start
  href: https://artifacts.apis.io/tenyks/sandbox/tenyks-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tenyks-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tenyks/conventions/tenyks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tenyks-conventions.yml
- group: design
  href: https://artifacts.apis.io/tenyks/errors/tenyks-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tenyks-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tenyks/lifecycle/tenyks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tenyks-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tenyks/data-model/tenyks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tenyks-data-model.yml
- group: design
  href: https://artifacts.apis.io/tenyks/conformance/tenyks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tenyks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tenyks.ai
- group: auth
  href: https://artifacts.apis.io/tenyks/security/tenyks-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tenyks-trust-center.yml
- group: other
  href: https://artifacts.apis.io/tenyks/overlays/tenyks-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tenyks-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/tenyks/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tenyks is a University of Cambridge spin-out (Y Combinator; backed by Speedinvest) building a visual-intelligence platform for computer vision. Its original product is an MLOps monitoring and validation platform that helps ML engineers working with computer-vision data find and fix what is wrong with their models — data-quality analysis, model performance comparison, text-to-image / image-to-image / object-level similarity search, embeddings, tagging and custom metadata across image and video datasets. Tenyks has since extended into a Vision AI / Video AI Agents platform that turns everyday camera feeds into privacy-first operational analytics for brick-and-mortar businesses. The Tenyks API (currently alpha, for Premium/Dashboard users, with a freemium Sandbox) lets teams authenticate with an API key + secret to obtain a Bearer token, then create datasets and models, and upload and ingest annotations and predictions directly from AWS S3, GCS or Azure. A Python SDK and CLI wrap
  the same surface.
finops:
- has_sources: true
  method: derived
  name: Tenyks Finops
  primary_unit: 1-4 users
  service_category: ''
  slug: tenyks-finops
  template: false
image: https://cdn.prod.website-files.com/63a0220866f41638081f4fce/63d07b4812f0f901e939d964_tenyks_logo-color.png
layout: provider
modified: '2026-07-21'
name: Tenyks
nav: Providers
network: true
overview: 'Tenyks publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Auth API, Data Upload API, and Datasets API. Tagged areas include Company, Computer Vision, Machine Learning, MLOps, and Data Quality.


  The Tenyks catalog on APIs.io includes 1 Spectral governance ruleset.


  Tenyks'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Tenyks Plans Pricing
  plan_count: 5
  slug: tenyks-plans-pricing
- name: Tenyks Price Estimates
  plan_count: 0
  slug: tenyks-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Tenyks API Rules
  rule_count: 61
  severity_counts:
    error: 58
    hint: 0
    info: 2
    warn: 1
  slug: tenyks-rules
score:
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.1
  facets:
    access_clarity: 72.4
    contract_governance: 31.8
    contract_quality: 54.7
    developer_ergonomics: 75.6
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tenyks/tenyks-2026-08-17T082314.png
security:
- kind: authentication
  name: Tenyks Authentication
  slug: tenyks-authentication
  summary_line: http/apiKey-exchange · 1 scheme
- kind: domain-security
  name: Tenyks Domain Security
  slug: tenyks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tenyks Trust Center
  slug: tenyks-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA
skill_count: 2
skills:
- name: Register a model and upload its predictions for evaluation
  slug: tenyks-evaluate-model
- name: Create a dataset and upload its annotations
  slug: tenyks-upload-dataset
slug: tenyks
tags:
- Company
- Computer Vision
- Machine Learning
- MLOps
- Data Quality
- Model Validation
- Visual Intelligence
- Video Analytics
- Artificial Intelligence
- Developer Tools
website: https://www.tenyks.ai/
---
