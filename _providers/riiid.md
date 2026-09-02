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
    agentic_commerce: false
    auth_clarity: false
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
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
overview: 'Riiid publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Adaptive Learning, Knowledge Tracing, Santa, and 1 more. Tagged areas include Artificial Intelligence, Education, Adaptive Learning, Knowledge Tracing, and EdTech.


  Riiid''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Riiid Plans Pricing
  plan_count: 2
  slug: riiid-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Riiid Rate Limits
  slug: riiid-rate-limits
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 27.9
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 23.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Riiid Domain Security
  slug: riiid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: riiid
tags:
- Artificial Intelligence
- Education
- Adaptive Learning
- Knowledge Tracing
- EdTech
website: https://www.riiid.com
---
