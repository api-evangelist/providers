---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Vatstack Agentic Access
  operation_count: 23
  slug: vatstack-agentic-access
  summary_line: 23 operations · 10 acting
api_count: 7
apis:
- description: The Batches API from Vatstack — 2 operation(s) for batches.
  name: Vatstack Batches API
  slug: vatstack-batches-api
- description: The Evidences API from Vatstack — 2 operation(s) for evidences.
  name: Vatstack Evidences API
  slug: vatstack-evidences-api
- description: The Hits API from Vatstack — 1 operation(s) for hits.
  name: Vatstack Hits API
  slug: vatstack-hits-api
- description: The Quotes API from Vatstack — 2 operation(s) for quotes.
  name: Vatstack Quotes API
  slug: vatstack-quotes-api
- description: The Rates API from Vatstack — 2 operation(s) for rates.
  name: Vatstack Rates API
  slug: vatstack-rates-api
- description: The Supplies API from Vatstack — 2 operation(s) for supplies.
  name: Vatstack Supplies API
  slug: vatstack-supplies-api
- description: The Validations API from Vatstack — 2 operation(s) for validations.
  name: Vatstack Validations API
  slug: vatstack-validations-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vatstack API Specification Batches API
  slug: open-vatstack-batches-api
- collection_type: open
  name: Vatstack API Specification Batches Evidences API
  slug: open-vatstack-evidences-api
- collection_type: open
  name: Vatstack API Specification Batches Hits API
  slug: open-vatstack-hits-api
- collection_type: open
  name: Vatstack API Specification Batches Quotes API
  slug: open-vatstack-quotes-api
- collection_type: open
  name: Vatstack API Specification Batches Rates API
  slug: open-vatstack-rates-api
- collection_type: open
  name: Vatstack API Specification Batches Supplies API
  slug: open-vatstack-supplies-api
- collection_type: open
  name: Vatstack API Specification Batches Validations API
  slug: open-vatstack-validations-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vatstack-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vatstack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vatstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vatstack-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vatstack.com
- group: docs
  title: ''
  type: Documentation
  url: https://vatstack.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/vatstack
- group: company
  title: ''
  type: Blog
  url: https://vatstack.com/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://vatstack.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vatstack.com
- group: other
  title: ''
  type: X
  url: https://x.com/vatstack
- group: commercial
  title: ''
  type: Plans
  url: plans/vatstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vatstack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vatstack-finops.yml
created: '2026-06-13'
description: VAT number validation and EU tax rates REST API for validating European business VAT IDs via VIES and accessing current VAT rates for all EU member states. Vatstack provides automated VAT compliance for digital businesses including real-time VAT number validation, EU GST rate synchronization, price quotation engine, and automated VAT reporting for EC Sales List and VAT OSS requirements.
examples:
- key_count: 3
  name: Batch Example
  slug: batch-example
- key_count: 3
  name: Error Example
  slug: error-example
- key_count: 3
  name: Evidence Example
  slug: evidence-example
- key_count: 3
  name: Hit Example
  slug: hit-example
- key_count: 3
  name: Quote Example
  slug: quote-example
- key_count: 3
  name: Rate Example
  slug: rate-example
- key_count: 3
  name: Supply Example
  slug: supply-example
- key_count: 3
  name: Validation Example
  slug: validation-example
finops:
- name: Vatstack Finops
  service_category: ''
  slug: vatstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vatstack.png
json_schemas:
- name: Batch
  property_count: 9
  slug: batch
- name: Error
  property_count: 2
  slug: error
- name: Evidence
  property_count: 7
  slug: evidence
- name: Hit
  property_count: 2
  slug: hit
- name: Quote
  property_count: 13
  slug: quote
- name: Rate
  property_count: 11
  slug: rate
- name: Supply
  property_count: 17
  slug: supply
- name: Validation
  property_count: 16
  slug: validation
jsonld:
- class_count: 9
  name: Vatstack Context
  property_count: 21
  slug: vatstack-context
layout: provider
modified: '2026-06-13'
name: Vatstack
nav: Providers
network: true
overview: 'Vatstack publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Batches API, Evidences API, Hits API, and 4 more. Tagged areas include VAT, Tax, Validation, EU, and Europe.


  The Vatstack catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vatstack''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Vatstack Plans Pricing
  plan_count: 3
  slug: vatstack-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 8
  name: Vatstack Rate Limits
  slug: vatstack-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Vatstack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vatstack-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.1
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 59.9
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vatstack/refs/heads/main/screenshots/vatstack-2026-06-20T200843.png
security:
- kind: authentication
  name: Vatstack Authentication
  slug: vatstack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vatstack Domain Security
  slug: vatstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vatstack Vulnerability Disclosure
  slug: vatstack-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vatstack
tags:
- VAT
- Tax
- Validation
- EU
- Europe
- Compliance
- Finance
- Business
website: https://vatstack.com
---
