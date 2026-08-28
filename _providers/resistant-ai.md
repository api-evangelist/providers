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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Resistant Ai Agentic Access
  operation_count: 19
  slug: resistant-ai-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 2
apis:
- description: The Submission API from Resistant AI — 10 operation(s) for submission.
  name: Resistant AI Submission API
  slug: resistant-ai-submission-api
- description: The Tenants API from Resistant AI — 4 operation(s) for tenants.
  name: Resistant AI Tenants API
  slug: resistant-ai-tenants-api
artifact_total: 13
asyncapis:
- description: ''
  name: Resistant Ai Documents Webhooks
  slug: resistant-ai-documents-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Resistant Documents Submission API
  slug: open-resistant-ai-submission-api
- collection_type: open
  name: Resistant Documents Submission Tenants API
  slug: open-resistant-ai-tenants-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/resistant-ai-documents-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://resistant.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.resistant.ai
- group: docs
  title: ''
  type: Documentation
  url: https://developers.resistant.ai
- group: docs
  title: ''
  type: APIReference
  url: https://developers.resistant.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.resistant.ai/getting-started/about
- group: start
  title: ''
  type: Quickstart
  url: https://developers.resistant.ai/getting-started/quickstart-api
- group: operate
  title: ''
  type: Support
  url: https://developers.resistant.ai/support/contact-support
- group: company
  title: ''
  type: Blog
  url: https://resistant.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://resistant.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://resistantai.statuspage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.resistant.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/resistant-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/resistant-ai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/resistant-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/resistant-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/resistant-ai-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/resistant-ai-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/resistant-ai-documents-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/resistant-ai-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/resistant-ai-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/resistant-ai-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/resistant-ai-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/resistant-ai-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/resistant-ai-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/resistant-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/resistant-ai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resistant-ai-domain-security.yml
created: '2026-07-17'
description: Resistant AI protects financial-services organizations from fraud and financial crime with AI. Its Documents product detects fake, tampered, forged, and AI-generated documents (PDFs and images) in seconds, and its Transactions product layers 80+ AI models over existing transaction-monitoring systems for AML and fraud detection. The Resistant Documents API provides programmatic document forensics — fraud, quality, classification, content extraction, and Adaptive Decision — through an OAuth2 create/upload/poll workflow across regional cells, with polling, Amazon SQS, and Svix webhook result delivery, plus a Tenant Management API for provisioning tenants and applications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/resistant-ai.png
layout: provider
mcp_servers:
- description: ''
  name: Resistant AI MCP Server
  slug: resistant-ai-mcp-server
modified: '2026-07-20'
name: Resistant AI
nav: Providers
network: true
overview: 'Resistant AI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Submission API and Tenants API. Tagged areas include Company, Artificial Intelligence, Fraud Detection, Financial Crime, and Document Verification.


  The Resistant AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Resistant AI''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, authentication, and 22 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 0
  name: Resistant Ai Rate Limits
  slug: resistant-ai-rate-limits
scopes:
- name: Resistant Ai Scopes
  scope_count: 2
  slug: resistant-ai-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 63.4
    developer_ergonomics: 66.1
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/resistant-ai/refs/heads/main/screenshots/resistant-ai-2026-08-17T081532.png
security:
- kind: authentication
  name: Resistant Ai Authentication
  slug: resistant-ai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Resistant Ai Domain Security
  slug: resistant-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Resistant Ai Trust Center
  slug: resistant-ai-trust-center
  summary_line: trust center published
slug: resistant-ai
tags:
- Company
- Artificial Intelligence
- Fraud Detection
- Financial Crime
- Document Verification
- Document Forensics
- AML
- Identity Verification
- Fintech
- Machine-Learning
website: https://resistant.ai
---
