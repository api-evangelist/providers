---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: Riiid's adaptive learning engine analyzes learner interaction data in real time to recommend personalized study paths and content. It is delivered inside Riiid/Socra products (Santa) and to partners v
  name: Riiid Adaptive Learning
  slug: adaptive-learning
- description: Proprietary deep knowledge tracing and score-prediction models (built on 100M+ student interactions, the EdNet dataset) estimate a learner's mastery and predict test outcomes in real time. Exposed thr
  name: Riiid Knowledge Tracing
  slug: knowledge-tracing
- description: Santa is Riiid's consumer AI tutor app for standardized English tests (TOEIC, and TOEFL via an ETS content partnership). It is distributed as iOS / Android mobile applications with no documented publi
  name: Riiid Santa
  slug: santa
- description: B2B / AI-as-a-Service (R.Inside) engagements that embed Riiid's adaptive learning and knowledge-tracing AI into partner education platforms. Access is sales-led and contract-based via partnership@socr
  name: Riiid Partner Solutions
  slug: partner-solutions
artifact_total: 9
collections:
- collection_type: open
  name: Riiid API
  slug: open-riiid
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riiid-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/riiid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/riiid
- group: company
  title: ''
  type: Website
  url: https://www.riiid.com
- group: docs
  title: ''
  type: Documentation
  url: https://corp.socra.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/riiid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/riiid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/riiid-finops.yml
created: '2026-06-21'
description: Riiid (now operating as Socra AI) is an AI education technology company whose proprietary deep-knowledge-tracing and score-prediction models power adaptive learning. Its consumer product Santa (AI TOEIC / TOEFL test prep) and its R.Inside AI-as-a-Service offering bring real-time student modeling to partners. Riiid does not publish a public, self-serve developer API; its AI is delivered through B2B partner integrations and packaged products.
finops:
- name: Riiid Finops
  service_category: AI and Machine Learning
  slug: riiid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/riiid.png
layout: provider
modified: '2026-06-21'
name: Riiid
nav: Providers
network: true
overview: 'Riiid publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Adaptive Learning, Knowledge Tracing, Santa, and 1 more. Tagged areas include AI, Education, Adaptive Learning, Knowledge Tracing, and EdTech.


  Riiid''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Riiid Plans Pricing
  plan_count: 2
  slug: riiid-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 2
  name: Riiid Rate Limits
  slug: riiid-rate-limits
score:
  band: emerging
  composite: 25.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Riiid Domain Security
  slug: riiid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: riiid
tags:
- AI
- Education
- Adaptive Learning
- Knowledge Tracing
- EdTech
website: https://www.riiid.com
---
