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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Ingest user actions and objects into per-workflow namespaces and asynchronously receive AI agent decisions (labels, risk scores, enforcement actions) via signed webhooks.
  name: SafetyKit Data API
  slug: safetykit-data-api
artifact_total: 6
asyncapis:
- description: ''
  name: Safetykit Webhooks
  slug: safetykit-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/safetykit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/safetykit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.safetykit.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.safetykit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.safetykit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.safetykit.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.safetykit.com/using-data-api/copy-and-paste-quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:support@safetykit.com
- group: company
  title: ''
  type: Blog
  url: https://safetykit.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetSafetyKit
- group: start
  title: ''
  type: SignUp
  url: https://app.safetykit.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.safetykit.com/msa_2024-03-25.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.safetykit.com/privacy.pdf
- group: auth
  title: ''
  type: Compliance
  url: security/safetykit-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: http://www.safetykitstatus.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/safetykit-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/safetykit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/safetykit-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/safetykit-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/safetykit-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/safetykit-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/safetykit-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/safetykit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/safetykit-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/safetykit-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/safetykit-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/safetykit-llms.txt
created: '2026-07-17'
description: SafetyKit is an AI trust, safety, and fraud-detection platform that lets marketplaces, fintechs, and social and creator platforms deploy AI agents to automate risk reviews, onboarding, and investigations. Its Data API ingests every user action and object through a lightweight SDK and API, organizes them into per-workflow namespaces, and asynchronously returns agent decisions — labels, risk scores, and enforcement actions such as account suspension — delivered back over signed webhooks. SafetyKit detects account takeover, multi-accounting, fake accounts, phishing, spam, harmful content, scams, and prohibited listings, and is used by companies including Upwork, Etsy, Eventbrite, Lyft, Discord, and Kickstarter.
image: https://cdn.prod.website-files.com/67f043481889440b9d0ed13e/67f043481889440b9d0ed170_a5826400373f60a9d521bc5bca8ad3f3_OG%20Image.jpg
layout: provider
mcp_servers:
- description: ''
  name: SafetyKit MCP Server
  slug: safetykit-mcp-server
modified: '2026-07-21'
name: SafetyKit
nav: Providers
network: true
overview: 'SafetyKit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Trust and Safety, Fraud Detection, and Content Moderation.


  The SafetyKit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SafetyKit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 47.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/safetykit/refs/heads/main/screenshots/safetykit-2026-08-17T081707.png
security:
- kind: authentication
  name: Safetykit Authentication
  slug: safetykit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Safetykit Domain Security
  slug: safetykit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Safetykit Trust Center
  slug: safetykit-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: safetykit
tags:
- Company
- Artificial Intelligence
- Trust and Safety
- Fraud Detection
- Content Moderation
- Risk
- AI Agents
- Compliance
website: https://www.safetykit.com
---
