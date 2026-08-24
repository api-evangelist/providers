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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Smile Identity Agentic Access
  operation_count: 15
  slug: smile-identity-agentic-access
  summary_line: 15 operations · 10 acting
api_count: 12
apis:
- description: The Authentication API from Smile Identity — 1 operation(s) for authentication.
  name: Smile Identity Authentication API
  slug: smile-identity-authentication-api
- description: The Biometric Authentication API from Smile Identity — 1 operation(s) for biometric authentication.
  name: Smile Identity Biometric Authentication API
  slug: smile-identity-biometric-authentication-api
- description: The Biometric Enrollment API from Smile Identity — 1 operation(s) for biometric enrollment.
  name: Smile Identity Biometric Enrollment API
  slug: smile-identity-biometric-enrollment-api
- description: The Biometric KYC API from Smile Identity — 1 operation(s) for biometric kyc.
  name: Smile Identity Biometric KYC API
  slug: smile-identity-biometric-kyc-api
- description: The Callback Replay API from Smile Identity — 1 operation(s) for callback replay.
  name: Smile Identity Callback Replay API
  slug: smile-identity-callback-replay-api
- description: The Document Verification API from Smile Identity — 1 operation(s) for document verification.
  name: Smile Identity Document Verification API
  slug: smile-identity-document-verification-api
- description: The Enhanced Document Verification API from Smile Identity — 1 operation(s) for enhanced document verification.
  name: Smile Identity Enhanced Document Verification API
  slug: smile-identity-enhanced-document-verification-api
- description: The Enhanced KYC API from Smile Identity — 1 operation(s) for enhanced kyc.
  name: Smile Identity Enhanced KYC API
  slug: smile-identity-enhanced-kyc-api
- description: The Services API from Smile Identity — 4 operation(s) for services.
  name: Smile Identity Services API
  slug: smile-identity-services-api
- description: The Smart Selfie Compare API from Smile Identity — 1 operation(s) for smart selfie compare.
  name: Smile Identity Smart Selfie Compare API
  slug: smile-identity-smart-selfie-compare-api
- description: The Users API from Smile Identity — 1 operation(s) for users.
  name: Smile Identity Users API
  slug: smile-identity-users-api
- description: The Verification Status API from Smile Identity — 1 operation(s) for verification status.
  name: Smile Identity Verification Status API
  slug: smile-identity-verification-status-api
artifact_total: 30
asyncapis:
- description: ''
  name: Smile Identity Verification Webhooks
  slug: smile-identity-verification-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smile ID V3 Authentication API
  slug: open-smile-identity-authentication-api
- collection_type: open
  name: Smile ID V3 Authentication Biometric Authentication API
  slug: open-smile-identity-biometric-authentication-api
- collection_type: open
  name: Smile ID V3 Authentication Biometric Enrollment API
  slug: open-smile-identity-biometric-enrollment-api
- collection_type: open
  name: Smile ID V3 Authentication Biometric KYC API
  slug: open-smile-identity-biometric-kyc-api
- collection_type: open
  name: Smile ID V3 Authentication Callback Replay API
  slug: open-smile-identity-callback-replay-api
- collection_type: open
  name: Smile ID V3 Authentication Document Verification API
  slug: open-smile-identity-document-verification-api
- collection_type: open
  name: Smile ID V3 Authentication Enhanced Document Verification API
  slug: open-smile-identity-enhanced-document-verification-api
- collection_type: open
  name: Smile ID V3 Authentication Enhanced KYC API
  slug: open-smile-identity-enhanced-kyc-api
- collection_type: open
  name: Smile ID V3 Authentication Services API
  slug: open-smile-identity-services-api
- collection_type: open
  name: Smile ID V3 Authentication Smart Selfie Compare API
  slug: open-smile-identity-smart-selfie-compare-api
- collection_type: open
  name: Smile ID V3 Authentication Users API
  slug: open-smile-identity-users-api
- collection_type: open
  name: Smile ID V3 Authentication Verification Status API
  slug: open-smile-identity-verification-status-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/smile-identity-v3-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smile-identity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usesmileid.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.usesmileid.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usesmileid.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usesmileid.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usesmileid.com/getting-started/run-your-first-test-job
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smileidentity
- group: company
  title: ''
  type: Blog
  url: https://usesmileid.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://portal.usesmileid.com
- group: commercial
  title: ''
  type: Pricing
  url: https://usesmileid.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usesmileid.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usesmileid.com/legal/terms-and-conditions
- group: build
  title: ''
  type: Postman
  url: https://docs.usesmileid.com/integration-options/rest-api/postman-collections
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.usesmileid.com/developer-resources/overview/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smile-identity-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/smile-identity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/smile-identity-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smile-identity-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/smile-identity-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/smile-identity-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smile-identity-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/smile-identity-verification-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/smile-identity-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/smile-identity-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/smile-identity-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/smile-identity-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/smile-identity-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/smile-identity-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smile-identity-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Smile Identity (Smile ID) is Africa's leading digital identity verification, fraud detection, AML and KYC/KYB compliance platform. Its V3 REST API and v12 mobile/web SDKs let businesses onboard and authenticate users across all 54 African countries and beyond, covering thousands of ID types and documents. Products include Biometric KYC, Document Verification, Enhanced Document Verification, Basic and Enhanced KYC, Business Verification (KYB), SmartSelfie registration/authentication/compare, phone and address verification, and AML monitoring. Verifications run against government and institutional data sources, with passive/active liveness, and results delivered synchronously and via asynchronous callback webhooks.
image: https://cdn.prod.website-files.com/69cecfcd51ce55fce000c092/6a198a55c9d40279f94b33a4_Smile-Favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Smile Identity MCP Server
  slug: smile-identity-mcp-server
modified: '2026-07-21'
name: Smile Identity
nav: Providers
network: true
overview: 'Smile Identity publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Biometric Authentication API, Biometric Enrollment API, and 9 more. Tagged areas include Company, Identity Verification, KYC, KYB, and Biometrics.


  The Smile Identity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Smile Identity''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, pricing, changelog, and 24 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 46.9
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 16.7
    contract_quality: 65.9
    developer_ergonomics: 47.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smile-identity/refs/heads/main/screenshots/smile-identity-2026-08-17T081942.png
security:
- kind: authentication
  name: Smile Identity Authentication
  slug: smile-identity-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Smile Identity Domain Security
  slug: smile-identity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smile-identity
tags:
- Company
- Identity Verification
- KYC
- KYB
- Biometrics
- Liveness Detection
- Document Verification
- AML
- Fraud Prevention
- Compliance
- Onboarding
- Africa
website: https://usesmileid.com
---
