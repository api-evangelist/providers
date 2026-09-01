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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 8
  name: Saviynt Agentic Access
  operation_count: 8
  slug: saviynt-agentic-access
  summary_line: 8 operations · 8 acting · 8 human-in-the-loop
api_count: 1
apis:
- description: The Analytics API from Saviynt — 8 operation(s) for analytics.
  name: Saviynt Analytics API
  slug: saviynt-analytics-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Saviynt Enterprise Identity Cloud (EIC) Analytics API
  slug: open-saviynt-analytics-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/saviynt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/saviynt-trust-center.yml
- group: auth
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
- group: commercial
  title: ''
  type: Plans
  url: plans/saviynt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/saviynt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/saviynt-finops.yml
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
overview: 'Saviynt publishes 1 API on the [APIs.io](https://apis.io/) network: Analytics API. Tagged areas include Identity Governance, Identity Administration, Access Management, Privileged Access Management, and Segregation of Duties.


  The Saviynt catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Saviynt''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Saviynt Plans Pricing
  plan_count: 3
  slug: saviynt-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
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
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 28.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 50.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 42.1
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
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
