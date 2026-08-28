---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Robin Ai Agentic Access
  operation_count: 14
  slug: robin-ai-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 5
apis:
- description: Upload and manage legal documents
  name: Robin AI Documents API
  slug: robin-ai-documents-api
- description: Organizational containers for documents and tables
  name: Robin AI Groups API
  slug: robin-ai-groups-api
- description: Typed custom property definitions for documents
  name: Robin AI Properties API
  slug: robin-ai-properties-api
- description: Bulk structured extraction from contract portfolios
  name: Robin AI Tables API
  slug: robin-ai-tables-api
- description: Reusable prompt sets that drive Table extraction
  name: Robin AI Templates API
  slug: robin-ai-templates-api
artifact_total: 58
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Robin Legal Intelligence Platform Documents API
  slug: open-robin-ai-documents-api
- collection_type: open
  name: Robin Legal Intelligence Platform Documents Groups API
  slug: open-robin-ai-groups-api
- collection_type: open
  name: Robin Legal Intelligence Platform Documents Properties API
  slug: open-robin-ai-properties-api
- collection_type: open
  name: Robin Legal Intelligence Platform Documents Tables API
  slug: open-robin-ai-tables-api
- collection_type: open
  name: Robin Legal Intelligence Platform Documents Templates API
  slug: open-robin-ai-templates-api
- collection_type: open
  name: Robin Legal Intelligence Platform API
  slug: open-robin-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/robin-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/robin-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/robin-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/robin-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://robinai.com
- group: start
  title: ''
  type: Portal
  url: https://robinai.com/robin-api
- group: docs
  title: ''
  type: Documentation
  url: https://robinai.com/robin-api
- group: docs
  title: ''
  type: Documentation
  url: https://robinai.com/news-and-resources/blog/introducing-robins-tables-api-unlock-structured-data-from-legal-documents
- group: docs
  title: ''
  type: Documentation
  url: https://robinai.com/news-and-resources/robin-university/legal-intelligence-platform-an-ai-powered-hub-for-all-your-legal-data
- group: docs
  title: ''
  type: Documentation
  url: https://robinai.com/news-and-resources/robin-university/how-to-streamline-your-contract-review-with-robin-ai
- group: docs
  title: ''
  type: Documentation
  url: https://robinai.com/news-and-resources/guides-reports/legal-ai-buyers-guide
- group: start
  title: ''
  type: Signup
  url: https://app.robinai.com
- group: start
  title: ''
  type: Signup
  url: https://robinai.com/demo
- group: commercial
  title: ''
  type: Pricing
  url: https://robinai.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/robin-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/robin-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/robin-ai-finops.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.robinai.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://robinai.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://robinai.com/terms
- group: company
  title: ''
  type: Blog
  url: https://robinai.com/news-and-resources/blog
- group: company
  title: ''
  type: Newsroom
  url: https://robinai.com/news-and-resources
- group: company
  title: ''
  type: Careers
  url: https://robinai.com/company/careers
- group: other
  title: ''
  type: Company
  url: https://robinai.com/company
- group: operate
  title: ''
  type: Contact
  url: https://robinai.com/contact
- group: operate
  title: ''
  type: Support
  url: https://robinai.com/help
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/robinai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Robin_LegalAI
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@robinaichannel
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ai-robin
- group: other
  title: ''
  type: Marketplace
  url: https://aws.amazon.com/marketplace/reviews/reviews-list/prodview-zvgmcfv4tqtma
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.microsoft.com/en-in/product/office/WA200006060
- group: other
  title: ''
  type: Customers
  url: ''
- group: company
  title: ''
  type: Partners
  url: ''
- group: auth
  title: ''
  type: Certifications
  url: ''
- group: other
  title: ''
  type: Office
  url: ''
- group: operate
  title: ''
  type: CompanyStatus
  url: ''
