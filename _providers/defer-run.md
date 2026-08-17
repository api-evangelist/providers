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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defer-run-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.defer.run
- group: docs
  title: ''
  type: Documentation
  url: https://docs.defer.run
- group: build
  title: ''
  type: GitHub
  url: https://github.com/defer-run
- group: build
  title: ''
  type: ClientSDK
  url: https://github.com/defer-run/defer.client
- group: build
  title: ''
  type: NextJSIntegration
  url: https://github.com/defer-run/nextjs
- group: build
  title: ''
  type: RedwoodJSIntegration
  url: https://github.com/defer-run/defer-redwoodjs
- group: start
  title: ''
  type: DemoApp
  url: https://github.com/defer-run/defer.demo
- group: other
  title: ''
  type: YCombinator
  url: https://www.ycombinator.com/companies/defer
- group: other
  title: ''
  type: YCombinatorLaunch
  url: https://www.ycombinator.com/launches/I2Y-defer-a-zero-infrastructure-platform-for-node-js-background-jobs
- group: other
  title: ''
  type: LaunchHN
  url: https://news.ycombinator.com/item?id=35096366
- group: other
  title: ''
  type: EndOfServiceAnnouncement
  url: https://news.ycombinator.com/item?id=39817493
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/defer
- group: company
  title: ''
  type: Twitter
  url: https://x.com/defer_run
- group: company
  title: ''
  type: IntroductionBlogPost
  url: https://dev.to/defer/introducing-defer-a-zero-infrastructure-background-jobs-nodejs-platform-43jb
created: '2026-05-25'
description: Defer was a Paris-based, Y Combinator-backed (W23) zero-infrastructure background jobs platform for Node.js and TypeScript developers, founded in 2022 by Bryan Frimin and Charly Poly. The product converted regular JavaScript/TypeScript async functions into managed background jobs with configurable retries, throttling, concurrency controls, scheduled crons, multi-environment support, alerting, and a hosted dashboard — removing the need for developers to operate their own queues, workers, and Redis-style infrastructure. Defer shipped client SDKs and framework integrations (Next.js, RedwoodJS) and a CLI/build pipeline that uploaded function bundles to the Defer cloud for execution. The company appears to have wound down its hosted service in 2024 — the defer.run domain now 301-redirects to digger.tools, no end-of-service post-mortem is publicly linked from the homepage, and the GitHub organization (github.com/defer-run) last saw meaningful activity in July 2024 with the final defer.client
  release v2.3.0 cut on 2024-03-06. The open source client libraries remain available but are effectively unmaintained and the hosted backend they depended on is no longer operational. This catalog entry preserves the historical footprint of Defer as part of the 2022-2024 wave of "zero-infrastructure" background-job and durable- execution startups (Inngest, Trigger.dev, Hatchet, Temporal Cloud, Restate) so the design pattern and the players who pursued it remain discoverable in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defer-run.png
layout: provider
modified: '2026-05-25'
name: Defer
nav: Providers
network: true
overview: 'Defer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Background Jobs, Asynchronous Processing, Job Queues, Serverless, and Node.js.


  Defer''s developer surface includes documentation, GitHub presence, and 13 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 7.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 7.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defer-run/refs/heads/main/screenshots/defer-run-2026-06-20T175853.png
security:
- kind: domain-security
  name: Defer Run Domain Security
  slug: defer-run-domain-security
  summary_line: TLSv1.3
slug: defer-run
tags:
- Background Jobs
- Asynchronous Processing
- Job Queues
- Serverless
- Node.js
- TypeScript
- Workflow Orchestration
- Cron
- Durable Execution
- Developer Tools
- Defunct
- Y Combinator
website: https://www.defer.run
---
