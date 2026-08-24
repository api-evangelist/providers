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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: DSpace-based institutional repository operated by Perpustakaan Tun Seri Lanang (UKM Library) providing access to theses, past-year exam papers, selected government publications and law documents. It e
  name: UKM Learning and Research Repository (OAI-PMH)
  slug: learning-research-repository-oai
- description: 'EPrints-based repository of journal articles published by UKM faculties, institutes and UKM Press. Registered in ROAR and OpenDOAR as supporting OAI-PMH 2.0 harvesting via its EPrints oai2 interface. '
  name: UKM Journal Article Repository (OAI-PMH)
  slug: journal-article-repository-oai
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ukm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ukm.my/portalukm/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universitikebangsaanmalaysia/
- group: commercial
  title: ''
  type: Plans
  url: plans/ukm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ukm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ukm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Kebangsaan Malaysia (UKM), The National University of Malaysia, is a public research university in Bangi, Selangor, ranked #138 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is concentrated in scholarly-communication infrastructure operated by the Perpustakaan Tun Seri Lanang (UKM Library): a DSpace-based UKM Learning and Research Repository and an EPrints-based UKM Journal Article Repository, both of which expose standards-based OAI-PMH harvesting interfaces. UKM does not publish a general-purpose developer portal; student and staff online services are gated behind institutional single sign-on and are not openly documented.'
finops:
- name: Ukm Finops
  service_category: Education
  slug: ukm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ukm.png
jsonld:
- class_count: 20
  name: Ukm Context
  property_count: 0
  slug: ukm-context
layout: provider
modified: '2026-06-03'
name: Universiti Kebangsaan Malaysia
nav: Providers
network: true
overview: 'Universiti Kebangsaan Malaysia publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The Universiti Kebangsaan Malaysia catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Ukm Plans Pricing
  plan_count: 2
  slug: ukm-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Ukm Rate Limits
  slug: ukm-rate-limits
score:
  band: emerging
  composite: 17.1
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ukm/refs/heads/main/screenshots/ukm-2026-06-20T200011.png
security:
- kind: domain-security
  name: Ukm Domain Security
  slug: ukm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ukm
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Institutional Repository
- OAI-PMH
- Library
- Malaysia
website: https://www.ukm.my/portalukm/
---
