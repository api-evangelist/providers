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
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: The Kamal CLI (`kamal`) is the primary command-line interface for packaging, shipping, and operating containerized web apps across one or more SSH-reachable servers. It reads `config/deploy.yml` (plus
  name: Kamal CLI
  slug: kamal
- description: Kamal Proxy is a minimal HTTP reverse proxy written in Go that powers the zero-downtime deploy switchover behind Kamal. It exposes a small `kamal-proxy` CLI with `run`, `deploy`, and `remove` commands
  name: Kamal Proxy
  slug: kamal-proxy
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kamal-deploy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kamal-deploy.org
- group: docs
  title: ''
  type: Documentation
  url: https://kamal-deploy.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://kamal-deploy.org/docs/installation/
- group: other
  title: ''
  type: Source
  url: https://github.com/basecamp/kamal
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/basecamp/kamal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/basecamp
- group: commercial
  title: MIT License
  type: License
  url: https://github.com/basecamp/kamal/blob/main/MIT-LICENSE
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/basecamp/kamal/releases
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/basecamp/kamal/releases
- group: operate
  title: GitHub Discussions
  type: Community
  url: https://github.com/basecamp/kamal/discussions
- group: operate
  title: Discord
  type: Community
  url: https://discord.gg/YgHVT7GCXS
- group: other
  title: ''
  type: Contributing
  url: https://github.com/basecamp/kamal/blob/main/CONTRIBUTING.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/basecamp/kamal/blob/main/CODE_OF_CONDUCT.md
- group: build
  title: kamal (RubyGem)
  type: SDKs
  url: https://rubygems.org/gems/kamal
- group: build
  title: kamal CLI
  type: CLI
  url: https://kamal-deploy.org/docs/commands/
created: '2026-05-25'
description: Kamal is an open-source deployment tool from 37signals (DHH / Basecamp) for deploying containerized web applications to any infrastructure — bare metal, cloud VMs, or a mix — with zero-downtime rolling restarts. Originally built for Rails apps, Kamal works with any web application that can be packaged as a Docker container. It uses SSHKit to drive remote commands over SSH and pairs with kamal-proxy, a lightweight HTTP proxy written in Go that seamlessly switches request traffic between old and new containers during a deploy. Kamal is imperative and Capistrano-like in feel, with a single `config/deploy.yml` describing servers, image, registry, accessories, env, secrets, and proxy/SSL settings. Capabilities include auto-provisioning Docker on new servers, remote builds, asset bridging, accessory services (databases, Redis, cron sidecars), automatic TLS via Let's Encrypt, host- and path-based routing, and hooks for custom pre/post-deploy logic. Kamal is the operational backbone
  of 37signals' on-premises exit from major cloud providers and powers their ONCE product line. Kamal itself is a CLI tool, not a hosted service — there is no public REST API, no SDK, and no paid tier. The project is released under the MIT License and developed openly on GitHub under the `basecamp` organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kamal-deploy.png
layout: provider
modified: '2026-05-25'
name: Kamal
nav: Providers
network: true
overview: 'Kamal publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Deployment, DevOps, Docker, Containers, and Zero Downtime.


  Kamal''s developer surface includes documentation, getting-started guide, release notes, changelog, CLI, and 11 more developer resources.'
random_paper: 43
score:
  band: emerging
  composite: 18.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kamal-deploy/refs/heads/main/screenshots/kamal-deploy-2026-06-20T183906.png
security:
- kind: domain-security
  name: Kamal Deploy Domain Security
  slug: kamal-deploy-domain-security
  summary_line: TLSv1.3
slug: kamal-deploy
tags:
- Deployment
- DevOps
- Docker
- Containers
- Zero Downtime
- Rolling Deploys
- Rails
- Ruby
- Open Source
- 37signals
- Basecamp
- On Premises
- Infrastructure
- CLI
- SSH
website: https://kamal-deploy.org
---
