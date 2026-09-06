---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: 'The BEP U.S. Currency Reader Program provides free currency readers to blind and visually impaired individuals in the United States, enabling them to identify Federal Reserve Note denominations using '
  name: BEP U.S. Currency Reader Program
  slug: bep-currency-reader-program
- description: The BEP redeems severely damaged or mutilated Federal Reserve Notes as a free public service. Citizens can submit damaged currency for examination and potential redemption.
  name: BEP Mutilated Currency Redemption
  slug: bep-mutilated-currency-redemption
- description: BEP publishes currency production figures, annual reports, and historical data about Federal Reserve Note printing. Data is available via data.gov for programmatic access.
  name: BEP Data and Publications
  slug: bep-data-catalog
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-engraving-and-printing-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-engraving-and-printing
- group: company
  title: ''
  type: Website
  url: https://www.bep.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bep.gov/footer/privacy-policy
- group: company
  title: ''
  type: About
  url: https://www.bep.gov/about-bep
- group: docs
  title: ''
  type: Documentation
  url: https://www.bep.gov/services
- group: operate
  title: ''
  type: Support
  url: https://www.bep.gov/contact-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-engraving-and-printing-llms.txt
coverage:
  checked: '2026-09-05'
  detail: BEP is a Treasury manufacturing bureau whose two public services — free currency readers and mutilated-currency redemption — run on mailed paper forms, and its only software product is the free EyeNote end-user phone app; www.bep.gov has no developer page, no /api, no spec at any probed path, no GitHub organization, and its former data.gov organization (bep-gov) now returns 404.
  evidence:
  - status: 404
    url: https://www.bep.gov/developers
  - status: 404
    url: https://www.bep.gov/api
  - status: 404
    url: https://www.bep.gov/openapi.json
  - status: 404
    url: https://www.bep.gov/llms.txt
  - status: 404
    url: https://www.bep.gov/.well-known/api-catalog
  - status: 404
    url: https://catalog.data.gov/organization/bep-gov
  - status: 404
    url: https://api.github.com/orgs/bep-gov
  reason: no-developer-program
  state: none
created: '2024-11-25'
description: The Bureau of Engraving and Printing (BEP) is an agency of the U.S. Department of the Treasury that designs and produces U.S. currency (Federal Reserve Notes), postage stamps, and other official U.S. government security documents. BEP offers a U.S. Currency Reader Program for the visually impaired and provides a mutilated currency redemption service.
finops:
- name: Bureau Of Engraving And Printing Finops
  service_category: API
  slug: bureau-of-engraving-and-printing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-engraving-and-printing.png
layout: provider
modified: '2026-09-05'
name: Bureau of Engraving and Printing
nav: Providers
network: true
overview: 'Bureau of Engraving and Printing publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Currency, Engraving, Federal-Government, Money, and Printing.


  Bureau of Engraving and Printing''s developer surface includes documentation, support, and 6 more developer resources.'
plans:
- name: Bureau Of Engraving And Printing Plans Pricing
  plan_count: 0
  slug: bureau-of-engraving-and-printing-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Bureau Of Engraving And Printing Rate Limits
  slug: bureau-of-engraving-and-printing-rate-limits
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-engraving-and-printing/refs/heads/main/screenshots/bureau-of-engraving-and-printing-2026-06-20T173806.png
security:
- kind: domain-security
  name: Bureau Of Engraving And Printing Domain Security
  slug: bureau-of-engraving-and-printing-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bureau-of-engraving-and-printing
tags:
- Currency
- Engraving
- Federal-Government
- Money
- Printing
- Security Printing
website: https://www.bep.gov/
---
