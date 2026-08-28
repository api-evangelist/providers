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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Extension risk assessment.
  name: Koi Security Risk API
  slug: koi-security-risk-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ExtensionTotal Risk API
  slug: open-koi-security-risk-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/koi-security-extensiontotal-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/extensiontotal/extensiontotal-vscode/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/extensiontotal/extensiontotal-vscode/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/extensiontotal/extensiontotal-vscode/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.koi.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.koi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.koi.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://www.koi.ai/blog/6-6-uncover-hidden-risks-cisos-guide-to-using-extensiontotal-api-for-your-organization
- group: company
  title: ''
  type: Blog
  url: https://www.koi.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/koi-security
- group: start
  title: ''
  type: SignUp
  url: https://www.koi.ai/get-a-demo
- group: operate
  title: ''
  type: Support
  url: https://www.koi.ai/chat-with-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.koi.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.koi.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.koi.ai/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/koi-security-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/koi-security-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/koi-security-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/koi-security-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/koi-security-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/koi-security-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/koi-security-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/koi-security-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koi-security-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/koi-security-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/koi-security-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Koi (formerly Koi Security, now operating as koi.ai) is an endpoint security platform built for non-binary software — browser extensions, IDE and editor extensions, open-source packages, MCP servers, AI models, AI agents, and containers — the install surface that traditional EDR and MDM tooling was never designed to govern. The platform ships three products: Koi Endpoint (agentless discovery and governance of every binary and non-binary install across macOS, Windows, and Linux), Koi Wings (continuous risk evaluation of code, behavior, publisher ownership changes, and update channels), and Koi Gateway (a network-based gate in front of marketplaces, app stores, and registries). Koi is widely known for the security research it publishes on software supply-chain attacks including GlassWorm, Shai-Hulud, PhantomRaven, GreedyBear, and the first malicious MCP server found in the wild. Koi also operates ExtensionTotal, a free community risk-scoring service for Visual Studio Code extensions
  that exposes a public HTTP API and a first-party VS Code extension. Koi raised $48M and has been acquired by Palo Alto Networks.'
image: https://cdn.prod.website-files.com/67bf17e426d92bdda54af956/689d7637775a71fd67d69618_link%20image.png
layout: provider
mcp_servers:
- description: ''
  name: Koi Security MCP Server
  slug: koi-security-mcp-server
modified: '2026-07-19'
name: Koi Security
nav: Providers
network: true
overview: 'Koi Security publishes 1 API on the [APIs.io](https://apis.io/) network: Risk API. Tagged areas include Company, Security, Endpoint Security, Supply Chain Security, and Browser Extensions.


  Koi Security''s developer surface includes documentation, API reference, engineering blog, signup flow, support, authentication, and 21 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 59.9
    developer_ergonomics: 28.0
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 36.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/koi-security/refs/heads/main/screenshots/koi-security-2026-07-25T224118.png
security:
- kind: authentication
  name: Koi Security Authentication
  slug: koi-security-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Koi Security Domain Security
  slug: koi-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: koi-security
tags:
- Company
- Security
- Endpoint Security
- Supply Chain Security
- Browser Extensions
- Developer Tools
- Threat Intelligence
- MCP Security
- Risk Scoring
website: https://www.koi.ai/
---
