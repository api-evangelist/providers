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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paviliondata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pavilion-hyperparallel-flash-array
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/pavilion-data_stock/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pavilion-data-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pavilion-data-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/pavilion-data-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pavilion-data-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: Pavilion Data Systems ceased operations on 2022-10-12; pavilion.io still resolves to two AWS addresses and publishes SPF/DMARC, but both A records refuse TCP 80 and 443 and every developer subdomain (docs, api, developer, portal, support, status) is NXDOMAIN.
  evidence:
  - status: 0
    url: https://pavilion.io/
  - status: 0
    url: https://pavilion.io/.well-known/agent-card.json
  - status: 0
    url: https://pavilion.io/openapi.json
  - status: 200
    url: https://github.com/paviliondata
  reason: defunct
  state: none
created: '2026-08-26'
description: Pavilion Data Systems was a San Jose, California storage company founded in 2014 by Kiran Malwankar, Sundar Kanthadai and VR Satish. It built the Pavilion HyperParallel Flash Array (HFA) — a rack-scale NVMe-over-Fabrics array with up to 20 controllers and 72 SSDs in a 4U chassis — running its own HyperOS storage operating system, later extended with the HyperParallel File System for AI, analytics and HPC workloads. The product datasheet advertised flexible management through a RESTful API, DMTF Redfish and SNIA Swordfish, a web GUI and a CLI, plus vCenter, Kubernetes and OpenStack integrations, but that management reference shipped with the appliance and was never published at a public developer URL. The company ceased operations on 12 October 2022 after attempts to sell the business and to raise a further round both failed, and pavilion.io no longer serves HTTP.
layout: provider
modified: '2026-08-26'
name: Pavilion
nav: Providers
network: true
overview: Pavilion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, Flash Storage, NVMe, and NVMe over Fabrics.
random_paper: 19
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Pavilion Data Domain Security
  slug: pavilion-data-domain-security
  summary_line: HSTS
slug: pavilion-data
tags:
- Company
- Storage
- Flash Storage
- NVMe
- NVMe over Fabrics
- Data Infrastructure
- Enterprise Hardware
- High Performance Computing
- Defunct
---
