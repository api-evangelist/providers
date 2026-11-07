---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Salesforce Commerce Cloud Agentic Access
  operation_count: 10
  slug: salesforce-commerce-cloud-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: Modern REST API family for B2C Commerce Cloud built on a unified RAML specification, organized into Shopper, Data, and Admin APIs for headless commerce. Authentication uses OAuth 2.0 via Salesforce Ac
  name: Salesforce Commerce API (SCAPI)
  slug: scapi
- description: 'Legacy REST API for B2C Commerce Cloud, organized into Shop API, Data API, and Meta API. Authentication uses OAuth 2.0 via Salesforce Account Manager. OCAPI is deprecated for new projects in favor of '
  name: Open Commerce API (OCAPI)
  slug: ocapi
- baseURL: https://<short-code>.api.commercecloud.salesforce.com
  baseurl_source: declared
  description: The Shopper API from Salesforce Commerce Cloud — 9 operation(s) for shopper.
  name: Salesforce Commerce Cloud Shopper API
  slug: salesforce-commerce-cloud-shopper-api
artifact_total: 34
collections:
- collection_type: open
  name: Salesforce Commerce API (SCAPI) - Subset Shopper API
  slug: open-salesforce-commerce-cloud-shopper-api
- collection_type: open
  name: Salesforce Commerce API (SCAPI) - Shopper Subset
  slug: open-salesforce-commerce-cloud
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: agent
  href: https://artifacts.apis.io/salesforce-commerce-cloud/agentic-access/salesforce-commerce-cloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-commerce-cloud-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/salesforce-commerce-cloud/security/salesforce-commerce-cloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/salesforce-commerce-cloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/salesforce-commerce-cloud/security/salesforce-commerce-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/salesforce-commerce-cloud-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/salesforce-commerce-cloud/authentication/salesforce-commerce-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/salesforce-commerce-cloud-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commercecloud-demandware
- group: company
  title: ''
  type: Website
  url: https://www.salesforce.com/products/commerce-cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs/commerce
- group: docs
  title: ''
  type: API Documentation
  url: https://developer.salesforce.com/docs/commerce/commerce-api/overview
- group: other
  title: ''
  type: API Explorer
  url: https://api-explorer.commercecloud.salesforce.com
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/salesforce-developers/salesforce-developers/documentation/1qkzgik/salesforce-commerce-b2c
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/products/commerce-cloud/pricing/
- group: start
  title: ''
  type: Signup
  url: https://developer.salesforce.com/signup
- group: other
  title: ''
  type: Trailhead
  url: https://trailhead.salesforce.com/content/learn/modules/b2c-integration-approaches/b2c-explore-ocapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SalesforceCommerceCloud
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/s/
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/SalesforceCommerceCloud/b2c-developer-tooling
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs/feed
created: '2026-05-11'
description: 'Salesforce Commerce Cloud (formerly Demandware) is an enterprise commerce platform supporting B2C and B2B storefronts, order management, product content, and headless commerce experiences. Commerce Cloud exposes two REST API products: the legacy Open Commerce API (OCAPI) and the modern Salesforce Commerce API (SCAPI), a unified RAML-defined API family built for headless commerce. SCAPI uses OAuth 2.0 via Salesforce Account Manager and groups APIs into Shopper, Data, and Admin tiers.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salesforce-commerce-cloud.png
layout: provider
modified: '2026-08-21'
name: Salesforce Commerce Cloud
nav: Providers
network: true
overview: 'Salesforce Commerce Cloud publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Shopper API, and 2 more. Tagged areas include Commerce, E-Commerce, Headless Commerce, Salesforce, and B2C Commerce.


  The Salesforce Commerce Cloud catalog on APIs.io includes 1 Spectral governance ruleset.


  Salesforce Commerce Cloud''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 12 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Salesforce Commerce Cloud API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: salesforce-commerce-cloud-rules
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 45.3
    developer_ergonomics: 46.9
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/salesforce-commerce-cloud/salesforce-commerce-cloud-2026-06-20T193346.png
security:
- kind: authentication
  name: Salesforce Commerce Cloud Authentication
  slug: salesforce-commerce-cloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Salesforce Commerce Cloud Domain Security
  slug: salesforce-commerce-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Salesforce Commerce Cloud Vulnerability Disclosure
  slug: salesforce-commerce-cloud-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 60
skills:
- name: api-client-development
  slug: api-client-development
- name: b2c-am
  slug: b2c-am
- name: b2c-bm-users-roles
  slug: b2c-bm-users-roles
- name: b2c-business-manager-extensions
  slug: b2c-business-manager-extensions
- name: b2c-cap
  slug: b2c-cap
- name: b2c-cip
  slug: b2c-cip
- name: b2c-code
  slug: b2c-code
- name: b2c-config
  slug: b2c-config
- name: b2c-content
  slug: b2c-content
- name: b2c-controllers
  slug: b2c-controllers
- name: b2c-custom-api-development
  slug: b2c-custom-api-development
- name: b2c-custom-caches
  slug: b2c-custom-caches
- name: b2c-custom-job-steps
  slug: b2c-custom-job-steps
- name: b2c-custom-objects
  slug: b2c-custom-objects
- name: b2c-debug
  slug: b2c-debug
- name: b2c-docs
  slug: b2c-docs
- name: b2c-ecdn
  slug: b2c-ecdn
- name: b2c-forms
  slug: b2c-forms
- name: b2c-hooks
  slug: b2c-hooks
- name: b2c-isml
  slug: b2c-isml
- name: b2c-job
  slug: b2c-job
- name: b2c-localization
  slug: b2c-localization
- name: b2c-logging
  slug: b2c-logging
- name: b2c-logs
  slug: b2c-logs
slug: salesforce-commerce-cloud
tags:
- Commerce
- E-Commerce
- Headless Commerce
- Salesforce
- B2C Commerce
- B2B Commerce
- Demandware
website: https://www.salesforce.com/products/commerce-cloud/
---
