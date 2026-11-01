---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Haystack provides API access for metrics, including global and team-specific endpoints. Documentation is available in markdown format.
  name: Haystack API
  slug: haystack-api
- baseURL: https://api.usehaystack.io
  baseurl_source: declared
  description: 'Haystack Analytics API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Haystack Analytics API
  slug: usehaystack-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/usehaystack/plans/usehaystack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usehaystack-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/usehaystack/rules/usehaystack-rules.yml
  title: ''
  type: Spectral
  url: rules/usehaystack-rules.yml
- group: design
  href: https://artifacts.apis.io/usehaystack/json-ld/usehaystack-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/usehaystack-context.jsonld
- group: design
  href: https://artifacts.apis.io/usehaystack/vocabulary/usehaystack-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/usehaystack-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/usehaystack/data-model/usehaystack-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usehaystack-data-model.yml
- group: operate
  href: https://artifacts.apis.io/usehaystack/changelog/usehaystack-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/usehaystack-changelog.yml
- group: design
  href: https://artifacts.apis.io/usehaystack/conformance/usehaystack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usehaystack-conformance.yml
- group: agent
  href: https://artifacts.apis.io/usehaystack/llms/usehaystack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usehaystack-llms.txt
- group: auth
  href: https://artifacts.apis.io/usehaystack/well-known/usehaystack-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/usehaystack-support-security.txt
- group: agent
  href: https://artifacts.apis.io/usehaystack/well-known/usehaystack-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/usehaystack-well-known.yml
- group: other
  href: https://artifacts.apis.io/usehaystack/hosts/usehaystack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usehaystack-hosts.yml
- group: other
  href: https://artifacts.apis.io/usehaystack/vendors/usehaystack-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usehaystack-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.usehaystack.io/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.usehaystack.io/other/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.usehaystack.io`
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usehaystack
- group: auth
  href: https://artifacts.apis.io/usehaystack/security/usehaystack-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/usehaystack-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/usehaystack/security/usehaystack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usehaystack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usehaystack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.usehaystack.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usehaystack.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.usehaystack.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usehaystack.io/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://help.usehaystack.io/getting-started/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://auth.usehaystack.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://auth.usehaystack.io/login
- group: operate
  title: ''
  type: Support
  url: https://help.usehaystack.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usehaystack.io/terms
coverage:
  checked: '2026-10-21'
  detail: Documentation provides API details in markdown but no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://help.usehaystack.io/features/api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Haystack Analytics provides a unified delivery operations platform for product and engineering leaders. It integrates Jira, Git, and the entire delivery stack into a single place, offering boards, risk detection, automated status updates, and operational dashboards. The solution helps developers, project managers, and scrum coaches deliver products faster with AI‑generated code, stakeholder alignment, and data‑driven insights.
image: https://cdn.prod.website-files.com/65531fd225d40f3e2bb9ab9d/65683c13a41bc6a28bbc234c_open-graph.png
json_schemas:
- name: PostPublicApiMetricsRequest
  property_count: 6
  slug: usehaystack-post-public-api-metrics-request
- name: PostPublicApiMetricsResponse
  property_count: 2
  slug: usehaystack-post-public-api-metrics-response
- name: PostPublicApiTeamTeamidMetricsRequest
  property_count: 6
  slug: usehaystack-post-public-api-team-teamid-metrics-request
- name: PostPublicApiTeamTeamidMetricsResponse
  property_count: 2
  slug: usehaystack-post-public-api-team-teamid-metrics-response
jsonld:
- class_count: 4
  name: Usehaystack Context
  property_count: 8
  slug: usehaystack-context
layout: provider
modified: '2026-10-21'
name: Haystack Analytics
nav: Providers
network: true
overview: 'Haystack Analytics is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeliveryOps, Product Management, Engineering, and Analytics.


  The Haystack Analytics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Haystack Analytics'' developer surface includes changelog, documentation, pricing, engineering blog, getting-started guide, signup flow, support, and 21 more developer resources.'
plans:
- name: Usehaystack Plans Pricing
  plan_count: 2
  slug: usehaystack-plans-pricing
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Haystack Analytics API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: usehaystack-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 64.8
    catalog_earned_first_party: 8.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 21.3
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Usehaystack Domain Security
  slug: usehaystack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Usehaystack Vulnerability Disclosure
  slug: usehaystack-vulnerability-disclosure
  summary_line: no policy recorded
slug: usehaystack
tags:
- Company
- DeliveryOps
- Product Management
- Engineering
- Analytics
website: https://www.usehaystack.io/
---
