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
api_count: 7
apis:
- description: RESTful API for managing storage volumes, disk groups, and storage operations.
  name: Veritas Volume Manager REST API
  slug: veritas-volume-manager-rest-api
- description: Command-line interface and scripting API for Veritas Volume Manager operations.
  name: VxVM Command Line API
  slug: vxvm-command-line-api
- description: Comprehensive API for Veritas Storage Foundation including volume management.
  name: Storage Foundation API
  slug: storage-foundation-api
- description: 'REST API for InfoScale storage configuration and management operations including volume, disk group, and cluster management. The REST server is configured on cluster nodes and supports operations for '
  name: Veritas InfoScale REST API
  slug: veritas-infoscale-rest-api
- description: REST API support for InfoScale 9.0 providing storage configuration and management operations, including HA configuration for the REST server and expanded supported operations for enterprise storage ma
  name: Veritas InfoScale 9.0 REST API
  slug: veritas-infoscale-90-rest-api
- description: HTTPS-based Web Services API for Veritas InfoScale Operations Manager (VIOM) providing the ability to query discovered data, manage user-defined attributes, and perform operations on InfoScale objects
  name: InfoScale Operations Manager Web Services API
  slug: infoscale-operations-manager-web-services-api
- description: API for administering and monitoring InfoScale in Kubernetes and OpenShift container environments. Provides CSI driver integration for persistent storage, volume snapshots, and storage class managemen
  name: InfoScale for Kubernetes API
  slug: infoscale-for-kubernetes-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/veritas-volume-manager-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veritas-volume-manager-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://my.veritas.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.veritas.com/support/en_US/article.GETSTART100
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veritas.com/about/legal/license-agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veritas.com/about/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.veritas.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.veritas.com/support/en_US/article.CHANGELOG
- group: company
  title: ''
  type: Blog
  url: https://www.veritas.com/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.veritas.com/support/en_US/dpp.InfoScaleStorageFoundation
created: '2024-01-01'
description: APIs for managing storage volumes, disk groups, and file systems using Veritas Volume Manager (VVM).
finops:
- name: Veritas Volume Manager Finops
  service_category: API
  slug: veritas-volume-manager-finops
image: https://www.veritas.com/content/dam/veritas/images/logos/veritas-logo.svg
layout: provider
modified: '2026-04-19'
name: Veritas Volume Manager
nav: Providers
network: true
overview: 'Veritas Volume Manager publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Disaster Recovery, Enterprise Storage, File Systems, Storage, and Volume Management.


  Veritas Volume Manager''s developer surface includes developer portal, getting-started guide, changelog, engineering blog, support, and 5 more developer resources.'
plans:
- name: Veritas Volume Manager Plans Pricing
  plan_count: 3
  slug: veritas-volume-manager-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Veritas Volume Manager Rate Limits
  slug: veritas-volume-manager-rate-limits
score:
  band: thin
  composite: 30.5
  delta: -1.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 28.6
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veritas-volume-manager/refs/heads/main/screenshots/veritas-volume-manager-2026-06-20T200935.png
security:
- kind: domain-security
  name: Veritas Volume Manager Domain Security
  slug: veritas-volume-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Veritas Volume Manager Vulnerability Disclosure
  slug: veritas-volume-manager-vulnerability-disclosure
  summary_line: disclosure policy published
slug: veritas-volume-manager
tags:
- Disaster Recovery
- Enterprise Storage
- File Systems
- Storage
- Volume Management
website: https://my.veritas.com
---
