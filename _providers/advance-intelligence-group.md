---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: Obtain an access token for calling the Open API.
  name: Advance Intelligence Group Authentication API
  slug: advance-intelligence-group-authentication-api
- description: Global document verification (SDK auth-license + result query).
  name: Advance Intelligence Group Document Verification API
  slug: advance-intelligence-group-document-verification-api
- description: Face comparison and biometric matching.
  name: Advance Intelligence Group Face Recognition API
  slug: advance-intelligence-group-face-recognition-api
- description: Optical character recognition for identity documents.
  name: Advance Intelligence Group OCR API
  slug: advance-intelligence-group-ocr-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ADVANCE.AI Open Authentication API
  slug: open-advance-intelligence-group-authentication-api
- collection_type: open
  name: ADVANCE.AI Open Authentication Document Verification API
  slug: open-advance-intelligence-group-document-verification-api
- collection_type: open
  name: ADVANCE.AI Open Authentication Face Recognition API
  slug: open-advance-intelligence-group-face-recognition-api
- collection_type: open
  name: ADVANCE.AI Open Authentication OCR API
  slug: open-advance-intelligence-group-ocr-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/advance-intelligence-group-advance-ai-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advance-intelligence-group-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://doc.advance.ai/
- group: company
  title: ''
  type: Website
  url: https://advance.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.advance.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://doc.advance.ai/global_document_verification.html
- group: operate
  title: ''
  type: Support
  url: https://support.advance.ai/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://advance.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://advance.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://advance.ai/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://advance.ai/security-compliance/
- group: auth
  title: ''
  type: Authentication
  url: authentication/advance-intelligence-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/advance-intelligence-group-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/advance-intelligence-group-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/advance-intelligence-group-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/advance-intelligence-group-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/advance-intelligence-group-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/advance-intelligence-group-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/advance-intelligence-group-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advance-intelligence-group-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/advance-intelligence-group-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Advance Intelligence Group is an AI-driven technology company headquartered in Singapore, founded in 2016 and backed by SoftBank Vision Fund, Warburg Pincus and others. It operates three core business lines: ADVANCE.AI (Southeast Asia''s leading provider of digital identity verification, KYC/KYB, AML, compliance and risk-management solutions, serving 500+ enterprise clients), Atome Financial (buy-now-pay-later and digital lending) and Ginee (e-commerce enablement). The ADVANCE.AI business unit exposes a public Open API for eKYC — token authentication, global document verification, OCR field extraction, face comparison and liveness detection — used across banking, fintech, payments, retail and e-commerce in emerging markets. This API Evangelist profile was enriched from the public developer documentation at doc.advance.ai.'
image: https://advance.ai/wp-content/uploads/2025/09/top-header-right-image.webp
layout: provider
mcp_servers:
- description: ''
  name: advance-intelligence-group-mcp.yml
  slug: advance-intelligence-group-mcpyml
modified: '2026-07-17'
name: Advance Intelligence Group
nav: Providers
network: true
overview: 'Advance Intelligence Group publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Document Verification API, Face Recognition API, and 1 more. Tagged areas include Company, Fintech, Identity Verification, KYC, and AML.


  Advance Intelligence Group''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 42.2
  delta: 0.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 30.3
    contract_quality: 55.1
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 0.0
  previous_composite: 41.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/advance-intelligence-group/refs/heads/main/screenshots/advance-intelligence-group-2026-07-25T181711.png
security:
- kind: authentication
  name: Advance Intelligence Group Authentication
  slug: advance-intelligence-group-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Advance Intelligence Group Domain Security
  slug: advance-intelligence-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: advance-intelligence-group
tags:
- Company
- Fintech
- Identity Verification
- KYC
- AML
- Face Recognition
- OCR
- Artificial Intelligence
- Risk Management
- Singapore
website: https://advance.ai/
---
