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
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diplomat-pharmacy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/diplomatrx
- group: company
  title: ''
  type: Website
  url: https://diplomatpharmacy.com
coverage:
  checked: '2026-09-06'
  detail: Diplomat Pharmacy was absorbed into UnitedHealth Group's OptumRx in December 2019 and no longer serves a site of its own — diplomatpharmacy.com and diplomat.is both answer every path, /.well-known/ included, with a blanket 301 into specialty.optum.com, and the apis.yml Website host diplomat-pharmacy.com does not resolve at all (NXDOMAIN).
  evidence:
  - status: 301
    url: https://diplomatpharmacy.com/
  - status: 301
    url: https://diplomatpharmacy.com/.well-known/security.txt
  - status: 0
    url: https://www.diplomat-pharmacy.com/
  - status: 301
    url: https://diplomatpharmacy.com/openapi.json
  reason: defunct
  state: none
created: '2026-03-24'
description: Diplomat Pharmacy was an independent provider of specialty pharmacy services that helped patients with chronic and complex conditions access and manage specialty medications. The company was acquired by UnitedHealth Group's OptumRx, and operations have been integrated under that brand. No publicly documented developer APIs are offered under the Diplomat Pharmacy name.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diplomat-pharmacy.png
layout: provider
modified: '2026-09-06'
name: Diplomat Pharmacy
nav: Providers
network: true
overview: Diplomat Pharmacy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Pharmacy, Specialty Pharmacy, Pharmaceuticals, and Fortune 1000.
press:
- date: '2026-05-25'
  title: Tech Data, Diplomat Pharmacy rise; Helmerich & Payne falls
  url: https://vancouver.citynews.ca/2019/11/29/tech-data-diplomat-pharmacy-rise-helmerich-payne-falls/
- date: '2026-05-25'
  title: Diplomat Pharmacy, Inc. - Drug pipelines, Patents, Clinical ...
  url: https://synapse-patsnap-com.libproxy1.nus.edu.sg/organization/c6794f39332b4496ab7d1b26f2009af8
- date: '2026-05-25'
  title: Diplomat Announces Review of Strategic Alternatives
  url: https://www.prnewswire.com/news-releases/diplomat-announces-review-of-strategic-alternatives-300899272.html
- date: '2026-05-25'
  title: KAHN SWICK & FOTI, LLC REMINDS INVESTORS WITH ...
  url: https://www.biospace.com/diplomat-pharmacy-shareholder-alert-by-former-louisiana-attorney-general-kahn-swick-and-amp-foti-llc-reminds-investors-with-losses-in-excess-of-100-000-of-lead-plaintiff-deadline-in-class-action-lawsuit-against-diplomat-pharmacy-inc-dplo
- date: '2026-05-25'
  title: Diplomat Pharmacy agrees to $300 million buyout by ...
  url: https://www.reuters.com/article/business/diplomat-pharmacy-agrees-to-300-million-buyout-by-unitedhealth-idUSKBN1YD12Q/
random_paper: 13
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: flat
security:
- kind: domain-security
  name: Diplomat Pharmacy Domain Security
  slug: diplomat-pharmacy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diplomat-pharmacy
tags:
- Healthcare
- Pharmacy
- Specialty Pharmacy
- Pharmaceuticals
- Fortune 1000
website: https://diplomatpharmacy.com
---
