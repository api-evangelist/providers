---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tettra Agentic Access
  operation_count: 2
  slug: tettra-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: The Teams API from Tettra — 2 operation(s) for teams.
  name: Tettra Teams API
  slug: tettra-teams-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tettra REST Teams API
  slug: open-tettra-teams-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tettra-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tettra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tettra-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tettra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.tettra.com/api-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://tettra.com/pricing/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.tettra.co/
- group: operate
  title: ''
  type: Status
  url: https://tettra.statuspage.io/
- group: company
  title: ''
  type: Blog
  url: https://tettra.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tettra
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Tettra
- group: commercial
  title: ''
  type: Plans
  url: plans/tettra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tettra-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tettra-finops.yml
created: '2026-06-13'
description: Tettra is an AI-powered knowledge management system that helps teams curate company policies, processes, and knowledge articles into a searchable internal wiki. It provides a REST API for managing pages, categories, and Q&A workflows, with an AI assistant (Kai) integrated directly into Slack and Microsoft Teams to answer repetitive questions from your knowledge base automatically.
examples:
- key_count: 6
  name: Create Question Request
  slug: create-question-request
- key_count: 3
  name: Search Response
  slug: search-response
finops:
- name: Tettra Finops
  service_category: ''
  slug: tettra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tettra.png
json_schemas:
- name: Category
  property_count: 3
  slug: category
- name: CreateQuestionRequest
  property_count: 6
  slug: create-question-request
- name: PageResult
  property_count: 7
  slug: page-result
jsonld:
- class_count: 9
  name: Tettra Context
  property_count: 0
  slug: tettra
layout: provider
modified: '2026-06-13'
name: Tettra
nav: Providers
network: true
overview: 'Tettra publishes 1 API on the [APIs.io](https://apis.io/) network: Teams API. Tagged areas include Knowledge-Management, Artificial Intelligence, Team Collaboration, Wiki, and Slack Integration.


  The Tettra catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tettra''s developer surface includes authentication, documentation, pricing, changelog, status page, engineering blog, GitHub presence, and 7 more developer resources.'
plans:
- name: Tettra Plans Pricing
  plan_count: 2
  slug: tettra-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Tettra Rate Limits
  slug: tettra-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tettra API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tettra-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.6
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tettra/refs/heads/main/screenshots/tettra-2026-06-20T195201.png
security:
- kind: authentication
  name: Tettra Authentication
  slug: tettra-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tettra Domain Security
  slug: tettra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tettra
tags:
- Knowledge-Management
- Artificial Intelligence
- Team Collaboration
- Wiki
- Slack Integration
- Q&A Bot
- Internal Documentation
website: https://tettra.com/
---
