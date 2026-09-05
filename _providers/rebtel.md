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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.rebtel.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.rebtel.com/en/help/overview/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rebtel.com/en/legal-information/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rebtel.com/en/legal-information/about-cookies/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rebtel-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rebtel-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rebtel-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rebtel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.rebtel.com/.well-known/security.txt
created: '2026-07-17'
description: Rebtel is a Swedish international communications company (Rebtel Networks AB, registered 556680-3622, headquartered in Stockholm) serving the world's roughly two billion international migrants with low-cost international calling, mobile top-up / airtime recharge, and calling cards delivered through its iOS and Android apps. It routes calls over optimized local phone lines to keep prices low. Backed by Balderton Capital and Index Ventures. Rebtel exposes no public developer API or SDK program; this profile captures the company's public web, legal, support, and security.txt surface for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rebtel.png
layout: provider
modified: '2026-07-21'
name: rebtel
nav: Providers
network: true
overview: 'rebtel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, VoIP, International Calling, and Mobile Top-Up.


  rebtel''s developer surface includes support and 8 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.6
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
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rebtel/refs/heads/main/screenshots/rebtel-2026-09-02T153032.png
security:
- kind: domain-security
  name: Rebtel Domain Security
  slug: rebtel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rebtel Vulnerability Disclosure
  slug: rebtel-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rebtel
tags:
- Company
- Telecommunications
- VoIP
- International Calling
- Mobile Top-Up
- Remittance
- Consumer
- Messaging
- Sweden
website: https://www.rebtel.com/en/
---
