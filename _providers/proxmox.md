---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
- baseURL: https://your.server:8006/api2/json
  baseurl_source: declared
  description: The Access API from Proxmox VE — 3 operation(s) for access.
  name: Proxmox VE Access API
  slug: proxmox-access-api
- baseURL: https://your.server:8006/api2/json
  baseurl_source: declared
  description: The Cluster API from Proxmox VE — 1 operation(s) for cluster.
  name: Proxmox VE Cluster API
  slug: proxmox-cluster-api
- baseURL: https://your.server:8006/api2/json
  baseurl_source: declared
  description: The Containers API from Proxmox VE — 2 operation(s) for containers.
  name: Proxmox VE Containers API
  slug: proxmox-containers-api
- baseURL: https://your.server:8006/api2/json
  baseurl_source: declared
  description: The Nodes API from Proxmox VE — 1 operation(s) for nodes.
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
