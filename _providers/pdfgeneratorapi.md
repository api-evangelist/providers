---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Pdfgeneratorapi Agentic Access
  operation_count: 26
  slug: pdfgeneratorapi-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 1
apis:
- baseURL: https://us1.pdfgeneratorapi.com/api/v4
  baseurl_source: declared
  description: Generate, store, and retrieve documents.
  name: PDF Generator API Documents API
  slug: pdfgeneratorapi-documents-api
- baseURL: https://us1.pdfgeneratorapi.com/api/v4
  baseurl_source: declared
  description: Manage reusable document templates and the template editor.
  name: PDF Generator API Templates API
  slug: pdfgeneratorapi-templates-api
- baseURL: https://us1.pdfgeneratorapi.com/api/v4
  baseurl_source: declared
  description: Manage multi-tenant workspaces within the organization.
  name: PDF Generator API Workspaces API
  slug: pdfgeneratorapi-workspaces-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PDF Generator Documents API
  slug: open-pdfgeneratorapi-documents-api
- collection_type: open
  name: PDF Generator Documents Templates API
  slug: open-pdfgeneratorapi-templates-api
- collection_type: open
  name: PDF Generator Documents Workspaces API
  slug: open-pdfgeneratorapi-workspaces-api
- collection_type: open
  name: PDF Generator API
  slug: open-pdfgeneratorapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pdfgeneratorapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdfgeneratorapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pdfgeneratorapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pdfgeneratorapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pdf-generator-api
- group: company
  title: ''
  type: Website
  url: https://pdfgeneratorapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pdfgeneratorapi.com/v4/
- group: commercial
  title: ''
  type: Plans
  url: plans/pdfgeneratorapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdfgeneratorapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdfgeneratorapi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://pdfgeneratorapi.com/blog
created: '2026-06-25'
description: PDF Generator API is a template-based document and PDF generation service. A drag-and-drop browser template editor plus a REST API let developers merge JSON data with reusable templates to produce PDFs, HTML, and other documents synchronously, asynchronously, or in batches, organized across multi-tenant workspaces.
finops:
- name: Pdfgeneratorapi Finops
  service_category: Developer Tools and Document Automation
  slug: pdfgeneratorapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdfgeneratorapi.png
layout: provider
modified: '2026-06-25'
name: PDF Generator API
nav: Providers
network: true
overview: 'PDF Generator API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Documents API, Templates API, and Workspaces API. Tagged areas include PDF, Document Generation, Templates, Reporting, and Workspaces.


  PDF Generator API''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Pdfgeneratorapi Plans Pricing
  plan_count: 7
  slug: pdfgeneratorapi-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Pdfgeneratorapi Rate Limits
  slug: pdfgeneratorapi-rate-limits
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.2
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pdfgeneratorapi/refs/heads/main/screenshots/pdfgeneratorapi-2026-08-07T191716.png
security:
- kind: authentication
  name: Pdfgeneratorapi Authentication
  slug: pdfgeneratorapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pdfgeneratorapi Domain Security
  slug: pdfgeneratorapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pdfgeneratorapi
tags:
- PDF
- Document Generation
- Templates
- Reporting
- Workspaces
website: https://pdfgeneratorapi.com
---
