---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Quickbase Agentic Access
  operation_count: 67
  slug: quickbase-agentic-access
  summary_line: 67 operations · 38 acting
api_count: 1
apis:
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Apps API from Quickbase — 5 operation(s) for apps.
  name: Quickbase Apps API
  slug: quickbase-apps-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Audit API from Quickbase — 1 operation(s) for audit.
  name: Quickbase Audit API
  slug: quickbase-audit-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Auth API from Quickbase — 2 operation(s) for auth.
  name: Quickbase Auth API
  slug: quickbase-auth-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Document Templates API from Quickbase — 1 operation(s) for document templates.
  name: Quickbase Document Templates API
  slug: quickbase-document-templates-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Fields API from Quickbase — 4 operation(s) for fields.
  name: Quickbase Fields API
  slug: quickbase-fields-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Files API from Quickbase — 1 operation(s) for files.
  name: Quickbase Files API
  slug: quickbase-files-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Formulas API from Quickbase — 1 operation(s) for formulas.
  name: Quickbase Formulas API
  slug: quickbase-formulas-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Groups API from Quickbase — 3 operation(s) for groups.
  name: Quickbase Groups API
  slug: quickbase-groups-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Platform Analytics API from Quickbase — 2 operation(s) for platform analytics.
  name: Quickbase Platform Analytics API
  slug: quickbase-platform-analytics-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Records API from Quickbase — 3 operation(s) for records.
  name: Quickbase Records API
  slug: quickbase-records-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Reports API from Quickbase — 3 operation(s) for reports.
  name: Quickbase Reports API
  slug: quickbase-reports-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Solutions API from Quickbase — 8 operation(s) for solutions.
  name: Quickbase Solutions API
  slug: quickbase-solutions-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Tables API from Quickbase — 5 operation(s) for tables.
  name: Quickbase Tables API
  slug: quickbase-tables-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Trustees API from Quickbase — 1 operation(s) for trustees.
  name: Quickbase Trustees API
  slug: quickbase-trustees-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The Users API from Quickbase — 5 operation(s) for users.
  name: Quickbase Users API
  slug: quickbase-users-api
- baseURL: https://api.quickbase.com/v1
  baseurl_source: declared
  description: The User Token API from Quickbase — 4 operation(s) for user token.
  name: Quickbase User Token API
  slug: quickbase-user-token-api
artifact_total: 39
asyncapis:
- description: ''
  name: Quickbase Webhooks
  slug: quickbase-webhooks
common:
- group: company
  title: ''
  type: Newsroom
  url: https://www.quickbase.com/news
- group: agent
  href: https://artifacts.apis.io/quickbase/agentic-access/quickbase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quickbase-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/quickbase/rate-limits/quickbase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quickbase-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/quickbase/plans/quickbase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quickbase-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/quickbase/rules/quickbase-rules.yml
  title: ''
  type: Spectral
  url: rules/quickbase-rules.yml
- group: design
  href: https://artifacts.apis.io/quickbase/json-ld/quickbase-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/quickbase-context.jsonld
- group: design
  href: https://artifacts.apis.io/quickbase/vocabulary/quickbase-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/quickbase-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/quickbase/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/quickbase/asyncapi/quickbase-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/quickbase-webhooks.yml
- group: design
  href: https://artifacts.apis.io/quickbase/data-model/quickbase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quickbase-data-model.yml
- group: design
  href: https://artifacts.apis.io/quickbase/components/quickbase-components.yml
  title: ''
  type: Components
  url: components/quickbase-components.yml
- group: build
  href: https://artifacts.apis.io/quickbase/cli/quickbase-cli.yml
  title: ''
  type: CLI
  url: cli/quickbase-cli.yml
- group: operate
  href: https://artifacts.apis.io/quickbase/changelog/quickbase-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/quickbase-changelog.yml
- group: design
  href: https://artifacts.apis.io/quickbase/conventions/quickbase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/quickbase-conventions.yml
- group: start
  href: https://artifacts.apis.io/quickbase/sandbox/quickbase-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/quickbase-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.quickbase.com/compliance
- group: auth
  title: ''
  type: Security
  url: https://www.quickbase.com/report-a-security-issue
- group: auth
  href: https://artifacts.apis.io/quickbase/authentication/quickbase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quickbase-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.quickbase.com/docs/what-is-the-quickbase-sandbox.md
- group: operate
  title: ''
  type: StatusPage
  url: https://service.quickbase.com/
- group: design
  href: https://artifacts.apis.io/quickbase/lifecycle/quickbase-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/quickbase-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/quickbase/errors/quickbase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/quickbase-problem-types.yml
- group: design
  href: https://artifacts.apis.io/quickbase/conformance/quickbase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quickbase-conformance.yml
- group: other
  href: https://artifacts.apis.io/quickbase/overlays/quickbase-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/quickbase-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/quickbase/llms/quickbase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quickbase-llms.txt
- group: auth
  href: https://artifacts.apis.io/quickbase/well-known/quickbase-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quickbase-security.txt
