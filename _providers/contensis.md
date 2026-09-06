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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Contensis Agentic Access
  operation_count: 7
  slug: contensis-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: 'The Contensis Delivery API focuses on delivering content created in content types and entries to websites and applications. It is a read-only HTTP API designed for high-performance content retrieval, '
  name: Contensis Delivery API
  slug: delivery-api
- description: 'The Contensis Management API allows developers to import and manage content within content types and entries. It provides full CRUD access to content models, entries, projects, and related resources, '
  name: Contensis Management API
  slug: management-api
- description: The Contensis Image API provides real-time image manipulation and optimization features as part of the Delivery API. It supports on-the-fly transformations such as resizing, cropping, format conversio
  name: Contensis Image API
  slug: image-api
- baseURL_template: https://{instance}.contensis.com
  baseurl_source: spec_template
  description: The Content Types API from Contensis — 2 operation(s) for content types.
  name: Contensis Content Types API
  slug: contensis-content-types-api
- baseURL_template: https://{instance}.contensis.com
  baseurl_source: spec_template
  description: The Entries API from Contensis — 3 operation(s) for entries.
  name: Contensis Entries API
  slug: contensis-entries-api
- baseURL_template: https://{instance}.contensis.com
  baseurl_source: spec_template
  description: The Projects API from Contensis — 1 operation(s) for projects.
  name: Contensis Projects API
  slug: contensis-projects-api
- baseURL_template: https://{instance}.contensis.com
  baseurl_source: spec_template
  description: The Taxonomy API from Contensis — 1 operation(s) for taxonomy.
  name: Contensis Taxonomy API
  slug: contensis-taxonomy-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Contensis Delivery API (HTTP) Content Types API
  slug: open-contensis-content-types-api
- collection_type: open
  name: Contensis Delivery API (HTTP) Content Types Entries API
  slug: open-contensis-entries-api
- collection_type: open
  name: Contensis Delivery API (HTTP) Content Types Projects API
  slug: open-contensis-projects-api
- collection_type: open
  name: Contensis Delivery API (HTTP) Content Types Taxonomy API
  slug: open-contensis-taxonomy-api
- collection_type: open
  name: Contensis Delivery API (HTTP)
  slug: open-contensis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contensis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/contensis-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/contensis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contensis-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contensis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/contensis
- group: company
  title: ''
  type: Website
  url: https://www.contensis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.contensis.com/help-and-docs/apis
- group: company
  title: ''
  type: Blog
  url: https://www.contensis.com/community/blog
- group: operate
  title: ''
  type: Community
  url: https://www.contensis.com/community
- group: operate
  title: ''
  type: Support
  url: https://www.contensis.com/help-and-docs
created: '2024-11-13'
description: Contensis is an enterprise-level Content Management System (CMS) developed by Zengenti, designed to help organizations create, manage, and deliver digital content across multiple platforms and devices through HTTP, JavaScript, and .Net APIs.
finops:
- name: Contensis Finops
  service_category: API
  slug: contensis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contensis.png
layout: provider
modified: '2026-04-28'
name: Contensis
nav: Providers
network: true
overview: 'Contensis publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Content Types API, Entries API, Projects API, and 1 more. Tagged areas include CMS, Content, and Headless CMS.


  Contensis'' developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
plans:
- name: Contensis Plans Pricing
  plan_count: 3
  slug: contensis-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Contensis Rate Limits
  slug: contensis-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.4
    commercial_clarity: 21.4
    contract_governance: 0.0
    contract_quality: 43.5
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contensis/refs/heads/main/screenshots/contensis-2026-06-20T174925.png
security:
- kind: domain-security
  name: Contensis Domain Security
  slug: contensis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contensis Vulnerability Disclosure
  slug: contensis-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Contensis Trust Center
  slug: contensis-trust-center
  summary_line: ISO 27001
slug: contensis
tags:
- CMS
- Content
- Headless CMS
website: https://www.contensis.com/
---
