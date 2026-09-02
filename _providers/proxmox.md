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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Proxmox Agentic Access
  operation_count: 8
  slug: proxmox-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- description: 'REST-style management API for Proxmox VE covering nodes, virtual machines, containers, storage, networking, clustering, pools, and access management. Authenticated via API tokens (PVEAPIToken header) '
  name: Proxmox VE API
  slug: ve-api
- description: The Access API from Proxmox VE — 3 operation(s) for access.
  name: Proxmox VE Access API
  slug: proxmox-access-api
- description: The Cluster API from Proxmox VE — 1 operation(s) for cluster.
  name: Proxmox VE Cluster API
  slug: proxmox-cluster-api
- description: The Containers API from Proxmox VE — 2 operation(s) for containers.
  name: Proxmox VE Containers API
  slug: proxmox-containers-api
- description: The Nodes API from Proxmox VE — 1 operation(s) for nodes.
  name: Proxmox VE Nodes API
  slug: proxmox-nodes-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Proxmox VE Access API
  slug: open-proxmox-access-api
- collection_type: open
  name: Proxmox VE Access Cluster API
  slug: open-proxmox-cluster-api
- collection_type: open
  name: Proxmox VE Access Containers API
  slug: open-proxmox-containers-api
- collection_type: open
  name: Proxmox VE Access Nodes API
  slug: open-proxmox-nodes-api
- collection_type: open
  name: Proxmox VE API
  slug: open-proxmox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/proxmox-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/proxmox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proxmox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/proxmox-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/proxmox
- group: company
  title: ''
  type: Website
  url: https://www.proxmox.com
- group: docs
  title: ''
  type: Documentation
  url: https://pve.proxmox.com/pve-docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.proxmox.com/en/proxmox-virtual-environment/pricing
- group: other
  title: ''
  type: Download
  url: https://www.proxmox.com/en/downloads
- group: other
  title: ''
  type: API Viewer
  url: https://pve.proxmox.com/pve-docs/api-viewer/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/proxmox
- group: operate
  title: ''
  type: Community Forum
  url: https://forum.proxmox.com
created: '2026-05-11'
description: Proxmox Virtual Environment (Proxmox VE) is an open-source server virtualization platform that combines KVM hypervisor and LXC containers, software-defined storage and networking, and clustering and high- availability features in a single web-managed solution. The Proxmox VE API exposes all platform operations under /api2/json on port 8006, including node, cluster, storage, pool, and access management endpoints. Supported authentication methods include stateless API tokens (PVEAPIToken header) and ticket-based sessions issued via /access/ticket.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/proxmox.png
layout: provider
modified: '2026-05-11'
name: Proxmox VE
nav: Providers
network: true
overview: 'Proxmox VE publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Access API, Cluster API, Containers API, and 1 more. Tagged areas include Virtualization, KVM, Containers, LXC, and Clustering.


  Proxmox VE''s developer surface includes authentication, documentation, pricing, GitHub presence, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 46.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/proxmox/refs/heads/main/screenshots/proxmox-2026-06-20T192222.png
security:
- kind: authentication
  name: Proxmox Authentication
  slug: proxmox-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Proxmox Domain Security
  slug: proxmox-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Proxmox Vulnerability Disclosure
  slug: proxmox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: proxmox
tags:
- Virtualization
- KVM
- Containers
- LXC
- Clustering
- Open-Source
website: https://www.proxmox.com
---
