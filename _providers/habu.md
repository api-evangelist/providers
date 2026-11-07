---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - '{''url'': ''https://habu.com'', ''status'': 301, ''note'': ''declared website redirects to https://liveramp.com/ — a different registrable domain (habu.com -> liveramp.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Billable Configs API from Habu — 2 operation(s) for billable configs.
  name: Habu Billable Configs API
  slug: habu-billable-configs-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom API from Habu — 2 operation(s) for cleanroom.
  name: Habu Cleanroom API
  slug: habu-cleanroom-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Datasets API from Habu — 5 operation(s) for cleanroom datasets.
  name: Habu Cleanroom Datasets API
  slug: habu-cleanroom-datasets-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Destinations API from Habu — 3 operation(s) for cleanroom destinations.
  name: Habu Cleanroom Destinations API
  slug: habu-cleanroom-destinations-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Exports API from Habu — 4 operation(s) for cleanroom exports.
  name: Habu Cleanroom Exports API
  slug: habu-cleanroom-exports-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Flow Runs API from Habu — 10 operation(s) for cleanroom flow runs.
  name: Habu Cleanroom Flow Runs API
  slug: habu-cleanroom-flow-runs-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Flows API from Habu — 10 operation(s) for cleanroom flows.
  name: Habu Cleanroom Flows API
  slug: habu-cleanroom-flows-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Partners API from Habu — 8 operation(s) for cleanroom partners.
  name: Habu Cleanroom Partners API
  slug: habu-cleanroom-partners-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Question Datasets API from Habu — 4 operation(s) for cleanroom question datasets.
  name: Habu Cleanroom Question Datasets API
  slug: habu-cleanroom-question-datasets-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Question Permissions API from Habu — 1 operation(s) for cleanroom question permissions.
  name: Habu Cleanroom Question Permissions API
  slug: habu-cleanroom-question-permissions-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Question Result Shares API from Habu — 1 operation(s) for cleanroom question result shares.
  name: Habu Cleanroom Question Result Shares API
  slug: habu-cleanroom-question-result-shares-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Question Run Schedule API from Habu — 2 operation(s) for cleanroom question run schedule.
  name: Habu Cleanroom Question Run Schedule API
  slug: habu-cleanroom-question-run-schedule-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Question Runs API from Habu — 10 operation(s) for cleanroom question runs.
  name: Habu Cleanroom Question Runs API
  slug: habu-cleanroom-question-runs-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Question Tags API from Habu — 2 operation(s) for cleanroom question tags.
  name: Habu Cleanroom Question Tags API
  slug: habu-cleanroom-question-tags-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Questions API from Habu — 5 operation(s) for cleanroom questions.
  name: Habu Cleanroom Questions API
  slug: habu-cleanroom-questions-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Roles API from Habu — 2 operation(s) for cleanroom roles.
  name: Habu Cleanroom Roles API
  slug: habu-cleanroom-roles-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanroom Users API from Habu — 3 operation(s) for cleanroom users.
  name: Habu Cleanroom Users API
  slug: habu-cleanroom-users-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Cleanrooms API from Habu — 4 operation(s) for cleanrooms.
  name: Habu Cleanrooms API
  slug: habu-cleanrooms-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Credential Sources API from Habu — 3 operation(s) for credential sources.
  name: Habu Credential Sources API
  slug: habu-credential-sources-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Data Connections API from Habu — 5 operation(s) for data connections.
  name: Habu Data Connections API
  slug: habu-data-connections-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Data Source Parameters API from Habu — 1 operation(s) for data source parameters.
  name: Habu Data Source Parameters API
  slug: habu-data-source-parameters-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Data Sources API from Habu — 2 operation(s) for data sources.
  name: Habu Data Sources API
  slug: habu-data-sources-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Data Types API from Habu — 2 operation(s) for data types.
  name: Habu Data Types API
  slug: habu-data-types-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The DataConnectionViews API from Habu — 2 operation(s) for dataconnectionviews.
  name: Habu Data Connection Views API
  slug: habu-dataconnectionviews-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Destinations API from Habu — 3 operation(s) for destinations.
  name: Habu Destinations API
  slug: habu-destinations-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Flow Decision Configurations API from Habu — 1 operation(s) for flow decision configurations.
  name: Habu Flow Decision Configurations API
  slug: habu-flow-decision-configurations-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Health API from Habu — 1 operation(s) for health.
  name: Habu Health API
  slug: habu-health-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Import Data Types API from Habu — 1 operation(s) for import data types.
  name: Habu Import Data Types API
  slug: habu-import-data-types-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Intelligence API from Habu — 4 operation(s) for intelligence.
  name: Habu Intelligence API
  slug: habu-intelligence-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: For internal LiveRamp consumption. These operations are not part of the supported external customer contract and may change without notice.
  name: Habu Internal API
  slug: habu-internal-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Invitations API from Habu — 3 operation(s) for invitations.
  name: Habu Invitations API
  slug: habu-invitations-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Organization Credentials API from Habu — 2 operation(s) for organization credentials.
  name: Habu Organization Credentials API
  slug: habu-organization-credentials-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Organization Users API from Habu — 1 operation(s) for organization users.
  name: Habu Organization Users API
  slug: habu-organization-users-api
- baseURL: https://api.habu.com/v1/
  baseurl_source: declared
  description: The Questions API from Habu — 3 operation(s) for questions.
  name: Habu Questions API
  slug: habu-questions-api
artifact_total: 49
collections:
- collection_type: open
  name: External APIs for Customer Integration
  slug: open-habu-clean-room-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/liveramp/
