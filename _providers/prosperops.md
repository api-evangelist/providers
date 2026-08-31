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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: ProsperOps provides autonomous cloud cost optimization through AI-driven management of AWS Reserved Instances and Savings Plans, maximizing discount coverage while minimizing commitment risk.
  name: ProsperOps
  slug: prosperops
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/prosperops-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prosperops-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prosperops
- group: company
  title: ''
  type: Website
  url: https://www.prosperops.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.prosperops.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.prosperops.com/blog/
- group: agent
  title: ''
  type: LlmsText
  url: https://prosperops.com/llms.txt
created: '2026-03-16'
description: ProsperOps is an autonomous cloud cost optimization platform that uses AI-driven algorithms to manage AWS Reserved Instances and Savings Plans, maximizing discount coverage while minimizing commitment risk.
finops:
- name: Prosperops Finops
  service_category: API
  slug: prosperops-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prosperops.png
layout: provider
modified: '2026-04-28'
name: ProsperOps
nav: Providers
network: true
overview: 'ProsperOps publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Cost Optimization and FinOps.


  ProsperOps'' developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Prosperops Plans Pricing
  plan_count: 3
  slug: prosperops-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Prosperops Rate Limits
  slug: prosperops-rate-limits
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prosperops/refs/heads/main/screenshots/prosperops-2026-06-20T192212.png
security:
- kind: domain-security
  name: Prosperops Domain Security
  slug: prosperops-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Prosperops Vulnerability Disclosure
  slug: prosperops-vulnerability-disclosure
  summary_line: disclosure policy published
slug: prosperops
tags:
- Cloud Cost Optimization
- FinOps
website: https://www.prosperops.com/
---
