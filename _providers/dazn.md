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
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.dazn.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getndazn
- group: company
  title: ''
  type: Blog
  url: https://medium.com/dazn-tech
- group: operate
  title: ''
  type: Support
  url: https://help.dazn.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.dazn.com/hc/en-gb/articles/16391473315101-TERMS-AND-CONDITIONS-07-November-2025
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.dazn.com/hc/en-us/articles/16394152093597-Privacy-Policy-and-Cookie-Notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dazn.com/
- group: auth
  title: ''
  type: Security
  url: https://help.dazn.com/hc/en-us/articles/16471531900317-Global-Responsible-Disclosure-for-Security-Vulnerabilities-Policy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dazn-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dazn-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dazn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dazn-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/dazn-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dazn-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dazn-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dazn-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dazn-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dazn-llms.txt
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/getndazn
coverage:
  checked: '2026-08-12'
  detail: DAZN is a consumer sports-streaming product with no developer program at all — developer.dazn.com, developers.dazn.com, docs.dazn.com and api.dazn.com have no DNS records, and the only machine- readable document served anywhere on www.dazn.com is an RFC 9116 security.txt, because every other path on that host returns an identical 95,145-byte single-page-app shell.
  evidence:
  - status: 0
    url: https://developer.dazn.com/
  - status: 0
    url: https://api.dazn.com/
  - status: 200
    url: https://www.dazn.com/openapi.json
  - status: 404
    url: https://www.dazn.com/.well-known/agent-card.json
  - status: 200
    url: https://www.dazn.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'DAZN is a global over-the-top live sports streaming service headquartered in London and owned by Access Industries. Launched in 2015 out of the former Perform Group, it streams boxing, football, MotoGP, UFC and other rights to subscribers across more than 200 countries and territories, and has expanded through the acquisitions of Eleven Group, Foxtel/Kayo Sports and ViewLift, alongside the DAZN Bet and DAZN Media brands. DAZN operates a large Node.js microservice estate on AWS and publishes open source engineering tooling (the Kopytko Roku ecosystem, dazn-lambda-powertools) from its GitHub organization, but it runs no public developer program: there is no developer portal, no API reference, and no machine-readable specification for the consumer platform APIs that power its apps.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-12'
name: DAZN
nav: Providers
network: true
overview: 'DAZN is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Streaming, Sports, Media, Entertainment, and Video.


  DAZN''s developer surface includes engineering blog, support, and 17 more developer resources.'
plans:
- name: Dazn Plans Pricing
  plan_count: 0
  slug: dazn-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Dazn Rate Limits
  slug: dazn-rate-limits
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 8.0
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dazn/refs/heads/main/screenshots/dazn-2026-09-02T145225.png
security:
- kind: domain-security
  name: Dazn Domain Security
  slug: dazn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dazn Vulnerability Disclosure
  slug: dazn-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: dazn
tags:
- Streaming
- Sports
- Media
- Entertainment
- Video
- OTT
- Live Streaming
- Broadcasting
- Subscription
- Open-Source
website: https://www.dazn.com/
---
