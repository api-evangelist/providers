---
access_model:
  confidence: high
  label: Customer-only API, keys issued by support ticket
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - plans
  - probe
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Choozle Agentic Access
  operation_count: 3
  slug: choozle-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 3
apis:
- baseURL: https://app.choozle.com/api
  baseurl_source: declared
  description: Returns the advertising account structure the API user can reach — accounts, their campaigns, and each campaign's ad groups — in one unpaginated document. One operation, read-only.
  name: Choozle Accounts API
  slug: choozle-accounts-api
- baseURL: https://app.choozle.com/api
  baseurl_source: declared
  description: The token exchange. POST an API profile email, an ISO 8601 timestamp within five minutes of server time, and an HMAC-SHA256 hex signature to receive a token valid two hours. One operation, the API's o
  name: Choozle Authorization API
  slug: choozle-authorization-api
- baseURL: https://app.choozle.com/api
  baseurl_source: declared
  description: Returns one performance row per active ad group per day for an account, optionally filtered by date range and by exactly one of campaign, campaign status, or ad group ids. Rows are omitted for days wi
  name: Choozle Reports API
  slug: choozle-reports-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Choozle Reporting Accounts API
  slug: open-choozle-accounts-api
- collection_type: open
  name: Choozle Reporting Authorization API
  slug: open-choozle-authorization-api
- collection_type: open
  name: Choozle Reporting Reports API
  slug: open-choozle-reports-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/openapi.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/choozle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/choozle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/choozle-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/choozle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/choozle-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/choozle-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/choozle-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://choozle.com/data-processing-agreement/
- group: design
  title: ''
  type: DataModel
  url: data-model/choozle-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/choozle-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/choozle-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vocabulary.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jsonld.json
- group: design
  title: ''
  type: Rules
  url: rules/choozle-jsonschema-spectral-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/choozle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/choozle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/choozle/refs/heads/main/finops/finops.md
- group: company
  title: ''
  type: Website
  url: https://choozle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.choozle.com/
- group: docs
  title: ''
  type: APIReference
  url: https://app.choozle.com/apidoc/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.choozle.com/connecting-to-choozles-reporting-api
- group: operate
  title: ''
  type: Support
  url: https://help.choozle.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/choozle
- group: company
  title: ''
  type: Blog
  url: https://choozle.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://choozle.com/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://choozle.com/managed-self-service/
- group: start
  title: ''
  type: Login
  url: https://app.choozle.com/users/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://choozle.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://choozle.com/privacy-policy/
- group: other
  title: ''
  type: Platform
  url: https://choozle.com/the-platform/
created: '2026-06-13'
description: 'Choozle is a Denver-based self-service demand-side platform (DSP) for programmatic digital advertising across Display, Connected TV, Video, Audio, Native, DOOH, Search and Social, with buying routed through The Trade Desk and Amazon DSP. Its public developer surface is a single read-only product, the Choozle Outbound Reporting API: three operations that exchange an HMAC-SHA256 signature for a two-hour token, return the account/campaign/ad group tree, and return daily per-ad-group performance rows. Campaign, audience, creative and deal management are performed in the web application only — no public API writes to them. Keys are issued by support ticket rather than self-service.'
examples:
- key_count: 5
  name: Get Reports
  slug: get-reports
- key_count: 5
  name: Get Token
  slug: get-token
- key_count: 5
  name: List Accounts
  slug: list-accounts
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/choozle.png
json_schemas:
- name: AuthorizationRequest
  property_count: 3
  slug: authorization-request
- name: ReportRow
  property_count: 17
  slug: report-row
layout: provider
modified: '2026-08-13'
name: Choozle
nav: Providers
network: true
overview: 'Choozle publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Authorization API, and Reports API. Tagged areas include Digital Advertising, Programmatic Advertising, DSP, Demand-Side Platform, and Advertising Reporting.


  The Choozle catalog on APIs.io includes 1 Spectral governance ruleset.


  Choozle''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Choozle Plans Pricing
  plan_count: 2
  slug: choozle-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Choozle Rate Limits
  slug: choozle-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Choozle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: choozle-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 26
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 43.2
    contract_quality: 66.0
    developer_ergonomics: 47.0
    discoverability: 74.1
    governance: 43.2
    operational_transparency: 2.6
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/choozle/refs/heads/main/screenshots/choozle-2026-06-20T174326.png
security:
- kind: authentication
  name: Choozle Authentication
  slug: choozle-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Choozle Domain Security
  slug: choozle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: choozle
tags:
- Digital Advertising
- Programmatic Advertising
- DSP
- Demand-Side Platform
- Advertising Reporting
- Campaign Reporting
- Display Advertising
- Connected TV
- CTV
- Video Advertising
- Native Advertising
- DOOH
- Reporting
- Real-Time Bidding
- RTB
- AdTech
website: https://choozle.com/
---
