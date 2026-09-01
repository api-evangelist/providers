---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 26.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Databook Agentic Access
  operation_count: 8
  slug: databook-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- description: The batch - create API from Databook — 3 operation(s) for batch - create.
  name: Databook batch - create API
  slug: databook-batch-create-api
- description: The batch - query API from Databook — 3 operation(s) for batch - query.
  name: Databook batch - query API
  slug: databook-batch-query-api
- description: The chat API from Databook — 1 operation(s) for chat.
  name: Databook Chat API
  slug: databook-chat-api
- description: The reasoning API from Databook — 1 operation(s) for reasoning.
  name: Databook Reasoning API
  slug: databook-reasoning-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://databook.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.databook.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.databook.com/redoc
- group: docs
  title: ''
  type: APIReference
  url: https://api.databook.com/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://api.databook.com/redoc#section/Getting-started
- group: company
  title: ''
  type: Blog
  url: https://databook.com/resources
- group: operate
  title: ''
  type: Support
  url: https://databook.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://databook.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://databook.com/privacy
- group: start
  title: ''
  type: Login
  url: https://chat.databook.com
- group: auth
  title: ''
  type: Security
  url: https://databook.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://databook.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.databook.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/databook-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/databook-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/databook-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/databook-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/databook-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/databook-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/databook-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/databook-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/databook-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/databook-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/databook-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/databook-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/databook-openapi-overlay.yaml
created: '2026-07-17'
description: 'Databook is an AI-powered decision system for enterprise sales teams, combining verified market intelligence with structured reasoning to give sellers visibility into their largest deals. The platform pairs an "Outside-In Radar" of signals beyond the CRM with an advanced reasoning engine, a dynamic Customer Context Graph modeling every buying group, guided sales agents tuned to specific KPIs, a CRO dashboard for leadership, and a Value Coach for executive narratives. It serves enterprise revenue organizations across cloud, cybersecurity, managed services, and software. Databook is a portfolio company of Bessemer Venture Partners and Threshold Ventures. It publishes a machine-readable REST API — the DatabookAI REST API, OpenAPI 3.1.0 at https://api.databook.com/openapi.json — exposing a catalog of 66 account-research insights, asynchronous CSV batch jobs that run those insights across many target accounts, a threaded chat endpoint, and a deep-reasoning endpoint that returns
  cited, structured analysis. Access is not self-serve: bearer tokens are provisioned by Databook support.'
image: https://storage.googleapis.com/gpt-engineer-file-uploads/rfjG12z2plW0k4X3iSgJgycEVfj1/social-images/social-1779217719891-Databook_Preview_Home.webp
layout: provider
modified: '2026-08-13'
name: Databook
nav: Providers
network: true
overview: 'Databook publishes 4 APIs on the [APIs.io](https://apis.io/) network, including batch - create API, batch - query API, Chat API, and 1 more. Tagged areas include Company, Vertical Software, Sales Intelligence, Account Intelligence, and Sales Enablement.


  Databook''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 21 more developer resources.'
plans:
- name: Databook Plans Pricing
  plan_count: 0
  slug: databook-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Databook Rate Limits
  slug: databook-rate-limits
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/databook/refs/heads/main/screenshots/databook-2026-07-25T211258.png
security:
- kind: authentication
  name: Databook Authentication
  slug: databook-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Databook Domain Security
  slug: databook-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Databook Vulnerability Disclosure
  slug: databook-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Databook Trust Center
  slug: databook-trust-center
  summary_line: SOC 2 Type 2, NIST 800-171, GDPR, CCPA
slug: databook
tags:
- Company
- Vertical Software
- Sales Intelligence
- Account Intelligence
- Sales Enablement
- Enterprise Sales
- Artificial Intelligence
- Revenue Operations
- REST API
- OpenAPI
- Batch Processing
- Agents
- Reasoning
- Company Data
website: https://databook.com/
---
