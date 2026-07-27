---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tsinghua Agentic Access
  operation_count: 1
  slug: tsinghua-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Endpoints describing mirror synchronization state.
  name: Tsinghua University Mirror Status API
  slug: tsinghua-mirror-status-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tsinghua-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tsinghua-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tsinghua.edu.cn/en/
- group: build
  title: ''
  type: Library
  url: https://lib.tsinghua.edu.cn/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tuna
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tsinghua-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/tsinghua-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tsinghua-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tsinghua-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tsinghua University is a leading public research university in Beijing, China, ranked #23 in the QS World University Rankings 2025. Like most Chinese universities, Tsinghua does not operate a centralized public developer portal or documented institutional API program; its student, course, and library systems sit behind campus SSO and are not publicly documented. The most notable public, programmatically accessible service is the TUNA open-source mirror (mirrors.tuna.tsinghua.edu.cn), run by the student TUNA association, which exposes machine-readable JSON status endpoints. A number of Tsinghua research labs (THUNLP, THUML, TUNA, Tsinghua Database Group) maintain active open-source code on GitHub, but these are project repositories rather than an institution-wide API platform.'
finops:
- name: Tsinghua Finops
  service_category: Education
  slug: tsinghua-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tsinghua.png
json_schemas:
- name: MirrorStatus
  property_count: 13
  slug: tsinghua-mirror-status
json_structures:
- name: Tsinghua Mirror Status Structure
  property_count: 13
  slug: tsinghua-mirror-status-structure
jsonld:
- class_count: 11
  name: Tsinghua Context
  property_count: 6
  slug: tsinghua-context
layout: provider
modified: '2026-06-03'
name: Tsinghua University
nav: Providers
network: true
overview: 'Tsinghua University publishes 1 API on the [APIs.io](https://apis.io/) network: Mirror Status API. Tagged areas include Education, Higher Education, University, Research, and China.


  The Tsinghua University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tsinghua University''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: Tsinghua Plans Pricing
  plan_count: 2
  slug: tsinghua-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Tsinghua Rate Limits
  slug: tsinghua-rate-limits
rules:
- name: Tsinghua University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tsinghua-jsonschema-spectral-rules
- name: Tsinghua University API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: tsinghua-rules
score:
  band: thin
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.6
    developer_ergonomics: 0.0
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 43.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tsinghua/refs/heads/main/screenshots/tsinghua-2026-06-20T195921.png
security:
- kind: domain-security
  name: Tsinghua Domain Security
  slug: tsinghua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tsinghua
tags:
- Education
- Higher Education
- University
- Research
- China
- Open Source
website: https://www.tsinghua.edu.cn/en/
---
