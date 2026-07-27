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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for CentAUR, the Central Archive University of Reading institutional repository (EPrints). Supports standard OAI-PMH verbs (Identify, ListRecords, ListMetadat
  name: CentAUR OAI-PMH Metadata API
  slug: centaur-oai-pmh
- description: OAI-PMH metadata harvesting interface for the University of Reading Research Data Archive (EPrints), a multidisciplinary service for the registration, preservation, and publication of research dataset
  name: Research Data Archive OAI-PMH Metadata API
  slug: research-data-archive-oai-pmh
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-reading-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-reading-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reading.ac.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/school/university-of-reading/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-reading-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-reading-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-reading-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Reading is a public research university in Reading, England, ranked #172 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on open research and scholarly metadata rather than a formal developer portal. The university operates two EPrints-based repositories — CentAUR (the Central Archive University of Reading) and the University of Reading Research Data Archive — both of which expose live OAI-PMH metadata harvesting endpoints. No general-purpose, self-service developer portal, public REST API catalog, or official GitHub organization could be confirmed; administrative, identity, and student-information interfaces are gated behind institutional affiliation and federated authentication.'
finops:
- name: University Of Reading Finops
  service_category: Education
  slug: university-of-reading-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-reading.png
jsonld:
- class_count: 15
  name: University Of Reading Context
  property_count: 6
  slug: university-of-reading-context
layout: provider
modified: '2026-06-03'
name: University of Reading
nav: Providers
network: true
overview: 'University of Reading publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Open Access.


  The University of Reading catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: University Of Reading Plans Pricing
  plan_count: 2
  slug: university-of-reading-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: University Of Reading Rate Limits
  slug: university-of-reading-rate-limits
score:
  band: emerging
  composite: 21.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-reading/refs/heads/main/screenshots/university-of-reading-2026-06-20T200222.png
security:
- kind: domain-security
  name: University Of Reading Domain Security
  slug: university-of-reading-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Reading Vulnerability Disclosure
  slug: university-of-reading-vulnerability-disclosure
  summary_line: disclosure policy published
slug: university-of-reading
tags:
- Education
- Higher Education
- University
- Research
- Open Access
- Repository
- Metadata
- United Kingdom
website: https://www.reading.ac.uk/
---
