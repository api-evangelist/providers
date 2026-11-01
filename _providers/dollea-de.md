---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Agent API for Dollea Salon and Beauty Coworking platform
  name: Dollea Agent API
  slug: dollea-agent-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/dollea-de/authentication/dollea-de-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dollea-de-authentication.yml
- group: design
  href: https://artifacts.apis.io/dollea-de/conformance/dollea-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dollea-de-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dollea-de/well-known/dollea-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dollea-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/dollea-de/hosts/dollea-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dollea-de-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dollea.de/media/workspaces/photos/IMG_7545.png
- group: auth
  href: https://artifacts.apis.io/dollea-de/security/dollea-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dollea-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dollea.de/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dollea.de/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dollea.de/legal/privacy/
- group: other
  title: ''
  type: Imprint
  url: https://www.dollea.de/legal/imprint/
created: '2026-10-30'
description: Dollea Beauty Studio is a cosmetics and wellness salon located in Munich Haidhausen, Germany. It offers a range of exclusive treatments including manicures, pedicures, eyelash extensions, eyebrow styling, and facial care, focusing on high-quality, personalized services for clients seeking aesthetic enhancements and relaxation. The studio also provides coworking spaces and multilingual support (German, English, Russian).
image: https://www.dollea.de/static/IMG_7535.webp
layout: provider
modified: '2026-10-30'
name: dollea-de
nav: Providers
network: true
overview: 'dollea-de is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Beauty, Salon, Munich, Cosmetics, and Wellness.


  dollea-de''s developer surface includes authentication and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dollea De Authentication
  slug: dollea-de-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dollea De Domain Security
  slug: dollea-de-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dollea-de
tags:
- Beauty
- Salon
- Munich
- Cosmetics
- Wellness
website: https://www.dollea.de/
---
