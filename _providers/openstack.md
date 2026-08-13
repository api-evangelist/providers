---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Openstack Agentic Access
  operation_count: 41
  slug: openstack-agentic-access
  summary_line: 41 operations · 19 acting · 1 human-in-the-loop
api_count: 22
apis:
- description: Neutron provides networking as a service, exposing endpoints for networks, subnets, ports, routers, floating IPs, security groups, load balancers, firewalls, and VPN-as-a-Service.
  name: OpenStack Networking (Neutron) API
  slug: neutron
- description: Cinder provides persistent block-level storage volumes that can be attached to Nova instances. The v3 API exposes endpoints for volumes, snapshots, backups, volume types, attachments, transfers, and q
  name: OpenStack Block Storage (Cinder) API
  slug: cinder
- description: Swift is the OpenStack object storage service. The API exposes endpoints for accounts, containers, and objects with eventual- consistency replication, large-object support, and configurable access con
  name: OpenStack Object Storage (Swift) API
  slug: swift
- description: Glance manages disk and server images. The v2 API exposes endpoints for images, image members, image tags, image data upload/download, tasks, schemas, and metadata definitions.
  name: OpenStack Image (Glance) API
  slug: glance
- description: Heat is the OpenStack orchestration service that manages infrastructure-as-code deployments via HOT (Heat Orchestration Template) and AWS CloudFormation-compatible templates. The API exposes endpoints
  name: OpenStack Orchestration (Heat) API
  slug: heat
- description: Octavia provides Load Balancing as a Service. The v2 API exposes endpoints for load balancers, listeners, pools, members, health monitors, L7 policies and rules, and TLS containers.
  name: OpenStack Load Balancer (Octavia) API
  slug: octavia
- description: Designate is the OpenStack DNS-as-a-Service. The v2 API exposes endpoints for zones, recordsets, pools, transfers, and TSIG keys.
  name: OpenStack DNS (Designate) API
  slug: designate
- description: Trove is the OpenStack Database-as-a-Service that provisions and manages database instances (MySQL, PostgreSQL, MongoDB, Redis, MariaDB, Cassandra, etc.) on top of OpenStack.
  name: OpenStack Database (Trove) API
  slug: trove
- description: Domain management for multi-tenancy.
  name: OpenStack Domains API
  slug: openstack-domains-api
- description: Service endpoint URLs per region and interface.
  name: OpenStack Endpoints API
  slug: openstack-endpoints-api
- description: Compute instance flavors.
  name: OpenStack Flavors API
  slug: openstack-flavors-api
- description: Group management.
  name: OpenStack Groups API
  slug: openstack-groups-api
- description: Image references.
  name: OpenStack Images API
  slug: openstack-images-api
- description: SSH key pair management.
  name: OpenStack Keypairs API
  slug: openstack-keypairs-api
- description: Project (tenant) management.
  name: OpenStack Projects API
  slug: openstack-projects-api
- description: Role definitions and assignments.
  name: OpenStack Roles API
  slug: openstack-roles-api
- description: Lifecycle actions on servers.
  name: OpenStack Server Actions API
  slug: openstack-server-actions-api
- description: Compute instance management.
  name: OpenStack Servers API
  slug: openstack-servers-api
- description: Service catalog entries.
  name: OpenStack Services API
  slug: openstack-services-api
- description: Issue and validate authentication tokens.
  name: OpenStack Tokens API
  slug: openstack-tokens-api
- description: User management.
  name: OpenStack Users API
  slug: openstack-users-api
- description: API version discovery.
  name: OpenStack Versions API
  slug: openstack-versions-api
artifact_total: 33
collections:
- collection_type: open
  name: OpenStack Identity (Keystone) API v3
  slug: open-openstack-keystone
- collection_type: open
  name: OpenStack Compute (Nova) API
  slug: open-openstack-nova
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openstack-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openstack
- group: company
  title: ''
  type: Website
  url: https://www.openstack.org/
- group: start
  title: ''
  type: Portal
  url: https://docs.openstack.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openstack.org/api-ref/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.openstack.org/api-quick-start/
- group: operate
  title: ''
  type: Community
  url: https://www.openstack.org/community/
- group: company
  title: ''
  type: Blog
  url: https://www.openstack.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openstack
- group: build
  title: ''
  type: SourceCode
  url: https://opendev.org/openstack
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openstack.org/legal/
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: other
  title: ''
  type: Organization
  url: https://www.openstack.org/foundation/
created: '2025-01-01'
description: Open source cloud computing platform for building and managing public and private clouds, providing infrastructure as a service (IaaS) through a set of interrelated services including Compute (Nova), Object Storage (Swift), Block Storage (Cinder), Networking (Neutron), Identity (Keystone), Image (Glance), Orchestration (Heat), Database (Trove), DNS (Designate), and Load Balancer (Octavia). Each service exposes its own REST API; clients authenticate against Keystone and use the returned service catalog to discover per-region endpoints for the remaining services.
finops:
- name: Openstack Finops
  service_category: Infrastructure / IaaS
  slug: openstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openstack.png
json_schemas:
- name: OpenStack Nova Server
  property_count: 20
  slug: openstack-server
jsonld:
- class_count: 6
  name: Openstack Context
  property_count: 0
  slug: openstack-context
layout: provider
modified: '2026-05-19'
name: OpenStack
nav: Providers
network: true
overview: 'OpenStack publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Domains API, Endpoints API, Flavors API, and 11 more. Tagged areas include Cloud Platform, Infrastructure as a Service, Open Source, Virtualization, and Linux Foundation.


  The OpenStack catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenStack''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Openstack Plans Pricing
  plan_count: 1
  slug: openstack-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Openstack Rate Limits
  slug: openstack-rate-limits
rules:
- name: OpenStack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: openstack-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 62.3
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openstack/refs/heads/main/screenshots/openstack-2026-06-20T191039.png
security:
- kind: authentication
  name: Openstack Authentication
  slug: openstack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openstack Domain Security
  slug: openstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openstack
tags:
- Cloud Platform
- Infrastructure as a Service
- Open Source
- Virtualization
- Linux Foundation
website: https://www.openstack.org/
---
