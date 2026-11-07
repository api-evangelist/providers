---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.yoodli.ai/api
  baseurl_source: declared
  description: Operations on Multi Org feature.
  name: Yoodli Multi Org Management API
  slug: yoodli-multi-org-management-api
- baseURL: https://app.yoodli.ai/api
  baseurl_source: declared
  description: Operations on members of Organizations and their User Groups.
  name: Yoodli Organization User Management API
  slug: yoodli-organization-user-management-api
- baseURL: https://app.yoodli.ai/api
  baseurl_source: declared
  description: Operations on recordings and their feedback exports.
  name: Yoodli Speech API
  slug: yoodli-speech-api
- baseURL: https://app.yoodli.ai/api
  baseurl_source: declared
  description: Operations on User Groups.
  name: Yoodli User Group Management API
  slug: yoodli-user-group-management-api
artifact_total: 17
asyncapis:
- description: ''
  name: Yoodli Web Embed Events
  slug: yoodli-web-embed-events
common:
- group: other
  href: https://artifacts.apis.io/yoodli/capabilities/yoodli-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/yoodli-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/yoodli/overlays/yoodli-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/yoodli-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://yoodli.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.yoodli.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.yoodli.ai/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.yoodli.ai/reference/get_v3-orgs-orgid-users
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.yoodli.ai/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/yoodli/authentication/yoodli-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yoodli-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://support.yoodli.ai/
- group: company
  title: ''
  type: Blog
  url: https://yoodli.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Yoodli
- group: commercial
  title: ''
  type: Pricing
  url: https://yoodli.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.yoodli.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.yoodli.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yoodli.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yoodli.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://yoodli.statuspage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.yoodli.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.yoodli.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.yoodli.ai/changelog
- group: agent
  href: https://artifacts.apis.io/yoodli/mcp/yoodli-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/yoodli-mcp.yml
- group: build
  href: https://artifacts.apis.io/yoodli/mcp/yoodli-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/yoodli-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/yoodli/llms/yoodli-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yoodli-llms.txt
- group: commercial
  href: https://artifacts.apis.io/yoodli/plans/yoodli-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yoodli-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/yoodli/rate-limits/yoodli-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/yoodli-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/yoodli/conventions/yoodli-conventions.yml
  title: ''
  type: Conventions
  url: conventions/yoodli-conventions.yml
- group: design
  href: https://artifacts.apis.io/yoodli/errors/yoodli-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/yoodli-problem-types.yml
- group: design
  href: https://artifacts.apis.io/yoodli/lifecycle/yoodli-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/yoodli-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/yoodli/conformance/yoodli-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yoodli-conformance.yml
- group: design
  href: https://artifacts.apis.io/yoodli/data-model/yoodli-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yoodli-data-model.yml
- group: build
  href: https://artifacts.apis.io/yoodli/packages/yoodli-packages.yml
  title: ''
  type: Packages
  url: packages/yoodli-packages.yml
- group: design
  href: https://artifacts.apis.io/yoodli/components/yoodli-components.yml
  title: ''
  type: Components
  url: components/yoodli-components.yml
- group: agent
  href: https://artifacts.apis.io/yoodli/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/yoodli/security/yoodli-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yoodli-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/yoodli/changelog/yoodli-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yoodli-changelog.yml
created: '2026-09-04'
description: 'Yoodli is a Seattle-based AI communication coaching company, founded in 2021 by former Google engineers and spun out of the Allen Institute for AI incubator. Its platform runs AI roleplays and speech analysis so sales, leadership, L&D and customer-facing teams can rehearse high-stakes conversations — pitches, interviews, performance reviews, discovery calls — and get private, rubric-scored feedback on filler words, pacing, and content. Yoodli publishes a REST API (OpenAPI 3.1.0, base https://app.yoodli.ai/api) for administrative programmatic access: managing Organization members, User Groups (hubs), invites and membership expirations, Multi Org seat allocation, and downloading a recording''s rubric goal scores, coaching feedback, reviewer comments and transcript. It also ships a Web Embed API (iframe + postMessage) for embedding Yoodli activities in a host application, and a remote MCP server over its ReadMe developer portal.'
finops:
- has_sources: true
  method: derived
  name: Yoodli Finops
  primary_unit: user
  service_category: ''
  slug: yoodli-finops
  template: false
image: https://files.readme.io/00bff5691627b960ef3c81cd866921c2c7e950e9f964ec08eb36d59b5e1d307a-yoodli_logo_purplebg_16_9.svg
layout: provider
mcp_servers:
- description: Remote MCP server at developers.yoodli.ai over HTTP; 5 tools listed.
  name: Yoodli MCP Server
  slug: yoodli-developer-portal
modified: '2026-09-04'
name: Yoodli
nav: Providers
network: true
overview: 'Yoodli publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Multi Org Management API, Organization User Management API, Speech API, and 1 more. Tagged areas include Artificial Intelligence, Communications, Coaching, Learning and Development, and Sales Enablement.


  The Yoodli catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Yoodli''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Yoodli Plans Pricing
  plan_count: 5
  slug: yoodli-plans-pricing
- name: Yoodli Price Estimates
  plan_count: 0
  slug: yoodli-price-estimates
random_paper: 8
rate_limits:
- limit_count: 3
  name: Yoodli Rate Limits
  slug: yoodli-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Yoodli API Rules
  rule_count: 55
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 2
  slug: yoodli-rules
score:
  band: strong
  composite: 63.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.8
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 55.5
    developer_ergonomics: 58.9
    discoverability: 75.0
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 58.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/yoodli/yoodli-2026-10-11T200122.png
security:
- kind: authentication
  name: Yoodli Authentication
  slug: yoodli-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yoodli Domain Security
  slug: yoodli-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Yoodli Trust Center
  slug: yoodli-trust-center
  summary_line: SOC 2 Type 2, GDPR
skill_count: 3
skills:
- name: Deprovision Yoodli members and User Groups safely
  slug: yoodli-deprovision-members
- name: Export Yoodli coaching feedback for a session
  slug: yoodli-export-speech-feedback
- name: Onboard a cohort into a Yoodli Organization and User Group
  slug: yoodli-onboard-org-cohort
slug: yoodli
tags:
- Artificial Intelligence
- Communications
- Coaching
- Learning and Development
- Sales Enablement
- Speech Analysis
- Human Resources
- Enterprise Software
- Software-as-a-Service
website: https://yoodli.ai/
---
