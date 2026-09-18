---
access_model:
  confidence: high
  label: No public API program
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - '{''url'': ''https://www.ferro.com'', ''status'': 301, ''note'': ''declared website redirects to https://vibrantz.com/ — a different registrable domain (ferro.com -> vibrantz.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  - '{''url'': ''https://vibrantz.com/developers/'', ''status'': 404, ''note'': ''successor site publishes no developer program; api.ferro.com and developer.ferro.com are NXDOMAIN (probed 2026-09-17)''}'
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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-17'
api_count: 1
apis:
- description: Machine-readable historical filing data for Ferro Corporation is available from the U.S. Securities and Exchange Commission, not from the company. The SEC EDGAR submissions API returns the full filing
  name: SEC EDGAR Filings (Ferro Corporation, CIK 0000035214)
  slug: sec-edgar-filings
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://vibrantz.com/
- group: company
  title: ''
  type: Website
  url: https://www.ferro.com
- group: operate
  title: ''
  type: Contact
  url: https://vibrantz.com/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://vibrantz.com/careers/
- group: operate
  title: ''
  type: PressReleases
  url: https://vibrantz.com/press/
- group: company
  title: ''
  type: Blog
  url: https://vibrantz.com/vibrantz-edge/
- group: company
  title: ''
  type: BlogRSS
  url: https://vibrantz.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vibrantz.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vibrantz.com/legal/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ferro-corporation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vibrantztechnologies
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ferro/refs/heads/main/llms/ferro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ferro-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ferro/refs/heads/main/security/ferro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ferro-domain-security.yml
coverage:
  checked: '2026-09-17'
  detail: Ferro Corporation was absorbed into Vibrantz Technologies in 2022 — ferro.com 301-redirects every path to the vibrantz.com root, the scaffolded hosts api.ferro.com and developer.ferro.com do not resolve in DNS, and vibrantz.com answers 404 on /developers/, /api/, /openapi.json and every /.well-known/ path, publishing only a Yoast llms.txt, an RSS feed and the default WordPress /wp-json/ index.
  evidence:
  - status: 301
    url: https://www.ferro.com/
  - status: 404
    url: https://vibrantz.com/developers/
  - status: 404
    url: https://vibrantz.com/openapi.json
  - status: 404
    url: https://vibrantz.com/.well-known/agent-card.json
  - status: 200
    url: https://vibrantz.com/llms.txt
  reason: defunct
  state: none
created: '2026-04-19'
description: 'Ferro Corporation was a Cleveland-area, NYSE-listed (FOE) Fortune 1000 producer of functional coatings, color solutions, glass enamels, pigments and electronic materials. In April 2022 it was acquired by Prince International (American Securities) and merged with Prince and Chromaflo to form Vibrantz Technologies (vibrantz.com); Ferro filed a Form 15 with the SEC on 2022-05-02 and ferro.com now 301-redirects to vibrantz.com. Neither the legacy Ferro brand nor Vibrantz publishes a developer program, an API reference or a machine-readable contract: api.ferro.com and developer.ferro.com do not resolve, vibrantz.com answers 404 on every developer, OpenAPI and /.well-known/ path probed on 2026-09-17, and its only machine-readable surfaces are a Yoast-generated llms.txt, an RSS feed and the default WordPress /wp-json/ index. Machine-readable company data exists only through third-party channels — Ferro''s historical SEC filings (CIK 0000035214) remain on the SEC''s own EDGAR APIs.'
finops:
- name: Ferro Finops
  service_category: Specialty Chemicals / Materials
  slug: ferro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ferro.png
layout: provider
modified: '2026-09-17'
name: Ferro Corporation
nav: Providers
network: true
overview: 'Ferro Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Functional Materials, Electronics, Chemicals, Specialty Chemicals, and Pigments.


  Ferro Corporation''s developer surface includes engineering blog and 12 more developer resources.'
plans:
- name: Ferro Plans Pricing
  plan_count: 1
  slug: ferro-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Ferro Rate Limits
  slug: ferro-rate-limits
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.3
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    operational_transparency: 5.3
  previous_composite: 11.6
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ferro/refs/heads/main/screenshots/ferro-2026-06-20T181142.png
security:
- kind: domain-security
  name: Ferro Domain Security
  slug: ferro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ferro
tags:
- Functional Materials
- Electronics
- Chemicals
- Specialty Chemicals
- Pigments
- Coatings
- Vibrantz Technologies
- Acquired
- Fortune 1000
website: https://vibrantz.com/
---
