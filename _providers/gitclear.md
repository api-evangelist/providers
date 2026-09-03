---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Gitclear Agentic Access
  operation_count: 18
  slug: gitclear-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 1
apis:
- baseURL: https://www.gitclear.com/api/v1
  baseurl_source: declared
  description: The API Tokens API from GitClear — 1 operation(s) for api tokens.
  name: GitClear API Tokens API
  slug: gitclear-api-tokens-api
- baseURL: https://www.gitclear.com/api/v1
  baseurl_source: declared
  description: The Code Introspection API from GitClear — 1 operation(s) for code introspection.
  name: GitClear Code Introspection API
  slug: gitclear-code-introspection-api
- baseURL: https://www.gitclear.com/api/v1
  baseurl_source: declared
  description: The Data Audit API from GitClear — 1 operation(s) for data audit.
  name: GitClear Data Audit API
  slug: gitclear-data-audit-api
- baseURL: https://www.gitclear.com/api/v1
  baseurl_source: declared
  description: The Developers API from GitClear — 4 operation(s) for developers.
  name: GitClear Developers API
  slug: gitclear-developers-api
- baseURL: https://www.gitclear.com/api/v1
  baseurl_source: declared
  description: The Imports API from GitClear — 1 operation(s) for imports.
  name: GitClear Imports API
  slug: gitclear-imports-api
- baseURL: https://www.gitclear.com/api/v1
  baseurl_source: declared
  description: The Releases API from GitClear — 1 operation(s) for releases.
  name: GitClear Releases API
  slug: gitclear-releases-api
- baseURL: https://www.gitclear.com/api/v1
  baseurl_source: declared
  description: The Reports API from GitClear — 2 operation(s) for reports.
  name: GitClear Reports API
  slug: gitclear-reports-api
- baseURL: https://www.gitclear.com/api/v1
  baseurl_source: declared
  description: The Teams API from GitClear — 2 operation(s) for teams.
  name: GitClear Teams API
  slug: gitclear-teams-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GitClear Public API Tokens API
  slug: open-gitclear-api-tokens-api
- collection_type: open
  name: GitClear Public API Tokens Code Introspection API
  slug: open-gitclear-code-introspection-api
- collection_type: open
  name: GitClear Public API Tokens Data Audit API
  slug: open-gitclear-data-audit-api
- collection_type: open
  name: GitClear Public API Tokens Developers API
  slug: open-gitclear-developers-api
- collection_type: open
  name: GitClear Public API Tokens Imports API
  slug: open-gitclear-imports-api
- collection_type: open
  name: GitClear Public API Tokens Releases API
  slug: open-gitclear-releases-api
- collection_type: open
  name: GitClear Public API Tokens Reports API
  slug: open-gitclear-reports-api
- collection_type: open
  name: GitClear Public API Tokens Teams API
  slug: open-gitclear-teams-api
- collection_type: open
  name: GitClear Public API
  slug: open-gitclear
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gitclear-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gitclear-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gitclear-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gitclear-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gitclear-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitclear
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gitclear
- group: company
  title: ''
  type: Website
  url: https://www.gitclear.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.gitclear.com/api_reference
- group: commercial
  title: ''
  type: Plans
  url: plans/gitclear-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gitclear-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gitclear-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gitclear.com/blog
created: '2026-06-21'
description: GitClear provides code and commit analytics for engineering teams, centered on its Diff Delta metric (formerly Line Impact) that scores durable code change beyond raw lines. Its public REST API exposes repositories, commits/data audits, Diff Delta reports, and developer management so teams can pull research-backed productivity and AI-ROI metrics programmatically.
finops:
- name: Gitclear Finops
  service_category: Developer Tools and Analytics
  slug: gitclear-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gitclear.png
layout: provider
modified: '2026-06-21'
name: GitClear
nav: Providers
network: true
overview: 'GitClear publishes 8 APIs on the [APIs.io](https://apis.io/) network, including API Tokens API, Code Introspection API, Data Audit API, and 5 more. Tagged areas include Code Analytics, Commit Analytics, Developer Productivity, Diff Delta, and Engineering Metrics.


  GitClear''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Gitclear Plans Pricing
  plan_count: 4
  slug: gitclear-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Gitclear Rate Limits
  slug: gitclear-rate-limits
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 53.4
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gitclear/refs/heads/main/screenshots/gitclear-2026-07-25T215835.png
security:
- kind: authentication
  name: Gitclear Authentication
  slug: gitclear-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gitclear Domain Security
  slug: gitclear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gitclear Vulnerability Disclosure
  slug: gitclear-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gitclear Trust Center
  slug: gitclear-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: gitclear
tags:
- Code Analytics
- Commit Analytics
- Developer Productivity
- Diff Delta
- Engineering Metrics
website: https://www.gitclear.com
---
