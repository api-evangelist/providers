---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: RESTful API for managing cluster resources, service groups, and cluster configuration.
  name: Veritas Cluster Server REST API
  slug: veritas-cluster-server-rest-api
- description: Python SDK for programmatic cluster management and automation.
  name: Veritas Cluster Server Python API
  slug: veritas-cluster-server-python-api
- description: Java-based API for integrating VCS management into enterprise applications.
  name: Veritas Cluster Server Java API
  slug: veritas-cluster-server-java-api
- description: Command-line tools for cluster administration and monitoring.
  name: Veritas Cluster Server Command Line Interface
  slug: veritas-cluster-server-command-line-interface
- description: SNMP-based monitoring interface for cluster health and status.
  name: Veritas Cluster Server SNMP Agent
  slug: veritas-cluster-server-snmp-agent
- description: REST API for InfoScale storage and cluster configuration and management operations, supporting storage provisioning, disk group management, and volume operations. Available in InfoScale 8.0 and 9.0.
  name: Veritas InfoScale REST API
  slug: veritas-infoscale-rest-api
- description: Web services API for InfoScale Operations Manager (VIOM) providing meta, query, update, and operations APIs for managing InfoScale objects over HTTPS. Supports management of hosts, clusters, LDEVs, an
  name: Veritas InfoScale Operations Manager Web Services API
  slug: veritas-infoscale-operations-manager-web-services-api
- description: InfoScale container support for Kubernetes and OpenShift, providing CSI-compliant storage drivers for dynamic and static provisioning, volume snapshots, and Prometheus metrics integration for monitori
  name: Veritas InfoScale for Kubernetes Environments
  slug: veritas-infoscale-for-kubernetes-environments
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/veritas-cluster-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veritas-cluster-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.veritas.com/support/en_US
- group: start
  title: ''
  type: Portal
  url: https://my.veritas.com/
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://www.veritas.com/support/en_US/article-search.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veritas.com/about/legal/license-agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veritas.com/about/legal/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://sort.veritas.com/documents/doc_details/via/8.0/Linux/Documentation/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.veritas.com/availability/infoscale/whats-new
- group: company
  title: ''
  type: Blog
  url: https://vox.veritas.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/VeritasTechLLC
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VeritasOS
created: '2024-01-15'
description: APIs for managing and monitoring Veritas Cluster Server (VCS) and InfoScale infrastructure, providing high availability, disaster recovery, and storage management capabilities across on-premises and containerized environments.
finops:
- name: Veritas Cluster Finops
  service_category: API
  slug: veritas-cluster-finops
image: /assets/icons/veritas-cluster.png
layout: provider
modified: '2026-04-19'
name: Veritas Cluster Server
nav: Providers
network: true
overview: 'Veritas Cluster Server publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Clustering, Containers, Disaster Recovery, Failover, and High Availability.


  Veritas Cluster Server''s developer surface includes support, developer portal, documentation, release notes, engineering blog, and 7 more developer resources.'
plans:
- name: Veritas Cluster Plans Pricing
  plan_count: 3
  slug: veritas-cluster-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 5
  name: Veritas Cluster Rate Limits
  slug: veritas-cluster-rate-limits
score:
  band: thin
  composite: 29.3
  delta: -1.2
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 25.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 30.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veritas-cluster/refs/heads/main/screenshots/veritas-cluster-2026-06-20T200934.png
security:
- kind: domain-security
  name: Veritas Cluster Domain Security
  slug: veritas-cluster-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Veritas Cluster Vulnerability Disclosure
  slug: veritas-cluster-vulnerability-disclosure
  summary_line: disclosure policy published
slug: veritas-cluster
tags:
- Clustering
- Containers
- Disaster Recovery
- Failover
- High Availability
- InfoScale
- Infrastructure Management
- Kubernetes
- Storage Management
- Veritas
website: https://my.veritas.com/
---
