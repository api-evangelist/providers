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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Shlink Agentic Access
  operation_count: 52
  slug: shlink-agentic-access
  summary_line: 52 operations · 18 acting
api_count: 1
apis:
- baseURL_template: '{scheme}://{host}'
  baseurl_source: spec_template
  description: Operations to manage domains used on short URLs
  name: Shlink Domains API
  slug: shlink-domains-api
- baseURL_template: '{scheme}://{host}'
  baseurl_source: spec_template
  description: Handle services with which shlink is integrated
  name: Shlink Integrations API
  slug: shlink-integrations-api
- baseURL_template: '{scheme}://{host}'
  baseurl_source: spec_template
  description: Public endpoints designed to monitor the service
  name: Shlink Monitoring API
  slug: shlink-monitoring-api
- baseURL_template: '{scheme}://{host}'
  baseurl_source: spec_template
  description: Handle dynamic rule-based redirects
  name: Shlink Redirect rules API
  slug: shlink-redirect-rules-api
- baseURL_template: '{scheme}://{host}'
  baseurl_source: spec_template
  description: Operations that can be performed on short URLs
  name: Shlink Short URLs API
  slug: shlink-short-urls-api
- baseURL_template: '{scheme}://{host}'
  baseurl_source: spec_template
  description: Let you handle the list of available tags
  name: Shlink Tags API
  slug: shlink-tags-api
- baseURL_template: '{scheme}://{host}'
  baseurl_source: spec_template
  description: Non-rest endpoints, used to be publicly exposed
  name: Shlink URL Shortener API
  slug: shlink-url-shortener-api
- baseURL_template: '{scheme}://{host}'
  baseurl_source: spec_template
  description: Operations to manage visits on short URLs
  name: Shlink Visits API
  slug: shlink-visits-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/shlink/agentic-access/shlink-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shlink-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/shlink/rules/shlink-rules.yml
  title: ''
  type: Spectral
  url: rules/shlink-rules.yml
- group: design
  href: https://artifacts.apis.io/shlink/vocabulary/shlink-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shlink-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/shlink/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/shlink/components/shlink-components.yml
  title: ''
  type: Components
  url: components/shlink-components.yml
- group: operate
  href: https://artifacts.apis.io/shlink/changelog/shlink-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shlink-changelog.yml
- group: auth
  href: https://artifacts.apis.io/shlink/authentication/shlink-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shlink-authentication.yml
- group: design
  href: https://artifacts.apis.io/shlink/errors/shlink-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shlink-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shlink/conformance/shlink-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shlink-conformance.yml
- group: other
  href: https://artifacts.apis.io/shlink/overlays/shlink-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shlink-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/shlink/hosts/shlink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shlink-hosts.yml
- group: build
  href: https://artifacts.apis.io/shlink/packages/shlink-packages.yml
  title: ''
  type: SDKs
  url: packages/shlink-packages.yml
- group: build
  href: https://artifacts.apis.io/shlink/packages/shlink-packages.yml
  title: ''
  type: Packages
  url: packages/shlink-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://shlink.io/documentation
- group: auth
  href: https://artifacts.apis.io/shlink/security/shlink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shlink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shlink.io/
created: '2026-10-28'
description: Shlink is a self‑hosted, PHP‑based URL shortener that provides a RESTful API, a command‑line interface, and Docker images for easy deployment. It enables users to create and manage short URLs under their own domain, supports custom domains, tagging, visit tracking, redirect rules, and integrates with services like Mercure for real‑time updates. The open‑source project is actively maintained and documented at shlink.io.
image: https://raw.githubusercontent.com/shlinkio/shlink.io/main/public/images/shlink-hero.png
layout: provider
modified: '2026-10-28'
name: Shlink
nav: Providers
network: true
overview: 'Shlink publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Domains API, Integrations API, Monitoring API, and 5 more. Tagged areas include Company, URL Shorteners, PHP, Self-Hosted, and Open Source.


  The Shlink catalog on APIs.io includes 1 Spectral governance ruleset.


  Shlink''s developer surface includes changelog, authentication, documentation, and 13 more developer resources.'
plans:
- name: Shlink Plans Pricing
  plan_count: 0
  slug: shlink-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Shlink Rate Limits
  slug: shlink-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Shlink API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: shlink-rules
scopes:
- name: Shlink Scopes
  scope_count: 0
  slug: shlink-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 46.3
    developer_ergonomics: 30.2
    discoverability: 57.1
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shlink/shlink-2026-11-03T143134.png
security:
- kind: authentication
  name: Shlink Authentication
  slug: shlink-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Shlink Domain Security
  slug: shlink-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 1
skills:
- name: shlink-short-url-management
  slug: shlink-short-url-management
slug: shlink
tags:
- Company
- URL Shorteners
- PHP
- Self-Hosted
- Open Source
- REST API
website: https://shlink.io/
---
