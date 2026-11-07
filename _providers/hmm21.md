---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hmm21 Agentic Access
  operation_count: 9
  slug: hmm21-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 6
apis:
- baseURL: https://apigw.hmm21.com/gateway/AN/v1
  baseurl_source: declared
  description: The Arrival Notice API from HMM — 1 operation(s) for arrival notice.
  name: HMM Arrival Notice API
  slug: hmm21-arrival-notice-api
- baseURL: https://apigw.hmm21.com/gateway/AN/v1
  baseurl_source: declared
  description: The Bookings API from HMM — 2 operation(s) for bookings.
  name: HMM Bookings API
  slug: hmm21-bookings-api
- baseURL: https://apigw.hmm21.com/gateway/AN/v1
  baseurl_source: declared
  description: The Eblcompany Id Requests API from HMM — 1 operation(s) for eblcompany id requests.
  name: HMM Eblcompany Id Requests API
  slug: hmm21-eblcompany-id-requests-api
- baseURL: https://apigw.hmm21.com/gateway/AN/v1
  baseurl_source: declared
  description: The KR NEXAWAVE CERT FILE API from HMM — 1 operation(s) for kr nexawave cert file.
  name: HMM KR NEXAWAVE CERT FILE API
  slug: hmm21-kr-nexawave-cert-file-api
- baseURL: https://apigw.hmm21.com/gateway/AN/v1
  baseurl_source: declared
  description: The KR NEXAWAVE CLASS SURVEY API from HMM — 1 operation(s) for kr nexawave class survey.
  name: HMM KR NEXAWAVE CLASS SURVEY API
  slug: hmm21-kr-nexawave-class-survey-api
- baseURL: https://apigw.hmm21.com/gateway/AN/v1
  baseurl_source: declared
  description: The KR NEXAWAVE CMS PMS API from HMM — 1 operation(s) for kr nexawave cms pms.
  name: HMM KR NEXAWAVE CMS PMS API
  slug: hmm21-kr-nexawave-cms-pms-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/hmm21/vocabulary/hmm21-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hmm21-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/hmm21/integrations/hmm21-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/hmm21-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/hmm21/agentic-access/hmm21-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hmm21-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/hmm21/rules/hmm21-rules.yml
  title: ''
  type: Spectral
  url: rules/hmm21-rules.yml
- group: agent
  href: https://artifacts.apis.io/hmm21/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hmm21/conventions/hmm21-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hmm21-conventions.yml
- group: start
  href: https://artifacts.apis.io/hmm21/sandbox/hmm21-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hmm21-sandbox.yml
- group: design
  href: https://artifacts.apis.io/hmm21/errors/hmm21-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hmm21-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hmm21/conformance/hmm21-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hmm21-conformance.yml
- group: other
  href: https://artifacts.apis.io/hmm21/overlays/hmm21-arrival-notice-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hmm21-arrival-notice-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/hmm21/well-known/hmm21-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hmm21-well-known.yml
- group: other
  href: https://artifacts.apis.io/hmm21/hosts/hmm21-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hmm21-hosts.yml
- group: other
  href: https://artifacts.apis.io/hmm21/vendors/hmm21-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hmm21-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hmm21/authentication/hmm21-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hmm21-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hmm21/security/hmm21-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hmm21-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hmm21.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.hmm21.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hmm21.com/company/digital/digitalInterfaceApi.do
- group: docs
  title: ''
  type: APIReference
  url: https://apiportal.hmm21.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://apiportal.hmm21.com/info
- group: start
  title: ''
  type: SignUp
  url: https://apiportal.hmm21.com/signup
- group: start
  title: ''
  type: Login
  url: https://apiportal.hmm21.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.hmm21.com/company/faq.do
- group: company
  title: ''
  type: News
  url: https://www.hmm21.com/company/newsList.do
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hmm21.com/company/privacypolicy.do
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hyundai-merchant-marine
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/hmmofficial1976
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/hmm21.official/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/hmm21.official/
created: '2026-10-18'
description: HMM Co., Ltd. is a South Korean shipping and logistics company headquartered at the Hyundai Group Building in Seoul. Its services include container shipping (general, reefer, oversized and dangerous cargo), bulk shipping (tankers, gas tankers, pure car and truck carriers, heavy lift and project cargo), terminals and intermodal transport. HMM says it launched four API services in 2022 and is adding more, from booking through to payment, that follow the Digital Container Shipping Association (DCSA) standards. The APIs are offered through the HMM Open API Developer Portal (apiportal.hmm21.com), where companies sign up and wait for approval before using them. The gallery lists APIs such as DCSA Arrival Notice, DCSA Booking and e-BL Company ID receipt.
image: https://apiportal.hmm21.com/image/logo.png
layout: provider
modified: '2026-10-18'
name: HMM
nav: Providers
network: true
overview: 'HMM publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Arrival Notice API, Bookings API, Eblcompany Id Requests API, and 3 more. Tagged areas include Company, Shipping, Logistics, Container Shipping, and Maritime.


  The HMM catalog on APIs.io includes 1 Spectral governance ruleset.


  HMM''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, signup flow, support, and 22 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: HMM API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: hmm21-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 40.5
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hmm21/hmm21-2026-11-03T133425.png
security:
- kind: authentication
  name: Hmm21 Authentication
  slug: hmm21-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hmm21 Domain Security
  slug: hmm21-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: hmm21-manage-booking
  slug: hmm21-manage-booking
slug: hmm21
tags:
- Company
- Shipping
- Logistics
- Container Shipping
- Maritime
- DCSA
- Supply Chain
website: https://www.hmm21.com
---
