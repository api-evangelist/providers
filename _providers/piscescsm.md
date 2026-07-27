---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
- acting_count: 1
  human_in_the_loop: 0
  name: Piscescsm Agentic Access
  operation_count: 2
  slug: piscescsm-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: The Predict API from piscesCSM — 1 operation(s) for predict.
  name: piscesCSM Predict API
  slug: piscescsm-predict-api
artifact_total: 7
collections:
- collection_type: open
  name: piscesCSM API
  slug: open-piscescsm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/piscescsm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/piscescsm-domain-security.yml
created: '2025-03-01'
description: Here we offer an API (Application Programming Interface) to assist users in integrating piscesCSM into their research pipelines.In summary, all jobs submitted to our server are labelled with a unique ID which is used to query the status of the job.
finops:
- name: Piscescsm Finops
  service_category: API
  slug: piscescsm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/piscescsm.png
layout: provider
modified: '2026-05-19'
name: piscesCSM
nav: Providers
network: true
overview: 'piscesCSM publishes 1 API on the [APIs.io](https://apis.io/) network: Predict API. Tagged areas include Bioinformatics, Drug Discovery, and Cancer.'
plans:
- name: Piscescsm Plans Pricing
  plan_count: 3
  slug: piscescsm-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Piscescsm Rate Limits
  slug: piscescsm-rate-limits
score:
  band: thin
  composite: 34.0
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 30.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/piscescsm/refs/heads/main/screenshots/piscescsm-2026-06-20T191731.png
security:
- kind: domain-security
  name: Piscescsm Domain Security
  slug: piscescsm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: piscescsm
tags:
- Bioinformatics
- Drug Discovery
- Cancer
---
