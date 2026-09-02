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
- description: Scrapy is an open-source Python web crawling framework for extracting structured data from websites using spiders and built-in data pipelines.
  name: Scrapy
  slug: scrapy
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scrapy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scrapy.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scrapy.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scrapy
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.scrapy.org/llms.txt
created: '2026-03-29'
description: Scrapy is an open-source Python web crawling framework for extracting structured data from websites using spiders and built-in data pipelines.
finops:
- name: Scrapy Finops
  service_category: API
  slug: scrapy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scrapy.png
layout: provider
modified: '2026-03-29'
name: Scrapy
nav: Providers
network: true
overview: 'Scrapy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Crawling, Data Extraction, and Scraping.


  Scrapy''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Scrapy Plans Pricing
  plan_count: 3
  slug: scrapy-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Scrapy Rate Limits
  slug: scrapy-rate-limits
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scrapy/refs/heads/main/screenshots/scrapy-2026-06-20T193600.png
security:
- kind: domain-security
  name: Scrapy Domain Security
  slug: scrapy-domain-security
  summary_line: TLSv1.3 · HSTS
slug: scrapy
tags:
- Crawling
- Data Extraction
- Scraping
website: https://scrapy.org/
---
