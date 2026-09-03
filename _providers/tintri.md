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
  band: human-only
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
  score: 3.4
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Tintri REST API (version v310.91, mapping to TXOS 4.5 and Tintri Global Center 4.1+) runs on each VMstore appliance and TGC instance. It is session-authenticated (POST /api/v310/session/login with
  name: Tintri VMstore REST API
  slug: tintri-vmstore-rest-api
artifact_total: 4
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Tintri/tintri-rest-api/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/Tintri/tintri-rest-api/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tintri-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tintri.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tintri.github.io/tintri-rest-api/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://tintri.github.io/tintri-rest-api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://tintri.github.io/tintri-rest-api/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tintri
- group: company
  title: ''
  type: Blog
  url: https://tintri.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://tintri.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tintri.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tintri.com/terms-of-use/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Tintri/tintri-rest-api
- group: build
  title: ''
  type: Packages
  url: packages/tintri-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tintri-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tintri-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tintri-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tintri-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tintri-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tintri-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tintri-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tintri-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tintri-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Tintri, now part of DDN, builds intelligent enterprise data-management and storage infrastructure: the VMstore virtualization-aware storage platform, the Tintri Cloud Platform (TCP) and Cloud Engine (TCE), and the Tintri Global Center (TGC) management fabric. Tintri exposes a versioned, session-authenticated REST API (v310) on every VMstore appliance and TGC instance, letting operators automate VM- and virtual-disk-level provisioning, snapshots, replication, QoS, alerting, and per-VM analytics. First-party automation ships as a Python SDK (PySDK), a PowerShell Automation Toolkit, Ansible playbooks, and Kubernetes CSI and OpenStack Cinder storage drivers, all published in the public Tintri GitHub organization alongside the REST API reference and code examples.'
image: https://tintri.github.io/tintri-rest-api/TintriLogo-300.png
layout: provider
mcp_servers:
- description: Candidate Model Context Protocol server for the Tintri VMstore REST API. Tintri publishes no official hosted/remote MCP server; this is a derived candidate tool list mapped from the documented v310 RE
  name: Tintri MCP Server
  slug: tintri-mcp-server
modified: '2026-07-21'
name: Tintri
nav: Providers
network: true
overview: 'Tintri publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, Data Management, Infrastructure, and Virtualization.


  Tintri''s developer surface includes documentation, API reference, engineering blog, support, getting-started guide, authentication, and 18 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  open_source:
    applies: true
    score: 0.0
  previous_composite: 22.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tintri/refs/heads/main/screenshots/tintri-2026-09-02T163809.png
security:
- kind: authentication
  name: Tintri Authentication
  slug: tintri-authentication
  summary_line: session · 1 scheme
- kind: domain-security
  name: Tintri Domain Security
  slug: tintri-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tintri
tags:
- Company
- Storage
- Data Management
- Infrastructure
- Virtualization
- Cloud
- Kubernetes
- DevOps
- Enterprise
- REST API
website: https://tintri.com/
---
