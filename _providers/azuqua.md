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
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Azuqua Agentic Access
  operation_count: 28
  slug: azuqua-agentic-access
  summary_line: 28 operations · 15 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.azuqua.com
  baseurl_source: spec
  description: The Account API from Azuqua — 2 operation(s) for account.
  name: Azuqua Account API
  slug: azuqua-account-api
- baseURL: https://api.azuqua.com
  baseurl_source: spec
  description: The Accounts API from Azuqua — 1 operation(s) for accounts.
  name: Azuqua Accounts API
  slug: azuqua-accounts-api
- baseURL: https://api.azuqua.com
  baseurl_source: spec
  description: The Connectors API from Azuqua — 1 operation(s) for connectors.
  name: Azuqua Connectors API
  slug: azuqua-connectors-api
- baseURL: https://api.azuqua.com
  baseurl_source: spec
  description: The Flo API from Azuqua — 8 operation(s) for flo.
  name: Azuqua Flo API
  slug: azuqua-flo-api
- baseURL: https://api.azuqua.com
  baseurl_source: spec
  description: The Folder API from Azuqua — 5 operation(s) for folder.
  name: Azuqua Folder API
  slug: azuqua-folder-api
- baseURL: https://api.azuqua.com
  baseurl_source: spec
  description: The Folders API from Azuqua — 1 operation(s) for folders.
  name: Azuqua Folders API
  slug: azuqua-folders-api
- baseURL: https://api.azuqua.com
  baseurl_source: spec
  description: The Org API from Azuqua — 3 operation(s) for org.
  name: Azuqua Org API
  slug: azuqua-org-api
- baseURL: https://api.azuqua.com
  baseurl_source: spec
  description: The User API from Azuqua — 1 operation(s) for user.
  name: Azuqua User API
  slug: azuqua-user-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/azuqua/vocabulary/azuqua-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/azuqua-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/azuqua/well-known/azuqua-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/azuqua-apis-security.txt
- group: agent
  href: https://artifacts.apis.io/azuqua/agentic-access/azuqua-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/azuqua-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/azuqua/rules/azuqua-rules.yml
  title: ''
  type: Spectral
  url: rules/azuqua-rules.yml
- group: design
  href: https://artifacts.apis.io/azuqua/errors/azuqua-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/azuqua-problem-types.yml
- group: design
  href: https://artifacts.apis.io/azuqua/conformance/azuqua-conformance.yml
  title: ''
  type: Conformance
  url: conformance/azuqua-conformance.yml
- group: agent
  href: https://artifacts.apis.io/azuqua/well-known/azuqua-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/azuqua-well-known.yml
- group: other
  href: https://artifacts.apis.io/azuqua/hosts/azuqua-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azuqua-hosts.yml
- group: other
  href: https://artifacts.apis.io/azuqua/vendors/azuqua-vendors.yml
  title: ''
  type: Vendors
  url: vendors/azuqua-vendors.yml
- group: build
  href: https://artifacts.apis.io/azuqua/packages/azuqua-packages.yml
  title: ''
  type: SDKs
  url: packages/azuqua-packages.yml
- group: build
  href: https://artifacts.apis.io/azuqua/packages/azuqua-packages.yml
  title: ''
  type: Packages
  url: packages/azuqua-packages.yml
- group: auth
  href: https://artifacts.apis.io/azuqua/authentication/azuqua-authentication.yml
  title: ''
  type: Authentication
  url: authentication/azuqua-authentication.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/okta/
- group: company
  title: ''
  type: Website
  url: https://azuqua.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.azuqua.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.azuqua.com/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.azuqua.com/changelog/
- group: operate
  href: https://artifacts.apis.io/azuqua/changelog/azuqua-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/azuqua-changelog.yml
- group: agent
  href: https://artifacts.apis.io/azuqua/llms/azuqua-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azuqua-llms.txt
- group: design
  href: https://artifacts.apis.io/azuqua/lifecycle/azuqua-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/azuqua-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/azuqua/lifecycle/azuqua-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/azuqua-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/azuqua/security/azuqua-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azuqua-domain-security.yml
created: '2026-07-17'
description: 'Azuqua was a Seattle-based integration platform as a service (iPaaS) and no-code workflow-automation company, backed by Insight Partners and Techstars, that let business teams build integrations and automated workflows (FLOs) across SaaS applications such as Salesforce, Slack, Marketo and ServiceNow. Azuqua was acquired by Okta in 2019 and its workflow orchestration engine and connectors were folded into Okta Workflows (part of Okta Lifecycle Management). The standalone product is now end-of-life: azuqua.com serves an acquisition notice and the API is no longer available for purchase. This API Evangelist profile documents the surviving public developer surface (legacy ReadMe docs, changelog, llms.txt) and the product''s lifecycle status.'
image: https://files.readme.io/72b94d0-small-logo_blue.png
layout: provider
modified: '2026-07-18'
name: Azuqua
nav: Providers
network: true
overview: 'Azuqua publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Connectors API, and 5 more. Tagged areas include Company, Integration, iPaaS, Workflow Automation, and Integration Platform.


  The Azuqua catalog on APIs.io includes 1 Spectral governance ruleset.


  Azuqua''s developer surface includes authentication, documentation, API reference, changelog, and 18 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Azuqua API Rules
  rule_count: 48
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 2
  slug: azuqua-rules
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.8
    catalog_earned_first_party: 0.0
    catalog_gap: 82.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  previous_composite: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/azuqua/azuqua-2026-07-25T202126.png
security:
- kind: authentication
  name: Azuqua Authentication
  slug: azuqua-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Azuqua Domain Security
  slug: azuqua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azuqua
tags:
- Company
- Integration
- iPaaS
- Workflow Automation
- Integration Platform
- Automation
- Connectors
- No-Code
website: https://azuqua.com/
---
