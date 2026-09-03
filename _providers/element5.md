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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Element5 Agentic Access
  operation_count: 8
  slug: element5-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.e5.ai
  baseurl_source: declared
  description: Authorization related APIs
  name: Element5 Authorization API
  slug: element5-authorization-api
- baseURL: https://api.e5.ai
  baseurl_source: declared
  description: Eligibility related APIs
  name: Element5 Eligibility API
  slug: element5-eligibility-api
- baseURL: https://api.e5.ai
  baseurl_source: declared
  description: Object Store related APIs
  name: Element5 Object Store API
  slug: element5-object-store-api
- baseURL: https://api.e5.ai
  baseurl_source: declared
  description: Generic E5 Task related APIs and Webhooks
  name: Element5 Automation API
  slug: element5-automation-api
arazzos:
- description: Upload a supporting file object, submit a prior-authorization request, then poll status.
  name: Element5 — Upload document and submit authorization
  slug: element5-submit-authorization
- description: Submit an eligibility request and poll until the task succeeds or fails.
  name: Element5 — Verify eligibility and await result
  slug: element5-verify-eligibility
artifact_total: 14
asyncapis:
- description: ''
  name: Element5 Webhooks
  slug: element5-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Element5 Authorization API
  slug: open-element5-authorization-api
- collection_type: open
  name: Element5 Authorization Eligibility API
  slug: open-element5-eligibility-api
- collection_type: open
  name: Element5 Authorization Object Store API
  slug: open-element5-object-store-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/element5-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Element5
nav: Providers
network: true
overview: 'Element5 publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Eligibility API, Object Store API, and 1 more. Tagged areas include Company, Healthcare, Revenue Cycle Management, Post-Acute Care, and Workflow-Automation.


  The Element5 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Element5''s developer surface includes authentication, sandbox, documentation, API reference, support, and 20 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 62.2
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Workflow-Automation
- Eligibility Verification
- Prior Authorization
- Claims Processing
- Webhook
- Artificial Intelligence
website: https://www.e5.ai/
---
