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
api_count: 3
apis:
- description: Public REST API for CaltechDATA, the Caltech institutional research data repository built on InvenioRDM. Supports querying and retrieving records, metadata (DataCite 4 JSON), files, and DOIs. Verified
  name: CaltechDATA REST API
  slug: caltechdata-rest
- description: OAI-PMH metadata harvesting endpoint for CaltechDATA, enabling programmatic harvesting of repository metadata records. Verified live via the Identify verb.
  name: CaltechDATA OAI-PMH
  slug: caltechdata-oai
- description: Caltech/IPAC NASA Infrared Science Archive (IRSA) exposes IVOA-standard Virtual Observatory APIs, including Table Access Protocol (TAP), Simple Cone Search (SCS), and Simple Image Access (SIA v2), for
  name: IRSA Virtual Observatory APIs (IPAC)
  slug: irsa-vo
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caltech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caltech.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/caltechlibrary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/california-institute-of-technology/
- group: commercial
  title: ''
  type: Plans
  url: plans/caltech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/caltech-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/caltech-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The California Institute of Technology (Caltech) is a private research university in Pasadena, California, ranked #10 in the QS World University Rankings 2025. Caltech''s public, machine-readable footprint is concentrated in its research-data and astronomy infrastructure rather than a single central developer portal. CaltechDATA, the institutional research data repository, runs on InvenioRDM and exposes a public REST API and an OAI-PMH interface, with an accompanying open-source Python client. Caltech-operated IPAC runs the NASA/IPAC Infrared Science Archive (IRSA), which publishes Virtual Observatory (IVOA) standard APIs including TAP, Simple Cone Search, and Simple Image Access. There is no single unified institution-wide API developer portal; the official GitHub "caltech" org is an unofficial community group, while caltechlibrary and Caltech-IPAC host the bulk of the open-source code.'
finops:
- name: Caltech Finops
  service_category: Education
  slug: caltech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caltech.png
jsonld:
- class_count: 15
  name: Caltech Context
  property_count: 5
  slug: caltech-context
layout: provider
modified: '2026-06-03'
name: California Institute of Technology
nav: Providers
network: true
overview: 'California Institute of Technology publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Astronomy.


  The California Institute of Technology catalog on APIs.io includes 1 JSON-LD context.


  California Institute of Technology''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: Caltech Plans Pricing
  plan_count: 2
  slug: caltech-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 1
  name: Caltech Rate Limits
  slug: caltech-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: -3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caltech/refs/heads/main/screenshots/caltech-2026-06-20T173852.png
security:
- kind: domain-security
  name: Caltech Domain Security
  slug: caltech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: caltech
tags:
- Education
- Higher Education
- University
- Research Data
- Astronomy
- Open Data
- United States
website: https://www.caltech.edu/
---
