---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/api-evangelist/servicenow/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/api-evangelist/servicenow/tree/main/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/service-now-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/api-evangelist/servicenow
- group: start
  title: ''
  type: Portal
  url: https://developer.servicenow.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.servicenow.com/docs/bundle/yokohama-api-reference/page/integrate/inbound-rest/concept/c_RESTAPI.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.servicenow.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.servicenow.com/products.html
- group: start
  title: ''
  type: Sandbox
  url: https://developer.servicenow.com/dev.do
- group: company
  title: ''
  type: Blog
  url: https://www.servicenow.com/blogs.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.servicenow.com/community/now-platform-articles/tkb-p/now-platform-articles
- group: operate
  title: ''
  type: StatusPage
  url: https://status.servicenow.com
created: '2026-05-23'
description: This repository is an alias for the canonical API Evangelist ServiceNow profile. The provider is published as `servicenow` at https://github.com/api-evangelist/servicenow, which holds the apis.yml index, OpenAPI specs, Naftiko capabilities, JSON Schema, JSON Structure, JSON-LD, examples, plans, rate-limits, FinOps, and Spectral rules for every documented ServiceNow REST API (Table, Aggregate, Attachment, Import Set, Batch, Scripted REST, Now Assist, and related surfaces). Use the canonical repo for all profiling artifacts and updates. ServiceNow's product domain uses the hyphenated `service-now.com` (the instance base URL) while the company brand and developer portal use `servicenow.com`; both resolve to the same provider profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/service-now.png
layout: provider
modified: '2026-05-23'
name: ServiceNow (alias)
nav: Providers
network: true
overview: 'ServiceNow (alias) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Alias, Enterprise Platform, ITSM, and Workflow-Automation.


  ServiceNow (alias)''s developer surface includes developer portal, API reference, documentation, pricing, sandbox, engineering blog, changelog, and 5 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 16.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/service-now/refs/heads/main/screenshots/service-now-2026-06-20T193736.png
security:
- kind: domain-security
  name: Service Now Domain Security
  slug: service-now-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: service-now
tags:
- Alias
- Enterprise Platform
- ITSM
- Workflow-Automation
website: https://developer.servicenow.com
---
