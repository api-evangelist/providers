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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Programmatic access to O-RAN Software Community open interface specifications, RAN intelligence APIs, near-real-time RIC (RICAPP), Non-RT RIC (NONRTRIC), and network virtualization tools.
  name: O-RAN Software Community API
  slug: o-ran-sc-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/o-ran-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/o-ran
- group: company
  title: ''
  type: Website
  url: https://o-ran.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.o-ran-sc.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/o-ran-sc
- group: other
  title: ''
  type: Wiki
  url: https://wiki.o-ran-sc.org/
- group: build
  title: ''
  type: SourceCode
  url: https://gerrit.o-ran-sc.org/
- group: other
  title: ''
  type: LinuxFoundation
  url: https://www.lfnetworking.org/projects/o-ran-sc/
created: '2026-03-16'
description: O-RAN supports the Open Radio Access Network architecture under the Linux Foundation for more interoperable and virtualized mobile network infrastructure. It defines open interfaces between RAN components enabling multi-vendor deployments and network intelligence through AI and machine learning.
finops:
- name: O Ran Finops
  service_category: API
  slug: o-ran-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/o-ran.png
layout: provider
modified: '2026-04-28'
name: O-RAN
nav: Providers
network: true
overview: 'O-RAN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Linux Foundation, Mobile Network, Open-Source, RAN, and Radio.


  O-RAN''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: O Ran Plans Pricing
  plan_count: 3
  slug: o-ran-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: O Ran Rate Limits
  slug: o-ran-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/o-ran/refs/heads/main/screenshots/o-ran-2026-06-20T190544.png
security:
- kind: domain-security
  name: O Ran Domain Security
  slug: o-ran-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: o-ran
tags:
- Linux Foundation
- Mobile Network
- Open-Source
- RAN
- Radio
- Telecom
website: https://o-ran.org/
---
