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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-04'
api_count: 7
apis:
- description: Branch API provides deep linking, attribution, and analytics endpoints as documented in the public markdown API reference.
  name: Branch API
  slug: branch-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Analytics API from Branch — 1 operation(s) for analytics.
  name: Branch Analytics API
  slug: branch-messenger-analytics-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The App API from Branch — 1 operation(s) for app.
  name: Branch App API
  slug: branch-messenger-app-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Branch API API from Branch — 1 operation(s) for branch api.
  name: Branch Branch API
  slug: branch-messenger-branch-api-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Event API from Branch — 1 operation(s) for event.
  name: Branch Event API
  slug: branch-messenger-event-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Img1 API from Branch — 1 operation(s) for img1.
  name: Branch Img1 API
  slug: branch-messenger-img1-api
- baseURL: https://api2.branch.io
  baseurl_source: declared
  description: The Query API from Branch — 1 operation(s) for query.
  name: Branch Query API
  slug: branch-messenger-query-api
artifact_total: 14
asyncapis:
- description: ''
  name: Branch Messenger Webhooks
  slug: branch-messenger-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/rules/branch-messenger-rules.yml
  title: ''
  type: Spectral
  url: rules/branch-messenger-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/json-ld/branch-messenger-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/branch-messenger-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/vocabulary/branch-messenger-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/branch-messenger-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/asyncapi/branch-messenger-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/branch-messenger-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/data-model/branch-messenger-data-model.yml
  title: ''
  type: DataModel
  url: data-model/branch-messenger-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.branch.io/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/conformance/branch-messenger-conformance.yml
  title: ''
  type: Conformance
  url: conformance/branch-messenger-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/llms/branch-messenger-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/branch-messenger-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/well-known/branch-messenger-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/branch-messenger-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/well-known/branch-messenger-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/branch-messenger-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/hosts/branch-messenger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branch-messenger-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/vendors/branch-messenger-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branch-messenger-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.branch.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.branch.io
- group: auth
  title: ''
  type: Security
  url: https://branch.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.branch.io/saas/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://branch.io/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.branch.io/resources/category/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.branch.io/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.branch.io/resources/category/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://help.branch.io/apidocs
- group: start
  title: ''
  type: GettingStarted
  url: https://help.branch.io/apidocs/scheduled-log-exports-cloud-setup
- group: docs
  title: ''
  type: Documentation
  url: https://developer.branch.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/security/branch-messenger-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/branch-messenger-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branch-messenger/refs/heads/main/security/branch-messenger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branch-messenger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://branchapp.com/
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite public markdown docs.
  evidence:
  - status: 200
    url: https://help.branch.io/apidocs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Branch provides a mobile measurement and deep linking platform that helps marketers and developers create, manage, and analyze deep links, attribution, and user engagement across apps and web. The service offers tools for link management, attribution analytics, fraud detection, and integration with advertising and analytics platforms, supporting a wide range of industries such as finance, retail, and media.
json_schemas:
- name: PutV1AppBranchkeyRequest
  property_count: 15
  slug: branch-messenger-put-v1-app-branchkey-request
- name: PutV1AppBranchkeyResponse
  property_count: 19
  slug: branch-messenger-put-v1-app-branchkey-response
jsonld:
- class_count: 2
  name: Branch Messenger Context
  property_count: 19
  slug: branch-messenger-context
layout: provider
modified: '2026-10-03'
name: Branch
nav: Providers
network: true
overview: 'Branch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, App API, Branch API, and 4 more. Tagged areas include Mobile, Deep Linking, Attribution, Marketing, and Analytics.


  The Branch catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Branch''s developer surface includes support, pricing, engineering blog, API reference, getting-started guide, documentation, and 20 more developer resources.'
random_paper: 8
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Branch API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: branch-messenger-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 30.2
    developer_ergonomics: 35.7
    discoverability: 69.6
    operational_transparency: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Branch Messenger Domain Security
  slug: branch-messenger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Branch Messenger Trust Center
  slug: branch-messenger-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: branch-messenger
tags:
- Mobile
- Deep Linking
- Attribution
- Marketing
- Analytics
website: https://branchapp.com/
---
