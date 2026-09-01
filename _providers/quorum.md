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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Quorum Agentic Access
  operation_count: 9
  slug: quorum-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 1
apis:
- description: Quorum Royalty Accounting API enables access to royalty payment calculations, owner statements, suspense management, and title data for oil and gas mineral rights owners and operators.
  name: Quorum Royalty Accounting API
  slug: quorum-royalty-accounting-api
- description: Quorum Production Reporting API provides access to well production volumes, allocations, gas balancing, and regulatory reporting data for upstream oil and gas operations.
  name: Quorum Production Reporting API
  slug: quorum-production-reporting-api
- description: Division order management
  name: Quorum Software DivisionOrders API
  slug: quorum-divisionorders-api
- description: Oil and gas lease management
  name: Quorum Software Leases API
  slug: quorum-leases-api
- description: Mineral interest owner management
  name: Quorum Software Owners API
  slug: quorum-owners-api
- description: Land tract records
  name: Quorum Software Tracts API
  slug: quorum-tracts-api
- description: Well master data
  name: Quorum Software Wells API
  slug: quorum-wells-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quorum Land Management DivisionOrders API
  slug: open-quorum-divisionorders-api
- collection_type: open
  name: Quorum Land Management API
  slug: open-quorum-land-management
- collection_type: open
  name: Quorum Land Management DivisionOrders Leases API
  slug: open-quorum-leases-api
- collection_type: open
  name: Quorum Land Management DivisionOrders Owners API
  slug: open-quorum-owners-api
- collection_type: open
  name: Quorum Land Management DivisionOrders Tracts API
  slug: open-quorum-tracts-api
- collection_type: open
  name: Quorum Land Management DivisionOrders Wells API
  slug: open-quorum-wells-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quorum-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/quorum-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quorum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quorum-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/quorum-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QuorumUS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quorum-software
- group: start
  title: ''
  type: Portal
  url: https://www.quorumsoftware.com/
- group: company
  title: ''
  type: Website
  url: https://www.quorumsoftware.com/
- group: operate
  title: ''
  type: Support
  url: https://community.quorumsoftware.com/s/login/
- group: company
  title: ''
  type: Blog
  url: https://resources.quorumsoftware.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quorumsoftware.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quorumsoftware.com/terms-and-conditions/
created: '2026-03-18'
description: Quorum Software is a leading provider of energy software for upstream oil and gas operations, providing solutions for land management, royalty accounting, production reporting, and operational data management.
finops:
- name: Quorum Finops
  service_category: Energy Software
  slug: quorum-finops
image: https://www.quorumsoftware.com/hubfs/quorum-logo.svg
json_schemas:
- name: Quorum Oil & Gas Lease
  property_count: 19
  slug: quorum-lease
jsonld:
- class_count: 0
  name: Quorum Context
  property_count: 35
  slug: quorum-context
layout: provider
modified: '2026-05-19'
name: Quorum Software
nav: Providers
network: true
overview: 'Quorum Software publishes 5 APIs on the [APIs.io](https://apis.io/) network, including DivisionOrders API, Leases API, Owners API, and 2 more. Tagged areas include Energy, Oil and Gas, Upstream, Land Management, and Royalty Accounting.


  The Quorum Software catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Quorum Software''s developer surface includes authentication, developer portal, support, engineering blog, and 9 more developer resources.'
plans:
- name: Quorum Plans Pricing
  plan_count: 1
  slug: quorum-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Quorum Rate Limits
  slug: quorum-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Quorum Software API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: quorum-jsonschema-spectral-rules
scopes:
- name: Quorum Scopes
  scope_count: 2
  slug: quorum-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 58.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 9.8
    contract_quality: 62.0
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quorum/refs/heads/main/screenshots/quorum-2026-06-20T192444.png
security:
- kind: authentication
  name: Quorum Authentication
  slug: quorum-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Quorum Domain Security
  slug: quorum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Quorum Trust Center
  slug: quorum-trust-center
  summary_line: SOC 2, ISO 27001
slug: quorum
tags:
- Energy
- Oil and Gas
- Upstream
- Land Management
- Royalty Accounting
- Production Reporting
website: https://www.quorumsoftware.com/
---
