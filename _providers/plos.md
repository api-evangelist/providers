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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'These examples use the search API to search the PLOS corpus of scientific articles. These examples are not intended to be a full explanation on the use of Solr. A full Solr query language explanation '
  name: PLOS Search API
  slug: plos
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plos-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PLOS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/public-library-of-science
- group: company
  title: ''
  type: Website
  url: https://plos.org
- group: docs
  title: ''
  type: Documentation
  url: https://api.plos.org/solr/examples/
- group: company
  title: ''
  type: Blog
  url: https://theplosblog.plos.org/feed/
created: '2025-02-06'
description: These examples use the search API to search the PLOS corpus of scientific articles. These examples are not intended to be a full explanation on the use of Solr. A full Solr query language explanation can be found here and a tutorial here. The construction of PLOS search queries deviates from the standard Solr query URL by using search instead of select when making request to the end point. The primary endpoint is http://api.plos.org/search and supports parameters such as q, fl, wt, start, and rows for querying the PLOS Solr index.
finops:
- name: Plos Finops
  service_category: API
  slug: plos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plos.png
layout: provider
modified: '2026-04-28'
name: PLOS
nav: Providers
network: true
overview: 'PLOS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Scientific Articles, Research, Search, Solr, and Open Access.


  PLOS''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Plos Plans Pricing
  plan_count: 3
  slug: plos-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Plos Rate Limits
  slug: plos-rate-limits
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plos/refs/heads/main/screenshots/plos-2026-06-20T191812.png
security:
- kind: domain-security
  name: Plos Domain Security
  slug: plos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plos
tags:
- Scientific Articles
- Research
- Search
- Solr
- Open Access
website: https://plos.org
---
