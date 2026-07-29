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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata-harvesting interface for the USM Repository (Repository@USM), an EPrints 3.3.16 institutional repository of USM research and publications. The Identify response confirms repositor
  name: USM Repository OAI-PMH
  slug: eprints-oai
- description: USM's institutional API developer portal operated by PPKT (Pusat Pengetahuan, Komunikasi dan Teknologi). The landing page describes REST API benefits for integration and innovation, but the API catalo
  name: API@USM Developer Portal (Gated)
  slug: api-portal
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usm.my/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.usm.my/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universiti-sains-malaysia-official/
- group: commercial
  title: ''
  type: Plans
  url: plans/usm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/usm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Sains Malaysia (USM) is a public research university founded in 1969 and headquartered in Penang, Malaysia, holding APEX (Accelerated Programme for Excellence) status and ranked #146 in the QS World University Rankings 2025. Its public developer/API footprint is modest: USM operates an API developer portal at api.usm.my run by the Pusat Pengetahuan, Komunikasi dan Teknologi (PPKT), but the catalog and documentation sit behind authentication. The most openly accessible machine-readable interface is the EPrints-based institutional repository at eprints.usm.my, which exposes a live OAI-PMH 2.0 metadata-harvesting endpoint.'
finops:
- name: Usm Finops
  service_category: Education
  slug: usm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usm.png
jsonld:
- class_count: 12
  name: Usm Context
  property_count: 3
  slug: usm-context
layout: provider
modified: '2026-06-03'
name: Universiti Sains Malaysia
nav: Providers
network: true
overview: 'Universiti Sains Malaysia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Universiti Sains Malaysia catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Usm Plans Pricing
  plan_count: 2
  slug: usm-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Usm Rate Limits
  slug: usm-rate-limits
score:
  band: emerging
  composite: 19.4
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usm/refs/heads/main/screenshots/usm-2026-06-20T200723.png
security:
- kind: domain-security
  name: Usm Domain Security
  slug: usm-domain-security
  summary_line: TLSv1.3
slug: usm
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- OAI-PMH
- Malaysia
website: https://www.usm.my/en/
---
