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
- description: API reference for Apache Polaris data platform, documented at the official docs site.
  name: Apache Polaris API
  slug: apache-polaris-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apache-polaris/refs/heads/main/well-known/apache-polaris-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apache-polaris-status-security.txt
- group: auth
  title: ''
  type: Security
  url: https://security.apache.org/report/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apache-polaris/refs/heads/main/well-known/apache-polaris-apache-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apache-polaris-apache-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apache-polaris/refs/heads/main/well-known/apache-polaris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apache-polaris-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apache-polaris/refs/heads/main/hosts/apache-polaris-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apache-polaris-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apache-polaris/refs/heads/main/vendors/apache-polaris-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apache-polaris-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apache-polaris/refs/heads/main/packages/apache-polaris-packages.yml
  title: ''
  type: SDKs
  url: packages/apache-polaris-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apache-polaris/refs/heads/main/packages/apache-polaris-packages.yml
  title: ''
  type: Packages
  url: packages/apache-polaris-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apache.org/
- group: operate
  title: ''
  type: ChangeLog
  url: https://polaris.apache.org/releases/
- group: docs
  title: ''
  type: APIReference
  url: https://polaris.apache.org/releases/1.4.0/helm-chart/reference/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apache-polaris/refs/heads/main/security/apache-polaris-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-polaris-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apache-polaris/refs/heads/main/security/apache-polaris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apache-polaris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://polaris.apache.org
- group: docs
  title: ''
  type: Documentation
  url: https://polaris.apache.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://polaris.apache.org/guides/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://polaris.apache.org/community/
- group: company
  title: ''
  type: Blog
  url: https://polaris.apache.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/polaris
coverage:
  checked: '2026-10-13'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://polaris.apache.org/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Apache Polaris is an open‑source, cloud‑native data platform project under the Apache Software Foundation. It provides a unified catalog, governance, and data management capabilities across multiple storage backends such as Apache Ozone, Ceph, and RustFS. Polaris supports analytics engines like Spark, Trino, and Flink, and includes tools for migration, benchmarking, and synchronization. The project aims to simplify data lake management, enable observability via Prometheus and Jaeger, and integrate with authentication providers like Keycloak.
layout: provider
modified: '2026-10-13'
name: Apache Polaris
nav: Providers
network: true
overview: 'Apache Polaris is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Platform, Open Source, Cloud-Native, and Apache.


  Apache Polaris'' developer surface includes changelog, API reference, documentation, getting-started guide, support, engineering blog, and 13 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 53.6
    operational_transparency: 47.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apache Polaris Domain Security
  slug: apache-polaris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Polaris Vulnerability Disclosure
  slug: apache-polaris-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-polaris
tags:
- Company
- Data Platform
- Open Source
- Cloud-Native
- Apache
website: https://polaris.apache.org
---
