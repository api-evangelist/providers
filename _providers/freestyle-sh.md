---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 62
  human_in_the_loop: 6
  name: Freestyle Sh Agentic Access
  operation_count: 128
  slug: freestyle-sh-agentic-access
  summary_line: 128 operations · 62 acting · 6 human-in-the-loop
api_count: 11
apis:
- description: The Auth API from Freestyle — 2 operation(s) for auth.
  name: Freestyle Auth API
  slug: freestyle-sh-auth-api
- description: APIs for managing SSL certificates.
  name: Freestyle Certs API
  slug: freestyle-sh-certs-api
- description: The Cron API from Freestyle — 5 operation(s) for cron.
  name: Freestyle Cron API
  slug: freestyle-sh-cron-api
- description: APIs for managing DNS records.
  name: Freestyle DNS API
  slug: freestyle-sh-dns-api
- description: APIs for managing domains. This is only relevant when you want to start to deploy to custom domains. Please read [this guide](https://github.com/freestyle-sh/sandbox_sdks/blob/main/docs/custom_domains
  name: Freestyle Domains API
  slug: freestyle-sh-domains-api
- description: APIs for running code. Send the code using the [execute](#tag/execute/POST/execute/v1/execute) endpoint, and you'll get the output back. Works with any TypeScript or JavaScript code + handles any node
  name: Freestyle Execute API
  slug: freestyle-sh-execute-api
- description: APIs for managing git repositories and accessing git objects like commits, trees, blobs, tags, and refs.
  name: Freestyle Git API
  slug: freestyle-sh-git-api
- description: APIs for managing identities and access tokens.
  name: Freestyle Identity API
  slug: freestyle-sh-identity-api
- description: APIs for observability.
  name: Freestyle Observability API
  slug: freestyle-sh-observability-api
- description: APIs for managing lightweight virtual machines (VMs) to run your code in isolated environments.
  name: Freestyle VM API
  slug: freestyle-sh-vm-api
- description: 'APIs for deploying websites. We handle node modules caching, scaling, certificates and the whole end to end process. Send the code using the [deploy](#tag/web/POST/web/v1/deploy) endpoint, and you''ll '
  name: Freestyle Web API
  slug: freestyle-sh-web-api
artifact_total: 87
collections:
- collection_type: postman
  name: Freestyle Cron Auth API
  slug: postman-freestyle-sh-auth-api
- collection_type: postman
  name: Freestyle Cron Auth Certs API
  slug: postman-freestyle-sh-certs-api
- collection_type: postman
  name: Freestyle Auth Cron API
  slug: postman-freestyle-sh-cron-api
- collection_type: postman
  name: Freestyle Cron Auth DNS API
  slug: postman-freestyle-sh-dns-api
- collection_type: postman
  name: Freestyle Cron Auth Domains API
  slug: postman-freestyle-sh-domains-api
- collection_type: postman
  name: Freestyle Cron Auth Execute API
  slug: postman-freestyle-sh-execute-api
- collection_type: postman
  name: Freestyle Cron Auth Git API
  slug: postman-freestyle-sh-git-api
- collection_type: postman
  name: Freestyle Cron Auth Identity API
  slug: postman-freestyle-sh-identity-api
- collection_type: postman
  name: Freestyle Cron Auth Observability API
  slug: postman-freestyle-sh-observability-api
- collection_type: postman
  name: Freestyle Cron Auth VM API
  slug: postman-freestyle-sh-vm-api
- collection_type: postman
  name: Freestyle Cron Auth Web API
  slug: postman-freestyle-sh-web-api
- collection_type: open
  name: Freestyle Cron API
  slug: open-freestyle-cron-api
- collection_type: open
  name: Freestyle Domains API
  slug: open-freestyle-domains-api
- collection_type: open
  name: Freestyle Execute API
  slug: open-freestyle-execute-api
- collection_type: open
  name: Freestyle Git API
  slug: open-freestyle-git-api
- collection_type: open
  name: Freestyle Identity API
  slug: open-freestyle-identity-api
- collection_type: open
  name: Freestyle Observability API
  slug: open-freestyle-observability-api
- collection_type: open
  name: Freestyle VMs API
  slug: open-freestyle-vm-api
- collection_type: open
  name: Freestyle Web Deployments API
  slug: open-freestyle-web-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/freestyle/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freestyle-sh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freestyle-sh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freestyle-sh-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.freestyle.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.freestyle.sh/v2/about
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.freestyle.sh/openapi.json
- group: start
  title: ''
  type: Signup
  url: https://admin.freestyle.sh
- group: other
  title: ''
  type: Dashboard
  url: https://admin.freestyle.sh
- group: commercial
  title: ''
  type: Pricing
  url: https://www.freestyle.sh/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.freestyle.sh/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.freestyle.sh
- group: operate
  title: ''
  type: Forums
  url: https://discord.com/invite/YTRprVkdnz
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.freestyle.sh/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freestyle-sh
- group: build
  title: ''
  type: SDKs
  url: https://github.com/freestyle-sh/sandbox_sdks
- group: build
  title: ''
  type: SDKs
  url: https://github.com/freestyle-sh/sandbox-sdks-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/freestyle-sh/rigkit
- group: build
  title: ''
  type: Tools
  url: https://github.com/freestyle-sh/freestyle-auth
- group: build
  title: ''
  type: Tools
  url: https://github.com/freestyle-sh/Adorable
- group: build
  title: ''
  type: Tools
  url: https://github.com/freestyle-sh/cloudstate
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/freestyle-sh/freestyle-execute-chat
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/freestyle-sh/freestyle-astro-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/freestyle-sh/freestyle-sveltekit-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/freestyle-sh/freestyle-solid-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/freestyle-sh/freestyle-next-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/freestyle-sh/freestyle-vite-react
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/freestyle-sh/freestyle-react-native-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/freestyle-sh/freestyle-deno-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/freestyle-sh/freestyle-expo
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/integrations/node
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/integrations/python
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/integrations/bun
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/integrations/deno
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/integrations/ruby
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/integrations/java
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/integrations/postgres
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/integrations/opencode
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/integrations/web-terminal
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/custom-integrations
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/vms/cli
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/git/cli
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/serverless/deployments/cli
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/serverless/runs/cli
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freestyle.sh/v2/domains/cli
- group: commercial
  title: ''
  type: Plans
  url: plans/freestyle-sh-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freestyle-sh-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/freestyle-sh-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Freestyle is the infrastructure for code you didn't write — VMs and Git for AI agents. The platform provides Linux microVMs that boot in under 600ms with live-fork, pause-resume, and persistent snapshots; a multi-tenant Git service with branchable filesystems, GitHub Sync, full-text search, and webhook triggers; an Execute (Serverless Runs) API for ephemeral JavaScript/TypeScript code; a Web Deployments API for hosted Node.js apps and static sites; Cron schedules; custom Domains with wildcard SSL; an Identity service for scoped per-user and per-agent access tokens; and Observability logs. Freestyle is a direct sandbox option for AI app builders, background agents, code review bots, and long-running assistants — a usage-priced alternative to running Anthropic's hosted Code Execution tool or building bespoke microVM infrastructure on Firecracker, Modal, or E2B.
features:
- Linux microVMs that boot in under 600ms with restored memory snapshots
- Live VM forking — clone a running VM into multiple copies in milliseconds
- Pause and resume — hibernate idle VMs and pay nothing while paused
- Snapshots (memory + disk) with persistent snapshot retention on Hobby+
- Multi-tenant Git hosting with branchable filesystems for AI agents
- GitHub bidirectional sync (pull, push, or both) per repository
- Full-text search across files, commit messages, and diffs
- Webhook triggers on commits and refs
- Per-repo and per-VM identity permissions with scoped access tokens
- Custom domains with verification, wildcard SSL, DNS record management, and deployment mappings
- Serverless Runs (execute) for ephemeral JS/TS code execution
- Serverless Deployments for hosted Node.js apps and static sites
- Cron schedules with execution history and metrics timeline
- Observability logs across VMs, deployments, runs, and identities
- First-class language integrations — Node.js, Bun, Deno, Python, uv, Ruby, Java, PostgreSQL, OpenCode, Web Terminal
- TypeScript and Python SDKs plus Vercel AI, LangGraph, and Mastra SDK adapters
- rigkit CLI for local dev machines
- SSH access to VMs
- Bearer-token auth (Authorization header) for all REST APIs
- Pricing per vCPU-hour, GiB-memory-hour, and GiB-storage-hour with daily free allowances
- Plan tiers Free, Hobby ($50/mo + usage), Pro ($500/mo + usage), Enterprise
finops:
- name: Freestyle Sh Finops
  service_category: Compute
  slug: freestyle-sh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freestyle-sh.png
integrations:
- Anthropic Claude — Code Execution tool, Managed Agents, Skills (Freestyle sandbox positioned as an alternative or complement to Anthropic's hosted code execution sandbox)
- GitHub — bidirectional repo sync, GitHub Sync configuration per repo
- Vercel AI SDK — first-party adapter in sandbox_sdks
- LangGraph — first-party adapter in sandbox_sdks
- Mastra — first-party adapter in sandbox_sdks
- Node.js, Bun, Deno — first-class VM runtimes
- Python (with uv), Ruby, Java — first-class VM runtimes
- PostgreSQL — managed inside VMs
- OpenCode — VM integration
- Cloudstate — Freestyle's own JavaScript database runtime
- Adorable — Freestyle's own open-source Lovable-style AI app builder
- Astro, Next.js, SvelteKit, Solid Start, React Native, Expo, Vite — starter templates
json_schemas:
- name: Freestyle Repository
  property_count: 0
  slug: freestyle-repository
- name: Freestyle VM
  property_count: 0
  slug: freestyle-vm
jsonld:
- class_count: 0
  name: Freestyle Sh Context
  property_count: 13
  slug: freestyle-sh-context
layout: provider
modified: '2026-05-25'
name: Freestyle
nav: Providers
network: true
overview: 'Freestyle publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Certs API, Cron API, and 8 more. Tagged areas include AI, Agents, Sandboxes, VMs, and MicroVMs.


  The Freestyle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Freestyle''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 43 more developer resources.'
plans:
- name: Freestyle Sh Plans Pricing
  plan_count: 5
  slug: freestyle-sh-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 4
  name: Freestyle Sh Rate Limits
  slug: freestyle-sh-rate-limits
rules:
- name: Freestyle API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: freestyle-sh-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.4
  delta: -3.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 73.5
    developer_ergonomics: 60.9
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freestyle-sh/refs/heads/main/screenshots/freestyle-sh-2026-06-20T181533.png
security:
- kind: authentication
  name: Freestyle Sh Authentication
  slug: freestyle-sh-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Freestyle Sh Domain Security
  slug: freestyle-sh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: freestyle-sh
solutions:
- VMs and Git for AI Agents — give agents real Linux VMs with a Git-backed branchable filesystem, replacing per-step container snapshots with full-machine VM snapshots
- Multi-tenant App Hosting — every end user or AI project gets its own VM, repo, and custom domain
- AI Code Sandboxing — safer alternative to running LLM-generated code in your own process, with egress control and microVM isolation
- Background Agent Infrastructure — persistent VMs that pause when idle and resume on event for long-running agentic workloads
tags:
- AI
- Agents
- Sandboxes
- VMs
- MicroVMs
- Git
- Code Execution
- JavaScript
- TypeScript
- Serverless
- Hosting
- Developer Tools
- Infrastructure
use_cases:
- AI app builders (Lovable, Bolt, V0 style) provisioning a sandbox VM per project with cloned source, dev servers, and *.style.dev preview domains
- Background agents (Devin, Cursor Agent style) forking a base VM into parallel workers — one builds the API, one builds the UI, one writes tests
- Code review bots (CodeRabbit, Greptile style) cloning a repo at a PR SHA, running lint/test, and posting a Claude-generated review
- Long-running AI assistants (Claude, OpenClaw, Cowork style) using a persistent VM with 60s idle pause to keep per-user state at $0 cost between turns
- LLM code-interpreter style — execute model-generated code safely in an isolated microVM with egress control
- Sandboxed AI agent evals on ephemeral microVMs (one VM per eval run)
- Multi-tenant SaaS where each end user gets their own Freestyle Git repo and isolated VM
- Reinforcement learning on microVMs — fan out, train, fold in
- Deep-research agents that spawn, suspend on idle, and resume on event
- Hosted code playgrounds for educational and developer-tool products
website: https://www.freestyle.sh
---
