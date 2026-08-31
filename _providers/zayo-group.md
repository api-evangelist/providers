---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zayo Group Agentic Access
  operation_count: 1
  slug: zayo-group-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Zayo Group Holdings API provides access to platform services and data for enterprise integration and automation.
  name: Zayo Group Holdings API
  slug: zayo-group-api
- description: Building validation and location lookup.
  name: Zayo Group Holdings Network Discovery API
  slug: zayo-group-network-discovery-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zayo Group Network Discovery API
  slug: open-zayo-group-network-discovery-api
- collection_type: open
  name: Zayo Group API
  slug: open-zayo-group
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zayo-group-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zayo-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zayo-group-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zayo-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zayo-group-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zayo-group
- group: company
  title: ''
  type: Website
  url: https://www.zayo.com
- group: company
  title: ''
  type: Blog
  url: https://www.zayo.com/feed/
created: '2026-04-19'
description: Zayo Group Holdings is a major US corporation and Fortune 1000 company. The Zayo Group Holdings API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Zayo Group Finops
  service_category: Network Connectivity
  slug: zayo-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zayo-group.png
layout: provider
modified: '2026-04-19'
name: Zayo Group Holdings
nav: Providers
network: true
overview: 'Zayo Group Holdings publishes 1 API on the [APIs.io](https://apis.io/) network: Network Discovery API. Tagged areas include Fiber, Network, and Infrastructure.


  Zayo Group Holdings'' developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Zayo Group Plans Pricing
  plan_count: 1
  slug: zayo-group-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Zayo Group Rate Limits
  slug: zayo-group-rate-limits
scopes:
- name: Zayo Group Scopes
  scope_count: 1
  slug: zayo-group-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 13.6
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zayo-group/refs/heads/main/screenshots/zayo-group-2026-06-20T201802.png
security:
- kind: authentication
  name: Zayo Group Authentication
  slug: zayo-group-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zayo Group Domain Security
  slug: zayo-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zayo Group Vulnerability Disclosure
  slug: zayo-group-vulnerability-disclosure
  summary_line: disclosure policy published
slug: zayo-group
tags:
- Fiber
- Network
- Infrastructure
website: https://www.zayo.com
---
