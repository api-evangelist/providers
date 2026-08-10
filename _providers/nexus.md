---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Nexus Agentic Access
  operation_count: 16
  slug: nexus-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 9
apis:
- description: Comprehensive REST API for managing repositories, components, assets, search, security, blob stores, capabilities, tasks, tags, staging, and scripts in Sonatype Nexus Repository Manager 3. The full Op
  name: Nexus Repository Manager REST API
  slug: nexus-rest-api
- description: The Assets API from Nexus Repository Manager — 2 operation(s) for assets.
  name: Nexus Repository Manager Assets API
  slug: nexus-assets-api
- description: The BlobStores API from Nexus Repository Manager — 1 operation(s) for blobstores.
  name: Nexus Repository Manager BlobStores API
  slug: nexus-blobstores-api
- description: The Components API from Nexus Repository Manager — 2 operation(s) for components.
  name: Nexus Repository Manager Components API
  slug: nexus-components-api
- description: The Repositories API from Nexus Repository Manager — 2 operation(s) for repositories.
  name: Nexus Repository Manager Repositories API
  slug: nexus-repositories-api
- description: The Search API from Nexus Repository Manager — 2 operation(s) for search.
  name: Nexus Repository Manager Search API
  slug: nexus-search-api
- description: The Security API from Nexus Repository Manager — 2 operation(s) for security.
  name: Nexus Repository Manager Security API
  slug: nexus-security-api
- description: The Status API from Nexus Repository Manager — 1 operation(s) for status.
  name: Nexus Repository Manager Status API
  slug: nexus-status-api
- description: The Tasks API from Nexus Repository Manager — 1 operation(s) for tasks.
  name: Nexus Repository Manager Tasks API
  slug: nexus-tasks-api
artifact_total: 16
collections:
- collection_type: open
  name: Sonatype Nexus Repository REST API
  slug: open-nexus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nexus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexus-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonatype
- group: company
  title: ''
  type: Website
  url: https://www.sonatype.com/products/nexus-repository
- group: docs
  title: ''
  type: Documentation
  url: https://help.sonatype.com/repomanager3
- group: operate
  title: ''
  type: Support
  url: https://support.sonatype.com
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sonatype.com/repomanager3/getting-started
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sonatype/nexus-public
- group: company
  title: ''
  type: Blog
  url: https://www.sonatype.com/blog/rss.xml
created: '2024-01-01'
description: Nexus Repository Manager by Sonatype is an enterprise-grade artifact repository manager supporting multiple package formats including Maven, npm, Docker, PyPI, NuGet, RubyGems, Helm, Go, and more. It provides a central hub for managing software supply chain components, proxying remote repositories, hosting private artifacts, and grouping repositories. Nexus exposes a comprehensive REST API documented via an OpenAPI/Swagger specification served at `<nexus_url>/service/rest/swagger.json` on each instance.
finops:
- name: Nexus Finops
  service_category: API
  slug: nexus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nexus.png
layout: provider
modified: '2026-04-28'
name: Nexus Repository Manager
nav: Providers
network: true
overview: 'Nexus Repository Manager publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Assets API, BlobStores API, Components API, and 5 more. Tagged areas include Artifact Management, DevOps, Docker, Maven, and Npm.


  Nexus Repository Manager''s developer surface includes authentication, documentation, support, getting-started guide, GitHub presence, engineering blog, and 4 more developer resources.'
plans:
- name: Nexus Plans Pricing
  plan_count: 3
  slug: nexus-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 5
  name: Nexus Rate Limits
  slug: nexus-rate-limits
score:
  band: thin
  composite: 40.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.4
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nexus/refs/heads/main/screenshots/nexus-2026-06-20T190305.png
security:
- kind: authentication
  name: Nexus Authentication
  slug: nexus-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Nexus Domain Security
  slug: nexus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nexus
tags:
- Artifact Management
- DevOps
- Docker
- Maven
- Npm
- Package Management
- Repository Manager
- Software Supply Chain
website: https://www.sonatype.com/products/nexus-repository
---
