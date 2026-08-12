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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Permutive Agentic Access
  operation_count: 23
  slug: permutive-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 6
apis:
- description: Create, read, update and delete audience cohorts.
  name: Permutive Cohorts API
  slug: permutive-cohorts-api
- description: Retrieve contextual cohort targeting values for ad-server integration.
  name: Permutive Contextual API
  slug: permutive-contextual-api
- description: Track first-party behavioural events into Permutive.
  name: Permutive Events API
  slug: permutive-events-api
- description: Create user IDs and associate identities with a Permutive user.
  name: Permutive Identity API
  slug: permutive-identity-api
- description: Cohort-based Segmentation (CCS) — evaluate a user's events into cohorts.
  name: Permutive Segmentation API
  slug: permutive-segmentation-api
- description: Manage second-party data imports and their segment taxonomy.
  name: Permutive Taxonomy API
  slug: permutive-taxonomy-api
artifact_total: 11
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/permutive-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.permutive.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.permutive.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.permutive.com/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.permutive.com/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/permutive-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://permutive.com/resources?category=blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/permutive-engineering
- group: operate
  title: ''
  type: Support
  url: https://support.permutive.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://permutive.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://permutive.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.permutive.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/permutive-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/permutive-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/permutive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/permutive-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/permutive-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/permutive-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/permutive-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/permutive-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/permutive-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/permutive-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/permutive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/permutive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://permutive.com/
created: '2026-07-17'
description: Permutive is an agentic data collaboration and activation platform for premium publishers, advertisers and agencies. Its platform spans a Data Management Platform, a Data Clean Room for privacy-safe collaboration with 150+ premium publishers, AI-curated audiences, and the Halo agentic suite that scales direct buying. The developer platform exposes REST APIs for event tracking, identity, audience cohort management, contextual segmentation and second-party data imports, plus web, mobile and CTV SDKs and an official Model Context Protocol (MCP) server that makes audience intelligence available to AI agents.
image: https://mintcdn.com/permutive/zX9G7jjpccuZZlEf/logo/permutive-logo-light.svg
layout: provider
mcp_servers:
- description: ''
  name: permutive-mcp.yml
  slug: permutive-mcpyml
modified: '2026-07-20'
name: Permutive
nav: Providers
network: true
overview: 'Permutive publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cohorts API, Contextual API, Events API, and 3 more. Tagged areas include Company, Publishing, Advertising, AdTech, and MarTech.


  Permutive''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, and 20 more developer resources.'
random_paper: 65
score:
  band: developing
  composite: 47.5
  delta: -0.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.7
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Permutive Authentication
  slug: permutive-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Permutive Domain Security
  slug: permutive-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Permutive Trust Center
  slug: permutive-trust-center
  summary_line: trust center published
slug: permutive
tags:
- Company
- Publishing
- Advertising
- AdTech
- MarTech
- Audience
- Data Collaboration
- Data Management Platform
- Contextual
- Identity
website: https://permutive.com/
---
