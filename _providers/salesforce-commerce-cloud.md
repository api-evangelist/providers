---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Salesforce Commerce Cloud Agentic Access
  operation_count: 10
  slug: salesforce-commerce-cloud-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 3
apis:
- description: Modern REST API family for B2C Commerce Cloud built on a unified RAML specification, organized into Shopper, Data, and Admin APIs for headless commerce. Authentication uses OAuth 2.0 via Salesforce Ac
  name: Salesforce Commerce API (SCAPI)
  slug: scapi
- description: 'Legacy REST API for B2C Commerce Cloud, organized into Shop API, Data API, and Meta API. Authentication uses OAuth 2.0 via Salesforce Account Manager. OCAPI is deprecated for new projects in favor of '
  name: Open Commerce API (OCAPI)
  slug: ocapi
- description: The Shopper API from Salesforce Commerce Cloud — 9 operation(s) for shopper.
  name: Salesforce Commerce Cloud Shopper API
  slug: salesforce-commerce-cloud-shopper-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesforce Commerce API (SCAPI) - Subset Shopper API
  slug: open-salesforce-commerce-cloud-shopper-api
- collection_type: open
  name: Salesforce Commerce API (SCAPI) - Shopper Subset
  slug: open-salesforce-commerce-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-commerce-cloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/salesforce-commerce-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-commerce-cloud-domain-security.yml
- group: auth
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
graphqls:
- description: This is a conceptual GraphQL schema for Salesforce Commerce Cloud (SFCC), derived from the
  name: Salesforce Commerce Cloud GraphQL Schema
  slug: salesforce-commerce-cloud-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salesforce-commerce-cloud.png
layout: provider
modified: '2026-05-19'
name: Salesforce Commerce Cloud
nav: Providers
network: true
overview: 'Salesforce Commerce Cloud publishes 1 API on the [APIs.io](https://apis.io/) network: Shopper API. Tagged areas include Commerce, E-Commerce, Headless Commerce, Salesforce, and B2C Commerce.


  Salesforce Commerce Cloud''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 11 more developer resources.'
random_paper: 147
score:
  band: thin
  composite: 35.7
  delta: -0.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 47.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce-commerce-cloud/refs/heads/main/screenshots/salesforce-commerce-cloud-2026-06-20T193346.png
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
  summary_line: disclosure policy published
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
