---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The commit_tags API from Vers — 2 operation(s) for commit_tags.
  name: Vers commit_tags API
  slug: vers-commit-tags-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The commits API from Vers — 4 operation(s) for commits.
  name: Vers commits API
  slug: vers-commits-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The deploy API from Vers — 1 operation(s) for deploy.
  name: Vers deploy API
  slug: vers-deploy-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The domains API from Vers — 2 operation(s) for domains.
  name: Vers domains API
  slug: vers-domains-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The env_vars API from Vers — 2 operation(s) for env_vars.
  name: Vers env_vars API
  slug: vers-env-vars-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The images API from Vers — 5 operation(s) for images.
  name: Vers images API
  slug: vers-images-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The keys API from Vers — 1 operation(s) for keys.
  name: Vers keys API
  slug: vers-keys-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The public_repositories API from Vers — 4 operation(s) for public_repositories.
  name: Vers public_repositories API
  slug: vers-public-repositories-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The repositories API from Vers — 6 operation(s) for repositories.
  name: Vers repositories API
  slug: vers-repositories-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The System API from Vers — 1 operation(s) for system.
  name: Vers System API
  slug: vers-system-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The vm API from Vers — 20 operation(s) for vm.
  name: Vers vm API
  slug: vers-vm-api
- baseURL: https://api.vers.sh
  baseurl_source: declared
  description: The vms API from Vers — 2 operation(s) for vms.
  name: Vers vms API
  slug: vers-vms-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orchestrator Control Plane commit_tags API
  slug: open-vers-commit-tags-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags commits API
  slug: open-vers-commits-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags deploy API
  slug: open-vers-deploy-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags domains API
  slug: open-vers-domains-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags env_vars API
  slug: open-vers-env-vars-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags images API
  slug: open-vers-images-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags keys API
  slug: open-vers-keys-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags public_repositories API
  slug: open-vers-public-repositories-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags repositories API
  slug: open-vers-repositories-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags System API
  slug: open-vers-system-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags vm API
  slug: open-vers-vm-api
- collection_type: open
  name: Orchestrator Control Plane commit_tags vms API
  slug: open-vers-vms-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/vers-orchestrator-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://vers.sh/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vers.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vers.sh/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vers.sh/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vers.sh/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hdresearch
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/MFvKgPe3sT
- group: company
  title: ''
  type: Blog
  url: https://vers.sh/blog
- group: start
  title: ''
  type: SignUp
  url: https://vers.sh/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vers.sh/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vers.sh/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/vers-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vers-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/vers-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vers-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vers-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vers-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vers-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/vers-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/vers-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vers-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vers-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vers-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vers-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Vers is "git for running compute" — a branchable microVM platform from HD Research (hdresearch) that lets you fork a live virtual machine (memory, processes, sockets and all) in roughly 258 microseconds, commit its state as an immutable content-addressable snapshot, and restore or branch that snapshot anywhere. Built for AI agent swarms, parallel scenario and database-state testing, CI preview environments, and time-travel debugging, Vers exposes a 63-operation Orchestrator Control Plane API (OpenAPI 3.1) behind a bearer API key, plus a git-style CLI, official SDKs for nine languages, and two Model Context Protocol servers so coding agents can drive compute directly.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vers.png
layout: provider
mcp_servers:
- description: ''
  name: Vers MCP Server
  slug: vers-mcp-server
modified: '2026-07-21'
name: Vers
nav: Providers
network: true
overview: 'Vers publishes 12 APIs on the [APIs.io](https://apis.io/) network, including commit_tags API, commits API, deploy API, and 9 more. Tagged areas include Company, Compute, Virtualization, MicroVM, and Orchestration.


  Vers'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 47.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 40.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vers/refs/heads/main/screenshots/vers-2026-08-17T082735.png
security:
- kind: authentication
  name: Vers Authentication
  slug: vers-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vers Domain Security
  slug: vers-domain-security
  summary_line: TLSv1.3 · HSTS
slug: vers
tags:
- Company
- Compute
- Virtualization
- MicroVM
- Orchestration
- Infrastructure
- AI Agents
- Developer Tools
- Sandbox
- CI/CD
website: https://vers.sh/
---