created: '2026-05-24'
description: Robin AI is a London-headquartered legal intelligence platform founded in 2019 by former Clifford Chance disputes lawyer Richard Robinson and machine learning researcher James Clough. The platform automates contract review, drafting, search, obligation tracking, and structured extraction for enterprise legal teams via a Microsoft Word add-in, a web workspace, and a public REST API. Robin AI shipped on Anthropic's Claude models (Claude 3 entered the stack in March 2024) and processed 500k+ documents for customers including KPMG, PwC, Pfizer, GE, UBS, and PepsiCo, advertising 80% faster contract review and 3-second clause search. The company's public-facing Robin Legal Intelligence Platform API (openapi 3.1.0, version 0.2.0-dev, base URL https://api.robinai.com, X-API-Key auth) exposes Documents, Templates, Tables, Properties, and Groups — the Tables API is the flagship extraction surface that turns unstructured legal text into clean structured data tables for CLMs, CRMs, ERPs,
  BI dashboards, and risk engines. NOTE Robin AI collapsed in late 2025 after failing to close a $50M funding round; the managed services arm was acquired by Scissero in December 2025 and the engineering team was acqui-hired by Microsoft in January 2026 to strengthen Word's legal AI capabilities. This profile documents the API surface as it was published at robinai.com/robin-api.
examples:
- key_count: 2
  name: Robin Ai Create Document Example
  slug: robin-ai-create-document-example
- key_count: 2
  name: Robin Ai Create Table Example
  slug: robin-ai-create-table-example
- key_count: 2
  name: Robin Ai List Table Results Example
  slug: robin-ai-list-table-results-example
features:
- Tables API — bulk extraction of structured data points from contract portfolios using reusable Templates
- Documents API — upload PDFs and Word files, list and filter by name, type, group, and processing status
- Templates API — list reusable prompt sets that drive Table extraction (each prompt has name, prompt_text, and typed answer_format)
- Properties API — define and assign custom typed properties (string, number, currency, date-time, boolean) to documents
- Groups API — organize documents into personal, private, public, and report-scoped groups
- Clickable Citations — every Tables answer links back to the originating span in the source document
- Microsoft Word Add-In — embeds review and chat directly inside Word, the native drafting surface for lawyers
- Workspace web app — collaborative document chat, advanced search, obligation tracking, and renewal alerts
- Playbook-based redlining — flags clause deviations from a company's playbook and produces redlined drafts in seconds
- Anthropic Claude-powered review — Claude 3 entered the stack in March 2024, enabling large commercial-lease analysis in a single pass
- Cursor pagination (limit up to 1000 plus starting_after) and ISO 8601 date-range filters across all list endpoints
- X-API-Key header authentication; standard 4xx/5xx error envelope including 402 Payment Required, 422 Unprocessable Entity, and 429 Too Many Requests
- GDPR, ISO 27001, and SOC 2 certified; Privacy by Design methodology
- Hosted on AWS; available via AWS Marketplace and Microsoft AppSource
finops:
- name: Robin Ai Finops
  service_category: ''
  slug: robin-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/robin-ai.png
integrations:
- Contract Lifecycle Management (CLM) systems
- Customer Relationship Management (CRM) systems
- Enterprise Resource Planning (ERP) systems
- Business Intelligence dashboards (PowerBI)
- Risk engines
- Microsoft Word (native Add-In)
- Anthropic Claude models
- Amazon Web Services
json_schemas:
- name: Robin AI Document
  property_count: 9
  slug: robin-ai-document
- name: Robin AI Table
  property_count: 13
  slug: robin-ai-table
- name: Robin AI Template
  property_count: 6
  slug: robin-ai-template
json_structures:
- name: Robin Ai Document Structure
  property_count: 0
  slug: robin-ai-document-structure
jsonld:
- class_count: 33
  name: Robin Ai Context
  property_count: 6
  slug: robin-ai-context
layout: provider
modified: '2026-05-24'
name: Robin AI
nav: Providers
network: true
overview: 'Robin AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Groups API, Properties API, and 2 more. Tagged areas include Legal, Legal Tech, Contract Review, Contract Analysis, and Contract Lifecycle Management.


  The Robin AI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Robin AI''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, support, and 25 more developer resources.'
plans:
- name: Robin Ai Plans Pricing
  plan_count: 4
  slug: robin-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Robin Ai Rate Limits
  slug: robin-ai-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Robin AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: robin-ai-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Robin AI API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 2
  slug: robin-ai-rules
score:
  band: developing
  composite: 45.5
  delta: -0.9
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 13.6
    contract_quality: 60.5
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 2.6
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/robin-ai/refs/heads/main/screenshots/robin-ai-2026-06-20T193139.png
security:
- kind: authentication
  name: Robin Ai Authentication
  slug: robin-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Robin Ai Domain Security
  slug: robin-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: trust-center
  name: Robin Ai Trust Center
  slug: robin-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: robin-ai
tags:
- Legal
- Legal Tech
- Contract Review
- Contract Analysis
- Contract Lifecycle Management
- CLM
- Document Extraction
- Structured Data
- Legal AI
- Artificial Intelligence
- Word Add-In
- Playbook
- Redlining
- Obligation Tracking
- Anthropic
- Claude
use_cases:
- Auto-populating CLM systems with contract metadata extracted at scale
- Eliminating manual data entry from contract intake and onboarding
- Running high-volume extraction across thousands of agreements using pre-existing Templates
- Risk visualization across large contract portfolios in PowerBI and other BI dashboards
- Playbook-based first-pass review and redlining for legal, procurement, and commercial teams
- Obligation tracking — payment deadlines, renewals, and reporting duties
- Searching a contract estate in natural language and chatting with documents
website: https://robinai.com
---
