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
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Serverless HTTP endpoints that render SVG cards (GitHub stats, top languages, repository pin, gist and WakaTime cards) from GitHub data, called with GET query parameters and embedded as images in Mark
  name: GitHub ReadMe Stats
  slug: github-readme-stats
artifact_total: 3
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.urlencoder.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.urlencoder.org/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.urlencoder.org/
- group: company
  title: ''
  type: Website
  url: https://www.urlencoder.org/
- group: design
  href: https://artifacts.apis.io/github-readme-stats/conventions/github-readme-stats-conventions.yml
  title: ''
  type: Conventions
  url: conventions/github-readme-stats-conventions.yml
- group: other
  href: https://artifacts.apis.io/github-readme-stats/hosts/github-readme-stats-hosts.yml
  title: ''
  type: Hosts
  url: hosts/github-readme-stats-hosts.yml
- group: other
  href: https://artifacts.apis.io/github-readme-stats/vendors/github-readme-stats-vendors.yml
  title: ''
  type: Vendors
  url: vendors/github-readme-stats-vendors.yml
- group: auth
  href: https://artifacts.apis.io/github-readme-stats/security/github-readme-stats-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/github-readme-stats-domain-security.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/anuraghazra/github-readme-stats
- group: operate
  title: ''
  type: Support
  url: https://github.com/anuraghazra/github-readme-stats/issues
coverage:
  checked: '2026-11-05'
  detail: The five SVG-card GET endpoints (/api, /api/pin, /api/top-langs, /api/gist, /api/wakatime) are documented only as README prose on github.com, with no OpenAPI anywhere, and the public instance github-readme-stats.vercel.app answered 503 to every probe.
  evidence:
  - status: 200
    url: https://github.com/anuraghazra/github-readme-stats
  - status: 503
    url: https://github-readme-stats.vercel.app/api?username=anuraghazra
  - status: 503
    url: https://github-readme-stats.vercel.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-28'
description: GitHub ReadMe Stats is an open-source (MIT) project by Anurag Hazra that dynamically generates SVG statistics cards for GitHub profile READMEs. It exposes GET endpoints for stats, top languages, repository pins, gists and WakaTime cards, served from a best-effort public Vercel instance and designed to be self-hosted on Vercel or run through a GitHub Actions workflow.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/github-readme-stats.png
layout: provider
modified: '2026-11-05'
name: GitHub ReadMe Stats
nav: Providers
network: true
overview: 'GitHub ReadMe Stats is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Badges, Developer Tools, GitHub, Open Source, and Open Source Projects.


  GitHub ReadMe Stats'' developer surface includes documentation, support, and 9 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 0
  name: Github Readme Stats Rate Limits
  slug: github-readme-stats-rate-limits
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.9
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 3.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/github-readme-stats/github-readme-stats-2026-06-20T181844.png
security:
- kind: domain-security
  name: Github Readme Stats Domain Security
  slug: github-readme-stats-domain-security
  summary_line: TLSv1.3 · DMARC
slug: github-readme-stats
tags:
- Badges
- Developer Tools
- GitHub
- Open Source
- Open Source Projects
- Profile README
- Public APIs
- SVG
website: https://www.urlencoder.org/
---
