---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Autocrypt provides API access to its security platform (no public spec discovered)
  name: Autocrypt API
  slug: autocrypt-api
artifact_total: 3
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://autocrypt.io/feed/
- group: auth
  href: https://artifacts.apis.io/autocrypt/security/autocrypt-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/autocrypt-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/autocrypt/hosts/autocrypt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autocrypt-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autocrypt.io/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autocrypt.io/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://autocrypt.io/news/
- group: company
  title: ''
  type: Blog
  url: https://autocrypt.io/blog/
- group: auth
  href: https://artifacts.apis.io/autocrypt/security/autocrypt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autocrypt-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/autocrypt/security/autocrypt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autocrypt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autocrypt.io/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files were found at common endpoints on autocrypt.io or api.autocrypt.io.
  evidence:
  - status: 0
    url: https://api.autocrypt.io/openapi.json
  - status: 404
    url: https://autocrypt.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Autocrypt provides cyber‑physical security solutions for autonomous and connected vehicles, in‑vehicle systems, V2X communications, EV charging infrastructure, robotics, and defense applications. Founded in 2007 in Seoul, South Korea, the company offers hardware security modules, trusted execution environments, digital key management, intrusion detection, and compliance services to protect physical AI systems across mobility and industrial sectors.
image: https://autocrypt.io/wp-content/uploads/2021/08/AUTOCRYPT-Contact-Us.png
layout: provider
modified: '2026-10-06'
name: Autocrypt
nav: Providers
network: true
overview: 'Autocrypt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Automotive, Physical AI, and Mobility.


  Autocrypt''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 58.0
    operational_transparency: 10.5
  previous_composite: 12.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/autocrypt/autocrypt-2026-10-11T100924.png
security:
- kind: domain-security
  name: Autocrypt Domain Security
  slug: autocrypt-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Autocrypt Vulnerability Disclosure
  slug: autocrypt-vulnerability-disclosure
  summary_line: no policy recorded
slug: autocrypt
tags:
- Company
- Cybersecurity
- Automotive
- Physical AI
- Mobility
website: https://autocrypt.io/
---
