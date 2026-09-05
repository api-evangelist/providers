---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Docparser Agentic Access
  operation_count: 8
  slug: docparser-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.docparser.com/v1
  baseurl_source: declared
  description: Upload and manage documents for parsing
  name: Docparser Documents API
  slug: docparser-documents-api
- baseURL: https://api.docparser.com/v1
  baseurl_source: declared
  description: Manage document parser configurations
  name: Docparser Parsers API
  slug: docparser-parsers-api
- baseURL: https://api.docparser.com/v1
  baseurl_source: declared
  description: Health check and connectivity test
  name: Docparser Ping API
  slug: docparser-ping-api
- baseURL: https://api.docparser.com/v1
  baseurl_source: declared
  description: Retrieve parsed data results
  name: Docparser Results API
  slug: docparser-results-api
artifact_total: 29
collections:
- collection_type: postman
  name: Docparser REST Documents API
  slug: postman-docparser-documents-api
- collection_type: postman
  name: Docparser REST Documents Parsers API
  slug: postman-docparser-parsers-api
- collection_type: postman
  name: Docparser REST Documents Ping API
  slug: postman-docparser-ping-api
- collection_type: postman
  name: Docparser REST Documents Results API
  slug: postman-docparser-results-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Docparser REST Documents API
  slug: open-docparser-documents-api
- collection_type: open
  name: Docparser REST Documents Parsers API
  slug: open-docparser-parsers-api
- collection_type: open
  name: Docparser REST Documents Ping API
  slug: open-docparser-ping-api
- collection_type: open
  name: Docparser REST Documents Results API
  slug: open-docparser-results-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/docparser/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/docparser-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/docparser-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docparser-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/docparser-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://docparser.com
- group: docs
  title: ''
  type: Documentation
  url: https://docparser.com/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Docparser
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/docparser
- group: other
  title: ''
  type: X
  url: https://x.com/docparser
- group: company
  title: ''
  type: Blog
  url: https://docparser.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://docparser.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.docparser.com/
- group: design
  title: ''
  type: Webhooks
  url: https://docparser.com/integrations/webhooks/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Docparser
- group: commercial
  title: ''
  type: Plans
  url: plans/docparser-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/docparser-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/docparser-finops.yml
created: '2026-06-13'
description: Docparser is a document data extraction REST API that enables developers and businesses to parse structured data from PDFs, Word documents, and scanned image files using custom parsing rules. The platform supports advanced zonal OCR, pattern recognition, and anchor keyword detection for automating data extraction from invoices, contracts, purchase orders, bank statements, HR forms, and shipping documents. Docparser provides a REST API with endpoints for uploading documents, fetching parsed results, managing parsers, and re-processing documents, along with webhook support for real-time data delivery and official SDKs for PHP, Node.js, and Salesforce Apex.
examples:
- key_count: 19
  name: Get Results By Document Response
  slug: get-results-by-document-response
- key_count: 1
  name: Ping Response
  slug: ping-response
- key_count: 3
  name: Upload Document Base64 Request
  slug: upload-document-base64-request
- key_count: 4
  name: Upload Document Response
  slug: upload-document-response
finops:
- name: Docparser Finops
  service_category: ''
  slug: docparser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docparser.png
json_schemas:
- name: Docparser Document Upload Response
  property_count: 4
  slug: docparser-document-upload
- name: Docparser Parsed Result
  property_count: 7
  slug: docparser-parsed-result
- name: Docparser Parser
  property_count: 2
  slug: docparser-parser
jsonld:
- class_count: 5
  name: Docparser Context
  property_count: 25
  slug: docparser-context
layout: provider
modified: '2026-06-13'
name: Docparser
nav: Providers
network: true
overview: 'Docparser publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Parsers API, Ping API, and 1 more. Tagged areas include Document Parsing, Data Extraction, PDF, OCR, and Document Automation.


  The Docparser catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Docparser''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Docparser Plans Pricing
  plan_count: 4
  slug: docparser-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 8
  name: Docparser Rate Limits
  slug: docparser-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Docparser API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: docparser-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 78.3
    catalog_earned_first_party: 0.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 61.7
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 60.5
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docparser/refs/heads/main/screenshots/docparser-2026-06-20T180109.png
security:
- kind: authentication
  name: Docparser Authentication
  slug: docparser-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Docparser Domain Security
  slug: docparser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Docparser Trust Center
  slug: docparser-trust-center
  summary_line: HIPAA, GDPR
slug: docparser
tags:
- Document Parsing
- Data Extraction
- PDF
- OCR
- Document Automation
- Invoices
- Contracts
- REST API
website: https://docparser.com
---
