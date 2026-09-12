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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foreign-claims-settlement-commission-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.justice.gov/fcsc
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/foreign-claims-settlement-commission-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/foreign-claims-settlement-commission-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.justice.gov/jmd/vulnerability-disclosure-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.justice.gov/doj/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.justice.gov/legalpolicies
- group: operate
  title: ''
  type: Contact
  url: https://www.justice.gov/fcsc/contact-commission
- group: other
  title: ''
  type: X-FinalOpinionsAndOrders
  url: https://www.justice.gov/fcsc/final-opinions-and-orders-5
- group: other
  title: ''
  type: X-Publications
  url: https://www.justice.gov/fcsc/publications
- group: other
  title: ''
  type: X-CurrentPrograms
  url: https://www.justice.gov/fcsc/current-programs
- group: other
  title: ''
  type: X-CompletedPrograms
  url: https://www.justice.gov/fcsc/completed-programs
- group: other
  title: ''
  type: X-FOIA
  url: https://www.justice.gov/fcsc/fcsc-freedom-information-act
coverage:
  checked: '2026-09-10'
  detail: 'The FCSC is a quasi-judicial claims tribunal that runs no host of its own — its entire public surface is a section of www.justice.gov, and contract discovery on 2026-09-10 turned up only HTML pages and PDF decisions: /openapi.json, /swagger.json, /jsonapi and every named /.well-known/ path 404''d on www.justice.gov (a negative-control path 404''d too, so the host is not a catch-all), and the parent department''s DOJ News API ignores a component=fcsc filter, returning the unfiltered department-wide feed byte-for-byte.'
  evidence:
  - status: 200
    url: https://www.justice.gov/fcsc
  - status: 404
    url: https://www.justice.gov/openapi.json
  - status: 404
    url: https://www.justice.gov/jsonapi
  - status: 404
    url: https://www.justice.gov/.well-known/api-catalog
  - status: 404
    url: https://www.justice.gov/.well-known/agent-card.json
  - status: 404
    url: https://www.justice.gov/llms.txt
  - status: 200
    url: https://www.justice.gov/news/rss?type=press_release&component=fcsc
  reason: not-a-software-company
  state: none
created: '2024-12-03'
description: The Foreign Claims Settlement Commission of the United States (FCSC) is a quasi-judicial, independent agency within the U.S. Department of Justice that adjudicates claims of U.S. nationals against foreign governments, under the International Claims Settlement Act (22 U.S.C. 1621 et seq.) and the War Claims Act (50 U.S.C. 4101-4147). Established in 1954 from the War Claims Commission and the International Claims Commission, it has run 43 completed country programs — Germany, Iran, Yugoslavia, Hungary, the Soviet Union, Poland, Italy, Cuba, China, Vietnam, Egypt, Panama and Albania among them — adjudicating more than 660,000 claims with awards in the billions of dollars. The Albania program remains open and the Commission serves as Special Master in Helms-Burton claims against Cuba. It publishes Final Opinions and Orders and annual reports on www.justice.gov, and operates no API or developer program of its own.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foreign-claims-settlement-commission.png
layout: provider
modified: '2026-09-10'
name: Foreign Claims Settlement Commission
nav: Providers
network: true
overview: Foreign Claims Settlement Commission is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Adjudication, Claims, Federal-Government, International Claims, and Justice.
random_paper: 0
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    operational_transparency: 10.5
  previous_composite: 11.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/foreign-claims-settlement-commission/refs/heads/main/screenshots/foreign-claims-settlement-commission-2026-06-20T181419.png
security:
- kind: domain-security
  name: Foreign Claims Settlement Commission Domain Security
  slug: foreign-claims-settlement-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Foreign Claims Settlement Commission Vulnerability Disclosure
  slug: foreign-claims-settlement-commission-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: foreign-claims-settlement-commission
tags:
- Adjudication
- Claims
- Federal-Government
- International Claims
- Justice
- Legal
website: https://www.justice.gov/fcsc
---
