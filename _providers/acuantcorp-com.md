---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Identity verification and document capture APIs as described on the Acuant (now GBG) developer pages.
  name: Acuant API
  slug: acuant-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/acuantcorp-com/llms/acuantcorp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/acuantcorp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/acuantcorp-com/hosts/acuantcorp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/acuantcorp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/acuantcorp-com/vendors/acuantcorp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/acuantcorp-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.gbg.com/en/trust/
- group: operate
  title: ''
  type: Support
  url: https://www.gbg.com/nz/support/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.gbg.com/en-us/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gbg.com/en/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.gbg.com/en-us/news/
- group: start
  title: ''
  type: Login
  url: https://www.gbg.com/en/login/
- group: company
  title: ''
  type: Blog
  url: https://www.gbg.com/en-us/blog/
- group: auth
  href: https://artifacts.apis.io/acuantcorp-com/security/acuantcorp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/acuantcorp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gbg.com/en-us/
created: '2026-10-25'
description: Acuant provides identity verification, document capture, and biometric authentication solutions for businesses. Their platform enables secure onboarding, fraud detection, and compliance across industries such as finance, healthcare, and government. Acuant’s APIs allow developers to integrate document scanning, facial recognition, and data extraction into applications, supporting a range of formats and regulatory requirements. The company focuses on delivering scalable, cloud‑based services that streamline identity proofing and enhance security for digital transactions.
image: https://www.gbg.com/media/fj1baavn/facebook-profile-picture.png
layout: provider
modified: '2026-10-25'
name: Acuant
nav: Providers
network: true
overview: 'Acuant is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IdentityVerification, DocumentCapture, BiometricAuthentication, and FraudDetection.


  Acuant''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acuantcorp Com Domain Security
  slug: acuantcorp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acuantcorp-com
tags:
- Company
- IdentityVerification
- DocumentCapture
- BiometricAuthentication
- FraudDetection
website: https://www.gbg.com/en-us/
---
