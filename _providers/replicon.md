---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Proprietary JSON-over-HTTPS web-service API for the Replicon Time Intelligence Platform and Polaris PSA — users, clients, projects, tasks, time, billing/costing and analytics. Tenants resolve their re
  name: Replicon & Polaris API
  slug: replicon-polaris-api
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/replicon/well-known/replicon-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/replicon-status-security.txt
- group: agent
  href: https://artifacts.apis.io/replicon/well-known/replicon-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/replicon-well-known.yml
- group: other
  href: https://artifacts.apis.io/replicon/hosts/replicon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/replicon-hosts.yml
- group: build
  href: https://artifacts.apis.io/replicon/integrations/replicon-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/replicon-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/replicon/vendors/replicon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/replicon-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.deltek.com/company/leadership/
- group: auth
  href: https://artifacts.apis.io/replicon/security/replicon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/replicon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.replicon.com
- group: docs
  title: ''
  type: Documentation
  url: https://learning.deltek.com/category/replicon?labelkey=product_replicon
- group: docs
  title: ''
  type: APIReference
  url: https://learning.deltek.com/bundle/RepliconRESTService/page/RepliconDevRes_RESTS_APIReference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://learning.deltek.com/bundle/Replicon/page/getting-started-with-the-replicon-and-polaris-api.html
- group: operate
  title: ''
  type: Support
  url: https://www.deltek.com/resources/support/
- group: company
  title: ''
  type: Blog
  url: https://www.deltek.com/resources/articles/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/replicon
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deltek.com/deltek-contracts/saas-terms/replicon/terms-and-conditions/
- group: start
  title: ''
  type: Login
  url: https://polarislogin.replicon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.replicon.com/
- group: auth
  href: https://artifacts.apis.io/replicon/authentication/replicon-authentication.yml
  title: ''
  type: Authentication
  url: authentication/replicon-authentication.yml
- group: design
  href: https://artifacts.apis.io/replicon/conventions/replicon-conventions.yml
  title: ''
  type: Conventions
  url: conventions/replicon-conventions.yml
- group: design
  href: https://artifacts.apis.io/replicon/errors/replicon-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/replicon-error-codes.yml
- group: design
  href: https://artifacts.apis.io/replicon/lifecycle/replicon-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/replicon-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/replicon/changelog/replicon-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/replicon-changelog.yml
- group: start
  href: https://artifacts.apis.io/replicon/sandbox/replicon-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/replicon-sandbox.yml
- group: design
  href: https://artifacts.apis.io/replicon/conformance/replicon-conformance.yml
  title: ''
  type: Conformance
  url: conformance/replicon-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.deltek.com/
- group: auth
  href: https://artifacts.apis.io/replicon/security/replicon-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/replicon-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/replicon/security/replicon-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/replicon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.deltek.com/company/security-and-trust/
- group: company
  title: ''
  type: Newsroom
  url: https://www.deltek.com/company/news/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.replicon.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Replicon, now a Deltek company, is a time-tracking, project time and expense, and professional-services automation (PSA) platform. Its Time Intelligence Platform and the Polaris PSA product manage timesheets, projects, tasks, clients, resources, billing and costing for professional-services and enterprise teams. Replicon exposes a proprietary JSON-over-HTTPS web-service API (no public OpenAPI) covering users, clients, projects, tasks, time, billing and analytics; callers resolve a tenant swimlane through a global discovery service and authenticate with an Api-token header or HTTP Basic.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/replicon.png
layout: provider
modified: '2026-10-20'
name: Replicon
nav: Providers
network: true
overview: 'Replicon is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise Software, Time Tracking, Timesheets, and Project Management.


  Replicon''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 22 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 40.5
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 33.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/replicon/replicon-2026-09-02T153504.png
security:
- kind: authentication
  name: Replicon Authentication
  slug: replicon-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Replicon Domain Security
  slug: replicon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Replicon Vulnerability Disclosure
  slug: replicon-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Replicon Trust Center
  slug: replicon-trust-center
  summary_line: ISO/IEC 27001:2013
slug: replicon
tags:
- Company
- Enterprise Software
- Time Tracking
- Timesheets
- Project Management
- Professional Services Automation
- Workforce Management
- Billing
website: https://www.replicon.com
---
