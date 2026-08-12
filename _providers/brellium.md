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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Brellium Agentic Access
  operation_count: 17
  slug: brellium-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 9
apis:
- description: The Audits API from Brellium — 2 operation(s) for audits.
  name: Brellium Audits API
  slug: brellium-audits-api
- description: The Auth API from Brellium — 1 operation(s) for auth.
  name: Brellium Auth API
  slug: brellium-auth-api
- description: The Coding API from Brellium — 2 operation(s) for coding.
  name: Brellium Coding API
  slug: brellium-coding-api
- description: The Documents API from Brellium — 3 operation(s) for documents.
  name: Brellium Documents API
  slug: brellium-documents-api
- description: The Documents Multiple API from Brellium — 1 operation(s) for documents multiple.
  name: Brellium Documents Multiple API
  slug: brellium-documents-multiple-api
- description: The Link Providers API from Brellium — 1 operation(s) for link providers.
  name: Brellium Link Providers API
  slug: brellium-link-providers-api
- description: The Question Sets API from Brellium — 1 operation(s) for question sets.
  name: Brellium Question Sets API
  slug: brellium-question-sets-api
- description: The Update Audits Flags API from Brellium — 1 operation(s) for update audits flags.
  name: Brellium Update Audits Flags API
  slug: brellium-update-audits-flags-api
- description: The Users API from Brellium — 2 operation(s) for users.
  name: Brellium Users API
  slug: brellium-users-api
artifact_total: 15
asyncapis:
- description: ''
  name: Brellium Webhooks
  slug: brellium-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brellium-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brellium-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brellium-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brellium-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brellium-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brellium-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brellium-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brellium-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brellium-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.brellium.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/brellium-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brellium-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brellium-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/brellium-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/brellium-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://brellium-ai.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://brellium-ai.readme.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://brellium-ai.readme.io/reference/post_auth
- group: start
  title: ''
  type: GettingStarted
  url: https://brellium-ai.readme.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.brellium.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@brellium.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brellium.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brellium.com/privacy-policy
created: '2026-07-17'
description: Brellium is an AI-powered clinical compliance platform for healthcare organizations. Its clinical AI audits 100% of a provider's clinical documentation and medical coding across every patient visit, checking notes against payor, clinical-quality, and billing requirements to catch compliance risks before they become clawbacks and to surface earned-but-unbilled revenue. It flags issues such as inaccurate MDM/E&M coding, cloned notes, and inconsistent session lengths, and gives clinical teams instant correction guidance. Brellium serves tech-enabled clinics, behavioral health, ABA, hospice, and digital-health providers, and exposes a REST API so platforms can embed chart-review and coding audits directly into their EMR or telehealth workflows.
image: https://brellium.com/og-image.png?v=3
layout: provider
mcp_servers:
- description: ''
  name: brellium-mcp.yml
  slug: brellium-mcpyml
modified: '2026-07-18'
name: Brellium
nav: Providers
network: true
overview: 'Brellium publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Audits API, Auth API, Coding API, and 6 more. Tagged areas include Company, Healthcare, Clinical Compliance, Clinical Documentation, and Medical Coding.


  The Brellium catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Brellium''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, support, and 17 more developer resources.'
random_paper: 48
score:
  band: developing
  composite: 45.1
  delta: -0.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 56.8
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brellium/refs/heads/main/screenshots/brellium-2026-07-25T203751.png
security:
- kind: authentication
  name: Brellium Authentication
  slug: brellium-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brellium Domain Security
  slug: brellium-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Brellium Trust Center
  slug: brellium-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, HIPAA
slug: brellium
tags:
- Company
- Healthcare
- Clinical Compliance
- Clinical Documentation
- Medical Coding
- Audit
- Behavioral Health
- Digital Health
- API
website: https://brellium-ai.readme.io/
---
