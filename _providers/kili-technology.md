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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Kili Technology Agentic Access
  operation_count: 1
  slug: kili-technology-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The GraphQL API from Kili Technology — 1 operation(s) for graphql.
  name: Kili Technology GraphQL API
  slug: kili-technology-graphql-api
artifact_total: 14
asyncapis:
- description: AsyncAPI 2.6 description of Kili Technology's **GraphQL subscription** surface. Kili's labeling application is served from a single GraphQL endpoint at `https://cloud.kili-technology.com/api/label/v2/
  name: Kili Technology Label Subscription (GraphQL over WebSocket)
  slug: kili-technology-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kili Technology GraphQL API
  slug: open-kili-technology-graphql-api
- collection_type: open
  name: Kili Technology GraphQL API
  slug: open-kili-technology
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kili-technology-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kili-technology-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kili-technology-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kili-technology-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kili-technology
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kili-technology
- group: company
  title: ''
  type: Website
  url: https://kili-technology.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kili-technology.com
- group: commercial
  title: ''
  type: Plans
  url: plans/kili-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kili-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kili-technology-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://kili-technology.com/blog/rss.xml
created: '2026-06-21'
description: Kili Technology is a training-data and data-labeling platform for building high-quality datasets for machine learning and LLMs. Its labeling application is fully programmable through a single GraphQL API (and a Python SDK) covering projects, assets, labels, issues, and users at https://cloud.kili-technology.com/api/label/v2/graphql.
finops:
- name: Kili Technology Finops
  service_category: AI and Machine Learning
  slug: kili-technology-finops
graphqls:
- description: GraphQL interface for the [Kili Technology](https://kili-technology.com) training-data and
  name: Kili Technology GraphQL API
  slug: kili-technology-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kili-technology.png
layout: provider
modified: '2026-06-21'
name: Kili Technology
nav: Providers
network: true
overview: 'Kili Technology publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include AI, Data Labeling, Training Data, Annotation, and GraphQL.


  The Kili Technology catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kili Technology''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Kili Technology Plans Pricing
  plan_count: 4
  slug: kili-technology-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 3
  name: Kili Technology Rate Limits
  slug: kili-technology-rate-limits
rules:
- name: Kili Technology API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: kili-technology-asyncapi-spectral-rules
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 73.9
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kili-technology/refs/heads/main/screenshots/kili-technology-2026-07-25T223739.png
security:
- kind: authentication
  name: Kili Technology Authentication
  slug: kili-technology-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Kili Technology Domain Security
  slug: kili-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Kili Technology Trust Center
  slug: kili-technology-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: kili-technology
tags:
- AI
- Data Labeling
- Training Data
- Annotation
- GraphQL
website: https://kili-technology.com
---