- group: auth
  href: https://artifacts.apis.io/quickbase/well-known/quickbase-quickbase-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quickbase-quickbase-security.txt
- group: agent
  href: https://artifacts.apis.io/quickbase/well-known/quickbase-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quickbase-well-known.yml
- group: other
  href: https://artifacts.apis.io/quickbase/hosts/quickbase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quickbase-hosts.yml
- group: build
  href: https://artifacts.apis.io/quickbase/integrations/quickbase-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/quickbase-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/quickbase/vendors/quickbase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quickbase-vendors.yml
- group: build
  href: https://artifacts.apis.io/quickbase/packages/quickbase-packages.yml
  title: ''
  type: SDKs
  url: packages/quickbase-packages.yml
- group: build
  href: https://artifacts.apis.io/quickbase/packages/quickbase-packages.yml
  title: ''
  type: Packages
  url: packages/quickbase-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.quickbase.com/docs/before-you-begin-user-setup
- group: company
  title: ''
  type: Website
  url: https://www.quickbase.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.quickbase.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.quickbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.quickbase.com/docs/welcome-to-the-quickbase-api-guide
- group: auth
  title: ''
  type: Authentication
  url: https://developer.quickbase.com/auth
- group: operate
  title: ''
  type: Support
  url: https://www.quickbase.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.quickbase.com/
- group: operate
  title: ''
  type: Forum
  url: https://community.quickbase.com/
- group: company
  title: ''
  type: Blog
  url: https://www.quickbase.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QuickBase
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quickbase.com/plans-and-pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.quickbase.com/trial-register
- group: start
  title: ''
  type: Login
  url: https://login.quickbase.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quickbase.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quickbase.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quickbase
- group: auth
  href: https://artifacts.apis.io/quickbase/security/quickbase-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/quickbase-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/quickbase/security/quickbase-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/quickbase-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/quickbase/security/quickbase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quickbase-domain-security.yml
created: '2026-10-18'
description: Quickbase is a no-code / low-code application platform for dynamic work and complex project management, letting business teams build custom apps on shared data to improve their processes. Developers can access Quickbase apps programmatically through the Quickbase JSON RESTful API (developer.quickbase.com, downloadable as OpenAPI), covering apps, tables, fields, reports, records, files, users, groups, audit and platform analytics, alongside the legacy XML/HTTP API.
image: https://payload-assets-us-west-2.marketing.quickbase.com/share-general-seo-image-eden%20(1)-1200x630.png
json_schemas:
- name: appResponse
  property_count: 13
  slug: quickbase-app-response
- name: fieldResponse
  property_count: 15
  slug: quickbase-field-response
- name: fieldUsageResponse
  property_count: 0
  slug: quickbase-field-usage-response
- name: reportResponse
  property_count: 9
  slug: quickbase-report-response
- name: runReportResponse
  property_count: 3
  slug: quickbase-run-report-response
- name: tableResponse
  property_count: 16
  slug: quickbase-table-response
jsonld:
- class_count: 21
  name: Quickbase Context
  property_count: 64
  slug: quickbase-context
layout: provider
modified: '2026-10-18'
name: Quickbase
nav: Providers
network: true
overview: 'Quickbase publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Audit API, Auth API, and 13 more. Tagged areas include Company, Low-Code, No-Code, Application Development, and Project Management.


  The Quickbase catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Quickbase''s developer surface includes CLI, changelog, sandbox, authentication, getting-started guide, API reference, documentation, and 46 more developer resources.'
plans:
- name: Quickbase Plans Pricing
  plan_count: 4
  slug: quickbase-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Quickbase Rate Limits
  slug: quickbase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Quickbase API Rules
  rule_count: 48
  severity_counts:
    error: 37
    hint: 0
    info: 3
    warn: 8
  slug: quickbase-rules
scopes:
- name: Quickbase Scopes
  scope_count: 0
  slug: quickbase-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -14.4
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 66.7
    developer_ergonomics: 51.8
    discoverability: 75.0
    operational_transparency: 75.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 79.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/quickbase/quickbase-2026-11-03T141831.png
security:
- kind: authentication
  name: Quickbase Authentication
  slug: quickbase-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Quickbase Domain Security
  slug: quickbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quickbase Vulnerability Disclosure
  slug: quickbase-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Quickbase Trust Center
  slug: quickbase-trust-center
  summary_line: HIPAA
skill_count: 6
skills:
- name: quickbase-build-an-app
  slug: quickbase-build-an-app
- name: quickbase-manage-group-membership
  slug: quickbase-manage-group-membership
- name: quickbase-query-records
  slug: quickbase-query-records
- name: quickbase-run-a-report
  slug: quickbase-run-a-report
- name: quickbase-sync-changed-records
  slug: quickbase-sync-changed-records
- name: quickbase-upsert-records
  slug: quickbase-upsert-records
slug: quickbase
tags:
- Company
- Low-Code
- No-Code
- Application Development
- Project Management
- Workflow Automation
- Database
website: https://www.quickbase.com/
---
