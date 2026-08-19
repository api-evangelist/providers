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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Tint Agentic Access
  operation_count: 41
  slug: tint-agentic-access
  summary_line: 41 operations · 24 acting
api_count: 6
apis:
- description: Claims handling from FNOL through settlement.
  name: Tint Claims API
  slug: tint-claims-api
- description: Decision Engine decisions and Score Module scores.
  name: Tint Decisions API
  slug: tint-decisions-api
- description: Policy lifecycle and endorsements.
  name: Tint Policies API
  slug: tint-policies-api
- description: Insurance products (programs) and plans.
  name: Tint Programs API
  slug: tint-programs-api
- description: Questionnaire definitions attached to policies.
  name: Tint Questionnaires API
  slug: tint-questionnaires-api
- description: Rated plan quotes for a policy.
  name: Tint Quotes API
  slug: tint-quotes-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tint Claims API
  slug: open-tint-claims-api
- collection_type: open
  name: Tint Claims Decisions API
  slug: open-tint-decisions-api
- collection_type: open
  name: Tint Claims Policies API
  slug: open-tint-policies-api
- collection_type: open
  name: Tint Claims Programs API
  slug: open-tint-programs-api
- collection_type: open
  name: Tint Claims Questionnaires API
  slug: open-tint-questionnaires-api
- collection_type: open
  name: Tint Claims Quotes API
  slug: open-tint-quotes-api
- collection_type: open
  name: Tint API
  slug: open-tint
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tint-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tint-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tint-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tint-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tint-ai
- group: company
  title: ''
  type: Website
  url: https://www.tint.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tint.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/tint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tint-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tint-finops.yml
created: '2026-06-25'
description: Tint is an embedded protection / insurance-as-a-service infrastructure provider whose Hermes platform lets tech platforms launch and operate embedded insurance programs. The Tint API v2 exposes programmatic quoting, binding, policy lifecycle management, endorsements, claims, payments, and webhooks under a single Bearer-authenticated REST surface at https://api.tint.ai/v2.
finops:
- name: Tint Finops
  service_category: Insurance and Financial Services
  slug: tint-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tint.png
layout: provider
modified: '2026-06-25'
name: Tint
nav: Providers
network: true
overview: 'Tint publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Claims API, Decisions API, Policies API, and 3 more. Tagged areas include Insurance, Embedded Insurance, InsurTech, Insurance as a Service, and Protection.


  Tint''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Tint Plans Pricing
  plan_count: 1
  slug: tint-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Tint Rate Limits
  slug: tint-rate-limits
score:
  band: thin
  composite: 31.8
  delta: 0.2
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Tint Authentication
  slug: tint-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tint Domain Security
  slug: tint-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tint
tags:
- Insurance
- Embedded Insurance
- InsurTech
- Insurance as a Service
- Protection
website: https://www.tint.ai
---
