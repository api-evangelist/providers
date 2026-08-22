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
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.6
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.fr.luko.eu
- group: operate
  title: ''
  type: Support
  url: https://www.fr.luko.eu/aide/
- group: company
  title: ''
  type: Blog
  url: https://www.fr.luko.eu/assurance-voyage/blog-voyage/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fr.luko.eu/cgu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fr.luko.eu/confidentialite-donnees/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/luko-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/luko-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/luko-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fr.luko.eu/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luko-domain-security.yml
created: '2026-07-17'
description: Luko is an online home, travel, and auto insurance provider founded in France in 2016 and now operating as Luko by Allianz Direct after its acquisition by the Allianz group. It sells rental, owner-occupied, non-occupant-owner (PNO), student, and co-housing home policies from around EUR 5 per month, plus travel and Eurofil-partnered auto cover, with sub-two-minute online subscription, instant attestations, digital claims declaration through a customer account portal, and 24/7 emergency support. Originally a VC-backed insurtech (Accel, Speedinvest), Luko today runs as a consumer insurance brand with no public developer API, SDK, or API documentation surface; this profile captures its verifiable security and identity footprint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/luko.png
layout: provider
modified: '2026-07-20'
name: Luko
nav: Providers
network: true
overview: 'Luko is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Insurance, Insurtech, and Home Insurance.


  Luko''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.5
  delta: -2.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/luko/refs/heads/main/screenshots/luko-2026-07-25T225651.png
security:
- kind: domain-security
  name: Luko Domain Security
  slug: luko-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Luko Vulnerability Disclosure
  slug: luko-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: luko
tags:
- Company
- Consumer
- Insurance
- Insurtech
- Home Insurance
- Travel Insurance
- Auto Insurance
- France
- Allianz
website: https://www.fr.luko.eu
---
