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
api_count: 1
apis:
- description: 'The Sensu Go backend REST API for managing observability resources: checks, events, entities, filters, handlers, mutators, hooks, pipelines, assets, silences, namespaces, roles, role bindings, cluster'
  name: Sensu Go Backend REST API
  slug: sensu-go-backend-rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sensu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sensu.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sensu.io/sensu-go/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sensu.io/sensu-go/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sensu.io/sensu-go/latest/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sensu.io/sensu-go/latest/operations/deploy-sensu/install-sensu/
- group: operate
  title: ''
  type: Support
  url: https://discourse.sensu.io
- group: company
  title: ''
  type: Blog
  url: https://sensu.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sensu
- group: commercial
  title: ''
  type: Pricing
  url: https://sensu.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://account.sensu.io/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://account.sensu.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sumologic.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sumologic.com/privacy-statement/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sensu-llms.txt
created: '2026-07-17'
description: Sensu (Sensu by Sumo Logic) is an observability pipeline that delivers monitoring as code across multi-cloud and hybrid environments. Sensu Go codifies monitoring workflows into declarative, versionable configuration and exposes a backend REST API (core/v2 plus namespaced and cluster-wide enterprise APIs) for managing checks, events, entities, filters, handlers, mutators, pipelines, assets, silences, roles, and users. It integrates with Nagios, StatsD, Telegraf, and Prometheus, automates registration and de-registration of servers, containers, services, and functions, and drives self-healing and automated diagnosis from bare metal to Kubernetes. The platform ships the sensuctl command-line interface, an open-source Go codebase, and role-based access control, with JWT access tokens and persistent API keys for authentication and OIDC single sign-on for operators.
image: https://sensu.io/img/sensu-logo.png
layout: provider
modified: '2026-07-21'
name: Sensu
nav: Providers
network: true
overview: 'Sensu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Observability, Infrastructure, and DevOps.


  Sensu''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 12
screenshot: https://raw.githubusercontent.com/api-evangelist/sensu/refs/heads/main/screenshots/sensu-2026-09-02T154919.png
security:
- kind: authentication
  name: Sensu Authentication
  slug: sensu-authentication
  summary_line: http/apiKey/openIdConnect · 3 schemes
- kind: domain-security
  name: Sensu Domain Security
  slug: sensu-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sensu
tags:
- Company
- Monitoring
- Observability
- Infrastructure
- DevOps
- Metrics
- Event
- Alerting
- Monitoring as Code
- Kubernetes
website: https://sensu.io
---
