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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Zoho Writer Agentic Access
  operation_count: 12
  slug: zoho-writer-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- description: REST API for programmatic document creation, editing, mail merge, electronic signing, webhook automation, and multi-format document export. Supports Document, Meta, Combine, Merge, and Sign API catego
  name: Zoho Writer API
  slug: zoho-writer-api
- baseURL: https://writer.zoho.com/api/v1
  baseurl_source: declared
  description: Combine multiple PDF documents into one
  name: Zoho Writer Combine API
  slug: zoho-writer-combine-api
- baseURL: https://writer.zoho.com/api/v1
  baseurl_source: declared
  description: Create, upload, list, download, and inspect documents
  name: Zoho Writer Documents API
  slug: zoho-writer-documents-api
- baseURL: https://writer.zoho.com/api/v1
  baseurl_source: declared
  description: 'Mail-merge operations: merge to bytes, link, store, invoke, or sign'
  name: Zoho Writer Merge API
  slug: zoho-writer-merge-api
- baseURL: https://writer.zoho.com/api/v1
  baseurl_source: declared
  description: Electronic signature workflows via Zoho Sign
  name: Zoho Writer Signatures API
  slug: zoho-writer-signatures-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zoho Writer Combine API
  slug: open-zoho-writer-combine-api
- collection_type: open
  name: Zoho Writer Combine Documents API
  slug: open-zoho-writer-documents-api
- collection_type: open
  name: Zoho Writer Combine Merge API
  slug: open-zoho-writer-merge-api
- collection_type: open
  name: Zoho Writer Combine Signatures API
  slug: open-zoho-writer-signatures-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-writer-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-writer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-writer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-writer-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-writer-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/writer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/writer/help/api/v1/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zoho
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/writer/
- group: commercial
  title: ''
  type: Pricing
  url: https://help.zoho.com/portal/en/kb/writer/writer-add-ons/pricing-faq/articles/how-can-i-purchase-the-writer-add-on
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com
- group: other
  title: ''
  type: X
  url: https://x.com/ZohoWriter
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-writer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-writer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-writer-finops.yml
created: '2026-06-13'
description: Zoho Writer is an online word processor with a REST API for creating, editing, merging, converting, and signing documents, and automating document workflows within the Zoho ecosystem. The API supports document CRUD operations, mail merge with templates, fillable forms, electronic signatures via Zoho Sign integration, webhook-triggered automation, and multi-format document export (PDF, DOCX, HTML). OAuth 2.0 authentication is used with domain-specific base URLs across global data centers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-writer.png
json_schemas:
- name: ZohoWriterDocument
  property_count: 30
  slug: document
jsonld:
- class_count: 37
  name: Zoho Writer Context
  property_count: 0
  slug: zoho-writer-context
layout: provider
modified: '2026-06-13'
name: Zoho Writer
nav: Providers
network: true
overview: 'Zoho Writer publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Combine API, Documents API, Merge API, and 1 more. Tagged areas include Documents, Word Processor, Mail Merge, Document Generation, and Electronic Signatures.


  The Zoho Writer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zoho Writer''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Zoho Writer Plans Pricing
  plan_count: 4
  slug: zoho-writer-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Zoho Writer Rate Limits
  slug: zoho-writer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zoho Writer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zoho-writer-jsonschema-spectral-rules
scopes:
- name: Zoho Writer Scopes
  scope_count: 6
  slug: zoho-writer-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 9.8
    contract_quality: 58.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-writer/refs/heads/main/screenshots/zoho-writer-2026-06-20T201950.png
security:
- kind: authentication
  name: Zoho Writer Authentication
  slug: zoho-writer-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zoho Writer Domain Security
  slug: zoho-writer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Writer Vulnerability Disclosure
  slug: zoho-writer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-writer
tags:
- Documents
- Word Processor
- Mail Merge
- Document Generation
- Electronic Signatures
- Zoho
- Office Suite
- Automation
website: https://www.zoho.com/writer/
---
