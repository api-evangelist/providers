---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Alerta provides a RESTful API for alert management as described in the documentation.
  name: Alerta API
  slug: alerta-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/alerta/cli/alerta-cli.yml
  title: ''
  type: CLI
  url: cli/alerta-cli.yml
- group: operate
  href: https://artifacts.apis.io/alerta/changelog/alerta-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alerta-changelog.yml
- group: auth
  href: https://artifacts.apis.io/alerta/authentication/alerta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alerta-authentication.yml
- group: other
  href: https://artifacts.apis.io/alerta/hosts/alerta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alerta-hosts.yml
- group: other
  href: https://artifacts.apis.io/alerta/vendors/alerta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alerta-vendors.yml
- group: build
  href: https://artifacts.apis.io/alerta/packages/alerta-packages.yml
  title: ''
  type: SDKs
  url: packages/alerta-packages.yml
- group: build
  href: https://artifacts.apis.io/alerta/packages/alerta-packages.yml
  title: ''
  type: Packages
  url: packages/alerta-packages.yml
- group: auth
  href: https://artifacts.apis.io/alerta/security/alerta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alerta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alerta.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alerta.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.alerta.io/api/reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alerta.io/quick-start.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alerta
coverage:
  checked: '2026-10-26'
  detail: Documentation provides HTML reference but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is available.
  evidence:
  - status: 200
    url: https://docs.alerta.io/api/reference.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Alerta provides an open-source alert management system that aggregates alerts from various monitoring tools, supports deduplication, silencing, and routing via plugins. It offers a RESTful API, web UI, CLI, and SDKs for integration with systems like Prometheus, Grafana, Nagios, Zabbix, and many others. The platform enables teams to manage alert lifecycles, define custom views, and extend functionality through a rich plugin ecosystem.
layout: provider
modified: '2026-10-26'
name: Alerta
nav: Providers
network: true
overview: 'Alerta is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Alerting, Monitoring, OpenSource, and DevOps.


  Alerta''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 53.6
    operational_transparency: 21.1
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alerta Authentication
  slug: alerta-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Alerta Domain Security
  slug: alerta-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: alerta
tags:
- Company
- Alerting
- Monitoring
- OpenSource
- DevOps
- IncidentManagement
website: https://alerta.io/
---
