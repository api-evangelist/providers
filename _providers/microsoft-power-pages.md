---
access_model:
  confidence: medium
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
  - security
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Power Pages Agentic Access
  operation_count: 6
  slug: microsoft-power-pages-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 4
apis:
- description: The Power Pages Web API provides CRUD operations on Dataverse tables from Power Pages websites. It enables authenticated and anonymous users to interact with business data through portal pages using s
  name: Power Pages Web API
  slug: web-api
- baseURL: https://{site}.powerappsportals.com/_api/
  baseurl_source: declared
  description: The Records API from Microsoft Power Pages — 2 operation(s) for records.
  name: Microsoft Power Pages Records API
  slug: microsoft-power-pages-records-api
- baseURL: https://{site}.powerappsportals.com/_api/
  baseurl_source: declared
  description: The Tables API from Microsoft Power Pages — 2 operation(s) for tables.
  name: Microsoft Power Pages Tables API
  slug: microsoft-power-pages-tables-api
- description: 'Administrative operations for Power Pages websites exposed through the Power Platform API (API version 2024-10-01): create, list, restart, delete and convert websites, manage custom domains, SSL bindi'
  name: Power Platform API - Power Pages Websites
  slug: power-platform-api-websites
artifact_total: 17
collections:
- collection_type: open
  name: Microsoft Power Pages Web Records API
  slug: open-microsoft-power-pages-records-api
- collection_type: open
  name: Microsoft Power Pages Web Records Tables API
  slug: open-microsoft-power-pages-tables-api
- collection_type: open
  name: Microsoft Power Pages Web API
  slug: open-microsoft-power-pages
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: design
  href: https://artifacts.apis.io/microsoft-power-pages/rules/microsoft-power-pages-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-power-pages-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-power-pages/json-ld/microsoft-power-pages-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-power-pages-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-power-pages/vocabulary/microsoft-power-pages-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-power-pages-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-power-pages/data-model/microsoft-power-pages-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-power-pages-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-power-pages/cli/microsoft-power-pages-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-power-pages-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-power-pages/conventions/microsoft-power-pages-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-power-pages-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/power-pages/configure/web-api-overview
- group: design
  href: https://artifacts.apis.io/microsoft-power-pages/lifecycle/microsoft-power-pages-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-power-pages-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-power-pages/errors/microsoft-power-pages-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-power-pages-error-codes.yml
- group: design
  href: https://artifacts.apis.io/microsoft-power-pages/errors/microsoft-power-pages-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-power-pages-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-power-pages/conformance/microsoft-power-pages-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-power-pages-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-power-pages/llms/microsoft-power-pages-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-power-pages-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-power-pages/well-known/microsoft-power-pages-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-power-pages-www-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-power-pages/well-known/microsoft-power-pages-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-power-pages-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-power-pages/hosts/microsoft-power-pages-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-power-pages-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-power-pages/vendors/microsoft-power-pages-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-power-pages-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/power-platform/products/power-pages/pricing
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: commercial
  href: https://artifacts.apis.io/microsoft-power-pages/plans/microsoft-power-pages-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-power-pages-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-power-pages/rate-limits/microsoft-power-pages-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-power-pages-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-power-pages/finops/microsoft-power-pages-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-power-pages-finops.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-power-pages/agentic-access/microsoft-power-pages-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-power-pages-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-power-pages/security/microsoft-power-pages-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-power-pages-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-power-pages/security/microsoft-power-pages-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-power-pages-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-power-pages/authentication/microsoft-power-pages-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-power-pages-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://make.powerpages.microsoft.com/
- group: company
  title: ''
  type: Website
  url: https://powerpages.microsoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-pages/
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
- group: operate
  title: ''
  type: Community
  url: https://community.powerplatform.com/forums/thread/?threadid=4f8c3d6b-df78-ef11-a317-7c1e522703d5
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/power-platform/blog/power-pages/feed/
created: '2024-01-01'
description: Microsoft Power Pages is a secure, enterprise-grade, low-code platform for creating, hosting, and administering modern external-facing business websites. It provides APIs for CRUD operations on Dataverse tables from portal pages.
finops:
- has_sources: false
  method: generated
  name: Microsoft Power Pages Finops
  primary_unit: request
  service_category: API
  slug: microsoft-power-pages-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-power-pages.png
json_schemas:
- name: RecordCollection
  property_count: 3
  slug: microsoft-power-pages-record-collection
jsonld:
- class_count: 1
  name: Microsoft Power Pages Context
  property_count: 1
  slug: microsoft-power-pages-context
layout: provider
modified: '2026-04-28'
name: Microsoft Power Pages
nav: Providers
network: true
overview: 'Microsoft Power Pages is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Records API, Tables API, and 2 more. Tagged areas include Dataverse, Low-Code, Microsoft, and Web Portals.


  The Microsoft Power Pages catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Power Pages'' developer surface includes getting-started guide, CLI, pricing, changelog, authentication, developer portal, documentation, and 30 more developer resources.'
plans:
- name: Microsoft Power Pages Plans Pricing
  plan_count: 3
  slug: microsoft-power-pages-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Microsoft Power Pages Rate Limits
  slug: microsoft-power-pages-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Microsoft Power Pages API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-power-pages-rules
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 66.2
    catalog_earned_first_party: 12.0
    catalog_gap: 48.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.2
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 53.3
    developer_ergonomics: 52.4
    discoverability: 71.4
    operational_transparency: 44.7
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-power-pages/microsoft-power-pages-2026-06-20T185523.png
security:
- kind: authentication
  name: Microsoft Power Pages Authentication
  slug: microsoft-power-pages-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Power Pages Domain Security
  slug: microsoft-power-pages-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Power Pages Vulnerability Disclosure
  slug: microsoft-power-pages-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-power-pages
tags:
- Dataverse
- Low-Code
- Microsoft
- Web Portals
website: https://powerpages.microsoft.com/
---
