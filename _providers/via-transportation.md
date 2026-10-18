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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Via Transportation public API (no machine-readable spec found)
  name: Via Transportation API
  slug: via-transportation-api
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/via-transportation/refs/heads/main/hosts/via-transportation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/via-transportation-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/via-transportation/refs/heads/main/vendors/via-transportation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/via-transportation-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://ridewithvia.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://ridewithvia.com/news/via-in-the-news?hsLang=en
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/via-transportation/refs/heads/main/security/via-transportation-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/via-transportation-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/via-transportation/refs/heads/main/security/via-transportation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/via-transportation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ridewithvia.com
- group: docs
  title: ''
  type: Documentation
  url: https://ridewithvia.com/resources
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ridewithvia.com/developer
- group: operate
  title: ''
  type: Support
  url: mailto:support@ridewithvia.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridewithvia.com/legal/privacy?hsLang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridewithvia.com/legal/terms-of-use?hsLang=en
- group: docs
  title: ''
  type: Documentation
  url: https://ridewithvia.com/resources
coverage:
  checked: '2026-10-13'
  detail: Developer portal provides no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract.
  evidence:
  - status: 200
    url: https://developer.ridewithvia.com/
  - status: 0
    url: https://api.ridewithvia.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Via Transportation provides on-demand public mobility solutions, offering microtransit, fixed‑route, paratransit, and student transit services. Their platform enables cities, transit authorities, universities, and corporations to launch flexible shared‑ride programs, improve rider experience, and optimize transit operations through advanced scheduling and AI‑driven analytics.
image: https://ridewithvia.com/hubfs/Open%20Graph-RWV-2026.png
layout: provider
modified: '2026-10-13'
name: Via Transportation
nav: Providers
network: true
overview: 'Via Transportation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation, Mobility, On-Demand, Public Transit, and Software.


  Via Transportation''s developer surface includes documentation, support, and 11 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Via Transportation Domain Security
  slug: via-transportation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Via Transportation Vulnerability Disclosure
  slug: via-transportation-vulnerability-disclosure
  summary_line: Hackerone
slug: via-transportation
tags:
- Transportation
- Mobility
- On-Demand
- Public Transit
- Software
website: https://ridewithvia.com
---
