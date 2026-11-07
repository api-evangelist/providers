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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
api_count: 5
apis:
- description: Revenue Assurance API providing friction metrics and analytics.
  name: Blue Triangle API
  slug: blue-triangle-api
- baseURL: https://api.bluetriangletech.com
  baseurl_source: declared
  description: The Content Security Policies API from Bluetriangletechnologies — 1 operation(s) for content security policies.
  name: Bluetriangletechnologies Content Security Policies API
  slug: bluetriangletechnologies-content-security-policies-api
- baseURL: https://api.bluetriangletech.com
  baseurl_source: declared
  description: The Event Markers API from Bluetriangletechnologies — 1 operation(s) for event markers.
  name: Bluetriangletechnologies Event Markers API
  slug: bluetriangletechnologies-event-markers-api
- baseURL: https://api.bluetriangletech.com
  baseurl_source: declared
  description: The Performance API from Bluetriangletechnologies — 1 operation(s) for performance.
  name: Bluetriangletechnologies Performance API
  slug: bluetriangletechnologies-performance-api
- baseURL: https://api.bluetriangletech.com
  baseurl_source: declared
  description: The Resource API from Bluetriangletechnologies — 1 operation(s) for resource.
  name: Bluetriangletechnologies Resource API
  slug: bluetriangletechnologies-resource-api
artifact_total: 13
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://bluetriangle.com/blog/rss.xml
- group: design
  href: https://artifacts.apis.io/bluetriangletechnologies/rules/bluetriangletechnologies-rules.yml
  title: ''
  type: Spectral
  url: rules/bluetriangletechnologies-rules.yml
- group: design
  href: https://artifacts.apis.io/bluetriangletechnologies/json-ld/bluetriangletechnologies-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bluetriangletechnologies-context.jsonld
- group: design
  href: https://artifacts.apis.io/bluetriangletechnologies/vocabulary/bluetriangletechnologies-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bluetriangletechnologies-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bluetriangletechnologies/data-model/bluetriangletechnologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bluetriangletechnologies-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bluetriangletechnologies/changelog/bluetriangletechnologies-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bluetriangletechnologies-changelog.yml
- group: auth
  href: https://artifacts.apis.io/bluetriangletechnologies/authentication/bluetriangletechnologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bluetriangletechnologies-authentication.yml
- group: design
  href: https://artifacts.apis.io/bluetriangletechnologies/conformance/bluetriangletechnologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bluetriangletechnologies-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bluetriangletechnologies/llms/bluetriangletechnologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bluetriangletechnologies-llms.txt
- group: auth
  href: https://artifacts.apis.io/bluetriangletechnologies/well-known/bluetriangletechnologies-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bluetriangletechnologies-status-security.txt
- group: agent
  href: https://artifacts.apis.io/bluetriangletechnologies/well-known/bluetriangletechnologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluetriangletechnologies-well-known.yml
- group: other
  href: https://artifacts.apis.io/bluetriangletechnologies/hosts/bluetriangletechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluetriangletechnologies-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluetriangletechnologies/vendors/bluetriangletechnologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluetriangletechnologies-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bluetriangle.com/
- group: other
  title: ''
  type: Leadership
  url: https://bluetriangle.com/team
- group: auth
  href: https://artifacts.apis.io/bluetriangletechnologies/security/bluetriangletechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluetriangletechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluetriangle.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.bluetriangle.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://bluetriangle.com/quick-tour-video-page
- group: operate
  title: ''
  type: Support
  url: https://help.bluetriangle.com/
- group: company
  title: ''
  type: Blog
  url: https://bluetriangle.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blue-triangle-tech
- group: start
  title: ''
  type: SignUp
  url: https://bluetriangle.com/schedule-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bluetriangle.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bluetriangle.com/privacy-policy
coverage:
  checked: '2026-09-29'
  detail: Developer portal at https://portal.bluetriangle.com/ loads content via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://portal.bluetriangle.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blue Triangle Technologies provides a Revenue Assurance Platform that quantifies website friction in monetary terms, enabling digital teams to prioritize fixes that impact revenue. The platform continuously measures visitor interactions, identifies costly friction points, and validates ROI of improvements, integrating with tools like Jira. It serves enterprises across eCommerce, financial services, travel, and healthcare, offering analytics, remediation plans, and AI‑assisted insights.
json_schemas:
- name: GetContentSecurityPoliciesResponse
  property_count: 5
  slug: bluetriangletechnologies-get-content-security-policies-response
- name: PostPerformanceRequest
  property_count: 7
  slug: bluetriangletechnologies-post-performance-request
- name: PostPerformanceResponse
  property_count: 4
  slug: bluetriangletechnologies-post-performance-response
- name: PostResourceRequest
  property_count: 7
  slug: bluetriangletechnologies-post-resource-request
jsonld:
- class_count: 4
  name: Bluetriangletechnologies Context
  property_count: 15
  slug: bluetriangletechnologies-context
layout: provider
modified: '2026-10-06'
name: Bluetriangletechnologies
nav: Providers
network: true
overview: 'Bluetriangletechnologies is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Content Security Policies API, Event Markers API, Performance API, and 2 more. Tagged areas include Company, Analytics, Revenue Assurance, Digital Experience, and Artificial Intelligence.


  The Bluetriangletechnologies catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bluetriangletechnologies'' developer surface includes changelog, authentication, getting-started guide, support, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Bluetriangletechnologies API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: bluetriangletechnologies-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 23.7
    developer_ergonomics: 26.2
    discoverability: 67.0
    operational_transparency: 36.8
  previous_composite: 36.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bluetriangletechnologies/bluetriangletechnologies-2026-10-11T102513.png
security:
- kind: authentication
  name: Bluetriangletechnologies Authentication
  slug: bluetriangletechnologies-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bluetriangletechnologies Domain Security
  slug: bluetriangletechnologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluetriangletechnologies
tags:
- Company
- Analytics
- Revenue Assurance
- Digital Experience
- Artificial Intelligence
website: https://bluetriangle.com
---
