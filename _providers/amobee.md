---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for managing cross-channel advertising campaigns including advertisers, insertion orders, line items, packages, creatives, and ads across programmatic channels. Authentication uses OAuth2 cli
  name: Amobee Campaign API
  slug: amobee-campaign-api
- description: The env-vars-test-controller API from Amobee — 1 operation(s) for env-vars-test-controller.
  name: Amobee Env Vars Test Controller API
  slug: amobee-env-vars-test-controller-api
- description: The gateway-swagger-controller API from Amobee — 2 operation(s) for gateway-swagger-controller.
  name: Amobee Gateway Swagger Controller API
  slug: amobee-gateway-swagger-controller-api
- description: The health-check API from Amobee — 1 operation(s) for health-check.
  name: Amobee Health Check API
  slug: amobee-health-check-api
- description: The ip-controller API from Amobee — 1 operation(s) for ip-controller.
  name: Amobee Ip Controller API
  slug: amobee-ip-controller-api
- description: The tcf-disclosure-controller API from Amobee — 2 operation(s) for tcf-disclosure-controller.
  name: Amobee Tcf Disclosure Controller API
  slug: amobee-tcf-disclosure-controller-api
artifact_total: 13
collections:
- collection_type: open
  name: OpenAPI definition
  slug: open-amobee-services
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amobee-vulnerability-disclosure.yml
- group: auth
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
  title: ''
  type: Security
  url: security/amobee-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amobee-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amobee-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/amobee-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amobee-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amobee-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amobee-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amobee-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/amobee-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/amobee-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amobee-services-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amobee-llms.txt
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
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amobee.png
layout: provider
modified: '2026-08-12'
name: Amobee
nav: Providers
network: true
overview: 'Amobee publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Env Vars Test Controller API, Gateway Swagger Controller API, Health Check API, and 2 more. Tagged areas include Digital Advertising, DSP, Programmatic, Campaign Management, and Audience Targeting.


  Amobee''s developer surface includes authentication and 21 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 8
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.9
  facets:
    access_clarity: 64.5
    commercial_clarity: 64.5
    contract_governance: 18.2
    contract_quality: 42.6
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 35.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/screenshots/amobee-2026-06-20T171938.png
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
  summary_line: Hackerone · security.txt · contact published
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
