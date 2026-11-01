---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/speakerdeck/plans/speakerdeck-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/speakerdeck-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/speakerdeck/llms/speakerdeck-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/speakerdeck-llms.txt
- group: other
  href: https://artifacts.apis.io/speakerdeck/hosts/speakerdeck-hosts.yml
  title: ''
  type: Hosts
  url: hosts/speakerdeck-hosts.yml
- group: other
  href: https://artifacts.apis.io/speakerdeck/vendors/speakerdeck-vendors.yml
  title: ''
  type: Vendors
  url: vendors/speakerdeck-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://speakerdeck.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://speakerdeck.com/privacy
- group: start
  title: ''
  type: Login
  url: https://speakerdeck.com/signin
- group: auth
  href: https://artifacts.apis.io/speakerdeck/security/speakerdeck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/speakerdeck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://speakerdeck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://speakerdeck.com/help
- group: company
  title: ''
  type: Blog
  url: https://blog.speakerdeck.com/
- group: operate
  title: ''
  type: Support
  url: https://help.speakerdeck.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://speakerdeck.com/signup
coverage:
  checked: '2026-10-28'
  detail: Developer portal at https://speakerdeck.com/developers provides only HTML docs with no OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://speakerdeck.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Speaker Deck is an online platform that enables users to upload, share, and embed presentation decks easily. It offers features such as private URLs, password protection, custom URLs, scheduled publishing, branding removal, and embedding restrictions, catering to professionals, educators, and developers who want to showcase their slides publicly or within teams.
image: https://d1eu30co0ohy4w.cloudfront.net/assets/speaker-deck-og-image-e5cb37b9a277dd3f1b3cfe930515037e02f08de5a834a606e9bfbef5d84e64a2.png
layout: provider
modified: '2026-10-28'
name: Speaker Deck
nav: Providers
network: true
overview: 'Speaker Deck is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Presentation, Sharing, Slides, and Education.


  Speaker Deck''s developer surface includes documentation, engineering blog, support, getting-started guide, and 9 more developer resources.'
plans:
- name: Speakerdeck Plans Pricing
  plan_count: 2
  slug: speakerdeck-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Speakerdeck Domain Security
  slug: speakerdeck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: speakerdeck
tags:
- Company
- Presentation
- Sharing
- Slides
- Education
- Developer
website: https://speakerdeck.com/
---
