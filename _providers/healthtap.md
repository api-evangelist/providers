---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthtap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.healthtap.com/
- group: company
  title: ''
  type: Blog
  url: https://www.healthtap.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.healthtap.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.healthtap.com/features-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.healthtap.com/sign_up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.healthtap.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.healthtap.com/privacy/statement/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HealthTap
- group: auth
  title: ''
  type: Compliance
  url: https://www.healthtap.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/healthtap-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/healthtap-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/healthtap-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/healthtap-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/healthtap-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/healthtap-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/healthtap_stock/
created: '2026-08-04'
description: 'HealthTap is a United States virtual primary care medical group and telehealth technology company. It operates a nationwide network of board-certified, U.S.-licensed physicians covering all 50 states and Washington, D.C., and delivers video and phone visits for primary care, urgent care, chronic condition management and preventive care, plus 90-day follow-up text messaging with the treating doctor, prescription and lab ordering, and Dr. A.I. symptom triage. It sells direct to consumers on a monthly membership plus a per-visit fee, is in network with commercial and Medicare plans, and is deployed white-labeled or co-branded with employers, health plans, health systems and retailers. HealthTap previously operated a public developer platform, HealthTap Cloud (developers.healthtap.com, launched November 2016), which offered REST APIs and iOS/Android SDKs over its HOPES health operating system; that portal no longer resolves in DNS and HealthTap publishes no public API documentation,
  OpenAPI, GraphQL, AsyncAPI or MCP surface today. Partner data exchange runs through contracted integrations such as Commure and Health Gorilla. Sector: healthtech.'
layout: provider
modified: '2026-08-04'
name: HealthTap
nav: Providers
network: true
overview: 'HealthTap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Telehealth, Telemedicine, and Virtual Care.


  HealthTap''s developer surface includes engineering blog, support, pricing, signup flow, and 13 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.7
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthtap/refs/heads/main/screenshots/healthtap-2026-08-07T170028.png
security:
- kind: domain-security
  name: Healthtap Domain Security
  slug: healthtap-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Healthtap Trust Center
  slug: healthtap-trust-center
  summary_line: SOC 2 Type 2, HIPAA
slug: healthtap
tags:
- Company
- Health Tech
- Telehealth
- Telemedicine
- Virtual Care
- Healthcare
- Primary Care
- Digital Health
website: https://www.healthtap.com/
---
