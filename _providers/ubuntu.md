---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ubuntu Agentic Access
  operation_count: 18
  slug: ubuntu-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 3
apis:
- description: API for managing Ubuntu Pro subscriptions and entitlements, including security patches, compliance tooling, and extended security maintenance.
  name: Ubuntu Pro API
  slug: ubuntu-pro-api
- description: Access to Ubuntu package repositories and archive information via the Launchpad API's Ubuntu distribution endpoint.
  name: Ubuntu Archive API
  slug: ubuntu-archive-api
- description: Systems management API for Ubuntu servers enabling automated patch management, compliance reporting, and fleet monitoring for Ubuntu deployments.
  name: Landscape API
  slug: landscape-api
- description: Metal as a Service API for physical server provisioning, enabling automated bare-metal infrastructure management and cloud-like workflows.
  name: MAAS API
  slug: maas-api
- description: Application modeling and deployment API supporting automated deployment, scaling, and management of applications across clouds and bare metal.
  name: Juju API
  slug: juju-api
- description: Bug tracking and management
  name: Ubuntu Bugs API
  slug: ubuntu-bugs-api
- description: Snap category listings
  name: Ubuntu Categories API
  slug: ubuntu-categories-api
- description: CVE security vulnerabilities
  name: Ubuntu CVEs API
  slug: ubuntu-cves-api
- description: Ubuntu distribution resources
  name: Ubuntu Distributions API
  slug: ubuntu-distributions-api
- description: Snap information and details
  name: Ubuntu Info API
  slug: ubuntu-info-api
- description: Snap usage metrics
  name: Ubuntu Metrics API
  slug: ubuntu-metrics-api
- description: Ubuntu Security Notices
  name: Ubuntu Notices API
  slug: ubuntu-notices-api
- description: Distribution package management
  name: Ubuntu Packages API
  slug: ubuntu-packages-api
- description: People and team resources
  name: Ubuntu People API
  slug: ubuntu-people-api
- description: Open-source project resources
  name: Ubuntu Projects API
  slug: ubuntu-projects-api
- description: Snap update and refresh operations
  name: Ubuntu Refresh API
  slug: ubuntu-refresh-api
- description: Snap search and discovery
  name: Ubuntu Search API
  slug: ubuntu-search-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ubuntu Security CVE Bugs API
  slug: open-ubuntu-bugs-api
- collection_type: open
  name: Ubuntu Security CVE Bugs Categories API
  slug: open-ubuntu-categories-api
- collection_type: open
  name: Ubuntu Security CVE API
  slug: open-ubuntu-cve
- collection_type: open
  name: Ubuntu Security CVE Bugs CVEs API
  slug: open-ubuntu-cves-api
- collection_type: open
  name: Ubuntu Security CVE Bugs Distributions API
  slug: open-ubuntu-distributions-api
- collection_type: open
  name: Ubuntu Security CVE Bugs Info API
  slug: open-ubuntu-info-api
- collection_type: open
  name: Launchpad REST API
  slug: open-ubuntu-launchpad
- collection_type: open
  name: Ubuntu Security CVE Bugs Metrics API
  slug: open-ubuntu-metrics-api
- collection_type: open
  name: Ubuntu Security CVE Bugs Notices API
  slug: open-ubuntu-notices-api
- collection_type: open
  name: Ubuntu Security CVE Bugs Packages API
  slug: open-ubuntu-packages-api
- collection_type: open
  name: Ubuntu Security CVE Bugs People API
  slug: open-ubuntu-people-api
- collection_type: open
  name: Ubuntu Security CVE Bugs Projects API
  slug: open-ubuntu-projects-api
- collection_type: open
  name: Ubuntu Security CVE Bugs Refresh API
  slug: open-ubuntu-refresh-api
- collection_type: open
  name: Ubuntu Security CVE Bugs Search API
  slug: open-ubuntu-search-api
- collection_type: open
  name: Snap Store Devices API
  slug: open-ubuntu-snap-store
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ubuntu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubuntu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ubuntu-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/ubuntu-linux
created: '2024-01-15'
description: Collection of APIs and services provided by Canonical for Ubuntu and related products. Includes the Snap Store API for package management, Launchpad API for project hosting and bug tracking, Ubuntu Security CVE API for vulnerability intelligence, and enterprise services including Ubuntu Pro, MAAS, Juju, and Landscape.
examples:
- key_count: 2
  name: Ubuntu Cve List Example
  slug: ubuntu-cve-list-example
- key_count: 2
  name: Ubuntu Snap Search Example
  slug: ubuntu-snap-search-example
finops:
- name: Ubuntu Finops
  service_category: Operating System / Security Maintenance
  slug: ubuntu-finops
image: https://assets.ubuntu.com/v1/29985a98-ubuntu-logo32.png
json_schemas:
- name: Ubuntu CVE
  property_count: 11
  slug: ubuntu-cve
- name: Snap Package
  property_count: 10
  slug: ubuntu-snap
json_structures:
- name: Ubuntu Snap Structure
  property_count: 0
  slug: ubuntu-snap-structure
jsonld:
- class_count: 8
  name: Ubuntu Context
  property_count: 18
  slug: ubuntu-context
layout: provider
modified: '2026-05-19'
name: Ubuntu
nav: Providers
network: true
overview: 'Ubuntu publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Bugs API, Categories API, CVEs API, and 9 more. Tagged areas include Cloud, Containers, DevOps, Enterprise, and Linux.


  The Ubuntu catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ubuntu''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Ubuntu Plans Pricing
  plan_count: 3
  slug: ubuntu-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Ubuntu Rate Limits
  slug: ubuntu-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ubuntu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ubuntu-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Ubuntu API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: ubuntu-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 41.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 69.3
    developer_ergonomics: 25.0
    discoverability: 81.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ubuntu/refs/heads/main/screenshots/ubuntu-2026-06-20T195936.png
security:
- kind: authentication
  name: Ubuntu Authentication
  slug: ubuntu-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ubuntu Domain Security
  slug: ubuntu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ubuntu
tags:
- Cloud
- Containers
- DevOps
- Enterprise
- Linux
- Security
- Ubuntu
- Package Management
- Open-Source
website: https://ubuntu.com
---
