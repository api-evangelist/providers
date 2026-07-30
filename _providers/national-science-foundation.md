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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Science Foundation Agentic Access
  operation_count: 3
  slug: national-science-foundation-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- description: The Awards API from National Science Foundation — 2 operation(s) for awards.
  name: National Science Foundation Awards API
  slug: national-science-foundation-awards-api
- description: The Awards.{format} API from National Science Foundation — 1 operation(s) for awards.{format}.
  name: National Science Foundation Awards.{format} API
  slug: national-science-foundation-awards-format-api
artifact_total: 8
collections:
- collection_type: open
  name: National Science Foundation Awards API
  slug: open-national-science-foundation
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-science-foundation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-science-foundation-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nsf-open
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-science-foundation
- group: company
  title: ''
  type: Website
  url: https://www.nsf.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.nsf.gov/developer
- group: company
  title: ''
  type: Blog
  url: https://www.nsf.gov/rss/rss_www_news.xml
created: '2024-12-03'
description: The National Science Foundation (NSF) is an independent federal agency that supports fundamental research and education in all the non-medical fields of science and engineering. NSF provides grants and funding to researchers and institutions to drive innovation, discovery, and progress.
finops:
- name: National Science Foundation Finops
  service_category: API
  slug: national-science-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-science-foundation.png
layout: provider
modified: '2026-05-19'
name: National Science Foundation
nav: Providers
network: true
overview: 'National Science Foundation publishes 2 APIs on the [APIs.io](https://apis.io/) network: Awards API and Awards.{format} API. Tagged areas include Federal Government, Research, and Science.


  National Science Foundation''s developer surface includes developer portal, engineering blog, and 5 more developer resources.'
plans:
- name: National Science Foundation Plans Pricing
  plan_count: 3
  slug: national-science-foundation-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: National Science Foundation Rate Limits
  slug: national-science-foundation-rate-limits
score:
  band: thin
  composite: 32.0
  delta: -1.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 44.9
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-science-foundation/refs/heads/main/screenshots/national-science-foundation-2026-06-20T190040.png
security:
- kind: domain-security
  name: National Science Foundation Domain Security
  slug: national-science-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-science-foundation
tags:
- Federal Government
- Research
- Science
website: https://www.nsf.gov/
---
