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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Programmatic access to the exe.dev command surface. POST the command exactly as typed in the ssh exe.dev REPL to https://exe.dev/exec with an exe1. bearer token; supported commands return JSON via --j
  name: exe.dev HTTPS API
  slug: exedev-https-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://exe.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://exe.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://exe.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://exe.dev/docs/https-api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://exe.dev/docs/what-is-exe.md
- group: commercial
  title: ''
  type: Pricing
  url: https://exe.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.exe.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boldsoftware
- group: operate
  title: ''
  type: Support
  url: https://exe.dev/docs/community.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exe.dev/docs/terms-of-service.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exe.dev/docs/privacy-notice.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exedev-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/exedev-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exedev-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/exedev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/exedev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exedev-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/exedev-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/exedev-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exedev-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/exedev-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/exedev-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/exedev-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/exedev-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/exedev-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/exedev-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/exedev-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/exedev-using-exe-dev.md
created: '2026-07-17'
description: exe.dev is a cloud computing platform from Bold Software that provisions Linux VMs with persistent disks, instant HTTPS, and built-in authentication — all managed over SSH ("just use ssh"). It offers disposable Sandboxes for running AI-generated code, persistent VPS-style VMs, and Devbox cloud development environments, each reachable at https://<vm>.exe.xyz with automatic TLS. A companion HTTPS API (POST /exec) runs the same command surface with exe1. bearer tokens, and Shelley — a first-party, web-based coding agent — runs inside the VMs. exe.dev raised a $35M Series A and is backed by Amplify Partners. This profile was enriched by the API Evangelist pipeline from the provider's public docs, llms.txt, GitHub org (boldsoftware), and well-known surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exedev.png
layout: provider
modified: '2026-07-19'
name: exe.dev
nav: Providers
network: true
overview: 'exe.dev publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Cloud Computing, Virtual Machines, and Sandbox.


  exe.dev''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, authentication, and 21 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 32.0
  provenance:
    conformance: derived
    mcp: derived
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exedev/refs/heads/main/screenshots/exedev-2026-07-25T213854.png
security:
- kind: authentication
  name: Exedev Authentication
  slug: exedev-authentication
  summary_line: ssh-key/http-bearer/openIdConnect · 3 schemes
- kind: domain-security
  name: Exedev Domain Security
  slug: exedev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Exedev Vulnerability Disclosure
  slug: exedev-vulnerability-disclosure
  summary_line: contact published
slug: exedev
tags:
- Company
- Developer Tools
- Cloud Computing
- Virtual Machines
- Sandbox
- AI Agents
- Infrastructure
- SSH
website: https://exe.dev
---
