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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: OpenBU is Boston University Libraries' open-access institutional repository, built on DSpace. It exposes a publicly accessible OAI-PMH 2.0 endpoint for harvesting metadata (theses, dissertations, jour
  name: OpenBU Repository OAI-PMH API
  slug: openbu-oai
- description: Boston University IS&T provides gated access to Large Language Model API keys for academic and research use, brokering frontier models via Microsoft Azure OpenAI and Amazon Bedrock (including Anthropi
  name: AI API Access (Azure OpenAI / Amazon Bedrock)
  slug: ai-api-access
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boston-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bu.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/bu-ist
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/boston-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/boston-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/boston-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/boston-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Boston University is a private research university in Boston, Massachusetts, chartered in 1869, ranked #88 in the QS World University Rankings 2025. It serves over 34,000 students across three campuses with 300+ programs of study. Its public developer/API footprint is modest and largely gated: the most clearly public, machine-readable interface is the OpenBU institutional repository (DSpace) OAI-PMH endpoint. Boston University also references an internal API portal (webapi.bu.edu) and offers gated LLM API key access via Azure OpenAI and Amazon Bedrock through IS&T, but those are not publicly reachable or documented without authorization.'
finops:
- name: Boston Finops
  service_category: Education
  slug: boston-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boston.png
jsonld:
- class_count: 25
  name: Boston Context
  property_count: 5
  slug: boston-context
layout: provider
modified: '2026-06-03'
name: Boston University
nav: Providers
network: true
overview: 'Boston University publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Library.


  The Boston University catalog on APIs.io includes 1 JSON-LD context.


  Boston University''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: Boston Plans Pricing
  plan_count: 2
  slug: boston-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 1
  name: Boston Rate Limits
  slug: boston-rate-limits
score:
  band: emerging
  composite: 21.4
  delta: 0.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.0
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boston/refs/heads/main/screenshots/boston-2026-06-20T173612.png
security:
- kind: domain-security
  name: Boston Domain Security
  slug: boston-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boston
tags:
- Education
- Higher Education
- University
- Research
- Library
- Open Data
- United States
website: https://www.bu.edu/
---
