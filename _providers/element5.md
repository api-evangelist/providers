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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Element5 Agentic Access
  operation_count: 8
  slug: element5-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 3
apis:
- description: Authorization related APIs
  name: Element5 Authorization API
  slug: element5-authorization-api
- description: Eligibility related APIs
  name: Element5 Eligibility API
  slug: element5-eligibility-api
- description: Object Store related APIs
  name: Element5 Object Store API
  slug: element5-object-store-api
arazzos:
- description: Upload a supporting file object, submit a prior-authorization request, then poll status.
  name: Element5 — Upload document and submit authorization
  slug: element5-submit-authorization
- description: Submit an eligibility request and poll until the task succeeds or fails.
  name: Element5 — Verify eligibility and await result
  slug: element5-verify-eligibility
artifact_total: 10
asyncapis:
- description: ''
  name: Element5 Webhooks
  slug: element5-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/element5-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/element5-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/element5-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/element5-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/element5-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/element5-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/element5-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/element5-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/element5-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/element5-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/element5-openapi-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/element5-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/element5-data-model.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/element5-verify-eligibility.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/element5-submit-authorization.yml
- group: company
  title: ''
  type: Website
  url: https://www.e5.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-doc.e5.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api-doc.e5.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api-doc.e5.ai/
- group: start
  title: ''
  type: Login
  url: https://app.e5.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.e5.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:apisupport@e5.ai
- group: auth
  title: ''
  type: Compliance
  url: https://www.e5.ai/security
created: '2026-07-17'
description: Element5 is a post-acute healthcare workflow automation platform that uses coordinated AI agents (Neos) to automate revenue cycle management (RCM) and back-office operations for home health, hospice, and palliative care providers. Its platform automates eligibility and benefit verification, prior authorization submission, claims processing, denials management, remittance and collections, and audit/compliance workflows, escalating only exceptions to human agents. Element5 exposes a public workflow API (Element5 API v2.2.0) protected by API keys that lets clients submit authorization and eligibility requests, process X12 270/271 eligibility transactions, upload and fetch file objects, and monitor long-running tasks via polling or webhook callbacks. The company is backed by Insight Partners and serves the post-acute care sector.
image: https://cdn.prod.website-files.com/658c60c4ff902effa2174f77/668c43e2bfb9956a2995b419_e5-logo-gradient.png
layout: provider
mcp_servers:
- description: ''
  name: element5-mcp.yml
  slug: element5-mcpyml
modified: '2026-07-19'
name: Element5
nav: Providers
network: true
overview: 'Element5 publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authorization API, Eligibility API, and Object Store API. Tagged areas include Company, Healthcare, Revenue Cycle Management, Post-Acute Care, and Workflow Automation.


  The Element5 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Element5''s developer surface includes authentication, sandbox, documentation, API reference, support, and 19 more developer resources.'
random_paper: 79
score:
  band: developing
  composite: 43.9
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 72.1
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/element5/refs/heads/main/screenshots/element5-2026-07-25T213120.png
security:
- kind: authentication
  name: Element5 Authentication
  slug: element5-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Element5 Domain Security
  slug: element5-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: element5
tags:
- Company
- Healthcare
- Revenue Cycle Management
- Post-Acute Care
- Workflow Automation
- Eligibility Verification
- Prior Authorization
- Claims Processing
- Webhooks
- Artificial Intelligence
website: https://www.e5.ai/
---
