---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gleif Agentic Access
  operation_count: 16
  slug: gleif-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- baseURL: https://api.gleif.org/api/v1
  baseurl_source: declared
  description: Corporate ownership and relationship hierarchy data
  name: GLEIF Corporate Relationships API
  slug: gleif-corporate-relationships-api
- baseURL: https://api.gleif.org/api/v1
  baseurl_source: declared
  description: Operations on accredited LEI Issuers (Local Operating Units)
  name: GLEIF LEI Issuers API
  slug: gleif-lei-issuers-api
- baseURL: https://api.gleif.org/api/v1
  baseurl_source: declared
  description: Operations on Legal Entity Identifier records
  name: GLEIF LEI Records API
  slug: gleif-lei-records-api
- baseURL: https://api.gleif.org/api/v1
  baseurl_source: declared
  description: Reference data including entity legal forms and registration authorities
  name: GLEIF Reference Data API
  slug: gleif-reference-data-api
- baseURL: https://api.gleif.org/api/v1
  baseurl_source: declared
  description: Search and autocomplete operations
  name: GLEIF Search API
  slug: gleif-search-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GLEIF LEI Corporate Relationships API
  slug: open-gleif-corporate-relationships-api
- collection_type: open
  name: GLEIF LEI Corporate Relationships LEI Issuers API
  slug: open-gleif-lei-issuers-api
- collection_type: open
  name: GLEIF LEI Corporate Relationships LEI Records API
  slug: open-gleif-lei-records-api
- collection_type: open
  name: GLEIF LEI Corporate Relationships Reference Data API
  slug: open-gleif-reference-data-api
- collection_type: open
  name: GLEIF LEI Corporate Relationships Search API
  slug: open-gleif-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gleif-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gleif-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gleif.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.gleif.org/en/lei-data/gleif-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/GLEIF-IT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/global-legal-entity-identifier-foundation-gleif-
- group: company
  title: ''
  type: Blog
  url: https://www.gleif.org/en/newsroom/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gleif.org/en/lei-data/access-and-use-lei-data
- group: operate
  title: ''
  type: StatusPage
  url: https://www.gleif.org/en/about/gleif-services/daily-service-availability
- group: other
  title: ''
  type: X
  url: https://twitter.com/gleif
- group: commercial
  title: ''
  type: Plans
  url: plans/gleif-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gleif-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gleif-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/gleif-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/gleif-context.jsonld
created: '2026-06-12'
description: The Global Legal Entity Identifier Foundation (GLEIF) provides a free, open REST API that gives developers access to the full LEI Data search engine functionality. The API supports filters, full-text and single-field searches of legal entity and ownership data, and fuzzy matching of relevant data fields such as entity names and addresses. In addition to LEI reference data, the API exposes reference data for LEI issuers, code lists, and mapped identifiers including BIC and ISIN codes. The API requires no authentication or registration, making LEI data freely accessible to any interested party for searching, validating, and retrieving legal entity identifiers and associated organizational reference data.
examples:
- key_count: 2
  name: Gleif Lei Record Example
  slug: gleif-lei-record-example
- key_count: 3
  name: Gleif Lei Records List Example
  slug: gleif-lei-records-list-example
finops:
- name: Gleif Finops
  service_category: ''
  slug: gleif-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gleif.png
json_schemas:
- name: GLEIF LEI Record
  property_count: 5
  slug: gleif-lei-record
jsonld:
- class_count: 0
  name: Gleif Context
  property_count: 50
  slug: gleif-context
layout: provider
modified: '2026-06-12'
name: GLEIF
nav: Providers
network: true
overview: 'GLEIF publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Corporate Relationships API, LEI Issuers API, LEI Records API, and 2 more. Tagged areas include Legal Entity Identifier, LEI, vLEI, Financial Data, and Corporate Identity.


  The GLEIF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GLEIF''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Gleif Plans Pricing
  plan_count: 1
  slug: gleif-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Gleif Rate Limits
  slug: gleif-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: GLEIF API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: gleif-jsonschema-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/gleif/refs/heads/main/screenshots/gleif-2026-06-20T181909.png
security:
- kind: domain-security
  name: Gleif Domain Security
  slug: gleif-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: gleif
tags:
- Legal Entity Identifier
- LEI
- vLEI
- Financial Data
- Corporate Identity
- Entity Verification
- Reference Data
- Open Data
website: https://www.gleif.org
---
