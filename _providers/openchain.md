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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: API for accessing OpenChain open source license compliance resources, standards documentation, and organizational benchmarking tools for software supply chain trust.
  name: OpenChain API
  slug: openchain-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openchain-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openchain
- group: docs
  title: ''
  type: Documentation
  url: https://www.openchainproject.org/resources
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/OpenChain-Project
- group: agent
  title: ''
  type: LlmsText
  url: https://openchainproject.org/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://openchainproject.org/feed
created: '2026-03-16'
description: OpenChain is an international standard (ISO/IEC 5230) under the Linux Foundation for open source license compliance programs. It helps organizations manage open source licensing consistently by providing a benchmark for trust between organizations in the software supply chain.
finops:
- name: Openchain Finops
  service_category: API
  slug: openchain-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openchain.png
layout: provider
modified: '2026-04-28'
name: OpenChain
nav: Providers
network: true
overview: 'OpenChain publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, Licensing, Linux Foundation, and Standards.


  OpenChain''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Openchain Plans Pricing
  plan_count: 3
  slug: openchain-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Openchain Rate Limits
  slug: openchain-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 19.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openchain/refs/heads/main/screenshots/openchain-2026-06-20T190919.png
security:
- kind: domain-security
  name: Openchain Domain Security
  slug: openchain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openchain
tags:
- Compliance
- Licensing
- Linux Foundation
- Standards
---
