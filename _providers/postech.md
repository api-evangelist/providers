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
api_count: 1
apis:
- description: Live OAI-PMH 2.0 metadata-harvesting endpoint for the POSTECH Library OASIS institutional repository (DSpace). Verified to respond to Identify, ListMetadataFormats, and ListSets. Repository name repor
  name: OASIS Repository OAI-PMH
  slug: oasis-oai-pmh
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.postech.ac.kr/eng/
- group: company
  title: ''
  type: LinkedIn
  url: https://kr.linkedin.com/school/pohang-university-of-science-and-technology/
- group: start
  title: ''
  type: x-Portal
  url: https://podium.postech.ac.kr
- group: other
  title: ''
  type: x-Repository
  url: https://oasis.postech.ac.kr/
- group: commercial
  title: ''
  type: Plans
  url: plans/postech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/postech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/postech-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Pohang University of Science and Technology (POSTECH) is a private research university in Pohang, South Korea, founded in 1986 by the steelmaker POSCO and ranked #87 in the QS World University Rankings 2025. POSTECH operates a public English-language website and a range of authenticated institutional systems (PODIUM portal, PLMS learning management, admissions, and certificate services). Its primary confirmed public, machine-readable API surface is the POSTECH Library OASIS institutional repository, a DSpace platform that exposes a live OAI-PMH 2.0 metadata-harvesting endpoint. No general-purpose developer portal or open-data API program was found; most other systems are login-gated.'
finops:
- name: Postech Finops
  service_category: Education
  slug: postech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postech.png
jsonld:
- class_count: 15
  name: Postech Context
  property_count: 3
  slug: postech-context
layout: provider
modified: '2026-06-03'
name: Pohang University of Science and Technology
nav: Providers
network: true
overview: 'Pohang University of Science and Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Institutional Repository.


  The Pohang University of Science and Technology catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Postech Plans Pricing
  plan_count: 2
  slug: postech-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 1
  name: Postech Rate Limits
  slug: postech-rate-limits
score:
  band: emerging
  composite: 18.6
  delta: -2.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postech/refs/heads/main/screenshots/postech-2026-06-20T192013.png
security:
- kind: domain-security
  name: Postech Domain Security
  slug: postech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: postech
tags:
- Education
- Higher Education
- University
- Research
- Institutional Repository
- OAI-PMH
- DSpace
- Library
- South Korea
- Korea
website: https://www.postech.ac.kr/eng/
---
