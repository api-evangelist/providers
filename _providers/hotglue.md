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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Hotglue Agentic Access
  operation_count: 12
  slug: hotglue-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: The Hotglue API v1 provides the original REST API for managing integration flows, linked sources, linked targets, source state, and job execution.
  name: Hotglue API V1
  slug: hotglue-api-v1
- description: Retrieve available and supported connectors.
  name: Hotglue Connector Metadata API
  slug: hotglue-connector-metadata-api
- description: Manage bookmark and sync state for linked connectors.
  name: Hotglue Connector State API
  slug: hotglue-connector-state-api
- description: Trigger and poll connector discovery.
  name: Hotglue Discover API
  slug: hotglue-discover-api
- description: Run jobs for linked connectors.
  name: Hotglue Jobs API
  slug: hotglue-jobs-api
- description: Create, retrieve, update, and delete linked connectors for a tenant.
  name: Hotglue Linked Connectors API
  slug: hotglue-linked-connectors-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hotglue API V2 Connector Metadata API
  slug: open-hotglue-connector-metadata-api
- collection_type: open
  name: Hotglue API V2 Connector Metadata Connector State API
  slug: open-hotglue-connector-state-api
- collection_type: open
  name: Hotglue API V2 Connector Metadata Discover API
  slug: open-hotglue-discover-api
- collection_type: open
  name: Hotglue API V2 Connector Metadata Jobs API
  slug: open-hotglue-jobs-api
- collection_type: open
  name: Hotglue API V2 Connector Metadata Linked Connectors API
  slug: open-hotglue-linked-connectors-api
- collection_type: open
  name: Hotglue API V2
  slug: open-hotglue
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hotglue-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/hotglue-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hotglue-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hotglue-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hotglue-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hotgluexyz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hotglue
- group: company
  title: ''
  type: Website
  url: https://hotglue.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hotglue.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hotglue.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://hotglue.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://hotglue.com/signup
- group: start
  title: ''
  type: Login
  url: https://hotglue.com/login
- group: agent
  title: ''
  type: LlmsText
  url: https://hotglue.com/llms.txt
created: '2026-03-16'
description: Hotglue is an embedded iPaaS platform that enables SaaS products to offer native integrations to their customers. Built on the Python ecosystem, it provides a code-first approach with over 600 open-source connectors, a CLI for programmatic configuration management, detailed job logs, webhooks, and observability integrations. Hotglue allows developers to build flexible, scalable integrations without the lock-in of traditional iPaaS tools.
finops:
- name: Hotglue Finops
  service_category: API
  slug: hotglue-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hotglue.png
layout: provider
modified: '2026-05-19'
name: Hotglue
nav: Providers
network: true
overview: 'Hotglue publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Connector Metadata API, Connector State API, Discover API, and 2 more. Tagged areas include Connectors, Embedded Integrations, ETL, Integration Platform, and iPaaS.


  Hotglue''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, and 9 more developer resources.'
plans:
- name: Hotglue Plans Pricing
  plan_count: 3
  slug: hotglue-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Hotglue Rate Limits
  slug: hotglue-rate-limits
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 0.0
    contract_quality: 53.3
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hotglue/refs/heads/main/screenshots/hotglue-2026-06-20T182845.png
security:
- kind: authentication
  name: Hotglue Authentication
  slug: hotglue-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hotglue Domain Security
  slug: hotglue-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Hotglue Vulnerability Disclosure
  slug: hotglue-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Hotglue Trust Center
  slug: hotglue-trust-center
  summary_line: ISO 27001, GDPR
slug: hotglue
tags:
- Connectors
- Embedded Integrations
- ETL
- Integration Platform
- iPaaS
website: https://hotglue.com/
---
