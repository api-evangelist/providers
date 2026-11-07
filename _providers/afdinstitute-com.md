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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/afdinstitute-com/llms/afdinstitute-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afdinstitute-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/afdinstitute-com/well-known/afdinstitute-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/afdinstitute-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/afdinstitute-com/hosts/afdinstitute-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afdinstitute-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://afdinstitute.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://afdinstitute.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://afdinstitute.com/news
- group: auth
  href: https://artifacts.apis.io/afdinstitute-com/security/afdinstitute-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afdinstitute-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://afdinstitute.com/
coverage:
  checked: '2026-11-01'
  detail: GraphQL endpoint https://api.afdinstitute.com/graphql returns 401 Unauthorized, blocking contract discovery.
  evidence:
  - status: 401
    url: https://api.afdinstitute.com/graphql
  reason: auth-required
  state: gated
created: '2026-10-31'
description: AFD Institute is a standards body based in Belgium that defines adaptive flow delivery methodologies for modern software delivery. It publishes a comprehensive framework, certifications, workshops, and AI‑native tools to help organizations improve delivery excellence. The institute offers a book, a growing library of templates, and a community of practitioners across Europe and beyond.
image: https://afdinstitute.com/images/og-default.jpg
layout: provider
modified: '2026-10-31'
name: AFD Institute
nav: Providers
network: true
overview: AFD Institute is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Standards, Education, Certification, Artificial Intelligence, and Belgium.
random_paper: 8
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 9.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afdinstitute Com Domain Security
  slug: afdinstitute-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: afdinstitute-com
tags:
- Standards
- Education
- Certification
- Artificial Intelligence
- Belgium
website: https://afdinstitute.com/
---
