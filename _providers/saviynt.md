---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 8
  name: Saviynt Agentic Access
  operation_count: 8
  slug: saviynt-agentic-access
  summary_line: 8 operations · 8 acting · 8 human-in-the-loop
api_count: 2
apis:
- baseURL: https://{tenant}.saviyntcloud.com/ECM/api
  baseurl_source: declared
  description: The Analytics API from Saviynt — 8 operation(s) for analytics.
  name: Saviynt Analytics API
  slug: saviynt-analytics-api
- baseURL: https://{tenant}.saviyntcloud.com/ECM/api
  baseurl_source: declared
  description: The connections API from Saviynt — 3 operation(s) for connections.
  name: Saviynt Connections API
  slug: saviynt-connections-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Saviynt Enterprise Identity Cloud (EIC) Analytics API
  slug: open-saviynt-analytics-api
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/rules/saviynt-rules.yml
  title: ''
  type: Spectral
  url: rules/saviynt-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/rules/saviynt-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/saviynt-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/json-ld/saviynt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/saviynt-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/vocabulary/saviynt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/saviynt-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/data-model/saviynt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/saviynt-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.saviynt.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/conformance/saviynt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/saviynt-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/llms/saviynt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/saviynt-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/well-known/saviynt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/saviynt-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/hosts/saviynt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/saviynt-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/vendors/saviynt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/saviynt-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/packages/saviynt-packages.yml
  title: ''
  type: SDKs
  url: packages/saviynt-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/packages/saviynt-packages.yml
  title: ''
  type: Packages
  url: packages/saviynt-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://saviynt.com/privacy-policy?hsLang=en
- group: company
  title: ''
  type: Newsroom
  url: https://saviynt.com/newsroom
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/agentic-access/saviynt-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/saviynt-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/security/saviynt-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/saviynt-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/security/saviynt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saviynt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://saviynt.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.saviyntcloud.com/bundle/API-Reference-Guide/page/Content/API-References.htm
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/saviynt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/saviynt
- group: company
  title: ''
  type: Blog
  url: https://saviynt.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://saviynt.com/contact-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.saviynt.com/
- group: other
  title: ''
  type: X
  url: https://x.com/saviynt
- group: operate
  title: ''
  type: Support
  url: https://saviynt.com/services/customer-support
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/plans/saviynt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/saviynt-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/rate-limits/saviynt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/saviynt-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/finops/saviynt-finops.yml
  title: ''
  type: FinOps
  url: finops/saviynt-finops.yml
coverage:
  checked: '2026-10-04'
  detail: No OpenAPI or other machine-readable contract could be found despite accessible documentation.
  evidence:
  - status: null
    url: https://developers.saviynt.com/apis/rest/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-06-13'
description: Saviynt is an identity governance and administration (IGA) platform providing REST APIs for managing user identities, access requests, SOD violations, certifications, and privileged access controls across enterprise environments. The Saviynt Enterprise Identity Cloud API enables CRUD operations on user, account, and entitlement records; access request and approval workflows; rule engineering; segregation of duties policy management; and identity analytics.
examples:
- key_count: 5
  name: Fetchcontrolattributes Request
  slug: fetchControlAttributes-request
- key_count: 4
  name: Fetchcontrollist Request
  slug: fetchControlList-request
- key_count: 5
  name: Fetchcontrollist Response 200
  slug: fetchControlList-response-200
- key_count: 6
  name: Fetchruntimecontrolsdata Request
  slug: fetchRuntimeControlsData-request
- key_count: 6
  name: Fetchruntimecontrolsdatav2 Request
  slug: fetchRuntimeControlsDataV2-request
finops:
- name: Saviynt Finops
  service_category: ''
  slug: saviynt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saviynt.png
json_schemas:
- name: FetchControlAttributesRequest
  property_count: 5
  slug: FetchControlAttributesRequest
- name: FetchControlDetailsESRequest
  property_count: 6
  slug: FetchControlDetailsESRequest
- name: FetchControlDetailsRequest
  property_count: 3
  slug: FetchControlDetailsRequest
- name: FetchControlListControl
  property_count: 10
  slug: FetchControlListControl
- name: FetchControlListESRequest
  property_count: 4
  slug: FetchControlListESRequest
- name: FetchControlListRequest
  property_count: 4
  slug: FetchControlListRequest
- name: FetchControlListResponse
  property_count: 5
  slug: FetchControlListResponse
- name: FetchRuntimeControlsDataRequest
  property_count: 6
  slug: FetchRuntimeControlsDataRequest
- name: FetchRuntimeControlsDataV2Request
  property_count: 6
  slug: FetchRuntimeControlsDataV2Request
- name: RunAnalyticsControlsRequest
  property_count: 5
  slug: RunAnalyticsControlsRequest
jsonld:
- class_count: 16
  name: Saviynt Context
  property_count: 5
  slug: saviynt-context
layout: provider
modified: '2026-06-13'
name: Saviynt
nav: Providers
network: true
overview: 'Saviynt publishes 2 APIs on the [APIs.io](https://apis.io/) network: Analytics API and Connections API. Tagged areas include Identity Governance, Identity Administration, Access Management, Privileged Access Management, and Segregation of Duties.


  The Saviynt catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Saviynt''s developer surface includes documentation, engineering blog, pricing, support, and 27 more developer resources.'
plans:
- name: Saviynt Plans Pricing
  plan_count: 3
  slug: saviynt-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Saviynt Rate Limits
  slug: saviynt-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Saviynt API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: saviynt-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Saviynt API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 2
    warn: 1
  slug: saviynt-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 84.4
    catalog_earned_first_party: 0.0
    catalog_gap: 30.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.0
  facets:
    access_clarity: 73.2
    contract_governance: 22.0
    contract_quality: 47.3
    developer_ergonomics: 39.9
    discoverability: 75.0
    operational_transparency: 49.5
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/saviynt/refs/heads/main/screenshots/saviynt-2026-06-20T193458.png
security:
- kind: domain-security
  name: Saviynt Domain Security
  slug: saviynt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Saviynt Trust Center
  slug: saviynt-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, FedRAMP, FIPS 140
slug: saviynt
tags:
- Identity Governance
- Identity Administration
- Access Management
- Privileged Access Management
- Segregation of Duties
- IGA
- Security
website: https://saviynt.com
---
