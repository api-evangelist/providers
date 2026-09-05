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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/by-miles-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/by-miles-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bymiles.co.uk/security-vulnerability-reporting-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.bymiles.co.uk/information-security
- group: design
  title: ''
  type: Conformance
  url: conformance/by-miles-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/by-miles-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/by-miles-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.bymiles.co.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.bymiles.co.uk/insure/magazine/
- group: operate
  title: ''
  type: Support
  url: https://help.bymiles.co.uk/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://dashboard.bymiles.co.uk/account/login
- group: company
  title: ''
  type: Partners
  url: https://www.bymiles.co.uk/partners
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bymiles.co.uk/terms-of-business
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.bymiles.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bymiles.co.uk/privacy-policy
- group: company
  title: ''
  type: Press
  url: https://www.bymiles.co.uk/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/by-miles
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bymiles
- group: company
  title: ''
  type: Twitter
  url: https://www.twitter.com/bymiles
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/gobymiles
created: '2026-07-25'
description: 'By Miles is a London-based insurtech that pioneered pay-by-mile motor insurance in the United Kingdom, founded in 2016 for low-mileage drivers who cover under roughly 7,000 miles a year. Its single line of business is UK private motor (personal lines property and casualty), priced as a fixed annual premium covering the parked car plus a per-mile charge for the distance actually driven. Mileage is measured either by the OBD-II "Miles Tracker" telematics dongle or, on its "connect" trackerless policies, by pulling odometer data directly from the manufacturer''s connected-car platform after the driver links a Tesla, Ford or Mercedes-Benz account. By Miles was acquired by Direct Line Group in April 2023 and, following Aviva''s acquisition of Direct Line Group, has been wound down — it stopped quoting new business and, from 6 January 2026, stopped offering renewal quotes to existing customers. Its API posture is that of a pure API CONSUMER, not a producer: it was the first UK insurtech
  directly authorised by the FCA as an AISP/PISP to consume Open Banking APIs (January 2020), and it consumes OEM connected-car APIs for mileage, but it publishes no public self-serve developer portal, no reference documentation, no OpenAPI, no Postman collection and no webhook catalogue. The only integration surface is a partnerships email address and a private AWS API Gateway host serving its own mobile app, so this record is a partner-gated stub by design.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: By Miles
nav: Providers
network: true
overview: 'By Miles is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Insurtech, Property and Casualty, and Motor Insurance.


  By Miles'' developer surface includes engineering blog, support, and 18 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 19.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: UK
      standard: uk-gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/by-miles/refs/heads/main/screenshots/by-miles-2026-07-25T204131.png
security:
- kind: domain-security
  name: By Miles Domain Security
  slug: by-miles-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: By Miles Vulnerability Disclosure
  slug: by-miles-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: by-miles
tags:
- Insurance
- United Kingdom
- Insurtech
- Property and Casualty
- Motor Insurance
- Usage-Based Insurance
- Telematics
- Connected Car
- Direct to Consumer
- Open Banking
- No Public API
website: https://www.bymiles.co.uk/
---