- group: other
  href: https://artifacts.apis.io/habu/capabilities/habu-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/habu-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.liveramp.com/clean-room-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.liveramp.com/clean-room-api/reference/clean-room-api-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.liveramp.com/clean-room-api/reference/python-tutorial-for-creating-and-running-questions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/liveramp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liveramp.com/liveramp-terms-of-service/
- group: start
  title: ''
  type: Login
  url: https://console.habu.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liveramp.com/
- group: design
  href: https://artifacts.apis.io/habu/lifecycle/habu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/habu-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/habu/changelog/habu-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/habu-changelog.yml
- group: build
  href: https://artifacts.apis.io/habu/packages/habu-packages.yml
  title: ''
  type: Packages
  url: packages/habu-packages.yml
- group: build
  href: https://artifacts.apis.io/habu/packages/habu-packages.yml
  title: ''
  type: SDKs
  url: packages/habu-packages.yml
- group: design
  href: https://artifacts.apis.io/habu/conventions/habu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/habu-conventions.yml
- group: design
  href: https://artifacts.apis.io/habu/errors/habu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/habu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/habu/conformance/habu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/habu-conformance.yml
- group: design
  href: https://artifacts.apis.io/habu/data-model/habu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/habu-data-model.yml
- group: operate
  href: https://artifacts.apis.io/habu/rate-limits/habu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/habu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/habu/plans/habu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/habu-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/habu/llms/habu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/habu-llms.txt
- group: other
  href: https://artifacts.apis.io/habu/overlays/habu-clean-room-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/habu-clean-room-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/habu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/habu/scopes/habu-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/habu-scopes.yml
- group: auth
  href: https://artifacts.apis.io/habu/authentication/habu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/habu-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://habu.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.liveramp.com/clean-room-api
- group: company
  title: ''
  type: Blog
  url: https://liveramp.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://liveramp.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://liveramp.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liveramp.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.liveramp.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.liveramp.com/
- group: auth
  title: ''
  type: Security
  url: https://liveramp.com/security/bug-bounty
- group: auth
  href: https://artifacts.apis.io/habu/security/habu-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/habu-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/habu/security/habu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/habu-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/habu/security/habu-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/habu-trust-center.yml
created: '2026-07-17'
description: 'Habu was a data clean room and data collaboration company, founded in 2017 and headquartered in San Francisco, that let brands, publishers, and media platforms run privacy-safe joins and analytics on each other''s first-party data without moving or exposing raw records. In January 2024 Habu was acquired by LiveRamp, and the product now ships as LiveRamp Clean Room within the LiveRamp data collaboration network. The habu.com marketing domain 301-redirects to liveramp.com and the old docs.habu.com / developer.habu.com hosts no longer resolve, but the product API itself is still very much alive on Habu''s own infrastructure: api.habu.com/v1 answers today, and LiveRamp publishes its full 151-operation OpenAPI 3.0.0 contract — titled "External APIs for Customer Integration", contact platform_admin@habu.com — under developers.liveramp.com. The console is still Habu-branded at console.habu.com. This profile originated as a portfolio-lead stub (backed by Norwest Venture Partners and
  Wing Venture Capital) and is enriched here from that live, publicly documented surface plus the security and compliance posture inherited by LiveRamp.'
finops:
- has_sources: true
  method: derived
  name: Habu Finops
  primary_unit: annual token commitment
  service_category: ''
  slug: habu-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/habu.png
layout: provider
mcp_servers:
- description: 'Habu itself ships no MCP server: api.habu.com/mcp returns 404 and there is no Habu-branded MCP endpoint. Two MCP endpoints exist on the acquirer''s infrastructure and both cover the Clean Room API docu'
  name: Habu MCP Server
  slug: habu-mcp-yml
modified: '2026-08-12'
name: Habu
nav: Providers
network: true
overview: 'Habu publishes 34 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billable Configs API, Cleanroom API, Cleanroom Datasets API, and 31 more. Tagged areas include Company, Data Clean Room, Data Collaboration, Advertising, and Privacy.


  The Habu catalog on APIs.io includes 1 Spectral governance ruleset.


  Habu''s developer surface includes API reference, getting-started guide, changelog, authentication, documentation, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Habu Plans Pricing
  plan_count: 3
  slug: habu-plans-pricing
- name: Habu Price Estimates
  plan_count: 0
  slug: habu-price-estimates
random_paper: 8
rate_limits:
- limit_count: 3
  name: Habu Rate Limits
  slug: habu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Habu API Rules
  rule_count: 68
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 14
  slug: habu-rules
scopes:
- name: Habu Scopes
  scope_count: 0
  slug: habu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 70.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.0
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 52.5
    developer_ergonomics: 66.1
    discoverability: 71.7
    operational_transparency: 76.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 60.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: sox
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/habu/habu-2026-07-25T220519.png
security:
- kind: authentication
  name: Habu Authentication
  slug: habu-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Habu Domain Security
  slug: habu-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Habu Vulnerability Disclosure
  slug: habu-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Habu Trust Center
  slug: habu-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, GDPR, CCPA, SOX
skill_count: 3
skills:
- name: habu-provision-a-data-connection
  slug: habu-provision-a-data-connection
- name: habu-run-a-cleanroom-question
  slug: habu-run-a-cleanroom-question
- name: habu-set-up-a-cleanroom-collaboration
  slug: habu-set-up-a-cleanroom-collaboration
slug: habu
tags:
- Company
- Data Clean Room
- Data Collaboration
- Advertising
- Privacy
- Identity
- Marketing
- Analytics
website: https://habu.com
---
