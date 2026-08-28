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
    agent_card: flavored
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: The Consent API from Inth — 1 operation(s) for consent.
  name: Inth Consent API
  slug: inth-consent-api
- description: The Init API from Inth — 1 operation(s) for init.
  name: Inth Init API
  slug: inth-init-api
- description: The Legal Documents API from Inth — 1 operation(s) for legal documents.
  name: Inth Legal Documents API
  slug: inth-legal-documents-api
- description: The Status API from Inth — 2 operation(s) for status.
  name: Inth Status API
  slug: inth-status-api
- description: The Subjects API from Inth — 2 operation(s) for subjects.
  name: Inth Subjects API
  slug: inth-subjects-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: c15t Backend Consent API
  slug: open-inth-consent-api
- collection_type: open
  name: c15t Backend Consent Init API
  slug: open-inth-init-api
- collection_type: open
  name: c15t Backend Consent Legal Documents API
  slug: open-inth-legal-documents-api
- collection_type: open
  name: c15t Backend Consent Status API
  slug: open-inth-status-api
- collection_type: open
  name: c15t Backend Consent Subjects API
  slug: open-inth-subjects-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/inth-c15t-consent-api-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/inth-a2a.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inth-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://c15t.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://c15t.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://c15t.com/docs/self-host
- group: start
  title: ''
  type: Quickstart
  url: https://c15t.com/docs/frameworks/react/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/c15t
- group: commercial
  title: ''
  type: Pricing
  url: https://inth.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://inth.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://inth.com/dashboard/sign-up
- group: operate
  title: ''
  type: Support
  url: https://github.com/c15t/c15t/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://c15t.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inth.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/inth-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/inth-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/inth-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/inth-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/inth-cli.yml
- group: design
  title: ''
  type: Components
  url: components/inth-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/inth-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inth-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/inth-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/inth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/inth-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/inth-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/inth-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/inth-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/inth-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/inth-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/inth-sandbox.yml
created: '2026-07-17'
description: Inth is a San Francisco, Y Combinator-backed company building enterprise privacy governance for teams that ship fast, making consent programmable, observable, and compliant by default. Its foundation is c15t (github.com/c15t), an open-source, developer-first consent management platform with 3M+ npm downloads used by teams like Zed, Expo, Infisical, and Unkey. c15t provides a headless, composable cookie banner, consent manager, and preference center for JavaScript, React, and Next.js, plus a self-hostable consent backend and REST API (@c15t/backend) that also runs as the inth.com managed service. It supports GDPR, CCPA, LGPD, IAB TCF 2.3, Google Consent Mode v2, and Global Privacy Control, with regional policy packs, audit-ready consent records, script and iframe gating, and first-party SDKs and CLI.
image: https://inth.com/opengraph-image.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface for the c15t consent backend, one tool per REST operation. c15t currently provides agent integration via a packaged Agent Skill (see skills/inth-c15t.md), not an MCP server.
  name: Inth MCP Server
  slug: inth-mcp-server
modified: '2026-07-19'
name: Inth
nav: Providers
network: true
overview: 'Inth publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Consent API, Init API, Legal Documents API, and 2 more. Tagged areas include Company, Consent Management, Privacy, Cookie Consent, and GDPR.


  Inth''s developer surface includes documentation, API reference, quickstart, pricing, engineering blog, signup flow, support, and 25 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 53.9
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 30.3
    contract_quality: 52.8
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 53.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inth/refs/heads/main/screenshots/inth-2026-07-25T222721.png
security:
- kind: authentication
  name: Inth Authentication
  slug: inth-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Inth Domain Security
  slug: inth-domain-security
  summary_line: TLSv1.3 · HSTS
slug: inth
tags:
- Company
- Consent Management
- Privacy
- Cookie Consent
- GDPR
- CCPA
- Compliance
- Consent
- Developer Tools
- Open-Source
website: https://c15t.com/docs
---
