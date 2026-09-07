---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-09-06'
api_count: 1
apis:
- description: An undocumented Take-Two API host. api.take2games.com resolves to a Google Cloud load balancer that returns a bare 403 Forbidden on every path probed, including the root. The sibling T2GP platform hos
  name: Take-Two Interactive Software API
  slug: take-two-interactive-api
artifact_total: 5
common:
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.take2games.com/
- group: company
  title: ''
  type: Careers
  url: https://www.take2games.com/careers
- group: company
  title: ''
  type: Website
  url: https://www.take2games.com
- group: operate
  title: ''
  type: Support
  url: https://www.take2games.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.take2games.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.take2games.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/take-two-archive
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/take-2-interactive-software-inc-
- group: company
  title: ''
  type: Blog
  url: https://ir.take2games.com/rss/news-releases.xml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/take-two-interactive-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/take-two-interactive-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/take-two-interactive-llms.txt
coverage:
  checked: '2026-09-06'
  detail: Take-Two's developer hosts docs.take2games.com and dev.take2games.com answer every path, including every /.well-known/ path, with a 302 to a Vouch Proxy + FusionAuth SSO login at fusionauth-vouch-proxy.t2gp.take2games.com, while the host previously on record, developer.take2games.com, no longer resolves at all.
  evidence:
  - status: 302
    url: https://docs.take2games.com/.well-known/api-catalog
  - status: 302
    url: https://dev.take2games.com/
  - status: 0
    url: https://developer.take2games.com/docs
  - status: 403
    url: https://api.take2games.com/openapi.json
  - status: 200
    url: https://api.t2gp.take2games.com/health
  reason: partner-login
  state: gated
created: '2026-04-19'
description: 'Take-Two Interactive Software, Inc. (NASDAQ: TTWO) is a US interactive-entertainment holding company headquartered in New York City that develops and publishes video games through its labels Rockstar Games, 2K, Zynga and Ghost Story Games. It is a Fortune 1000 corporation. Take-Two operates real API infrastructure — api.take2games.com and the T2GP (Take-Two Game Platform) API at api.t2gp.take2games.com, the backend behind its launcher and account system — but it runs no public developer program: no developer portal, no published reference, no machine-readable contract, no SDKs, and no plans or rate limits. Its developer-surface hosts (docs.take2games.com, dev.take2games.com) redirect every request to a FusionAuth SSO login.'
finops:
- name: Take Two Interactive Finops
  service_category: Interactive Entertainment
  slug: take-two-interactive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/take-two-interactive.png
layout: provider
modified: '2026-09-06'
name: Take-Two Interactive Software
nav: Providers
network: true
overview: 'Take-Two Interactive Software publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Video Games, Interactive Entertainment, Entertainment, and Publishing.


  Take-Two Interactive Software''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Take Two Interactive Plans Pricing
  plan_count: 0
  slug: take-two-interactive-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Take Two Interactive Rate Limits
  slug: take-two-interactive-rate-limits
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.0
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: flat
security:
- kind: domain-security
  name: Take Two Interactive Domain Security
  slug: take-two-interactive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: take-two-interactive
tags:
- Gaming
- Video Games
- Interactive Entertainment
- Entertainment
- Publishing
- Software
- Fortune 1000
website: https://www.take2games.com
---
