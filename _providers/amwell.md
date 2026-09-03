---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: 'Amwell''s Converge platform REST APIs, which Amwell states leverage HL7 FHIR and single sign-on, let partners embed and orchestrate virtual care — urgent, scheduled, behavioral, and specialty visits — '
  name: Amwell Converge Platform API
  slug: amwell-converge-platform-api
- description: Amwell's embedded telehealth software development kits for iOS, Android, and web, enabling organizations to plug live virtual visits directly into their own consumer and clinical applications. The SDK
  name: Amwell Telehealth SDK
  slug: amwell-telehealth-sdk
- description: 'Amwell''s verified embedded-telehealth integration for Epic, delivered through the Epic App Orchard, and its embedded telehealth solution inside Oracle Cerner Millennium, both launching virtual visits '
  name: Amwell EHR Integration
  slug: amwell-ehr-integration
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amwell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amwell.com
- group: docs
  title: ''
  type: Documentation
  url: https://business.amwell.com/the-amwell-platform
- group: company
  title: ''
  type: Blog
  url: https://business.amwell.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.amwell.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amwell-lifecycle.yml
- group: operate
  title: ''
  type: Support
  url: https://business.amwell.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://business.amwell.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://business.amwell.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amwell
- group: auth
  title: ''
  type: Authentication
  url: authentication/amwell-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amwell-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://business.amwell.com/who-we-serve/government
- group: build
  title: ''
  type: Packages
  url: packages/amwell-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amwell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amwell-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amwell-llms.txt
coverage:
  checked: '2026-08-15'
  detail: Amwell publishes no developer surface at all — developers.amwell.com is a wildcard vhost that answers 200 with the consumer Amwell "Online Care" sign-up app for any subdomain, including ones that do not exist — and the only stated route to the Converge API and telehealth SDK is emailing SDK@americanwell.com or the partner contact form.
  evidence:
  - status: 200
    url: https://developers.amwell.com/
  - status: 200
    url: https://zzz-not-a-real-host-9x.amwell.com/
  - status: 404
    url: https://developers.amwell.com/openapi.json
  - status: 404
    url: https://business.amwell.com/pricing/
  reason: sales-gate
  state: gated
created: '2026-07-24'
description: Amwell (American Well) is a United States telehealth and hybrid-care technology company headquartered in Boston, Massachusetts, whose Converge platform delivers virtual and in-person care at scale for health systems, health plans, employers, and government programs. Amwell describes Converge as an open architecture whose APIs leverage HL7 FHIR and single sign-on, with embedded telehealth mobile and web SDKs (iOS, Android, web) so partners can plug urgent, scheduled, behavioral, and specialty virtual visits directly into their own consumer apps, patient portals, and clinical workflows. Amwell ships a verified embedded-telehealth integration with Epic through the Epic App Orchard and an embedded telehealth solution inside Oracle Cerner Millennium, and connects software-enabled Carepoint devices. Amwell publishes no public developer portal, API reference, or machine-readable specification of any kind — SDK and API access is arranged through a partner and sales conversation (SDK@americanwell.com),
  so the integration contract is not readable before a deal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-15'
name: Amwell
nav: Providers
network: true
overview: 'Amwell publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Telehealth, Virtual Care, and FHIR.


  Amwell''s developer surface includes documentation, engineering blog, support, authentication, and 13 more developer resources.'
plans:
- name: Amwell Plans Pricing
  plan_count: 0
  slug: amwell-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Amwell Rate Limits
  slug: amwell-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 26.3
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
    score: 55.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amwell/refs/heads/main/screenshots/amwell-2026-07-25T200143.png
security:
- kind: authentication
  name: Amwell Authentication
  slug: amwell-authentication
  summary_line: oauth2/openIdConnect/saml · 4 schemes
- kind: domain-security
  name: Amwell Domain Security
  slug: amwell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amwell
tags:
- Healthcare
- United States
- Telehealth
- Virtual Care
- FHIR
- HL7
- Interoperability
- EHR
- SDK
website: https://www.amwell.com
---
