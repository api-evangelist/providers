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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Feathery Agentic Access
  operation_count: 46
  slug: feathery-agentic-access
  summary_line: 46 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.feathery.io
  baseurl_source: declared
  description: Team and account management
  name: Feathery Account API
  slug: feathery-account-api
- baseURL: https://api.feathery.io
  baseurl_source: declared
  description: Data hub entry actions
  name: Feathery Data Hubs API
  slug: feathery-data-hubs-api
- baseURL: https://api.feathery.io
  baseurl_source: declared
  description: AI-driven document extraction
  name: Feathery Document Intelligence API
  slug: feathery-document-intelligence-api
- baseURL: https://api.feathery.io
  baseurl_source: declared
  description: PDF and document template management
  name: Feathery Document Templates API
  slug: feathery-document-templates-api
- baseURL: https://api.feathery.io
  baseurl_source: declared
  description: End user management
  name: Feathery End Users API
  slug: feathery-end-users-api
- baseURL: https://api.feathery.io
  baseurl_source: declared
  description: Form creation and management
  name: Feathery Forms API
  slug: feathery-forms-api
- baseURL: https://api.feathery.io
  baseurl_source: declared
  description: Hidden field management
  name: Feathery Hidden Fields API
  slug: feathery-hidden-fields-api
- baseURL: https://api.feathery.io
  baseurl_source: declared
  description: API connector and email logs
  name: Feathery Logs API
  slug: feathery-logs-api
- baseURL: https://api.feathery.io
  baseurl_source: declared
  description: Workspace management
  name: Feathery Workspaces API
  slug: feathery-workspaces-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Feathery REST Account API
  slug: open-feathery-account-api
- collection_type: open
  name: Feathery REST Account Data Hubs API
  slug: open-feathery-data-hubs-api
- collection_type: open
  name: Feathery REST Account Document Intelligence API
  slug: open-feathery-document-intelligence-api
- collection_type: open
  name: Feathery REST Account Document Templates API
  slug: open-feathery-document-templates-api
- collection_type: open
  name: Feathery REST Account End Users API
  slug: open-feathery-end-users-api
- collection_type: open
  name: Feathery REST Account Forms API
  slug: open-feathery-forms-api
- collection_type: open
  name: Feathery REST Account Hidden Fields API
  slug: open-feathery-hidden-fields-api
- collection_type: open
  name: Feathery REST Account Logs API
  slug: open-feathery-logs-api
- collection_type: open
  name: Feathery REST Account Workspaces API
  slug: open-feathery-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/feathery-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/feathery-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/feathery-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.feathery.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.feathery.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/feathery-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/feathery-forms
- group: company
  title: ''
  type: Blog
  url: https://www.feathery.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.feathery.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.feathery.io
- group: other
  title: ''
  type: X
  url: https://x.com/feathery_io
- group: commercial
  title: ''
  type: Plans
  url: plans/feathery-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/feathery-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/feathery-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.feathery.io/product-updates
created: '2026-06-13'
description: Feathery is an enterprise form SDK and AI-driven data intake platform offering a REST API for creating multi-step forms, managing field logic, collecting submissions, and integrating with payment, authentication, and financial services systems. Purpose-built for financial services including insurance and wealth management.
examples:
- key_count: 12
  name: Feathery Extraction Run Example
  slug: feathery-extraction-run-example
- key_count: 8
  name: Feathery Form Example
  slug: feathery-form-example
- key_count: 6
  name: Feathery Submission Example
  slug: feathery-submission-example
finops:
- name: Feathery Finops
  service_category: ''
  slug: feathery-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/feathery.png
json_schemas:
- name: Feathery AI Extraction Configuration
  property_count: 8
  slug: feathery-extraction
- name: Feathery Form
  property_count: 8
  slug: feathery-form
- name: Feathery Form Submission
  property_count: 6
  slug: feathery-submission
jsonld:
- class_count: 52
  name: Feathery Context
  property_count: 42
  slug: feathery-context
layout: provider
modified: '2026-06-13'
name: Feathery
nav: Providers
network: true
overview: 'Feathery publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Data Hubs API, Document Intelligence API, and 6 more. Tagged areas include Forms, Form Builder, Multi-Step Forms, Document Intelligence, and Artificial Intelligence.


  The Feathery catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Feathery''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 10 more developer resources.'
plans:
- name: Feathery Plans Pricing
  plan_count: 3
  slug: feathery-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Feathery Rate Limits
  slug: feathery-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Feathery API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: feathery-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 66.7
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/feathery/refs/heads/main/screenshots/feathery-2026-06-20T181109.png
security:
- kind: authentication
  name: Feathery Authentication
  slug: feathery-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Feathery Domain Security
  slug: feathery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: feathery
tags:
- Forms
- Form Builder
- Multi-Step Forms
- Document Intelligence
- Artificial Intelligence
- Financial-Services
- Insurance
- Wealth Management
- E-Signature
- Workflows
- Data Intake
- Submissions
- Payments
- Authentication
website: https://www.feathery.io
---
