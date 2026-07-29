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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 74
  human_in_the_loop: 1
  name: Coolify Agentic Access
  operation_count: 136
  slug: coolify-agentic-access
  summary_line: 136 operations · 74 acting · 1 human-in-the-loop
api_count: 19
apis:
- description: The Coolify platform - an open-source, Apache-2.0 licensed, self-hostable PaaS written in PHP (Laravel) that automates deployment of applications, databases, and services to user-controlled servers vi
  name: Coolify
  slug: coolify
- description: Applications
  name: Coolify Applications API
  slug: coolify-applications-api
- description: Cloud Tokens
  name: Coolify Cloud Tokens API
  slug: coolify-cloud-tokens-api
- description: Databases
  name: Coolify Databases API
  slug: coolify-databases-api
- description: Deployments
  name: Coolify Deployments API
  slug: coolify-deployments-api
- description: The Disable API from Coolify — 1 operation(s) for disable.
  name: Coolify Disable API
  slug: coolify-disable-api
- description: The Enable API from Coolify — 1 operation(s) for enable.
  name: Coolify Enable API
  slug: coolify-enable-api
- description: GitHub Apps
  name: Coolify GitHub Apps API
  slug: coolify-github-apps-api
- description: The Health API from Coolify — 1 operation(s) for health.
  name: Coolify Health API
  slug: coolify-health-api
- description: Hetzner
  name: Coolify Hetzner API
  slug: coolify-hetzner-api
- description: The Mcp API from Coolify — 2 operation(s) for mcp.
  name: Coolify Mcp API
  slug: coolify-mcp-api
- description: Private Keys
  name: Coolify Private Keys API
  slug: coolify-private-keys-api
- description: Projects
  name: Coolify Projects API
  slug: coolify-projects-api
- description: Resources
  name: Coolify Resources API
  slug: coolify-resources-api
- description: Scheduled Tasks
  name: Coolify Scheduled Tasks API
  slug: coolify-scheduled-tasks-api
- description: Servers
  name: Coolify Servers API
  slug: coolify-servers-api
- description: Services
  name: Coolify Services API
  slug: coolify-services-api
- description: Teams
  name: Coolify Teams API
  slug: coolify-teams-api
- description: The Version API from Coolify — 1 operation(s) for version.
  name: Coolify Version API
  slug: coolify-version-api
artifact_total: 39
collections:
- collection_type: open
  name: Coolify
  slug: open-coolify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coolify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coolify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coolify-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coollabsio
- group: start
  title: ''
  type: Portal
  url: https://coolify.io/
- group: docs
  title: ''
  type: Documentation
  url: https://coolify.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://coolify.io/docs/installation
- group: start
  title: ''
  type: Login
  url: https://app.coolify.io/login
- group: start
  title: ''
  type: Signup
  url: https://app.coolify.io/register
- group: commercial
  title: ''
  type: Pricing
  url: https://coolify.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://coolify.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/coollabsio/coolify/releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coollabsio/coolify
- group: operate
  title: ''
  type: Support
  url: https://coolify.io/docs/contact
- group: operate
  title: ''
  type: Discord
  url: https://coolify.io/discord
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/coolifyio
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coollabsio
- group: other
  title: ''
  type: OpenCollective
  url: https://opencollective.com/coollabsio
- group: commercial
  title: ''
  type: License
  url: https://github.com/coollabsio/coolify/blob/main/LICENSE
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coolify.io/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coolify.io/legal/terms
- group: commercial
  title: ''
  type: Plans
  url: ''
- group: build
  title: ''
  type: CLI
  url: https://github.com/coollabsio/coolify-cli
- group: other
  title: ''
  type: Agent
  url: https://github.com/coollabsio/sentinel
- group: build
  title: ''
  type: Samples
  url: https://github.com/coollabsio/coolify-examples
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/coollabsio/coolify-docs
- group: other
  title: ''
  type: BuildPack
  url: https://github.com/coollabsio/coolpack
created: '2026-05-25'
description: Coolify is an open-source, self-hostable Platform-as-a-Service alternative to Vercel, Heroku, Netlify, and Railway. It lets you deploy static sites, APIs, full-stack applications, databases, and 280+ one-click services to any SSH-accessible server (VPS, bare-metal, Raspberry Pi, EC2, Hetzner, DigitalOcean) while keeping every configuration value, deployment, and dataset on infrastructure you own.
features:
- Apache-2.0 licensed, self-hostable PaaS
- One-line bash installer for any SSH-accessible Linux server
- Deploy from GitHub, GitLab, Bitbucket, Gitea, or any Git repo
- 280+ one-click services (databases, CMSes, analytics, observability)
- Native Docker and Docker Compose support
- Built-in databases - PostgreSQL, MySQL, MariaDB, MongoDB, Redis, KeyDB, Dragonfly, ClickHouse
- Automatic Let's Encrypt SSL certificates
- Scheduled database backups to any S3-compatible storage
- Pull-request preview deployments
- Real-time terminal access through the browser
- Team-based access control with role-based permissions
- Webhooks, notifications across Discord/Slack/Telegram/email
- REST API and CLI for full programmatic control
- GitHub App integration for private repositories
- Hetzner Cloud provisioning built in
- Free forever when self-hosted; managed cloud at app.coolify.io
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coolify.png
layout: provider
modified: '2026-05-25'
name: Coolify
nav: Providers
network: true
overview: 'Coolify publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Cloud Tokens API, Databases API, and 15 more. Tagged areas include Platform as a Service, Self-Hosting, Deployment, Open Source, and Containers.


  Coolify''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 19 more developer resources.'
random_paper: 64
score:
  band: developing
  composite: 43.4
  delta: -2.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.2
    developer_ergonomics: 52.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coolify/refs/heads/main/screenshots/coolify-2026-06-20T175004.png
security:
- kind: authentication
  name: Coolify Authentication
  slug: coolify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Coolify Domain Security
  slug: coolify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coolify
tags:
- Platform as a Service
- Self-Hosting
- Deployment
- Open Source
- Containers
- Docker
website: https://coolify.io/
---
