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
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: Intuit TurboTax API enables integration with TurboTax for consumer and business tax preparation workflows, including data import, tax calculation, and e-filing.
  name: TurboTax API
  slug: turbotax-api
- description: H&R Block provides tax preparation templates and tools for individual and small business returns, including document import and guided filing workflows.
  name: H&R Block API
  slug: h-r-block-api
- description: Xero's Tax API enables accounting software and tax providers to connect to Xero for seamless tax return preparation using real-time financial data.
  name: Xero Tax API
  slug: xero-tax-api
- description: QuickBooks Online API provides access to tax-related financial data including income, expenses, and payroll for generating tax templates and returns.
  name: QuickBooks Tax API
  slug: quickbooks-tax-api
- description: FATCA (Foreign Account Tax Compliance Act) and CRS (Common Reporting Standard) templates for financial institutions reporting foreign account holders to the IRS and international tax authorities.
  name: FATCA/CRS Reporting Templates
  slug: fatca-crs-reporting
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tax-templates-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.irs.gov/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tax-document-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tax-document-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tax-templates-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tax-templates-vocabulary.yml
created: '2025'
description: Pre-designed templates for organizing and filing tax documents and returns. Financial institutions and enterprises use these templates to streamline tax operations and manage fiscal responsibilities. Covers tax document collection, structured data formats for financial disclosures, corporate tax returns, and regulatory compliance frameworks across jurisdictions.
examples:
- key_count: 8
  name: W2 Document Example
  slug: w2-document-example
finops:
- name: Tax Templates Finops
  service_category: API
  slug: tax-templates-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tax-templates.png
json_schemas:
- name: Tax Document
  property_count: 9
  slug: tax-document
json_structures:
- name: Tax Document Structure
  property_count: 0
  slug: tax-document-structure
jsonld:
- class_count: 23
  name: Tax Templates Context
  property_count: 0
  slug: tax-templates-context
layout: provider
modified: '2026-05-03'
name: Tax Templates
nav: Providers
network: true
overview: 'Tax Templates publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Documentation, Finance, Tax, Templates, and Compliance.


  The Tax Templates catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Tax Templates Plans Pricing
  plan_count: 3
  slug: tax-templates-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Tax Templates Rate Limits
  slug: tax-templates-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tax Templates API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tax-templates-jsonschema-spectral-rules
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tax-templates/refs/heads/main/screenshots/tax-templates-2026-06-20T194933.png
security:
- kind: domain-security
  name: Tax Templates Domain Security
  slug: tax-templates-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tax-templates
tags:
- Documentation
- Finance
- Tax
- Templates
- Compliance
website: https://www.irs.gov/
---
