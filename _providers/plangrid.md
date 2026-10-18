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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Plangrid Agentic Access
  operation_count: 8
  slug: plangrid-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 2
apis:
- baseURL: https://io.plangrid.com
  baseurl_source: declared
  description: The Batch API from PlanGrid — 1 operation(s) for batch.
  name: PlanGrid Batch API
  slug: plangrid-batch-api
- baseURL: https://io.plangrid.com
  baseurl_source: declared
  description: The Me API from PlanGrid — 1 operation(s) for me.
  name: PlanGrid Me API
  slug: plangrid-me-api
- baseURL: https://io.plangrid.com
  baseurl_source: declared
  description: The Oauth API from PlanGrid — 2 operation(s) for oauth.
  name: PlanGrid OAuth API
  slug: plangrid-oauth-api
- baseURL: https://io.plangrid.com
  baseurl_source: declared
  description: The Projects API from PlanGrid — 2 operation(s) for projects.
  name: PlanGrid Projects API
  slug: plangrid-projects-api
- baseURL: https://io.plangrid.com
  baseurl_source: declared
  description: The Rate Limits API from PlanGrid — 1 operation(s) for rate limits.
  name: PlanGrid Rate Limits API
  slug: plangrid-rate-limits-api
artifact_total: 10
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/agentic-access/plangrid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/plangrid-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/rules/plangrid-rules.yml
  title: ''
  type: Spectral
  url: rules/plangrid-rules.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/hosts/plangrid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plangrid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/vendors/plangrid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plangrid-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.autodesk.com/trust/overview
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autodesk.com/company/legal-notices-trademarks/privacy-statement?_ga=2.254122760.1430555354.1713426746-2055187556.1708148316
- group: commercial
  title: ''
  type: Pricing
  url: https://construction.autodesk.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: http://www.autodesk.com/company/newsroom/overview
- group: company
  title: ''
  type: Blog
  url: https://blogs.autodesk.com/blog/test/
- group: company
  title: ''
  type: Website
  url: https://construction.autodesk.com/products/plangrid/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.plangrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.plangrid.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.plangrid.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.plangrid.com/reference/getting-started-1
- group: operate
  title: ''
  type: Support
  url: https://help.plangrid.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plangrid
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/authentication/plangrid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/plangrid-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/scopes/plangrid-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/plangrid-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/packages/plangrid-packages.yml
  title: ''
  type: SDKs
  url: packages/plangrid-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/packages/plangrid-packages.yml
  title: ''
  type: Packages
  url: packages/plangrid-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/mcp/plangrid-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/plangrid-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/conformance/plangrid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plangrid-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/errors/plangrid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plangrid-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/lifecycle/plangrid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/plangrid-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.plangrid.com/reference/api-versioning
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/changelog/plangrid-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plangrid-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/conventions/plangrid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/plangrid-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/data-model/plangrid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plangrid-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/security/plangrid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plangrid-domain-security.yml
created: '2026-07-17'
description: PlanGrid is a construction productivity platform (now part of Autodesk Construction Cloud) that gives field and office teams access to construction drawings, sheets, documents, photos, RFIs, submittals, field reports, tasks, and punch lists on web and mobile. The PlanGrid API is a REST API served from io.plangrid.com that lets developers programmatically manage projects, annotations, comments, documents, photos, sheets and versions, snapshots, RFIs, submittal packages, field reports, tasks and task lists, roles, and project team users. It supports OAuth 2.0 (authorization code and implicit grants) as well as HTTP Basic API-key authentication, media-type versioning via the Accept header, cursor-based pagination, batch requests, and multi-step file upload workflows for PDFs, photos, and documents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plangrid.png
layout: provider
modified: '2026-07-20'
name: PlanGrid
nav: Providers
network: true
overview: 'PlanGrid publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Me API, OAuth API, and 2 more. Tagged areas include Company, Enterprise, Construction, Construction Technology, and Project Management.


  The PlanGrid catalog on APIs.io includes 1 Spectral governance ruleset.


  PlanGrid''s developer surface includes pricing, engineering blog, documentation, API reference, getting-started guide, support, authentication, and 22 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: PlanGrid API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 1
  slug: plangrid-rules
scopes:
- name: Plangrid Scopes
  scope_count: 2
  slug: plangrid-scopes
  summary_line: 2 scopes · authorizationCode/implicit
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 19.6
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 46.4
    developer_ergonomics: 45.2
    discoverability: 67.9
    operational_transparency: 22.4
  previous_composite: 21.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/plangrid/refs/heads/main/screenshots/plangrid-2026-09-02T151414.png
security:
- kind: authentication
  name: Plangrid Authentication
  slug: plangrid-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Plangrid Domain Security
  slug: plangrid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: plangrid
tags:
- Company
- Enterprise
- Construction
- Construction Technology
- Project Management
- Field Reports
- Documents
- RFIs
- REST API
- Autodesk
website: https://construction.autodesk.com/products/plangrid/
---
