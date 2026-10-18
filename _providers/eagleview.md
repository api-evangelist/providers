---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Eagleview Agentic Access
  operation_count: 21
  slug: eagleview-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 1
apis:
- baseURL: https://sandbox.apicenter.eagleview.com
  baseurl_source: declared
  description: Occasionally, a report will need to be adjusted by the customer before it can continue processing. This could be due to a necessary upgrade/downgrade due to the image quality available.
  name: EagleView Order Adjustments API
  slug: eagleview-order-adjustments-api
- baseURL: https://sandbox.apicenter.eagleview.com
  baseurl_source: declared
  description: Once the report has been created in the Ordering stage, it is possible to query the status of the order via Order Status API methods.
  name: EagleView Order Status API
  slug: eagleview-order-status-api
- baseURL: https://sandbox.apicenter.eagleview.com
  baseurl_source: declared
  description: The EagleView ordering process offers many API methods which allow for varying degrees of customization. Ordering is the first step in the EagleView structure measurement process, as it kickstarts the
  name: EagleView Ordering API
  slug: eagleview-ordering-api
- baseURL: https://sandbox.apicenter.eagleview.com
  baseurl_source: declared
  description: Once a report has completed processing, it is possible to retrieve it via Retrieving Files API methods.
  name: EagleView Retrieving Files API
  slug: eagleview-retrieving-files-api
artifact_total: 10
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/agentic-access/eagleview-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eagleview-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/rate-limits/eagleview-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eagleview-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/plans/eagleview-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eagleview-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/rules/eagleview-rules.yml
  title: ''
  type: Spectral
  url: rules/eagleview-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/vocabulary/eagleview-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eagleview-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/data-model/eagleview-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eagleview-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/conventions/eagleview-conventions.yml
  title: ''
  type: Conventions
  url: conventions/eagleview-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/sandbox/eagleview-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/eagleview-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/authentication/eagleview-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eagleview-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/errors/eagleview-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eagleview-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/conformance/eagleview-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eagleview-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/llms/eagleview-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eagleview-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/hosts/eagleview-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eagleview-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eagleview.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eagleview.com/privacy-statement/
- group: company
  title: ''
  type: Newsroom
  url: https://www.eagleview.com/newsroom/
- group: other
  title: ''
  type: Leadership
  url: https://www.eagleview.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eagleview/refs/heads/main/security/eagleview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eagleview-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eagleview.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.eagleview.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.eagleview.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eagleview.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.eagleview.com/blogs/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.eagleview.com/help-center/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.eagleview.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: EagleView provides geospatial intelligence, aerial imagery, and data solutions for property intelligence. Their platform offers high‑resolution aerial imagery, 3D models, property reports, and AI‑driven analytics for residential, commercial, and government customers. EagleView serves industries such as roofing, solar, insurance, utilities, and emergency management, delivering actionable insights through cloud‑based applications and APIs.
image: https://www.eagleview.com/wp-content/uploads/2025/06/EV-Opengraph-Thumbnail-Logo.png
layout: provider
modified: '2026-10-13'
name: EagleView
nav: Providers
network: true
overview: 'EagleView publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Order Adjustments API, Order Status API, Ordering API, and 1 more. Tagged areas include Geospatial, AerialImagery, Data Analytics, Real Estate, and Insurance.


  The EagleView catalog on APIs.io includes 1 Spectral governance ruleset.


  EagleView''s developer surface includes sandbox, authentication, API reference, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Eagleview Plans Pricing
  plan_count: 24
  slug: eagleview-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Eagleview Rate Limits
  slug: eagleview-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: EagleView API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: eagleview-rules
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 46.7
    developer_ergonomics: 42.9
    discoverability: 76.8
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Eagleview Authentication
  slug: eagleview-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Eagleview Domain Security
  slug: eagleview-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eagleview
tags:
- Geospatial
- AerialImagery
- Data Analytics
- Real Estate
- Insurance
website: https://www.eagleview.com/
---
