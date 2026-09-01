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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.ottonova.de
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ottonova.de/datenschutz
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ottonova.de/impressum
- group: operate
  title: ''
  type: Support
  url: mailto:support@ottonova.de
- group: company
  title: ''
  type: Blog
  url: https://www.ottonova.de/magazin
- group: company
  title: ''
  type: Jobs
  url: https://www.ottonova.de/jobs
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ottonova-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ottonova-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ottonova-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/ottonova-vulnerability-disclosure.yml
created: '2026-07-17'
description: 'Ottonova is a Munich-based digital private health insurance provider (private Krankenversicherung) founded in 2015, positioned as "the insurance for the mobile age." It sells private full health insurance and supplementary dental and hospital coverage to consumers in Germany, delivering onboarding, claims, a concierge medical service and digital health records through its mobile app rather than through a public developer API. Ottonova is backed by venture investors including Earlybird and HV Capital and operates in the insurtech sector. This API Evangelist profile was created as a portfolio-lead stub and has been through one enrichment pass: probing confirmed a consumer web presence with a published RFC 9116 security.txt but no public API surface (no developer portal, OpenAPI, OAuth/OpenID metadata, or API catalog).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ottonova.png
layout: provider
modified: '2026-07-20'
name: Ottonova
nav: Providers
network: true
overview: 'Ottonova is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurtech, Insurance, Health Insurance, and Private Health Insurance.


  Ottonova''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 12.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ottonova/refs/heads/main/screenshots/ottonova-2026-08-07T191037.png
security:
- kind: vulnerability-disclosure
  name: Ottonova Vulnerability Disclosure
  slug: ottonova-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: ottonova
tags:
- Company
- Insurtech
- Insurance
- Health Insurance
- Private Health Insurance
- Germany
- Fintech
website: https://www.ottonova.de
---
