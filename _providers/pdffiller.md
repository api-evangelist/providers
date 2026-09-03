---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: negotiable
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
  score: 22.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Pdffiller Agentic Access
  operation_count: 73
  slug: pdffiller-agentic-access
  summary_line: 73 operations · 28 acting
api_count: 1
apis:
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Manage OAuth applications
  name: PDFfiller Applications API
  slug: pdffiller-applications-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: OAuth 2.0 authentication token management
  name: PDFfiller Auth API
  slug: pdffiller-auth-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Manage webhook callbacks for document events
  name: PDFfiller Callbacks API
  slug: pdffiller-callbacks-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Manage custom branding logos
  name: PDFfiller Custom Logos API
  slug: pdffiller-custom-logos-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Manage fillable form links and submissions
  name: PDFfiller Fillable Forms API
  slug: pdffiller-fillable-forms-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Organize documents into folders
  name: PDFfiller Folders API
  slug: pdffiller-folders-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Manage eSignature requests and workflows
  name: PDFfiller Signature Requests API
  slug: pdffiller-signature-requests-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Manage PDF document templates
  name: PDFfiller Templates API
  slug: pdffiller-templates-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Manage embedded document tokens
  name: PDFfiller Tokens API
  slug: pdffiller-tokens-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Document utility tools (merge, convert)
  name: PDFfiller Tools API
  slug: pdffiller-tools-api
- baseURL: https://api.pdffiller.com/v2/
  baseurl_source: declared
  description: Retrieve current user information
  name: PDFfiller Users API
  slug: pdffiller-users-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PDFfiller REST Applications API
  slug: open-pdffiller-applications-api
- collection_type: open
  name: PDFfiller REST Applications Auth API
  slug: open-pdffiller-auth-api
- collection_type: open
  name: PDFfiller REST Applications Callbacks API
  slug: open-pdffiller-callbacks-api
- collection_type: open
  name: PDFfiller REST Applications Custom Logos API
  slug: open-pdffiller-custom-logos-api
- collection_type: open
  name: PDFfiller REST Applications Fillable Forms API
  slug: open-pdffiller-fillable-forms-api
- collection_type: open
  name: PDFfiller REST Applications Folders API
  slug: open-pdffiller-folders-api
- collection_type: open
  name: PDFfiller REST Applications Signature Requests API
  slug: open-pdffiller-signature-requests-api
- collection_type: open
  name: PDFfiller REST Applications Templates API
  slug: open-pdffiller-templates-api
- collection_type: open
  name: PDFfiller REST Applications Tokens API
  slug: open-pdffiller-tokens-api
- collection_type: open
  name: PDFfiller REST Applications Tools API
  slug: open-pdffiller-tools-api
- collection_type: open
  name: PDFfiller REST Applications Users API
  slug: open-pdffiller-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pdffiller-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pdffiller-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pdffiller-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pdffiller-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.pdffiller.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pdffiller.com/docs/pdffiller/zmnt034fyekxf-pdf-filler-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.pdffiller.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pdffiller
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pdffiller-com
- group: company
  title: ''
  type: Blog
  url: https://blog.pdffiller.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pdffiller.com/en/pdf-api-pricing.htm
- group: other
  title: ''
  type: X
  url: https://x.com/pdf_filler
- group: commercial
  title: ''
  type: Plans
  url: plans/pdffiller-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pdffiller-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pdffiller-finops.yml
created: '2026-06-13'
description: PDFfiller is an online PDF editing and e-signature platform that provides a REST API for filling, editing, signing, converting, and managing PDF documents programmatically. The API enables developers to embed PDF editing, form-building, signature request workflows, and document management capabilities into their own applications. It is part of the airSlate family of products and supports OAuth 2.0 authentication with a base URL of https://api.pdffiller.com/v2/.
examples:
- key_count: 4
  name: Pdffiller Create Fillable Form Example
  slug: pdffiller-create-fillable-form-example
- key_count: 4
  name: Pdffiller Create Signature Request Example
  slug: pdffiller-create-signature-request-example
- key_count: 4
  name: Pdffiller Oauth Token Example
  slug: pdffiller-oauth-token-example
finops:
- name: Pdffiller Finops
  service_category: ''
  slug: pdffiller-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pdffiller.png
json_schemas:
- name: FillableForm
  property_count: 22
  slug: pdffiller-fillable-form
- name: SignatureRequest
  property_count: 11
  slug: pdffiller-signature-request
- name: Template
  property_count: 9
  slug: pdffiller-template
jsonld:
- class_count: 63
  name: Pdffiller Context
  property_count: 2
  slug: pdffiller-context
layout: provider
modified: '2026-06-13'
name: PDFfiller
nav: Providers
network: true
overview: 'PDFfiller publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Auth API, Callbacks API, and 8 more. Tagged areas include PDF, E-Signature, Document-Management, Form Builder, and PDF Editing.


  The PDFfiller catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PDFfiller''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Pdffiller Plans Pricing
  plan_count: 3
  slug: pdffiller-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Pdffiller Rate Limits
  slug: pdffiller-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: PDFfiller API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pdffiller-jsonschema-spectral-rules
scopes:
- name: Pdffiller Scopes
  scope_count: 2
  slug: pdffiller-scopes
  summary_line: 2 scopes · password/clientCredentials
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 62.6
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pdffiller/refs/heads/main/screenshots/pdffiller-2026-06-20T191529.png
security:
- kind: authentication
  name: Pdffiller Authentication
  slug: pdffiller-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pdffiller Domain Security
  slug: pdffiller-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pdffiller
tags:
- PDF
- E-Signature
- Document-Management
- Form Builder
- PDF Editing
- Electronic Signature
- Document Workflow
website: https://www.pdffiller.com
---
