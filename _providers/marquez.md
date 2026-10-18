---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Open-source metadata service API
  name: Marquez API
  slug: marquez-api
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://marquezproject.ai/docs/faq
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/marquez/refs/heads/main/hosts/marquez-hosts.yml
  title: ''
  type: Hosts
  url: hosts/marquez-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/marquez/refs/heads/main/vendors/marquez-vendors.yml
  title: ''
  type: Vendors
  url: vendors/marquez-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://marquezproject.ai/blog/tags/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://marquezproject.ai/docs/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/marquez/refs/heads/main/security/marquez-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/marquez-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marquezproject.ai
- group: docs
  title: ''
  type: APIReference
  url: https://marquezproject.ai/docs/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://marquezproject.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MarquezProject
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/marquezproject/shared_invite/zt-2iylxasbq-GG_zXNcJdNrhC9uUMr3B7A
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://marquezproject.ai
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Marquez Project provides an open-source metadata service that implements the OpenLineage specification. It enables organizations to collect, store, and visualize lineage metadata from various data processing tools such as Airflow, Spark, Flink, dbt, and Dagster. The platform offers a RESTful API, a web UI for visual graphs, and integrations with Slack and GitHub, helping teams improve data governance, quality monitoring, and performance analytics.
image: https://marquezproject.ai/img/marquez-social-card.jpg
layout: provider
modified: '2026-10-13'
name: Marquez
nav: Providers
network: true
overview: 'Marquez is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Source, DataLineage, Metadata, and OpenLineage.


  Marquez''s developer surface includes documentation, changelog, getting-started guide, API reference, engineering blog, and 6 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Marquez Domain Security
  slug: marquez-domain-security
  summary_line: TLSv1.3
slug: marquez
tags:
- Company
- Open Source
- DataLineage
- Metadata
- OpenLineage
website: https://marquezproject.ai
---
