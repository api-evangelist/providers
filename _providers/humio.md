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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Humio (Falcon LogScale) REST + GraphQL API. The REST API covers streaming ingest (structured, unstructured, Splunk HEC, and Elastic bulk endpoints) and search/query jobs against repositories; the Grap
  name: Humio API
  slug: humio-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/crowdstrike/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.humio.com
- group: other
  title: ''
  type: Product
  url: https://www.crowdstrike.com/products/next-gen-siem/falcon-logscale/
- group: docs
  title: ''
  type: Documentation
  url: https://library.humio.com/stable/
- group: docs
  title: ''
  type: APIReference
  url: https://library.humio.com/stable/docs/api/
- group: company
  title: ''
  type: Blog
  url: https://www.crowdstrike.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/humio
- group: build
  title: ''
  type: SDKs
  url: packages/humio-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/humio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/humio-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/humio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/humio-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/humio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.crowdstrike.com/report-a-security-bug/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/humio-llms.txt
created: '2026-07-17'
description: Humio is a log management and observability platform built for ingesting, storing, and searching machine data in real time at scale. Backed by Accel and acquired by CrowdStrike in 2021, Humio is now delivered as CrowdStrike Falcon LogScale. It provides high-throughput streaming ingest (including Splunk HEC and Elastic bulk compatible endpoints), a live query language for dashboards and alerts, and index-free retention. Developers integrate through a REST API for ingest and search plus a GraphQL API for administration (repositories, parsers, users, ingest tokens), with official client libraries for Python, Node.js, Go, and JavaScript and the humioctl command-line client.
image: https://avatars.githubusercontent.com/u/16662354?v=4
layout: provider
modified: '2026-07-19'
name: Humio
nav: Providers
network: true
overview: 'Humio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Big Data, Log Management, Observability, and Logging.


  Humio''s developer surface includes documentation, API reference, engineering blog, CLI, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 16.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humio/refs/heads/main/screenshots/humio-2026-07-25T221712.png
security:
- kind: domain-security
  name: Humio Domain Security
  slug: humio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Humio Vulnerability Disclosure
  slug: humio-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: humio
tags:
- Company
- Big Data
- Log Management
- Observability
- Logging
- SIEM
- Monitoring
- Security
website: https://www.humio.com
---
