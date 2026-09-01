---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-09-01'
api_count: 8
apis:
- description: The components API from Infinidat — 7 operation(s) for components.
  name: Infinidat Components API
  slug: infinidat-components-api
- description: The config API from Infinidat — 11 operation(s) for config.
  name: Infinidat Config API
  slug: infinidat-config-api
- description: The filesystems API from Infinidat — 2 operation(s) for filesystems.
  name: Infinidat Filesystems API
  slug: infinidat-filesystems-api
- description: The hosts API from Infinidat — 1 operation(s) for hosts.
  name: Infinidat Hosts API
  slug: infinidat-hosts-api
- description: The metadata API from Infinidat — 2 operation(s) for metadata.
  name: Infinidat Metadata API
  slug: infinidat-metadata-api
- description: The pools API from Infinidat — 1 operation(s) for pools.
  name: Infinidat Pools API
  slug: infinidat-pools-api
- description: The system API from Infinidat — 12 operation(s) for system.
  name: Infinidat System API
  slug: infinidat-system-api
- description: The users API from Infinidat — 2 operation(s) for users.
  name: Infinidat Users API
  slug: infinidat-users-api
artifact_total: 12
asyncapis:
- description: ''
  name: Infinidat Events
  slug: infinidat-events
collections:
- collection_type: open
  name: Infinidat InfiniBox REST API (7.3)
  slug: open-infinidat-infinibox
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/infinidat-infinibox-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.infinidat.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://support.infinidat.com/hc/en-us/categories/10106041231901-Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Infinidat/api_7_3
- group: start
  title: ''
  type: GettingStarted
  url: https://infinisdk.readthedocs.io/en/latest/getting_started.html
- group: operate
  title: ''
  type: Support
  url: https://support.infinidat.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.infinidat.com/en/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.infinidat.com/en/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Infinidat
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infinidat.com/en/sites/default/files/resource-pdfs/INFINIDAT-Customer-Product-Online-TCs.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infinidat.com/sites/default/files/resource-pdfs/Infinidat-Privacy-Policy.pdf
- group: build
  title: ''
  type: Postman
  url: postman/infinidat-infinibox-7-3-postman.json
- group: build
  title: ''
  type: Packages
  url: packages/infinidat-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/infinidat-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/infinidat-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/infinidat-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infinidat-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infinidat-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infinidat-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infinidat-data-model.yml
- group: other
  title: ''
  type: Events
  url: asyncapi/infinidat-events.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infinidat-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/infinidat-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infinidat-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infinidat-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infinidat-domain-security.yml
created: '2026-08-01'
description: 'Infinidat is an enterprise storage vendor — a Lenovo company since April 2026 — building petabyte-scale primary storage, all-flash arrays and cyber-resilient backup appliances: InfiniBox and InfiniBox SSA for primary block and file workloads, InfiniGuard for backup and rapid recovery, and the InfiniSafe cyber-resilience layer with immutable snapshots, logical air-gapping, a fenced forensic environment and cyber detection. Every InfiniBox array serves its own management REST API (InfiniAPI) at https://<array>/api/rest, alongside the InfiniShell CLI and an HTML5 GUI. Infinidat publishes a first-party Postman collection for the InfiniBox 7.3 API, the InfiniSDK Python SDK, an Ansible collection, a Kubernetes CSI driver and an OpenStack Cinder driver on GitHub.'
image: https://www.infinidat.com/themes/sitetheme/images/opengraph.jpg
layout: provider
modified: '2026-08-01'
name: Infinidat
nav: Providers
network: true
overview: 'Infinidat publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Components API, Config API, Filesystems API, and 5 more. Tagged areas include Company, Storage, Enterprise Storage, Data Infrastructure, and Data Protection.


  The Infinidat catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Infinidat''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 20 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 59.0
    developer_ergonomics: 68.5
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 43.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infinidat/refs/heads/main/screenshots/infinidat-2026-08-07T170658.png
security:
- kind: authentication
  name: Infinidat Authentication
  slug: infinidat-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Infinidat Domain Security
  slug: infinidat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: infinidat
tags:
- Company
- Storage
- Enterprise Storage
- Data Infrastructure
- Data Protection
- Cyber Resilience
- Backup and Recovery
- Kubernetes
- Infrastructure
- On-Premises
website: https://www.infinidat.com/en
---
