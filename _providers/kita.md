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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Kita Agentic Access
  operation_count: 52
  slug: kita-agentic-access
  summary_line: 52 operations · 22 acting
api_count: 14
apis:
- description: Loan application records.
  name: Kita Applications API
  slug: kita-applications-api
- description: Process up to 100 documents from URLs in one request.
  name: Kita Batch API
  slug: kita-batch-api
- description: Borrower message thread.
  name: Kita Conversation API
  slug: kita-conversation-api
- description: Deterministic credit picture — spread, adjustments, policy decision.
  name: Kita Credit API
  slug: kita-credit-api
- description: Borrower document upload and extraction.
  name: Kita Documents API
  slug: kita-documents-api
- description: PDF and XLSX exports.
  name: Kita Exports API
  slug: kita-exports-api
- description: Group documents into containers.
  name: Kita Folders API
  slug: kita-folders-api
- description: Cited credit memo synthesis and retrieval.
  name: Kita Memo API
  slug: kita-memo-api
- description: Submit documents for extraction.
  name: Kita Processing API
  slug: kita-processing-api
- description: Retrieve extraction results, summaries and exports.
  name: Kita Results API
  slug: kita-results-api
- description: Custom extraction schemas.
  name: Kita Schemas API
  slug: kita-schemas-api
- description: Plain-text document transcripts.
  name: Kita Transcripts API
  slug: kita-transcripts-api
- description: Cross-document verification checks.
  name: Kita Verification API
  slug: kita-verification-api
- description: Register and manage HMAC-signed outbound webhooks.
  name: Kita Webhooks API
  slug: kita-webhooks-api
artifact_total: 52
asyncapis:
- description: ''
  name: Kita Capture Webhooks
  slug: kita-capture-webhooks
collections:
- collection_type: postman
  name: Kita Capture Applications API
  slug: postman-kita-applications-api
- collection_type: postman
  name: Kita Capture Applications Batch API
  slug: postman-kita-batch-api
- collection_type: postman
  name: Kita Capture Applications Conversation API
  slug: postman-kita-conversation-api
- collection_type: postman
  name: Kita Capture Applications Credit API
  slug: postman-kita-credit-api
- collection_type: postman
  name: Kita Capture Applications Documents API
  slug: postman-kita-documents-api
- collection_type: postman
  name: Kita Capture Applications Exports API
  slug: postman-kita-exports-api
- collection_type: postman
  name: Kita Capture Applications Folders API
  slug: postman-kita-folders-api
- collection_type: postman
  name: Kita Capture Applications Memo API
  slug: postman-kita-memo-api
- collection_type: postman
  name: Kita Capture Applications Processing API
  slug: postman-kita-processing-api
- collection_type: postman
  name: Kita Capture Applications Results API
  slug: postman-kita-results-api
- collection_type: postman
  name: Kita Capture Applications Schemas API
  slug: postman-kita-schemas-api
- collection_type: postman
  name: Kita Capture Applications Transcripts API
  slug: postman-kita-transcripts-api
- collection_type: postman
  name: Kita Capture Applications Verification API
  slug: postman-kita-verification-api
- collection_type: postman
  name: Kita Capture Applications Webhooks API
  slug: postman-kita-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kita Capture Applications API
  slug: open-kita-applications-api
- collection_type: open
  name: Kita Capture Applications Batch API
  slug: open-kita-batch-api
- collection_type: open
  name: Kita Capture Applications Conversation API
  slug: open-kita-conversation-api
- collection_type: open
  name: Kita Capture Applications Credit API
  slug: open-kita-credit-api
- collection_type: open
  name: Kita Capture Applications Documents API
  slug: open-kita-documents-api
- collection_type: open
  name: Kita Capture Applications Exports API
  slug: open-kita-exports-api
- collection_type: open
  name: Kita Capture Applications Folders API
  slug: open-kita-folders-api
- collection_type: open
  name: Kita Capture Applications Memo API
  slug: open-kita-memo-api
