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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Maven Agentic Access
  operation_count: 8
  slug: maven-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 3
apis:
- description: The Deployment API from Maven — 5 operation(s) for deployment.
  name: Maven Deployment API
  slug: maven-deployment-api
- description: The Download API from Maven — 1 operation(s) for download.
  name: Maven Download API
  slug: maven-download-api
- description: The Search API from Maven — 1 operation(s) for search.
  name: Maven Search API
  slug: maven-search-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sonatype Central Portal Publishing Deployment API
  slug: open-maven-deployment-api
- collection_type: open
  name: Sonatype Central Portal Publishing Deployment Download API
  slug: open-maven-download-api
- collection_type: open
  name: Sonatype Central Portal Publishing API
  slug: open-maven-portal
- collection_type: open
  name: Sonatype Central Portal Publishing Deployment Search API
  slug: open-maven-search-api
- collection_type: open
  name: Maven Central Search API
  slug: open-maven-search
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maven-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/maven-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maven-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maven-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maven-hq
- group: company
  title: ''
  type: Website
  url: https://maven.apache.org
- group: docs
  title: ''
  type: Documentation
  url: https://maven.apache.org/guides/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/maven
- group: operate
  title: ''
  type: Support
  url: https://maven.apache.org/mailing-lists.html
created: '2024-01-01'
description: Apache Maven is a software project management and build automation tool used primarily for Java projects. Maven Central is the default artifact repository for Maven, and Sonatype provides REST APIs for searching and publishing artifacts to Maven Central.
finops:
- name: Maven Finops
  service_category: API
  slug: maven-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maven.png
layout: provider
modified: '2026-05-19'
name: Maven
nav: Providers
network: true
overview: 'Maven publishes 3 APIs on the [APIs.io](https://apis.io/) network: Deployment API, Download API, and Search API. Tagged areas include Artifacts, Build Tools, Java, Maven, and Package Management.


  Maven''s developer surface includes authentication, documentation, support, and 6 more developer resources.'
plans:
- name: Maven Plans Pricing
  plan_count: 3
  slug: maven-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Maven Rate Limits
  slug: maven-rate-limits
score:
  band: thin
  composite: 30.8
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maven/refs/heads/main/screenshots/maven-2026-06-20T185043.png
security:
- kind: authentication
  name: Maven Authentication
  slug: maven-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Maven Domain Security
  slug: maven-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Maven Vulnerability Disclosure
  slug: maven-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: maven
tags:
- Artifacts
- Build Tools
- Java
- Maven
- Package Management
- Repository
website: https://maven.apache.org
---
