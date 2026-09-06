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
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
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
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 35.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
