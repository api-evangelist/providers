---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 62
  human_in_the_loop: 6
  name: Freestyle Sh Agentic Access
  operation_count: 129
  slug: freestyle-sh-agentic-access
  summary_line: 129 operations · 62 acting · 6 human-in-the-loop
api_count: 8
apis:
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: The Auth API from Freestyle — 2 operation(s) for auth.
  name: Freestyle Auth API
  slug: freestyle-sh-auth-api
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: APIs for managing SSL certificates.
  name: Freestyle Certs API
  slug: freestyle-sh-certs-api
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: The Cron API from Freestyle — 5 operation(s) for cron.
  name: Freestyle Cron API
  slug: freestyle-sh-cron-api
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: APIs for managing DNS records.
  name: Freestyle DNS API
  slug: freestyle-sh-dns-api
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: APIs for managing domains. This is only relevant when you want to start to deploy to custom domains. Please read [this guide](https://github.com/freestyle-sh/sandbox_sdks/blob/main/docs/custom_domains
  name: Freestyle Domains API
  slug: freestyle-sh-domains-api
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: APIs for running code. Send the code using the [execute](#tag/execute/POST/execute/v1/execute) endpoint, and you'll get the output back. Works with any TypeScript or JavaScript code + handles any node
  name: Freestyle Execute API
  slug: freestyle-sh-execute-api
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: APIs for managing git repositories and accessing git objects like commits, trees, blobs, tags, and refs.
  name: Freestyle Git API
  slug: freestyle-sh-git-api
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: APIs for managing identities and access tokens.
  name: Freestyle Identity API
  slug: freestyle-sh-identity-api
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: APIs for observability.
  name: Freestyle Observability API
  slug: freestyle-sh-observability-api
- baseURL: https://api.freestyle.sh
  baseurl_source: spec
  description: 'APIs for deploying websites. We handle node modules caching, scaling, certificates and the whole end to end process. Send the code using the [deploy](#tag/web/POST/web/v1/deploy) endpoint, and you''ll '
  name: Freestyle Web API
  slug: freestyle-sh-web-api
- description: 'Run any call server-side and poll for its result: send `x-freestyle-background-after-secs: <n>` on the original request, and if it outlives that window you get a `202` with a request id to poll here. '
  name: Freestyle Background requests API
  slug: freestyle-sh-background-requests-api
- description: Read and write files inside a running VM
  name: Freestyle Filesystem API
  slug: freestyle-sh-filesystem-api
- description: The Firewall API from Freestyle — 6 operation(s) for firewall.
  name: Freestyle Firewall API
  slug: freestyle-sh-firewall-api
- description: The Hardware API from Freestyle — 4 operation(s) for hardware.
  name: Freestyle Hardware API
  slug: freestyle-sh-hardware-api
- description: 'Scoped access for your end users: identities, tokens, and per-VM grants'
  name: Freestyle Identities API
  slug: freestyle-sh-identities-api
- description: Capture a VM's exact state, memory and disk, and boot new VMs from it
  name: Freestyle Snapshots API
  slug: freestyle-sh-snapshots-api
- description: The TLS API from Freestyle — 8 operation(s) for tls.
  name: Freestyle TLS API
  slug: freestyle-sh-tls-api
- description: The Tunnels API from Freestyle — 8 operation(s) for tunnels.
  name: Freestyle Tunnels API
  slug: freestyle-sh-tunnels-api
- description: Boot, control, and run commands in your VMs
  name: Freestyle VMs API
  slug: freestyle-sh-vms-api
- description: Private networks your VMs can share
  name: Freestyle VPCs API
  slug: freestyle-sh-vpcs-api
artifact_total: 108
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
  name: Freestyle Cron Auth API
  slug: open-freestyle-sh-auth-api
- collection_type: open
  name: Freestyle Cron Auth Certs API
  slug: open-freestyle-sh-certs-api
- collection_type: open
  name: Freestyle Auth Cron API
  slug: open-freestyle-sh-cron-api
- collection_type: open
  name: Freestyle Cron Auth DNS API
  slug: open-freestyle-sh-dns-api
- collection_type: open
  name: Freestyle Cron Auth Domains API
  slug: open-freestyle-sh-domains-api
- collection_type: open
  name: Freestyle Cron Auth Execute API
  slug: open-freestyle-sh-execute-api
- collection_type: open
  name: Freestyle Cron Auth Git API
  slug: open-freestyle-sh-git-api
- collection_type: open
  name: Freestyle Cron Auth Identity API
  slug: open-freestyle-sh-identity-api
- collection_type: open
  name: Freestyle Cron Auth Observability API
  slug: open-freestyle-sh-observability-api
- collection_type: open
  name: Freestyle Cron Auth VM API
  slug: open-freestyle-sh-vm-api
- collection_type: open
  name: Freestyle Cron Auth Web API
  slug: open-freestyle-sh-web-api
- collection_type: open
  name: Freestyle VMs API
  slug: open-freestyle-vm-api
- collection_type: open
  name: Freestyle Web Deployments API
  slug: open-freestyle-web-api
common:
- group: other
  href: https://artifacts.apis.io/freestyle-sh/capabilities/freestyle-sh-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/freestyle-sh-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.freestyle.sh/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/freestyle/overview
- group: agent
  href: https://artifacts.apis.io/freestyle-sh/agentic-access/freestyle-sh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/freestyle-sh-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/freestyle-sh/security/freestyle-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freestyle-sh-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/freestyle-sh/authentication/freestyle-sh-authentication.yml
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
  href: https://artifacts.apis.io/freestyle-sh/plans/freestyle-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/freestyle-sh-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/freestyle-sh/rate-limits/freestyle-sh-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/freestyle-sh-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/freestyle-sh/finops/freestyle-sh-finops.yml
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
- has_sources: true
  method: derived
  name: Freestyle Sh Finops
  primary_unit: hour of vcpu
  service_category: ''
  slug: freestyle-sh-finops
  template: false
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
  property_count: 8
  slug: freestyle-repository
- name: Freestyle VM
  property_count: 7
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
overview: 'Freestyle publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Certs API, Cron API, and 17 more. Tagged areas include Artificial Intelligence, Agents, Sandbox, VMs, and MicroVM.


  The Freestyle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Freestyle''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 45 more developer resources.'
plans:
- name: Freestyle Sh Plans Pricing
  plan_count: 8
  slug: freestyle-sh-plans-pricing
- name: Freestyle Sh Price Estimates
  plan_count: 0
  slug: freestyle-sh-price-estimates
random_paper: 19
rate_limits:
- limit_count: 4
  name: Freestyle Sh Rate Limits
  slug: freestyle-sh-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Freestyle — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: freestyle-sh-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 73.3
    catalog_earned_first_party: 12.0
    catalog_gap: 41.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 73.7
    contract_governance: 9.8
    contract_quality: 67.4
    developer_ergonomics: 67.9
    discoverability: 62.5
    operational_transparency: 28.9
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 45.5
      total: 22
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/freestyle-sh/freestyle-sh-2026-06-20T181533.png
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
- Artificial Intelligence
- Agents
- Sandbox
- VMs
- MicroVM
- Version Control
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
website: https://www.freestyle.sh/
---
