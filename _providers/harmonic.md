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
    agent_skills: false
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Programmatic access to Aristotle, Harmonic's formal reasoning agent. Over HTTPS with an API key, submit Lean 4 proofs with `sorry` placeholders, natural-language math problems, or LaTeX papers; Aristo
  name: Aristotle API
  slug: aristotle-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.harmonic.fun
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aristotle.harmonic.fun
- group: start
  title: ''
  type: SignUp
  url: https://aristotle.harmonic.fun/auth/login?screen_hint=signup
- group: start
  title: ''
  type: Login
  url: https://aristotle.harmonic.fun/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aristotle.harmonic.fun/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aristotle.harmonic.fun/privacy
- group: company
  title: ''
  type: Blog
  url: https://harmonic.fun/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harmonic-ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/harmonic-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/harmonic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/harmonic-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/harmonic-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/harmonic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harmonic-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/harmonic-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/harmonic-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harmonic-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harmonic-domain-security.yml
created: '2026-07-17'
description: 'Harmonic is a Palo Alto AI lab building Mathematical Superintelligence (MSI) — AI that reasons with rigorous, verifiable logic rather than statistical pattern matching. Its flagship product, Aristotle, is a formal reasoning agent that uses Lean 4 to prove and formally verify graduate- and research-level problems in mathematics and software. Developers access Aristotle through the Aristotle API (https://aristotle.harmonic.fun) and the official Python SDK/CLI (aristotlelib): submit Lean 4 proof files with `sorry` placeholders, plain English math problems, or LaTeX research papers, and Aristotle attempts to complete, formalize, and formally verify them — running autonomously for up to 24 hours on larger tasks and returning only formally checked results. Harmonic was co-founded by Vlad Tenev (co-founder of Robinhood) and Tudor Achim, and is backed by Kleiner Perkins.'
image: https://www.harmonic.fun/images/harmonic-blue.svg
layout: provider
mcp_servers:
- description: Harmonic does not (as of this pass) publish an official MCP server for the Aristotle API. A working community MCP server, lean-aristotle-mcp (maintained by GitHub user septract), wraps the Aristotle c
  name: Harmonic MCP Server
  slug: harmonic-mcp-server
modified: '2026-07-19'
name: Harmonic
nav: Providers
network: true
overview: 'Harmonic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Mathematics, Formal Verification, and Theorem Proving.


  Harmonic''s developer surface includes signup flow, engineering blog, authentication, CLI, changelog, and 13 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 22.4
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harmonic/refs/heads/main/screenshots/harmonic-2026-07-25T220710.png
security:
- kind: authentication
  name: Harmonic Authentication
  slug: harmonic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Harmonic Domain Security
  slug: harmonic-domain-security
  summary_line: TLSv1.2 · DMARC
slug: harmonic
tags:
- Company
- Artificial Intelligence
- Mathematics
- Formal Verification
- Theorem Proving
- Lean
- Machine Reasoning
- Developer Tools
website: https://www.harmonic.fun
---
