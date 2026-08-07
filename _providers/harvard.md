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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: REST/JSON API to the Harvard Art Museums' collections data across 21 resources (Object, Person, Exhibition, Publication, Gallery, Classification, Culture, Medium, Period, Place, Image, and more), with
  name: Harvard Art Museums API
  slug: art-museums
- description: 'Open metadata hub aggregating Harvard bibliographic metadata (12.7M+ bib records, image records, ArchivesSpace finding aids). The public Item API returns normalized MODS or Dublin Core; a Collections '
  name: Harvard Library LibraryCloud API (Open Metadata)
  slug: librarycloud
- description: OAI-PMH 2.0 metadata harvesting endpoint for DASH (Digital Access to Scholarship at Harvard), the open-access institutional repository of 58,000+ scholarly works. Open, no key required.
  name: Harvard DASH OAI-PMH
  slug: dash
- description: HUIT's central catalog of administrative APIs — Courses, Person Data Service, Library Catalog (Ex Libris Primo), Dining, HR Departments, Zoom, Emailer, and Generative AI APIs. OpenAPI specs are viewab
  name: Harvard API Portal (HUIT)
  slug: api-portal
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/harvard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harvard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.harvard.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.harvard.edu/developers
- group: build
  title: ''
  type: GitHub
  url: https://github.com/harvard
- group: operate
  title: ''
  type: Status
  url: https://status.huit.harvard.edu/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Harvard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/harvard-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/harvard-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/harvard-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/harvard-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Harvard University (Cambridge, MA; founded 1636; QS World 2025 #4) maintains a substantial public developer footprint spread across several units. Its most prominent fully public, key-based APIs are the Harvard Art Museums API and the Harvard Library LibraryCloud / Open Metadata API, both serving open collections data. Harvard University Information Technology (HUIT) operates a central API Portal (HarvardKey-gated) cataloging administrative APIs (Courses, Person, Dining, Zoom, Library Catalog), and the DASH institutional repository exposes an open OAI-PMH metadata feed.'
finops:
- name: Harvard Finops
  service_category: Education
  slug: harvard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harvard.png
jsonld:
- class_count: 33
  name: Harvard Context
  property_count: 3
  slug: harvard-context
layout: provider
modified: '2026-06-03'
name: Harvard University
nav: Providers
network: true
overview: 'Harvard University publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and Libraries.


  The Harvard University catalog on APIs.io includes 1 JSON-LD context.


  Harvard University''s developer surface includes GitHub presence, status page, and 10 more developer resources.'
plans:
- name: Harvard Plans Pricing
  plan_count: 2
  slug: harvard-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 1
  name: Harvard Rate Limits
  slug: harvard-rate-limits
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harvard/refs/heads/main/screenshots/harvard-2026-06-20T182525.png
security:
- kind: domain-security
  name: Harvard Domain Security
  slug: harvard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Harvard Vulnerability Disclosure
  slug: harvard-vulnerability-disclosure
  summary_line: disclosure policy published
slug: harvard
tags:
- Education
- Higher Education
- University
- Research
- Libraries
- Museums
- Open Metadata
- OAI-PMH
website: https://www.harvard.edu/
---
