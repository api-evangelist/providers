---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Work with statistics through the Appodeal Reporting API, returning JSON data about ad performance.
  name: Reporting API
  slug: reporting-api
- baseURL: https://events.appsflyer.com
  baseurl_source: declared
  description: 'Appodeal API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Appodeal API
  slug: appodeal-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/appodeal/rules/appodeal-rules.yml
  title: ''
  type: Spectral
  url: rules/appodeal-rules.yml
- group: design
  href: https://artifacts.apis.io/appodeal/json-ld/appodeal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appodeal-context.jsonld
- group: design
  href: https://artifacts.apis.io/appodeal/vocabulary/appodeal-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appodeal-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/appodeal/data-model/appodeal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appodeal-data-model.yml
- group: design
  href: https://artifacts.apis.io/appodeal/conformance/appodeal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appodeal-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appodeal/llms/appodeal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appodeal-llms.txt
- group: agent
  href: https://artifacts.apis.io/appodeal/mcp/appodeal-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/appodeal-mcp.yml
- group: auth
  href: https://artifacts.apis.io/appodeal/well-known/appodeal-faq-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/appodeal-faq-security.txt
- group: agent
  href: https://artifacts.apis.io/appodeal/well-known/appodeal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appodeal-well-known.yml
- group: other
  href: https://artifacts.apis.io/appodeal/hosts/appodeal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appodeal-hosts.yml
- group: other
  href: https://artifacts.apis.io/appodeal/vendors/appodeal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appodeal-vendors.yml
- group: build
  href: https://artifacts.apis.io/appodeal/packages/appodeal-packages.yml
  title: ''
  type: SDKs
  url: packages/appodeal-packages.yml
- group: build
  href: https://artifacts.apis.io/appodeal/packages/appodeal-packages.yml
  title: ''
  type: Packages
  url: packages/appodeal-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appodeal.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appodeal.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.appodeal.com/signin
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.appodeal.com/ios/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appodeal
- group: auth
  href: https://artifacts.apis.io/appodeal/security/appodeal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appodeal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appodeal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://appodeal.com/mediation/
- group: operate
  title: ''
  type: Support
  url: https://appodeal.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://appodeal.com/blog/
coverage:
  checked: '2026-11-01'
  detail: Documentation describes a Reporting API but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is published.
  evidence:
  - status: 200
    url: https://docs.appodeal.com/docs/reporting/reporting-api.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Appodeal is a top mobile app marketing platform for app and game developers, offering a comprehensive mediation solution that helps establish and scale profitable mobile apps and games. The company emphasizes community values, serving others, and giving back through volunteering. Its platform includes features for ad mediation, growth tools, and accelerator programs, supporting developers to maximize revenue.
image: https://appodeal.com/wp-content/uploads/2025/07/FEAT_MAIN_2025_V3-1.png
json_schemas:
- name: GetApiMngAppsResponse
  property_count: 3
  slug: appodeal-get-api-mng-apps-response
- name: PostApiGdprV1OpendsrRequestsRequest
  property_count: 8
  slug: appodeal-post-api-gdpr-v1-opendsr-requests-request
- name: PostApiGdprV1StubRequest
  property_count: 8
  slug: appodeal-post-api-gdpr-v1-stub-request
- name: PostV1BundleidEventRequest
  property_count: 10
  slug: appodeal-post-v1-bundleid-event-request
- name: PostV20S2SInappsAppWebAppidRequest
  property_count: 16
  slug: appodeal-post-v20-s2-sinapps-app-web-appid-request
- name: PostV20S2SVisitsAppWebAppidRequest
  property_count: 13
  slug: appodeal-post-v20-s2-svisits-app-web-appid-request
jsonld:
- class_count: 10
  name: Appodeal Context
  property_count: 41
  slug: appodeal-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.appodeal.com.
  name: Appodeal MCP Server
  slug: appodeal-mcp-yml
modified: '2026-11-01'
name: Appodeal
nav: Providers
network: true
overview: 'Appodeal is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile, Advertising, Monetization, and SDK.


  The Appodeal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Appodeal''s developer surface includes changelog, documentation, support, engineering blog, and 19 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Appodeal API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 1
  slug: appodeal-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 25.4
    developer_ergonomics: 15.5
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 31.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appodeal Domain Security
  slug: appodeal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appodeal
tags:
- Company
- Mobile
- Advertising
- Monetization
- SDK
- Analytics
website: https://appodeal.com/
---
