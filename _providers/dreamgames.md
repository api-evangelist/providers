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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dreamgames-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dreamgames.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dreamgames-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dreamgames-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dreamgames-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://dreamgames.com/
- group: company
  title: ''
  type: About
  url: https://www.dreamgames.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://dreamgames.helpshift.com/hc/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dreamgames.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dreamgames.com/en/privacy
created: '2026-07-17'
description: 'Dream Games is a mobile gaming developer with offices in Istanbul and London that builds high-quality, long-lifecycle casual puzzle games, best known for Royal Match and Royal Kingdom. The company combines technology and creativity to produce polished match-3 titles played by tens of millions of players worldwide, and it was surfaced as a portfolio company of balderton-capital. Dream Games operates as a consumer game publisher rather than an API provider: it publishes no public developer portal, OpenAPI, SDKs, or programmatic API surface. This profile therefore captures the company''s real public web, legal, and security surface (website, terms, privacy, careers, help center, and a published security.txt) rather than developer artifacts.'
image: https://www.dreamgames.com/
layout: provider
modified: '2026-07-18'
name: dreamgames
nav: Providers
network: true
overview: 'dreamgames is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile Gaming, Games, Puzzle, and Consumer.


  dreamgames'' developer surface includes support and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dreamgames/refs/heads/main/screenshots/dreamgames-2026-07-25T212358.png
security:
- kind: domain-security
  name: Dreamgames Domain Security
  slug: dreamgames-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dreamgames Vulnerability Disclosure
  slug: dreamgames-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dreamgames
tags:
- Company
- Mobile Gaming
- Games
- Puzzle
- Consumer
- Entertainment
website: https://dreamgames.com/
---
