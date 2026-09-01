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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 3
  name: Upbound Agentic Access
  operation_count: 23
  slug: upbound-agentic-access
  summary_line: 23 operations · 13 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: Managed control plane lifecycle
  name: Upbound Control Planes API
  slug: upbound-control-planes-api
- description: Organization management
  name: Upbound Organizations API
  slug: upbound-organizations-api
- description: Package registry and repository management
  name: Upbound Repositories API
  slug: upbound-repositories-api
- description: Robot account and token management
  name: Upbound Robots API
  slug: upbound-robots-api
- description: Team and membership management
  name: Upbound Teams API
  slug: upbound-teams-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Upbound Control Planes API
  slug: open-upbound-control-planes-api
- collection_type: open
  name: Upbound Control Planes Organizations API
  slug: open-upbound-organizations-api
- collection_type: open
  name: Upbound Control Planes Repositories API
  slug: open-upbound-repositories-api
- collection_type: open
  name: Upbound Control Planes Robots API
  slug: open-upbound-robots-api
- collection_type: open
  name: Upbound Control Planes Teams API
  slug: open-upbound-teams-api
- collection_type: open
  name: Upbound API
  slug: open-upbound
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/upbound-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/upbound-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upbound-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upbound-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.upbound.io/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upbound-io
- group: company
  title: ''
  type: Website
  url: https://www.upbound.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.upbound.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upbound
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.upbound.io
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/upbound/marketplace-mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.upbound.io/llms.txt
created: '2026-03-27'
description: Upbound is a universal cloud platform built on Crossplane, providing managed control planes and a marketplace for cloud infrastructure APIs. The Upbound API enables programmatic management of organizations, spaces, control planes, package repositories, teams, and robot accounts.
examples:
- key_count: 2
  name: Upbound Create Control Plane Example
  slug: upbound-create-control-plane-example
- key_count: 2
  name: Upbound List Control Planes Example
  slug: upbound-list-control-planes-example
finops:
- name: Upbound Finops
  service_category: API
  slug: upbound-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upbound.png
json_schemas:
- name: Upbound Control Plane
  property_count: 11
  slug: upbound-control-plane
json_structures:
- name: Upbound Control Plane Structure
  property_count: 0
  slug: upbound-control-plane-structure
jsonld:
- class_count: 5
  name: Upbound Context
  property_count: 15
  slug: upbound-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Upbound
nav: Providers
network: true
overview: 'Upbound publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Control Planes API, Organizations API, Repositories API, and 2 more. Tagged areas include Cloud Infrastructure, Crossplane, Developer Experience, Internal Developer Platform, and Platform Engineering.


  The Upbound catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Upbound''s developer surface includes authentication, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Upbound Plans Pricing
  plan_count: 3
  slug: upbound-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Upbound Rate Limits
  slug: upbound-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Upbound API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: upbound-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Upbound API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 7
  slug: upbound-rules
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 67.1
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 36.9
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
screenshot: https://raw.githubusercontent.com/api-evangelist/upbound/refs/heads/main/screenshots/upbound-2026-06-20T200438.png
security:
- kind: authentication
  name: Upbound Authentication
  slug: upbound-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Upbound Domain Security
  slug: upbound-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Upbound Trust Center
  slug: upbound-trust-center
  summary_line: SOC 2, ISO 27001
slug: upbound
tags:
- Cloud Infrastructure
- Crossplane
- Developer Experience
- Internal Developer Platform
- Platform Engineering
website: https://www.upbound.io
---
