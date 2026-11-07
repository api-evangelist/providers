---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Microsoft Onenote Agentic Access
  operation_count: 17
  slug: microsoft-onenote-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 1
apis:
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The Notebooks API from Microsoft OneNote — 2 operation(s) for notebooks.
  name: Microsoft OneNote Notebooks API
  slug: microsoft-onenote-notebooks-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The Pages API from Microsoft OneNote — 4 operation(s) for pages.
  name: Microsoft OneNote Pages API
  slug: microsoft-onenote-pages-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The SectionGroups API from Microsoft OneNote — 2 operation(s) for sectiongroups.
  name: Microsoft OneNote SectionGroups API
  slug: microsoft-onenote-sectiongroups-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The Sections API from Microsoft OneNote — 3 operation(s) for sections.
  name: Microsoft OneNote Sections API
  slug: microsoft-onenote-sections-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.onenote API from Microsoft OneNote — 103 operation(s) for groups.onenote.
  name: Microsoft OneNote Groups.onenote API
  slug: microsoft-onenote-groups-onenote-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The sites.onenote API from Microsoft OneNote — 104 operation(s) for sites.onenote.
  name: Microsoft OneNote Sites.onenote API
  slug: microsoft-onenote-sites-onenote-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.onenote API from Microsoft OneNote — 103 operation(s) for users.onenote.
  name: Microsoft OneNote Users.onenote API
  slug: microsoft-onenote-users-onenote-api
artifact_total: 29
collections:
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph) Notebooks API
  slug: open-microsoft-onenote-notebooks-api
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph) Notebooks Pages API
  slug: open-microsoft-onenote-pages-api
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph) Notebooks SectionGroups API
  slug: open-microsoft-onenote-sectiongroups-api
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph) Notebooks Sections API
  slug: open-microsoft-onenote-sections-api
- collection_type: open
  name: Microsoft OneNote API (Microsoft Graph)
  slug: open-microsoft-onenote
common:
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: design
  href: https://artifacts.apis.io/microsoft-onenote/conventions/microsoft-onenote-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-onenote-conventions.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-onenote/rate-limits/microsoft-onenote-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-onenote-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onenote/rules/microsoft-onenote-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-onenote-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onenote/json-ld/microsoft-onenote-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-onenote-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-onenote/vocabulary/microsoft-onenote-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-onenote-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onenote/data-model/microsoft-onenote-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-onenote-data-model.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/graph/versioning-and-support
- group: design
  href: https://artifacts.apis.io/microsoft-onenote/lifecycle/microsoft-onenote-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-onenote-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onenote/errors/microsoft-onenote-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-onenote-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-onenote/conformance/microsoft-onenote-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-onenote-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-onenote/llms/microsoft-onenote-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-onenote-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-onenote/well-known/microsoft-onenote-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-onenote-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-onenote/well-known/microsoft-onenote-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-onenote-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-onenote/hosts/microsoft-onenote-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-onenote-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-onenote/integrations/microsoft-onenote-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-onenote-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-onenote/vendors/microsoft-onenote-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-onenote-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-onenote/packages/microsoft-onenote-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-onenote-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/analyticsonazure
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: auth
  href: https://artifacts.apis.io/microsoft-onenote/scopes/microsoft-onenote-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-onenote-scopes.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-onenote/plans/microsoft-onenote-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-onenote-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-onenote/finops/microsoft-onenote-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-onenote-finops.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-onenote/agentic-access/microsoft-onenote-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-onenote-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-onenote/security/microsoft-onenote-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-onenote-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-onenote/authentication/microsoft-onenote-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-onenote-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/onenote/digital-note-taking-app
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/integrate-with-onenote
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/graph/throttling
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2024-01-01'
description: Microsoft OneNote is a digital note-taking application. It provides API access through Microsoft Graph for managing notebooks, sections, section groups, and pages stored in OneDrive or SharePoint.
finops:
- has_sources: false
  method: generated
  name: Microsoft Onenote Finops
  primary_unit: request
  service_category: API
  slug: microsoft-onenote-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-onenote.png
json_schemas:
- name: GenericList
  property_count: 1
  slug: microsoft-onenote-generic-list
- name: GenericObject
  property_count: 0
  slug: microsoft-onenote-generic-object
- name: CopyNotebookModel
  property_count: 15
  slug: microsoft-onenote-microsoft-graph-copy-notebook-model
- name: microsoft.graph.notebook
  property_count: 15
  slug: microsoft-onenote-microsoft-graph-notebook
- name: microsoft.graph.onenotePage
  property_count: 14
  slug: microsoft-onenote-microsoft-graph-onenote-page
- name: microsoft.graph.onenote
  property_count: 7
  slug: microsoft-onenote-microsoft-graph-onenote
- name: microsoft.graph.onenoteSection
  property_count: 13
  slug: microsoft-onenote-microsoft-graph-onenote-section
- name: microsoft.graph.sectionGroup
  property_count: 13
  slug: microsoft-onenote-microsoft-graph-section-group
jsonld:
- class_count: 29
  name: Microsoft Onenote Context
  property_count: 36
  slug: microsoft-onenote-context
layout: provider
modified: '2026-05-19'
name: Microsoft OneNote
nav: Providers
network: true
overview: 'Microsoft OneNote publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Notebooks API, Pages API, SectionGroups API, and 4 more. Tagged areas include Microsoft, Microsoft 365, Notebooks, Notes, and Productivity.


  The Microsoft OneNote catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft OneNote''s developer surface includes engineering blog, getting-started guide, authentication, developer portal, documentation, changelog, support, and 31 more developer resources.'
plans:
- name: Microsoft Onenote Plans Pricing
  plan_count: 3
  slug: microsoft-onenote-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Microsoft Onenote Rate Limits
  slug: microsoft-onenote-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Microsoft OneNote API Rules
  rule_count: 58
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 11
  slug: microsoft-onenote-rules
scopes:
- name: Microsoft Onenote Scopes
  scope_count: 6
  slug: microsoft-onenote-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.8
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 55.0
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 68.4
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-onenote/microsoft-onenote-2026-06-20T185517.png
security:
- kind: authentication
  name: Microsoft Onenote Authentication
  slug: microsoft-onenote-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Onenote Domain Security
  slug: microsoft-onenote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-onenote
tags:
- Microsoft
- Microsoft 365
- Notebooks
- Notes
- Productivity
website: https://www.microsoft.com/en-us/microsoft-365/onenote/digital-note-taking-app
---
