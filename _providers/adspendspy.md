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
  band_gated_from: agent-native
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Meta Ad Library Spend API provided via AdSpendSpy
  name: Meta Ad Library Spend API
  slug: meta-ad-library-spend-api
- baseURL: https://www.adspendspy.com/api/v1
  baseurl_source: declared
  description: Account-scoped access to the advertisers you track in AdSpendSpy, their ads, your saved lists, projects and pending alerts, plus AdSpendSpy's estimated ad spend in EUR (cumulative).
  name: Meta Ad Library Spend API by AdSpendSpy API
  slug: meta-ad-library-spend-api-by-adspendspy-api
artifact_total: 13
asyncapis:
- description: ''
  name: Adspendspy Webhooks
  slug: adspendspy-webhooks
common:
- group: design
  href: https://artifacts.apis.io/adspendspy/rules/adspendspy-rules.yml
  title: ''
  type: Spectral
  url: rules/adspendspy-rules.yml
- group: design
  href: https://artifacts.apis.io/adspendspy/json-ld/adspendspy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adspendspy-context.jsonld
- group: design
  href: https://artifacts.apis.io/adspendspy/vocabulary/adspendspy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adspendspy-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/adspendspy/asyncapi/adspendspy-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/adspendspy-webhooks.yml
- group: design
  href: https://artifacts.apis.io/adspendspy/data-model/adspendspy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adspendspy-data-model.yml
- group: design
  href: https://artifacts.apis.io/adspendspy/errors/adspendspy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adspendspy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adspendspy/conformance/adspendspy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adspendspy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adspendspy/llms/adspendspy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adspendspy-llms.txt
- group: agent
  href: https://artifacts.apis.io/adspendspy/mcp/adspendspy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adspendspy-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adspendspy/well-known/adspendspy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adspendspy-well-known.yml
- group: other
  href: https://artifacts.apis.io/adspendspy/hosts/adspendspy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adspendspy-hosts.yml
- group: other
  href: https://artifacts.apis.io/adspendspy/vendors/adspendspy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adspendspy-vendors.yml
- group: build
  href: https://artifacts.apis.io/adspendspy/packages/adspendspy-packages.yml
  title: ''
  type: SDKs
  url: packages/adspendspy-packages.yml
- group: build
  href: https://artifacts.apis.io/adspendspy/packages/adspendspy-packages.yml
  title: ''
  type: Packages
  url: packages/adspendspy-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adspendspy.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.adspendspy.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adspendspy.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.adspendspy.com/press
- group: docs
  title: ''
  type: APIReference
  url: https://www.adspendspy.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdspendSpy
- group: auth
  href: https://artifacts.apis.io/adspendspy/security/adspendspy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adspendspy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adspendspy.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.adspendspy.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.adspendspy.com/api-docs
- group: operate
  title: ''
  type: Support
  url: https://www.adspendspy.com/contact
created: '2026-10-27'
description: AdSpendSpy provides a tool that leverages the official Meta Ad Library to estimate and analyze ad spend on Facebook and Meta platforms. Users can search for competitors, view ad creatives, spend estimates, and track campaign performance through an intuitive web interface and API endpoints. The service offers a free trial and subscription plans for deeper insights.
json_schemas:
- name: AdListResponse
  property_count: 5
  slug: adspendspy-ad-list-response
- name: CheckTrackedResponse
  property_count: 2
  slug: adspendspy-check-tracked-response
- name: IntegrationItemListResponse
  property_count: 4
  slug: adspendspy-integration-item-list-response
- name: ProjectsResponse
  property_count: 0
  slug: adspendspy-projects-response
- name: TopAdsResponse
  property_count: 3
  slug: adspendspy-top-ads-response
- name: TrackBrandResponse
  property_count: 13
  slug: adspendspy-track-brand-response
jsonld:
- class_count: 25
  name: Adspendspy Context
  property_count: 123
  slug: adspendspy-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.adspendspy.com.
  name: AdSpendSpy (Meta Ad Library Spend API) MCP Server
  slug: adspendspy-mcp-yml
modified: '2026-10-27'
name: AdSpendSpy (Meta Ad Library Spend API)
nav: Providers
network: true
overview: 'AdSpendSpy (Meta Ad Library Spend API) publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Meta Ad Library Spend API by AdSpendSpy API, and 1 more. Tagged areas include Company, Advertising, Analytics, and Meta.


  The AdSpendSpy (Meta Ad Library Spend API) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  AdSpendSpy (Meta Ad Library Spend API)''s developer surface includes signup flow, API reference, documentation, getting-started guide, support, and 20 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: AdSpendSpy (Meta Ad Library Spend API) API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: adspendspy-rules
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 64.9
    developer_ergonomics: 23.8
    discoverability: 64.2
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 46.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/adspendspy/adspendspy-2026-11-03T120319.png
security:
- kind: domain-security
  name: Adspendspy Domain Security
  slug: adspendspy-domain-security
  summary_line: TLSv1.3
slug: adspendspy
tags:
- Company
- Advertising
- Analytics
- Meta
website: https://www.adspendspy.com
---
