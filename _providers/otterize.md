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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://otterize.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.otterize.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.otterize.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.otterize.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/otterize
- group: operate
  title: ''
  type: Support
  url: https://joinslack.otterize.com
- group: build
  title: ''
  type: Packages
  url: packages/otterize-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/otterize-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/otterize-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/otterize-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/otterize-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/otterize-llms.txt
created: '2026-07-17'
description: 'Otterize is an open-source, Kubernetes-native platform for intent-based access control (IBAC). Application teams declare which services need to talk to which other services using ClientIntents, and Otterize automatically calculates, provisions, and enforces the underlying access controls: Kubernetes NetworkPolicies, AWS/GCP/Azure IAM, Istio Authorization Policies, Kafka ACLs, and MySQL/PostgreSQL grants. It ships three open-source operators (intents operator, credentials operator, network mapper) deployed via Helm, a Go CLI, and a managed Otterize Cloud. Its developer surface is the CLI, Kubernetes Custom Resources, and Helm/Terraform tooling rather than a public REST API. Otterize was surfaced as an Index Ventures portfolio company; otterize.com now redirects to Cyera following acquisition, while the open-source components, documentation, and CLI remain live.'
image: https://avatars.githubusercontent.com/otterize
layout: provider
modified: '2026-07-20'
name: Otterize
nav: Providers
network: true
overview: 'Otterize is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, Kubernetes, Access Control, and Cloud Native Security.


  Otterize''s developer surface includes documentation, getting-started guide, support, CLI, changelog, authentication, and 6 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 18.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/otterize/refs/heads/main/screenshots/otterize-2026-08-07T191031.png
security:
- kind: authentication
  name: Otterize Authentication
  slug: otterize-authentication
  summary_line: oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Otterize Domain Security
  slug: otterize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: otterize
tags:
- Company
- Business Applications
- Kubernetes
- Access Control
- Cloud Native Security
- Zero Trust
- DevSecOps
- IAM
- Open-Source
website: https://otterize.com/
---
