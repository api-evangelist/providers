---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for the AMD Pensando Policy and Services Manager control plane — manage clusters, networks, security policy, and services on Pensando DPUs. The API is served per-appliance; live interactive d
  name: AMD Pensando Policy and Services Manager (PSM) REST API
  slug: amd-pensando-policy-and-services-manager-psm-rest-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://amd.com/pensando
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pensando
- group: build
  title: ''
  type: SDKs
  url: packages/pensando-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/pensando-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pensando-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pensando-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pensando-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pensando-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pensando-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pensando-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pensando-llms.txt
created: '2026-07-17'
description: AMD Pensando (formerly Pensando Systems, acquired by AMD in 2022) builds programmable Distributed Services Cards (DPUs) and the Policy and Services Manager (PSM) control plane that operates them across cloud, distributed services switch, and enterprise deployments. PSM exposes a REST API — surfaced through auto-generated, first-party Python bindings on PyPI (pensando-cloud, pensando-dss, pensando-ent) and a Terraform provider — for managing clusters, networks, security policy, and services on Pensando infrastructure. Originally surfaced as a portfolio company of GV and Lightspeed Venture Partners and added to the API Evangelist network for enrichment.
image: https://avatars.githubusercontent.com/u/24572811
layout: provider
modified: '2026-07-21'
name: Pensando *
nav: Providers
network: true
overview: 'Pensando * publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Networking, DPU, and Infrastructure.


  Pensando *''s developer surface includes authentication and 10 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Pensando Authentication
  slug: pensando-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pensando Domain Security
  slug: pensando-domain-security
  summary_line: DMARC
slug: pensando
tags:
- Company
- Enterprise
- Networking
- DPU
- Infrastructure
- Cloud
- Security
- AMD
website: https://amd.com/pensando
---
