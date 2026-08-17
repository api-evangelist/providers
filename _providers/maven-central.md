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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Maven Central Agentic Access
  operation_count: 8
  slug: maven-central-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 3
apis:
- description: The Deployment API from Maven Central — 5 operation(s) for deployment.
  name: Maven Central Deployment API
  slug: maven-central-deployment-api
- description: The Download API from Maven Central — 1 operation(s) for download.
  name: Maven Central Download API
  slug: maven-central-download-api
- description: The Search API from Maven Central — 1 operation(s) for search.
  name: Maven Central Search API
  slug: maven-central-search-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sonatype Central Portal Publishing Deployment API
  slug: open-maven-central-deployment-api
- collection_type: open
  name: Sonatype Central Portal Publishing Deployment Download API
  slug: open-maven-central-download-api
- collection_type: open
  name: Sonatype Central Portal Publishing API
  slug: open-maven-central-portal
- collection_type: open
  name: Sonatype Central Portal Publishing Deployment Search API
  slug: open-maven-central-search-api
- collection_type: open
  name: Maven Central Search API
  slug: open-maven-central-search
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maven-central-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maven-central-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maven-central-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://central.sonatype.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://central.sonatype.org/publish/publish-guide/
- group: company
  title: ''
  type: Blog
  url: https://blog.sonatype.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.maven.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://central.sonatype.org/publish/terms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sonatype
- group: operate
  title: ''
  type: Support
  url: https://central.sonatype.org/support/
created: '2024-01-01'
description: Maven Central is the central repository for Java and other JVM-based artifacts, operated by Sonatype. It provides a REST API for searching artifact metadata and a publishing API for deploying open source libraries to the repository.
finops:
- name: Maven Central Finops
  service_category: API
  slug: maven-central-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maven-central.png
layout: provider
modified: '2026-05-19'
name: Maven Central
nav: Providers
network: true
overview: 'Maven Central publishes 3 APIs on the [APIs.io](https://apis.io/) network: Deployment API, Download API, and Search API. Tagged areas include Artifacts, Java, JVM, Maven, and Package Management.


  Maven Central''s developer surface includes authentication, developer portal, getting-started guide, engineering blog, support, and 5 more developer resources.'
plans:
- name: Maven Central Plans Pricing
  plan_count: 3
  slug: maven-central-plans-pricing
random_paper: 133
rate_limits:
- limit_count: 5
  name: Maven Central Rate Limits
  slug: maven-central-rate-limits
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 59.7
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maven-central/refs/heads/main/screenshots/maven-central-2026-06-20T185044.png
security:
- kind: authentication
  name: Maven Central Authentication
  slug: maven-central-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Maven Central Domain Security
  slug: maven-central-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maven-central
tags:
- Artifacts
- Java
- JVM
- Maven
- Package Management
- Repository
website: https://central.sonatype.com/
---
