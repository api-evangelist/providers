---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: The SST framework is an open source CLI and component library distributed via npm (`sst`) and as a Go-based CLI. Developers describe their full-stack application in a single `sst.config.ts` file using
  name: SST Framework
  slug: sst-framework
- description: SST Console is a hosted SaaS dashboard at console.sst.dev that connects to SST apps deployed to AWS. It surfaces CloudWatch logs, real-time issue detection for Node.js Lambdas and containers (with sou
  name: SST Console
  slug: sst-console
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sst-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sst.dev
- group: docs
  title: ''
  type: Documentation
  url: https://sst.dev/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sst
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/sst/sst
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/sst/console
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/sst/openauth
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/sst/opencode
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/sst/opencontrol
- group: company
  title: ''
  type: Blog
  url: https://sst.dev/blog
- group: operate
  title: ''
  type: Discord
  url: https://sst.dev/discord
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/SST_dev
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/sst-dev
- group: learn
  title: ''
  type: Tutorial
  url: https://guide.sst.dev
- group: build
  title: ''
  type: Examples
  url: https://sst.dev/docs/examples
- group: build
  title: ''
  type: NPM
  url: https://www.npmjs.com/package/sst
- group: other
  title: ''
  type: HomebrewTap
  url: https://github.com/sst/homebrew-tap
- group: commercial
  title: ''
  type: License
  url: https://github.com/sst/sst/blob/dev/LICENSE
created: '2026-05-25'
description: SST is an open source TypeScript framework for building full-stack applications on your own infrastructure. Originally known as Serverless Stack, it now ships as a single `sst.config.ts` file that uses Pulumi and Terraform providers under the hood to deploy components across AWS, Cloudflare, and 150+ other providers. SST covers Lambda functions, containers, queues, buckets, databases, cron jobs, and front-end frameworks like Next.js, Remix, Astro, and SvelteKit, with resource linking that wires components together without hardcoded ARNs. SST Console adds a hosted dashboard for logs, issues, deployments, and autodeploy from Git.
features:
- Single `sst.config.ts` declarative configuration for full-stack applications
- Built on Pulumi and Terraform providers (150+ supported providers)
- First-class AWS support — Lambda, Containers (ECS/Fargate), S3, SQS, SNS, EventBridge, DynamoDB, Postgres, VPC, Router, EFS, Workflow
- First-class Cloudflare support — Workers, R2, KV, D1, DNS
- Front-end framework components — Next.js, Remix, Astro, SvelteKit, SolidStart, React Router, Static Site
- Resource linking with typed SDK access at runtime — no hardcoded ARNs
- '`sst dev` live mode with Lambda live tunneling and VPC tunneling'
- Stage-based deployment model (`sst deploy --stage <name>`) with personal vs production stages
- Encrypted secrets management via `sst secret`
- SST Console — logs, issues, updates, autodeploy from GitHub branches & PRs
- Console issue detection for Node.js Lambdas and containers with source maps
- Per-update permalinks showing input/output diffs and build logs
- Autodeploy configured in `sst.config.ts` for branch and pull-request workflows
- Local `sst dev` logs streamed into the Console
- Open source MIT-licensed framework (sst/sst, sst/console)
- Sibling open source projects from Anomaly Innovations — OpenAuth, OpenCode, OpenControl, models.dev
- Cross-platform CLI — macOS, Linux, Windows (beta) via npm, Homebrew, Scoop
- Telemetry opt-out via `sst telemetry disable`
image: https://sst.dev/favicon.svg
layout: provider
modified: '2026-05-25'
name: SST
nav: Providers
network: true
overview: 'SST publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Serverless, Infrastructure as Code, Cloudflare, TypeScript, and Full-Stack.


  SST''s developer surface includes documentation, engineering blog, YouTube channel, tutorials, code examples, and 13 more developer resources.'
random_paper: 30
score:
  band: minimal
  composite: 10.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Sst Dev Domain Security
  slug: sst-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sst-dev
tags:
- Serverless
- Infrastructure as Code
- Cloudflare
- TypeScript
- Full-Stack
- Functions
- Containers
- Open Source
- Framework
website: https://sst.dev
---
