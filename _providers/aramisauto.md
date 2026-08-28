---
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Aramis Group publishes the machine-readable contracts behind the Aramisauto vehicle catalog as ten JSON Schema 2020-12 documents at https://schemas.aramis.group/ — a search request envelope (criteria/
  name: Aramisauto Vehicle Catalog Contracts
  slug: aramisauto-vehicle-catalog-contracts
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aramisauto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aramisauto.com/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aramisauto-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aramisauto-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aramisauto-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aramisauto-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/aramisauto-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aramisauto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aramisauto-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aramisauto-llms.txt
- group: start
  title: ''
  type: SchemaRegistry
  url: https://schemas.aramis.group/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ARAMISAUTO
- group: operate
  title: ''
  type: Support
  url: https://www.aramisauto.com/aide/faq
- group: operate
  title: ''
  type: Contact
  url: https://www.aramisauto.com/contact/vos-coordonnees/
- group: company
  title: ''
  type: Blog
  url: https://www.aramisauto.com/guide-pratique/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aramisauto.com/mentions-legales/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aramisauto.com/mentions-legales/politique-de-protection-des-donnees/
- group: commercial
  title: ''
  type: LegalNotices
  url: https://www.aramisauto.com/mentions-legales/mentions-legales/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.aramisauto.com/mentions-legales/gerer-mes-cookies/
- group: company
  title: ''
  type: About
  url: https://www.aramisauto.com/qui-sommes-nous
- group: other
  title: ''
  type: ParentCompany
  url: https://www.aramis-group.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aramisauto
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@aramisauto
created: '2026-08-17'
description: 'Aramisauto is the French retail brand of Aramis Group (Euronext Paris: ARAMI, majority-owned by Stellantis), founded in 2001 by Nicolas Chartier and Guillaume Paoli. It sells used, 0km and new cars online as a mandataire, reconditions vehicles in its own refurbishing centres, runs a trade-in service ("reprise") that pays within 24 hours, and arranges financing (crédit, LOA, LLD) through Cetelem, Socram, PSA Banque, Lizauto and Opteven. Aramisauto operates no public developer programme: there is no portal, no OpenAPI and no SDK. What it does publish is machine-readable and first-party — ten JSON Schema 2020-12 contracts at schemas.aramis.group covering the vehicle catalog (search request/response, the multi-language ingest model, the single-language read model served from "the preheated cache for the APIs", and the search-index projection) plus the four-stage collect/map/filter/enrich configuration contracts third-party marketplace sellers are onboarded with — and an llms.txt
  at the site root. Its API vhost, api.aramisauto.com, answers every anonymous request with an HTTP 403 demanding a WSSE (WS-Security UsernameToken) credential.'
examples:
- key_count: 7
  name: Aramisauto Catalog Search Request
  slug: aramisauto-catalog-search-request
- key_count: 6
  name: Aramisauto Catalog Search Response
  slug: aramisauto-catalog-search-response
- key_count: 79
  name: Aramisauto Catalog Vehicle Multi Language Input
  slug: aramisauto-catalog-vehicle-multi-language-input
- key_count: 83
  name: Aramisauto Catalog Vehicle Single Language Output
  slug: aramisauto-catalog-vehicle-single-language-output
- key_count: 59
  name: Aramisauto Catalog Vehicle Single Language Searchable Data
  slug: aramisauto-catalog-vehicle-single-language-searchable-data
image: https://website-app-static-content-ecommerce.aramisauto.com/common/icon/apple-touch-icon.png
json_schemas:
- name: Aramisauto Catalog Base.Schema
  property_count: 0
  slug: aramisauto-catalog-base.schema
- name: Aramisauto Catalog Search Request.Schema
  property_count: 7
  slug: aramisauto-catalog-search-request.schema
- name: Aramisauto Catalog Search Response.Schema
  property_count: 6
  slug: aramisauto-catalog-search-response.schema
- name: Aramisauto Catalog Vehicle Multi Language Input.Schema
  property_count: 80
  slug: aramisauto-catalog-vehicle-multi-language-input.schema
- name: Aramisauto Catalog Vehicle Single Language Output.Schema
  property_count: 83
  slug: aramisauto-catalog-vehicle-single-language-output.schema
- name: Aramisauto Catalog Vehicle Single Language Searchable Data.Schema
  property_count: 61
  slug: aramisauto-catalog-vehicle-single-language-searchable-data.schema
- name: Aramisauto Marketplace Collect.Schema
  property_count: 1
  slug: aramisauto-marketplace-collect.schema
- name: Aramisauto Marketplace Enrich.Schema
  property_count: 1
  slug: aramisauto-marketplace-enrich.schema
- name: Aramisauto Marketplace Filter.Schema
  property_count: 1
  slug: aramisauto-marketplace-filter.schema
- name: Aramisauto Marketplace Map.Schema
  property_count: 1
  slug: aramisauto-marketplace-map.schema
layout: provider
modified: '2026-08-17'
name: AramisAuto
nav: Providers
network: true
overview: 'AramisAuto publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Automotive, E-Commerce, and Used Cars.


  AramisAuto''s developer surface includes code examples, support, engineering blog, YouTube channel, and 21 more developer resources.'
plans:
- name: Aramisauto Plans Pricing
  plan_count: 0
  slug: aramisauto-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Aramisauto Rate Limits
  slug: aramisauto-rate-limits
score:
  band: emerging
  composite: 17.5
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 8.3
    contract_quality: 14.7
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 8.3
    operational_transparency: 2.6
  previous_composite: 17.5
  provenance:
    conformance: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Aramisauto Authentication
  slug: aramisauto-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aramisauto Domain Security
  slug: aramisauto-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aramisauto
tags:
- Company
- Consumer
- Automotive
- E-Commerce
- Used Cars
- Vehicle Data
- Marketplace
- Retail
- Auto Finance
- France
- JSON-Schema
website: https://www.aramisauto.com/
---
