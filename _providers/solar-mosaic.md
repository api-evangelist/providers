---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - rate-limits
  - security
  - '{''url'': ''https://joinmosaic.com/'', ''status'': 301, ''note'': ''declared website redirects to https://solarservicingllc.com/ — a different registrable domain (joinmosaic.com -> solarservicingllc.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 1
apis:
- description: The Mosaic Financing API is the integration surface Solar Mosaic published for its solar installer, dealer and capital partners, documented on a ReadMe-hosted developer portal titled "Mosaic Financing
  name: Mosaic Financing API
  slug: solar-mosaic-financing-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solar-mosaic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinmosaic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.joinmosaic.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solarmosaic
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solarservicingllc.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://solarservicingllc.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://solarservicingllc.com/contact-us/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solar-mosaic-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/solar-mosaic-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/solar-mosaic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solar-mosaic-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solar-mosaic-llms.txt
coverage:
  checked: '2026-08-28'
  detail: Solar Mosaic filed Chapter 11 on 2025-06-09 and its portfolio was acquired by Solar Servicing LLC, which does not originate new loans — joinmosaic.com now 301-redirects to solarservicingllc.com, the api.joinmosaic.com host answers nginx 503 on every path, and the Mosaic status page returns 200 with the title "Mosaic Status - Page Inactive"; the only surviving API surface is a ReadMe portal titled "Mosaic Financing API" whose every path 302s to a password gate.
  evidence:
  - status: 200
    url: https://joinmosaic.com/
  - status: 503
    url: https://api.joinmosaic.com/
  - status: 302
    url: https://developer.joinmosaic.com/
  - status: 200
    url: https://status.joinmosaic.com
  reason: defunct
  state: none
created: '2026-08-28'
description: Solar Mosaic, Inc. (trading as Mosaic) was a residential clean-energy lender founded in Oakland, California in 2010, originally as a solar crowdfunding platform and from 2014 as a point-of-sale financing platform for residential solar, battery storage and other sustainable home improvements funded through third-party capital partners. Mosaic originated loans through a dealer/installer channel and backed more than $15 billion in home energy loans across roughly 360,000 households. Its integration surface for installer and capital partners was the Mosaic Financing API, documented on a password-protected ReadMe developer portal at developer.joinmosaic.com. Solar Mosaic filed for Chapter 11 bankruptcy in the Southern District of Texas on 2025-06-09 and its loan portfolio was acquired in September 2025 by Solar Servicing LLC, which stated it would not originate new solar loans. As of this profile the joinmosaic.com website 301-redirects to solarservicingllc.com, the api.joinmosaic.com
  host returns HTTP 503, and the Mosaic status page reports "Page Inactive".
image: https://files.readme.io/0b31c0e-small-imageedit_17_2765500207.png
layout: provider
modified: '2026-08-28'
name: Solar Mosaic
nav: Providers
network: true
overview: 'Solar Mosaic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Lending, Solar, and Clean Energy.


  Solar Mosaic''s developer surface includes support and 11 more developer resources.'
plans:
- name: Solar Mosaic Plans Pricing
  plan_count: 0
  slug: solar-mosaic-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Solar Mosaic Rate Limits
  slug: solar-mosaic-rate-limits
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solar-mosaic/refs/heads/main/screenshots/solar-mosaic-2026-09-02T160117.png
security:
- kind: domain-security
  name: Solar Mosaic Domain Security
  slug: solar-mosaic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: solar-mosaic
tags:
- Company
- Financial-Services
- Lending
- Solar
- Clean Energy
- Home Improvement Finance
- Point of Sale Financing
- Consumer Finance
- Defunct
website: https://joinmosaic.com/
---
