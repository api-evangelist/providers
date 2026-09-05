---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://skydrive.co.jp/en/
- group: company
  title: ''
  type: About
  url: https://skydrive.co.jp/en/company/
- group: company
  title: ''
  type: Blog
  url: https://skydrive.co.jp/en/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://skydrive.co.jp/en/feed/
- group: operate
  title: ''
  type: Contact
  url: https://skydrive.co.jp/en/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skydrive.co.jp/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skydrive.co.jp/en/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://skydrive.co.jp/en/job/
- group: other
  title: ''
  type: Team
  url: https://skydrive.co.jp/en/leadership-team/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skydrive-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skydrive-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/skydrive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skydrive-rate-limits.yml
coverage:
  checked: '2026-08-28'
  detail: SkyDrive Inc. builds eVTOL aircraft, not software — its fourteen-page corporate WordPress site has no developer, docs or pricing section at all, every spec and /.well-known/ path 301s to the homepage, and the host's only HTTP interface is WordPress core, which answers 401 "rest_disabled".
  evidence:
  - status: 301
    url: https://skydrive.co.jp/openapi.json
  - status: 301
    url: https://skydrive.co.jp/.well-known/api-catalog
  - status: 401
    url: https://skydrive.co.jp/wp-json/
  - status: 200
    url: https://skydrive.co.jp/page-sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-28'
description: SkyDrive Inc. is a Japanese advanced air mobility manufacturer, founded in July 2018 by members of the CARTIVATOR volunteer project, that develops, manufactures, sells and operates eVTOL (electric vertical take-off and landing) aircraft. Its flagship aircraft, SKYDRIVE (model SD-05), is a compact three-seat electric aircraft in type certification with the Japan Civil Aviation Bureau and in concurrent validation with the US Federal Aviation Administration, and is produced with official manufacturing partner Suzuki Motor Corporation at Suzuki's plant in Iwata, Shizuoka. The company is headquartered in Toyota City, Aichi, with offices in Tokyo, Nagoya, Osaka and Yamaguchi and a US subsidiary, SkyDrive America. SkyDrive is a hardware and aircraft-operations company; it publishes no public developer program, API, SDK or machine-readable interface contract of any kind.
image: https://skydrive.co.jp/en/wp-content/uploads/2026/06/cropped-favicon-192x192.png
layout: provider
modified: '2026-08-28'
name: SkyDrive
nav: Providers
network: true
overview: 'SkyDrive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Aviation, Advanced Air Mobility, and eVTOL.


  SkyDrive''s developer surface includes engineering blog and 12 more developer resources.'
plans:
- name: Skydrive Plans Pricing
  plan_count: 0
  slug: skydrive-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Skydrive Rate Limits
  slug: skydrive-rate-limits
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skydrive/refs/heads/main/screenshots/skydrive-2026-09-02T155756.png
security:
- kind: domain-security
  name: Skydrive Domain Security
  slug: skydrive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skydrive
tags:
- Company
- Aerospace
- Aviation
- Advanced Air Mobility
- eVTOL
- Urban Air Mobility
- Manufacturing
- Transportation
- Japan
website: https://skydrive.co.jp/en/
---
