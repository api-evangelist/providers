---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 6.1
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://perseus.computer
- group: docs
  title: ''
  type: Documentation
  url: https://perseus.computer/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://perseus.computer/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://perseus.computer/console
- group: commercial
  title: ''
  type: Pricing
  url: https://perseus.computer/pricing
- group: company
  title: ''
  type: Blog
  url: https://perseus.computer/blog
- group: start
  title: ''
  type: SignUp
  url: https://perseus.computer/console/onboarding?plan=developer_monthly
- group: operate
  title: ''
  type: Support
  url: mailto:hello@perseus.computer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/efficientsystemsinc
- group: build
  title: ''
  type: CLI
  url: cli/perseus-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/perseus-code-search.md
- group: build
  title: ''
  type: Packages
  url: packages/perseus-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/perseus-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perseus-domain-security.yml
created: '2026-07-17'
description: 'Perseus (legal name Efficient Systems Inc.) is an applied AI lab focused on semantic search in latent spaces, founded by Samrath Chadha and backed by Y Combinator (Fall 2025 batch). Its first product is a retrieval engine that grounds coding agents in real code: developers and agents describe the code they are looking for in plain English and Perseus returns ranked file:line results with snippets in seconds, indexing the working tree (including uncommitted edits) so models like Claude Code, Cursor, and Codex can find the right context before editing. Rather than a public REST API, Perseus ships a first-party CLI (installed via a curl/PowerShell one-liner, as a PyInstaller binary or uv wheel), a provider-published Agent Skill, and a Factory Droid plugin, all under the efficientsystemsinc GitHub organization. The developer surface — docs, console, pricing, and blog — is live; there is no OpenAPI, MCP server, or /.well-known discovery document published as of this pass.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perseus.png
layout: provider
modified: '2026-07-20'
name: Perseus
nav: Providers
network: true
overview: 'Perseus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Developer Tools, Code Search, and Semantic Search.


  Perseus'' developer surface includes documentation, getting-started guide, pricing, engineering blog, signup flow, support, CLI, and 7 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 22.9
  provenance:
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perseus/refs/heads/main/screenshots/perseus-2026-09-02T151105.png
security:
- kind: authentication
  name: Perseus Authentication
  slug: perseus-authentication
  summary_line: token · 1 scheme
- kind: domain-security
  name: Perseus Domain Security
  slug: perseus-domain-security
  summary_line: TLSv1.3
slug: perseus
tags:
- Company
- Artificial Intelligence
- Developer Tools
- Code Search
- Semantic Search
- Coding Agents
- AI Agents
- Latent Space
- CLI
- Agent Skills
- Y Combinator
website: https://perseus.computer
---
