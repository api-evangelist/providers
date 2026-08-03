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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dokku-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dokku.com
- group: docs
  title: ''
  type: Documentation
  url: https://dokku.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://dokku.com/docs/getting-started/installation/
- group: learn
  title: ''
  type: Tutorials
  url: https://dokku.com/tutorials/
- group: company
  title: ''
  type: Blog
  url: https://dokku.com/blog/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dokku/dokku
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dokku/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/dokku/dokku/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/dokku/dokku/blob/master/LICENSE
- group: other
  title: ''
  type: Sponsorship
  url: https://github.com/sponsors/dokku
- group: other
  title: ''
  type: Pro
  url: https://pro.dokku.com/
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/dokku/github-action
- group: other
  title: ''
  type: AnsibleModules
  url: https://github.com/dokku/ansible-dokku
- group: build
  title: ''
  type: GitLabCI
  url: https://github.com/dokku/gitlab-ci
- group: other
  title: ''
  type: HomebrewTap
  url: https://github.com/dokku/homebrew-repo
- group: start
  title: ''
  type: AzureQuickstart
  url: https://github.com/dokku/azure-quickstart-templates
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/YQjANGMZ
- group: operate
  title: ''
  type: Slack
  url: https://slack.dokku.com/
- group: operate
  title: ''
  type: Forums
  url: https://github.com/dokku/dokku/discussions
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/dokku
created: '2026-05-25'
description: Dokku is an open-source Docker-powered self-hosted Platform-as-a-Service that helps you build and manage the lifecycle of applications from initial push to scaling out. Often described as "the smallest PaaS implementation you've ever seen" and a self-hosted mini-Heroku, Dokku turns a single Linux host (or a multi-host scheduler such as K3s or Nomad) into a git-push deployment target that builds applications from Heroku-compatible buildpacks, Cloud Native Buildpacks, Nixpacks, Railpack, Dockerfiles, or pre-built Docker images. Dokku is MIT licensed, written primarily in Bash, and maintained by the Dokku organization on GitHub since 2013. It ships an extensive plugin ecosystem covering data stores (Postgres, MySQL, MariaDB, Redis, MongoDB, RabbitMQ, Elasticsearch, ClickHouse, Meilisearch, Typesense), TLS via Let's Encrypt, HTTP basic auth, maintenance mode, redirects, schedulers for Docker, K3s and Nomad, multiple HTTP proxies (Nginx, HAProxy, Caddy, Traefik, OpenResty), CI integrations,
  and an official GitHub Action. Dokku's primary interface is the `dokku` CLI invoked over SSH; there is no first-party public HTTP REST API in core (the historical `dokku-api` Ruby wrapper is archived and unmaintained).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dokku.png
layout: provider
modified: '2026-05-25'
name: Dokku
nav: Providers
network: true
overview: 'Dokku is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include PaaS, Self-Hosted, Docker, Containers, and Buildpacks.


  Dokku''s developer surface includes documentation, getting-started guide, engineering blog, GitHub presence, release notes, and 16 more developer resources.'
random_paper: 67
score:
  band: minimal
  composite: 12.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 12.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dokku/refs/heads/main/screenshots/dokku-2026-06-20T180131.png
security:
- kind: domain-security
  name: Dokku Domain Security
  slug: dokku-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dokku
tags:
- PaaS
- Self-Hosted
- Docker
- Containers
- Buildpacks
- Deployment
- DevOps
- Heroku Alternative
- Open Source
- Git Push Deploy
- Kubernetes
- Nomad
- K3s
- CLI
- Plugins
website: https://dokku.com
---