- collection_type: open
  name: Kita Capture Applications Processing API
  slug: open-kita-processing-api
- collection_type: open
  name: Kita Capture Applications Results API
  slug: open-kita-results-api
- collection_type: open
  name: Kita Capture Applications Schemas API
  slug: open-kita-schemas-api
- collection_type: open
  name: Kita Capture Applications Transcripts API
  slug: open-kita-transcripts-api
- collection_type: open
  name: Kita Capture Applications Verification API
  slug: open-kita-verification-api
- collection_type: open
  name: Kita Capture Applications Webhooks API
  slug: open-kita-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kita-capture-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kita/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kita.ai/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://www.kita.ai/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.kita.ai/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kita.ai/documentation
- group: company
  title: ''
  type: Website
  url: https://www.kita.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.kita.ai/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@kita.ai
- group: start
  title: ''
  type: SignUp
  url: https://portal.usekita.com/
- group: start
  title: ''
  type: Login
  url: https://portal.usekita.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kita.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kita.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kita.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kita-Technologies
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Kita-Technologies/kita-api-examples
- group: auth
  title: ''
  type: Security
  url: https://www.kita.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.kita.ai/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kita-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://demo.kita.ai/
- group: build
  title: ''
  type: Packages
  url: packages/kita-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kita-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kita-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kita-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kita-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kita-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kita-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kita-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kita-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kita-plans.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kita-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kita-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kita-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kita-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/kita-examples.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kita-capture-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kita-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kita-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kita-trust-center.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kita-agentic-access.yml
created: '2026-07-17'
description: Kita is an AI-native loan origination and underwriting company (Y Combinator W26, San Francisco) building document intelligence and credit decisioning for lenders in emerging and undertapped markets. Kita ships two developer-facing APIs. Kita Capture is a document-intelligence API that turns scanned or photographed bank statements, payslips, government IDs, credit reports, tax filings and 30+ other document types into structured, validated, fraud-checked JSON, with cross-document verification, batch processing, custom extraction schemas and HMAC-signed webhooks. Kita Underwriter is a credit-file API that creates loan applications, ingests borrower documents, computes a deterministic credit picture (adjusted EBITDA, DSCR, margins, debt-to-worth, sensitivity and a policy-engine decision produced by a versioned calculation engine rather than an LLM) and synthesizes a cited credit memo. The platform is region-pinned across Singapore and Mexico deployments and is used by microfinance
  institutions, SME lenders, CDFIs and community banks across Southeast Asia, Latin America and the United States.
image: https://www.kita.ai/kita_logo_green.png
layout: provider
mcp_servers:
- description: ''
  name: Kita MCP Server
  slug: kita-mcp-server
modified: '2026-07-19'
name: Kita
nav: Providers
network: true
overview: 'Kita publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Batch API, Conversation API, and 11 more. Tagged areas include Company, Fintech, Lending, Underwriting, and Credit Scoring.


  The Kita catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kita''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, pricing, and 34 more developer resources.'
plans:
- name: Kita Plans
  plan_count: 3
  slug: kita-plans
random_paper: 5
rate_limits:
- limit_count: 0
  name: Kita Rate Limits
  slug: kita-rate-limits
score:
  band: exemplar
  composite: 69.3
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 16.7
    contract_quality: 68.9
    developer_ergonomics: 78.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 21.1
  previous_composite: 69.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kita/refs/heads/main/screenshots/kita-2026-07-25T223855.png
security:
- kind: authentication
  name: Kita Authentication
  slug: kita-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Kita Domain Security
  slug: kita-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kita Vulnerability Disclosure
  slug: kita-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Kita Trust Center
  slug: kita-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: kita
tags:
- Company
- Fintech
- Lending
- Underwriting
- Credit Scoring
- Document Intelligence
- Document Extraction
- Fraud Detection
- Artificial Intelligence
- Computer-Vision
- Emerging Markets
- Loan Origination
website: https://www.kita.ai/
---
