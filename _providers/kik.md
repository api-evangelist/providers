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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kik.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kik.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kik.com/terms
created: '2026-07-17'
description: Kik is a freeware instant-messaging mobile app for iOS and Android, known for letting users register with only a username rather than a phone number. Founded in 2009 by University of Waterloo students and released in 2010, Kik grew to hundreds of millions of registered users and was especially popular with teens. It has been owned by MediaLab AI since 2019. Kik formerly operated a developer surface — the Kik Bot Platform at dev.kik.com — and the Kin cryptocurrency, but that developer/bot API platform is no longer online and Kik currently publishes no public API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kik.png
layout: provider
modified: '2026-07-19'
name: Kik
nav: Providers
network: true
overview: Kik is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social-Media, Messaging, Chat, and Mobile.
random_paper: 4
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kik/refs/heads/main/screenshots/kik-2026-07-25T223731.png
security:
- kind: domain-security
  name: Kik Domain Security
  slug: kik-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: kik
tags:
- Company
- Social-Media
- Messaging
- Chat
- Mobile
- Bots
website: https://kik.com
---
