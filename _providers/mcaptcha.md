---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.mcaptcha.org
  baseurl_source: declared
  description: API for mCaptcha user registration, authentication, and account management.
  name: mCaptcha Guard API
  slug: mcaptcha-guard-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/mcaptcha/cli/mcaptcha-cli.yml
  title: ''
  type: CLI
  url: cli/mcaptcha-cli.yml
- group: design
  href: https://artifacts.apis.io/mcaptcha/conformance/mcaptcha-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mcaptcha-conformance.yml
- group: other
  href: https://artifacts.apis.io/mcaptcha/hosts/mcaptcha-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcaptcha-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://mcaptcha.org/security
- group: auth
  href: https://artifacts.apis.io/mcaptcha/security/mcaptcha-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mcaptcha-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mcaptcha/security/mcaptcha-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcaptcha-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcaptcha.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mcaptcha.org/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://mcaptcha.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://mcaptcha.org/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://mcaptcha.org/docs/webmasters/installing-captcha/
- group: operate
  title: ''
  type: Support
  url: https://mcaptcha.org/contact/
- group: company
  title: ''
  type: Blog
  url: https://mcaptcha.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mCaptcha
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcaptcha.org/privacy-policy/
created: '2026-10-28'
description: mCaptcha provides a proof‑of‑work based captcha system that is privacy‑focused, fully automated, and open source. It protects websites from automated abuse without tracking users, offering a silent, user‑friendly experience. The service includes drop‑in compatibility with reCAPTCHA and hCaptcha, extensive documentation, and client libraries under permissive licenses, while the core remains AGPL‑licensed.
image: https://mcaptcha.org/static/images/landing.jpg
layout: provider
modified: '2026-10-28'
name: mCaptcha
nav: Providers
network: true
overview: 'mCaptcha is listed with 1 API on the [APIs.io](https://apis.io/) network: Guard API. Tagged areas include Company, Captcha, Privacy, OpenSource, and PoW.


  mCaptcha''s developer surface includes CLI, documentation, API reference, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 29.0
    developer_ergonomics: 52.4
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mcaptcha Domain Security
  slug: mcaptcha-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Mcaptcha Vulnerability Disclosure
  slug: mcaptcha-vulnerability-disclosure
  summary_line: no policy recorded
slug: mcaptcha
tags:
- Company
- Captcha
- Privacy
- OpenSource
- PoW
- Security
website: https://mcaptcha.org/
---
