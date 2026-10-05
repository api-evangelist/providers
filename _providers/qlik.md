---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Qlik Agentic Access
  operation_count: 48
  slug: qlik-agentic-access
  summary_line: 48 operations · 24 acting
api_count: 1
apis:
- description: Qlik provides APIs to support automation, configuration, observability, and integration with third-party applications to incorporate Qlik Cloud capabilities directly into those applications.
  name: Qlik
  slug: qlik
- description: Manages IP restriction policies for controlling network access to the Qlik Cloud tenant.
  name: Qlik IP Policies API
  slug: ip-policies
- description: Manages change store configurations for tracking and storing changes in analytics data.
  name: Qlik Change Stores API
  slug: change-stores
- description: Manages data products within the Qlik data governance framework, enabling the packaging and sharing of curated data assets.
  name: Qlik Data Products API
  slug: data-products
- description: The JSON-RPC API over WebSocket that enables interaction with the Qlik Associative Engine for Qlik Sense applications, providing session-based access to app data models, objects, and calculations.
  name: Qlik Engine JSON-RPC API
  slug: qix
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1
  baseurl_source: declared
  description: The Apps API from Qlik — 22 operation(s) for apps.
  name: Qlik Apps API
  slug: qlik-apps-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1
  baseurl_source: declared
  description: The evaluation API from Qlik — 5 operation(s) for evaluation.
  name: Qlik Evaluation API
  slug: qlik-evaluation-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1
  baseurl_source: declared
  description: The filters API from Qlik — 3 operation(s) for filters.
  name: Qlik Filters API
  slug: qlik-filters-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1
  baseurl_source: declared
  description: The insight-analyses API from Qlik — 3 operation(s) for insight-analyses.
  name: Qlik Insight Analyses API
  slug: qlik-insight-analyses-api
artifact_total: 18
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/agentic-access/qlik-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/qlik-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/finops/qlik-finops.yml
  title: ''
  type: FinOps
  url: finops/qlik-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/rate-limits/qlik-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qlik-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/plans/qlik-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qlik-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/rules/qlik-rules.yml
  title: ''
  type: Spectral
  url: rules/qlik-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/json-ld/qlik-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/qlik-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/vocabulary/qlik-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qlik-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/data-model/qlik-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qlik-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/changelog/qlik-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/qlik-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/conventions/qlik-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qlik-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/authentication/qlik-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qlik-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/errors/qlik-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qlik-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/conformance/qlik-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qlik-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/hosts/qlik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qlik-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/vendors/qlik-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qlik-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/packages/qlik-packages.yml
  title: ''
  type: Packages
  url: packages/qlik-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.qlik.dev/
- group: company
  title: ''
  type: Website
  url: https://qlik.dev
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/security/qlik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qlik-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qlik
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qlik.dev
- group: auth
  title: ''
  type: Authentication
  url: https://qlik.dev/authenticate
- group: start
  title: ''
  type: GettingStarted
  url: https://qlik.dev/get-started
- group: build
  title: ''
  type: SDKs
  url: https://qlik.dev/toolkits/qlik-api/
- group: build
  title: ''
  type: CLI
  url: https://qlik.dev/toolkits/qlik-cli/
- group: docs
  title: ''
  type: Documentation
  url: https://qlik.dev/apis/rest/
- group: operate
  title: ''
  type: RateLimits
  url: https://qlik.dev/apis/rest/rate-limiting/
- group: build
  title: ''
  type: CodeExamples
  url: https://qlik.dev/examples/
- group: operate
  title: ''
  type: ChangeLog
  url: https://qlik.dev/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qlikcloud.com/
- group: company
  title: ''
  type: Blog
  url: https://community.qlik.com/t5/Qlik-Design-Blog/bg-p/qlik-design-blog
- group: operate
  title: ''
  type: Community
  url: https://community.qlik.com
- group: operate
  title: ''
  type: Support
  url: https://support.qlik.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/license-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/legal/privacy
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/qlik-oss/qlik-mcp-registry
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://qlik.dev
  reason: no-machine-readable-spec
  state: unreadable
created: '2025-02-24'
description: APIs for Qlik's analytics and data integration platform.
finops:
- name: Qlik Finops
  service_category: API
  slug: qlik-finops
image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
jsonld:
- class_count: 96
  name: Qlik Context
  property_count: 275
  slug: qlik-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-09-16'
name: Qlik
nav: Providers
network: true
overview: 'Qlik publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Evaluation API, Filters API, and 6 more. Tagged areas include Security, Access Control, Machine Learning, Artificial Intelligence, and Analytics.


  The Qlik catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Qlik''s developer surface includes changelog, authentication, getting-started guide, CLI, documentation, code examples, engineering blog, and 31 more developer resources.'
plans:
- name: Qlik Plans Pricing
  plan_count: 3
  slug: qlik-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Qlik Rate Limits
  slug: qlik-rate-limits
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Qlik API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 2
  slug: qlik-rules
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.8
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 58.4
    developer_ergonomics: 54.2
    discoverability: 48.2
    operational_transparency: 44.7
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/screenshots/qlik-2026-06-20T192340.png
security:
- kind: authentication
  name: Qlik Authentication
  slug: qlik-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Qlik Domain Security
  slug: qlik-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: qlik
tags:
- Security
- Access Control
- Machine Learning
- Artificial Intelligence
- Analytics
- Data Integration
- Cloud
website: https://qlik.dev
---
