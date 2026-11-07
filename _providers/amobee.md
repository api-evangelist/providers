---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 8
  name: Amobee Agentic Access
  operation_count: 19
  slug: amobee-agentic-access
  summary_line: 19 operations · 8 acting · 8 human-in-the-loop
api_count: 1
apis:
- description: REST API for managing cross-channel advertising campaigns including advertisers, insertion orders, line items, packages, creatives, and ads across programmatic channels. Authentication uses OAuth2 cli
  name: Amobee Campaign API
  slug: amobee-campaign-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The env-vars-test-controller API from Amobee — 1 operation(s) for env-vars-test-controller.
  name: Amobee Env Vars Test Controller API
  slug: amobee-env-vars-test-controller-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The gateway-swagger-controller API from Amobee — 2 operation(s) for gateway-swagger-controller.
  name: Amobee Gateway Swagger Controller API
  slug: amobee-gateway-swagger-controller-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The health-check API from Amobee — 1 operation(s) for health-check.
  name: Amobee Health Check API
  slug: amobee-health-check-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The ip-controller API from Amobee — 1 operation(s) for ip-controller.
  name: Amobee Ip Controller API
  slug: amobee-ip-controller-api
- baseURL: https://services.amobee.com/campaign/v3/api
  baseurl_source: declared
  description: The tcf-disclosure-controller API from Amobee — 2 operation(s) for tcf-disclosure-controller.
  name: Amobee Tcf Disclosure Controller API
  slug: amobee-tcf-disclosure-controller-api
artifact_total: 18
collections:
- collection_type: open
  name: OpenAPI definition
  slug: open-amobee-services
common:
- group: agent
  href: https://artifacts.apis.io/amobee/agentic-access/amobee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amobee-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/amobee/rules/amobee-rules.yml
  title: ''
  type: Spectral
  url: rules/amobee-rules.yml
- group: design
  href: https://artifacts.apis.io/amobee/json-ld/amobee-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amobee-context.jsonld
- group: design
  href: https://artifacts.apis.io/amobee/vocabulary/amobee-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amobee-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/amobee/data-model/amobee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amobee-data-model.yml
- group: operate
  href: https://artifacts.apis.io/amobee/lifecycle/amobee-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/amobee-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/amobee/hosts/amobee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amobee-hosts.yml
- group: build
  href: https://artifacts.apis.io/amobee/integrations/amobee-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/amobee-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/amobee/vendors/amobee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amobee-vendors.yml
- group: build
  href: https://artifacts.apis.io/amobee/packages/amobee-packages.yml
  title: ''
  type: SDKs
  url: packages/amobee-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.amobee.com/trust/ccpa/
- group: company
  title: ''
  type: Blog
  url: https://www.amobee.com/blog/moving-forward/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amobee.com/trust/master-service-terms/schedule-a/
- group: auth
  href: https://artifacts.apis.io/amobee/security/amobee-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amobee-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amobee/security/amobee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amobee-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amobee.com/trust/master-service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amobee.com/trust/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.amobee.com/
- group: start
  title: ''
  type: Login
  url: https://platform.amobee.com/app/account/index.htm
- group: auth
  href: https://artifacts.apis.io/amobee/security/amobee-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/amobee-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/amobee/well-known/amobee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amobee-well-known.yml
- group: auth
  href: https://artifacts.apis.io/amobee/well-known/amobee-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amobee-security.txt
- group: design
  href: https://artifacts.apis.io/amobee/conventions/amobee-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amobee-conventions.yml
- group: design
  href: https://artifacts.apis.io/amobee/errors/amobee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amobee-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amobee/lifecycle/amobee-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amobee-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/amobee/conformance/amobee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amobee-conformance.yml
- group: auth
  href: https://artifacts.apis.io/amobee/conformance/amobee-conformance.yml
  title: ''
  type: Compliance
  url: conformance/amobee-conformance.yml
- group: build
  href: https://artifacts.apis.io/amobee/packages/amobee-packages.yml
  title: ''
  type: Packages
  url: packages/amobee-packages.yml
- group: other
  href: https://artifacts.apis.io/amobee/overlays/amobee-services-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amobee-services-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Amobee
coverage:
  checked: '2026-08-12'
  detail: Amobee is now operated as Nexxen and its developer surface went with the rebrand — the Platform API reference at services.amobee.com/campaign/v3/doc/ returns 404 while the OAuth token endpoint and DSP console still serve existing customers, and the remaining reference lives in a Zendesk help center that refuses anonymous requests (403, Help Center API 401).
  evidence:
  - status: 404
    url: https://services.amobee.com/campaign/v3/doc/
  - status: 403
    url: https://help.amobee.com/hc/en-us
  - status: 401
    url: https://help.amobee.com/api/v2/help_center/en-us/categories.json
  - status: 405
    url: https://services.amobee.com/accounts/v1/api/token
  - status: 200
    url: https://services.amobee.com/v3/api-docs
  reason: customer-only-docs
  state: gated
created: '2026-06-13'
description: Amobee (now Nexxen) is a digital advertising platform offering REST APIs for managing cross-channel programmatic campaigns, audience targeting, data management, and advertising analytics. The platform enables advertisers and agencies to plan, activate, and measure media across display, video, mobile, social, and TV channels through a unified DSP.
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amobee.png
json_schemas:
- name: IpResponse
  property_count: 4
  slug: amobee-ip-response
- name: SwaggerResource
  property_count: 3
  slug: amobee-swagger-resource
jsonld:
- class_count: 5
  name: Amobee Context
  property_count: 58
  slug: amobee-context
layout: provider
modified: '2026-08-12'
name: Amobee
nav: Providers
network: true
overview: 'Amobee publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Env Vars Test Controller API, Gateway Swagger Controller API, Health Check API, and 3 more. Tagged areas include Digital Advertising, DSP, Programmatic, Campaign Management, and Audience Targeting.


  The Amobee catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amobee''s developer surface includes engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 17
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Amobee API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: amobee-rules
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 75.2
    catalog_earned_first_party: 16.0
    catalog_gap: 39.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 71.1
    contract_governance: 35.6
    contract_quality: 57.8
    developer_ergonomics: 8.3
    discoverability: 66.1
    operational_transparency: 42.1
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amobee/amobee-2026-06-20T171938.png
security:
- kind: authentication
  name: Amobee Authentication
  slug: amobee-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Amobee Domain Security
  slug: amobee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amobee Vulnerability Disclosure
  slug: amobee-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amobee
tags:
- Digital Advertising
- DSP
- Programmatic
- Campaign Management
- Audience Targeting
- Data Management Platform
- AdTech
- Samsung Ads
website: https://www.amobee.com/
---
