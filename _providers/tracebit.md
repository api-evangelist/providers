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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
  score: 25.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Alerts API from Tracebit — 2 operation(s) for alerts.
  name: Tracebit Alerts API
  slug: tracebit-alerts-api
- description: The Canary Credentials API from Tracebit — 2 operation(s) for canary credentials.
  name: Tracebit Canary Credentials API
  slug: tracebit-canary-credentials-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tracebit Alerts API
  slug: open-tracebit-alerts-api
- collection_type: open
  name: Tracebit Alerts Canary Credentials API
  slug: open-tracebit-canary-credentials-api
common:
- group: company
  title: ''
  type: Website
  url: https://tracebit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://community.tracebit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://community.tracebit.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://community.tracebit.com/api-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/tracebit-com/tracebit-community-cli#getting-started
- group: operate
  title: ''
  type: Support
  url: https://tracebit.com/contact
- group: company
  title: ''
  type: Blog
  url: https://tracebit.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tracebit-com
- group: commercial
  title: ''
  type: Pricing
  url: https://tracebit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://community.tracebit.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tracebit.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tracebit.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tracebit.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/tracebit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tracebit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tracebit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tracebit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tracebit-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tracebit-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tracebit-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tracebit-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/tracebit-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/tracebit-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tracebit-well-known.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tracebit-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tracebit-community-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tracebit-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tracebit-llms.txt
created: '2026-07-17'
description: Tracebit is a security-canary (deception) platform backed by Accel. It deploys realistic decoy credentials, secrets, and identities — canaries — across AWS, Azure, Google Cloud, Okta, Kubernetes, CI/CD pipelines, and workstations, and raises high-fidelity alerts the moment an attacker touches one during lateral movement or credential access. The free Community Edition exposes a public REST API (OpenAPI 3.1) for issuing and confirming canary credentials and reading alerts and their logs, alongside an open-source CLI, a GitHub Action, and a provider-published Agent Skill.
image: https://cdn.prod.website-files.com/663e4960fd682070c6a1bfdc/6a16ecb79f26e0be2459ffbd_tracebit-opengraph-home.jpg
layout: provider
mcp_servers:
- description: ''
  name: Tracebit MCP Server
  slug: tracebit-mcp-server
modified: '2026-07-21'
name: Tracebit
nav: Providers
network: true
overview: 'Tracebit publishes 2 APIs on the [APIs.io](https://apis.io/) network: Alerts API and Canary Credentials API. Tagged areas include Company, Cloud Saas, Security, Deception, and Canary Tokens.


  Tracebit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 56.5
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 44.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tracebit/refs/heads/main/screenshots/tracebit-2026-08-17T082426.png
security:
- kind: authentication
  name: Tracebit Authentication
  slug: tracebit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tracebit Domain Security
  slug: tracebit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tracebit Trust Center
  slug: tracebit-trust-center
  summary_line: trust center published
slug: tracebit
tags:
- Company
- Cloud Saas
- Security
- Deception
- Canary Tokens
- Threat Detection
- Cloud Security
- Incident Response
website: https://tracebit.com/
---
