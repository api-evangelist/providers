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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Braven Environmental's plastic waste management platform
  name: Braven Environmental API
  slug: braven-environmental-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/braven-environmental/refs/heads/main/well-known/braven-environmental-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/braven-environmental-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/braven-environmental/refs/heads/main/well-known/braven-environmental-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/braven-environmental-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/braven-environmental/refs/heads/main/hosts/braven-environmental-hosts.yml
  title: ''
  type: Hosts
  url: hosts/braven-environmental-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/braven-environmental/refs/heads/main/security/braven-environmental-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/braven-environmental-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/braven-environmental/refs/heads/main/security/braven-environmental-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/braven-environmental-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bravenenvironmental.com
- group: company
  title: ''
  type: Blog
  url: http://bravenenvironmental.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://bravenenvironmental.com/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://bravenenvironmental.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: http://bravenenvironmental.com/terms-of-use/
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: no-response
    url: https://api.bravenenvironmental.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Braven Environmental provides turn-key plastic waste management solutions through its Braven Reactor Train™ (BRT™) technology, converting waste plastics into valuable resources while reducing carbon footprints. The company partners with businesses and governments to implement sustainable waste processing facilities, offering a science-backed approach to address global plastic pollution.
layout: provider
modified: '2026-10-03'
name: Braven Environmental
nav: Providers
network: true
overview: 'Braven Environmental publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Plastic Waste, Sustainability, Renewable Energy, and Technology.


  Braven Environmental''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.4
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Braven Environmental Domain Security
  slug: braven-environmental-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Braven Environmental Vulnerability Disclosure
  slug: braven-environmental-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: braven-environmental
tags:
- Company
- Plastic Waste
- Sustainability
- Renewable Energy
- Technology
website: https://bravenenvironmental.com
---
