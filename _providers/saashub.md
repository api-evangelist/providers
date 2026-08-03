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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Saashub Agentic Access
  operation_count: 2
  slug: saashub-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Software alternatives discovery
  name: SaaSHub Alternatives API
  slug: saashub-alternatives-api
- description: Software product lookup
  name: SaaSHub Products API
  slug: saashub-products-api
artifact_total: 14
collections:
- collection_type: open
  name: SaaSHub API
  slug: open-saashub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/saashub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saashub-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saashub-it
- group: company
  title: ''
  type: Website
  url: https://www.saashub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.saashub.com/site/api
- group: auth
  title: ''
  type: Authentication
  url: https://www.saashub.com/profile/api_key
- group: operate
  title: ''
  type: FAQ
  url: https://www.saashub.com/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.saashub.com/site/privacy
- group: company
  title: ''
  type: Newsletter
  url: https://www.saashub.com/newsletter
- group: start
  title: ''
  type: Signup
  url: https://www.saashub.com/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://www.saashub.com/users/sign_in
- group: other
  title: ''
  type: X
  url: https://twitter.com/saashubcom
created: '2026-03-24'
description: SaaSHub is an independent software discovery platform that helps users find, compare, and discover software alternatives across SaaS, web, and cloud-based applications. The platform maintains a comprehensive catalog of software products with user reviews, pricing information, feature comparisons, and curated lists of alternatives. SaaSHub serves as a permanent directory where software vendors can list their products and users can discover alternatives to tools they already use.
examples:
- key_count: 2
  name: Saashub Get Product Alternatives Example
  slug: saashub-get-product-alternatives-example
finops:
- name: Saashub Finops
  service_category: API
  slug: saashub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saashub.png
json_schemas:
- name: SaaSHub Product
  property_count: 3
  slug: saashub-product
json_structures:
- name: Saashub Product Structure
  property_count: 0
  slug: saashub-product-structure
jsonld:
- class_count: 7
  name: Saashub Context
  property_count: 7
  slug: saashub-context
layout: provider
modified: '2026-05-19'
name: SaaSHub
nav: Providers
network: true
overview: 'SaaSHub publishes 2 APIs on the [APIs.io](https://apis.io/) network: Alternatives API and Products API. Tagged areas include Alternatives, SaaS, Software Discovery, and Software Catalog.


  The SaaSHub catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SaaSHub''s developer surface includes documentation, authentication, FAQ, signup flow, and 8 more developer resources.'
plans:
- name: Saashub Plans Pricing
  plan_count: 3
  slug: saashub-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 5
  name: Saashub Rate Limits
  slug: saashub-rate-limits
rules:
- name: SaaSHub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: saashub-jsonschema-spectral-rules
- name: SaaSHub API Rules
  rule_count: 12
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 9
  slug: saashub-spectral-rules
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 64.3
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Saashub Domain Security
  slug: saashub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: saashub
tags:
- Alternatives
- SaaS
- Software Discovery
- Software Catalog
website: https://www.saashub.com/
---
