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
- acting_count: 5
  human_in_the_loop: 0
  name: Doctly Ai Agentic Access
  operation_count: 9
  slug: doctly-ai-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.doctly.ai/api/v1
  baseurl_source: declared
  description: Upload documents for Markdown conversion and retrieve results.
  name: Doctly Documents API
  slug: doctly-ai-documents-api
- baseURL: https://api.doctly.ai/api/v1
  baseurl_source: declared
  description: Manage and run custom structured-data extractors.
  name: Doctly Extractors API
  slug: doctly-ai-extractors-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Doctly Documents API
  slug: open-doctly-ai-documents-api
- collection_type: open
  name: Doctly Documents Extractors API
  slug: open-doctly-ai-extractors-api
- collection_type: open
  name: Doctly API
  slug: open-doctly-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doctly-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doctly-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doctly-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/doctly-ai
- group: company
  title: ''
  type: Website
  url: https://doctly.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.doctly.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doctly
- group: commercial
  title: ''
  type: Plans
  url: plans/doctly-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doctly-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/doctly-ai-finops.yml
created: '2026-06-21'
description: Doctly is an AI document-to-Markdown and structured-data extraction API. It converts PDFs, DOCX, and image files into clean Markdown or JSON via an asynchronous submit-then-poll REST API, with LITE and ULTRA accuracy levels, optional custom extractors for structured extraction, and webhook callbacks on completion.
finops:
- name: Doctly Ai Finops
  service_category: AI and Machine Learning
  slug: doctly-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doctly-ai.png
layout: provider
modified: '2026-06-21'
name: Doctly
nav: Providers
network: true
overview: 'Doctly publishes 2 APIs on the [APIs.io](https://apis.io/) network: Documents API and Extractors API. Tagged areas include Artificial Intelligence, Document Parsing, PDF, Markdown, and Data Extraction.


  Doctly''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Doctly Ai Plans Pricing
  plan_count: 3
  slug: doctly-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Doctly Ai Rate Limits
  slug: doctly-ai-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doctly-ai/refs/heads/main/screenshots/doctly-ai-2026-07-25T212214.png
security:
- kind: authentication
  name: Doctly Ai Authentication
  slug: doctly-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Doctly Ai Domain Security
  slug: doctly-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: doctly-ai
tags:
- Artificial Intelligence
- Document Parsing
- PDF
- Markdown
- Data Extraction
- OCR
website: https://doctly.ai
---
