---
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-10-04'
api_count: 12
apis:
- description: API for submission ingestion, market intelligence, and marketplace access as described in the developer documentation.
  name: Bold Penguin API
  slug: bold-penguin-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Application Forms API from Bold Penguin — 1 operation(s) for application forms.
  name: Bold Penguin Application Forms API
  slug: bold-penguin-application-forms-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Attachments API from Bold Penguin — 1 operation(s) for attachments.
  name: Bold Penguin Attachments API
  slug: bold-penguin-attachments-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Auth API from Bold Penguin — 1 operation(s) for auth.
  name: Bold Penguin Auth API
  slug: bold-penguin-auth-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Exchange Application Forms API from Bold Penguin — 1 operation(s) for exchange application forms.
  name: Bold Penguin Exchange Application Forms API
  slug: bold-penguin-exchange-application-forms-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Invocations API from Bold Penguin — 1 operation(s) for invocations.
  name: Bold Penguin Invocations API
  slug: bold-penguin-invocations-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Leads API from Bold Penguin — 3 operation(s) for leads.
  name: Bold Penguin Leads API
  slug: bold-penguin-leads-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Market Recommendation API from Bold Penguin — 1 operation(s) for market recommendation.
  name: Bold Penguin Market Recommendation API
  slug: bold-penguin-market-recommendation-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Prospects API from Bold Penguin — 1 operation(s) for prospects.
  name: Bold Penguin Prospects API
  slug: bold-penguin-prospects-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Quote Requests API from Bold Penguin — 2 operation(s) for quote requests.
  name: Bold Penguin Quote Requests API
  slug: bold-penguin-quote-requests-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Tenants API from Bold Penguin — 5 operation(s) for tenants.
  name: Bold Penguin Tenants API
  slug: bold-penguin-tenants-api
- baseURL: https://partner-engine.boldpenguin.com
  baseurl_source: declared
  description: The Token API from Bold Penguin — 1 operation(s) for token.
  name: Bold Penguin Token API
  slug: bold-penguin-token-api
artifact_total: 28
asyncapis:
- description: ''
  name: Bold Penguin Webhooks
  slug: bold-penguin-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/rules/bold-penguin-rules.yml
  title: ''
  type: Spectral
  url: rules/bold-penguin-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/json-ld/bold-penguin-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bold-penguin-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/vocabulary/bold-penguin-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bold-penguin-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/asyncapi/bold-penguin-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bold-penguin-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/data-model/bold-penguin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bold-penguin-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/changelog/bold-penguin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bold-penguin-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/authentication/bold-penguin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bold-penguin-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/conformance/bold-penguin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bold-penguin-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/well-known/bold-penguin-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bold-penguin-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/well-known/bold-penguin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bold-penguin-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/hosts/bold-penguin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bold-penguin-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/vendors/bold-penguin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bold-penguin-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/packages/bold-penguin-packages.yml
  title: ''
  type: SDKs
  url: packages/bold-penguin-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/packages/bold-penguin-packages.yml
  title: ''
  type: Packages
  url: packages/bold-penguin-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.boldpenguin.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.boldpenguin.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.boldpenguin.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.boldpenguin.com/news
- group: start
  title: ''
  type: Login
  url: https://terminal.boldpenguin.com/auth/login
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.boldpenguin.com/docs/webhooks/wh_getting_started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.boldpenguin.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forgeglobal
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bold-penguin/refs/heads/main/security/bold-penguin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bold-penguin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boldpenguin.com/
coverage:
  checked: '2026-10-02'
  detail: Documentation pages are rendered via Docusaurus JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://developers.boldpenguin.com/docs/overview/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: Bold Penguin provides a digital exchange platform for commercial insurance, leveraging its DeX AI technology to connect carriers, brokers, and agents. The company offers APIs for submission ingestion, market intelligence, and marketplace access, enabling automated quoting, binding, and data-driven insights across the insurance value chain. Its solutions aim to modernize risk placement and improve efficiency for insurers and distribution partners.
image: https://boldpenguin.com/wp-content/uploads/2026/09/bp-og_1200x630-v2.webp
json_schemas:
- name: GetApplicationForms46D7A3432B7F46E39A61A75473086923LatestRes
  property_count: 24
  slug: bold-penguin-get-application-forms46-d7-a3432-b7-f46-e39-a61-a75473086923-latest-res
- name: GetAuthTokenResponse
  property_count: 8
  slug: bold-penguin-get-auth-token-response
- name: GetLeadsLeadidLeadAttributesResponse
  property_count: 12
  slug: bold-penguin-get-leads-leadid-lead-attributes-response
- name: GetMarketRecommendationResponse
  property_count: 12
  slug: bold-penguin-get-market-recommendation-response
- name: PostExchangeApplicationFormsResponse
  property_count: 24
  slug: bold-penguin-post-exchange-application-forms-response
- name: PostMarketRecommendationRequest
  property_count: 1
  slug: bold-penguin-post-market-recommendation-request
- name: PostProspectsRequest
  property_count: 31
  slug: bold-penguin-post-prospects-request
- name: PostTargetagentInvocationsRequest
  property_count: 9
  slug: bold-penguin-post-targetagent-invocations-request
- name: PostTargetagentInvocationsResponse
  property_count: 9
  slug: bold-penguin-post-targetagent-invocations-response
- name: PostTenantsTenantidApplicationFormsSearchRequest
  property_count: 6
  slug: bold-penguin-post-tenants-tenantid-application-forms-search-request
- name: PostTokenRequest
  property_count: 3
  slug: bold-penguin-post-token-request
jsonld:
- class_count: 27
  name: Bold Penguin Context
  property_count: 101
  slug: bold-penguin-context
layout: provider
modified: '2026-10-02'
name: Bold Penguin
nav: Providers
network: true
overview: 'Bold Penguin publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Application Forms API, Attachments API, Auth API, and 9 more. Tagged areas include Company, Insurance, Platform, Commercial, and Artificial Intelligence.


  The Bold Penguin catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bold Penguin''s developer surface includes changelog, authentication, getting-started guide, and 21 more developer resources.'
random_paper: 10
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bold Penguin API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: bold-penguin-rules
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 33.5
    developer_ergonomics: 40.5
    discoverability: 64.3
    operational_transparency: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 15
      marker_coverage: 100.0
      total: 15
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Bold Penguin Authentication
  slug: bold-penguin-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bold Penguin Domain Security
  slug: bold-penguin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bold-penguin
tags:
- Company
- Insurance
- Platform
- Commercial
- Artificial Intelligence
website: https://boldpenguin.com/
---
