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
- description: The UCSI University Library runs a Koha open-source integrated library system (OPAC) at koha.ucsiuniversity.edu.my. Koha software can expose OAI-PMH and ILS-DI / REST web services, but during this rev
  name: UCSI University Library Catalog (Koha)
  slug: library-catalog
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucsi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucsiuniversity.edu.my/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ucsi-education/
- group: commercial
  title: ''
  type: Plans
  url: plans/ucsi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucsi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucsi-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'UCSI University is a private, multi-campus university in Malaysia (Kuala Lumpur, Terengganu and Sarawak) ranked #265 in the QS World University Rankings 2025. It operates student-facing digital services including a student portal and mobile apps and runs a Koha-based library catalog, but UCSI does not publish a public developer portal or documented, openly accessible APIs. The systems that exist (portal, mobile-app backends, identity) are gated behind authentication and a web application firewall, so no public API endpoints could be confirmed during this review.'
finops:
- name: Ucsi Finops
  service_category: Education
  slug: ucsi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucsi.png
jsonld:
- class_count: 10
  name: Ucsi Context
  property_count: 3
  slug: ucsi-context
layout: provider
modified: '2026-06-03'
name: UCSI University
nav: Providers
network: true
overview: 'UCSI University publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Malaysia, and Library.


  The UCSI University catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Ucsi Plans Pricing
  plan_count: 2
  slug: ucsi-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 1
  name: Ucsi Rate Limits
  slug: ucsi-rate-limits
score:
  band: emerging
  composite: 17.7
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 20.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucsi/refs/heads/main/screenshots/ucsi-2026-06-20T195950.png
security:
- kind: domain-security
  name: Ucsi Domain Security
  slug: ucsi-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: ucsi
tags:
- Education
- Higher Education
- University
- Malaysia
- Library
- Koha
website: https://www.ucsiuniversity.edu.my/
---
