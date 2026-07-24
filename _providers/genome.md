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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Genome Agentic Access
  operation_count: 2
  slug: genome-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 3
apis:
- description: Below you can find the information and tutorials that will teach you how to use Genome hosted payment pages, host to host integration, Payout API and Query on demand API.
  name: Genome
  slug: genome
- description: Direct card processing
  name: Genome Host-to-Host API
  slug: genome-host-to-host-api
- description: Send funds to cardholders
  name: Genome Payouts API
  slug: genome-payouts-api
artifact_total: 9
collections:
- collection_type: open
  name: Genome Payments API
  slug: open-genome
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/genome-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genome-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genome
- group: company
  title: ''
  type: Website
  url: https://genome.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.genome.eu/
created: '2025-03-01'
description: Below you can find the information and tutorials that will teach you how to use Genome hosted payment pages, host to host integration, Payout API and Query on demand API.
finops:
- name: Genome Finops
  service_category: API
  slug: genome-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/genome.png
layout: provider
modified: '2026-04-28'
name: Genome
nav: Providers
network: true
overview: 'Genome publishes 2 APIs on the [APIs.io](https://apis.io/) network: Host-to-Host API and Payouts API. Tagged areas include Finance and Payments.


  Genome''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Genome Plans Pricing
  plan_count: 3
  slug: genome-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Genome Rate Limits
  slug: genome-rate-limits
score:
  band: emerging
  composite: 29.5
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 8.7
    discoverability: 42.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.4
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genome/refs/heads/main/screenshots/genome-2026-06-20T181737.png
security:
- kind: domain-security
  name: Genome Domain Security
  slug: genome-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: genome
tags:
- Finance
- Payments
website: https://genome.eu/
---
