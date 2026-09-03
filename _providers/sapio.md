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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Sapio REST API provides programmatic access to the Sapio Informatics Platform, enabling developers to query and create records, manage laboratory workflows, handle experimental data, configure dat
  name: Sapio REST API
  slug: sapio-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sapio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sapiosciences.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/sapiosciences/sapio-py-tutorials
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sapiosciences
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/sapio-sciences-llc
- group: company
  title: ''
  type: Blog
  url: https://www.sapiosciences.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sapiosciences.com/sapio-pricing/
- group: other
  title: ''
  type: X
  url: https://x.com/sapiosciences
- group: commercial
  title: ''
  type: Plans
  url: plans/sapio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sapio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sapio-finops.yml
created: '2026-06-13'
description: Sapio Sciences provides an AI-native lab informatics platform that unifies LIMS, ELN, and Scientific Data Cloud capabilities for life sciences research. The platform exposes a RESTful API enabling programmatic access to laboratory workflows, experimental data, LIMS processes, sample management, and instrument integrations. The official Python client library sapiopylib wraps all REST API functions, supporting data record manipulation, picklist services, notebook experiments, webhook servers, and batch request processing for high-performance lab automation.
finops:
- name: Sapio Finops
  service_category: ''
  slug: sapio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sapio.png
layout: provider
modified: '2026-06-13'
name: Sapio Sciences
nav: Providers
network: true
overview: 'Sapio Sciences publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include LIMS, ELN, Laboratory Informatics, Life Sciences, and Scientific Data.


  Sapio Sciences'' developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Sapio Plans Pricing
  plan_count: 3
  slug: sapio-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Sapio Rate Limits
  slug: sapio-rate-limits
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sapio/refs/heads/main/screenshots/sapio-2026-06-20T193445.png
security:
- kind: domain-security
  name: Sapio Domain Security
  slug: sapio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sapio
tags:
- LIMS
- ELN
- Laboratory Informatics
- Life Sciences
- Scientific Data
- Lab Automation
- Instrument Integration
- Biotech
- Pharma
website: https://www.sapiosciences.com/
---
