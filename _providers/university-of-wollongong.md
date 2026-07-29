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
- description: OAI-PMH metadata harvesting interface for University of Wollongong Research Online, the institution's open access repository running on bepress Digital Commons. Exposes journal articles, conference pa
  name: Research Online OAI-PMH
  slug: research-online-oai
- description: The UOW Library runs on the Ex Libris Alma library services platform with the Primo discovery layer (adopted 2020). Primo and Alma expose REST APIs for search, bibliographic, and resource-management w
  name: UOW Library Discovery (Ex Libris Primo/Alma)
  slug: library-primo-alma
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-wollongong-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uow.edu.au/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uowits
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/school/university-of-wollongong/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-wollongong-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-wollongong-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-wollongong-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.uow.edu.au/media/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.uow.edu.au/media/rss/index.php
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-wollongong-context.jsonld
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Wollongong (UOW) is a public research university based in Wollongong, New South Wales, Australia, ranked #167 in the QS World University Rankings 2025. UOW does not operate a public, self-service developer portal. Its confirmed machine-readable footprint is built on third-party platforms: the Research Online institutional repository runs on bepress Digital Commons and exposes an OAI-PMH metadata interface, while the UOW Library runs on the Ex Libris Alma/Primo platform whose REST APIs are documented through the Ex Libris Developer Network. UOW IT Services also maintains a small public GitHub organization. Most institutional systems (student administration, identity) are gated behind authentication and not publicly documented.'
finops:
- name: University Of Wollongong Finops
  service_category: Education
  slug: university-of-wollongong-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-wollongong.png
jsonld:
- class_count: 22
  name: University Of Wollongong Context
  property_count: 3
  slug: university-of-wollongong-context
layout: provider
modified: '2026-06-03'
name: University of Wollongong
nav: Providers
network: true
overview: 'University of Wollongong publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Australia, and Research Repository.


  The University of Wollongong catalog on APIs.io includes 1 JSON-LD context.


  University of Wollongong''s developer surface includes GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: University Of Wollongong Plans Pricing
  plan_count: 2
  slug: university-of-wollongong-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 1
  name: University Of Wollongong Rate Limits
  slug: university-of-wollongong-rate-limits
score:
  band: emerging
  composite: 18.8
  delta: -2.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 2.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 21.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-wollongong/refs/heads/main/screenshots/university-of-wollongong-2026-06-20T200355.png
security:
- kind: domain-security
  name: University Of Wollongong Domain Security
  slug: university-of-wollongong-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-wollongong
tags:
- Education
- Higher Education
- University
- Australia
- Research Repository
- Library
- Open Access
website: https://www.uow.edu.au/
---
