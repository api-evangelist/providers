---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/3ammiya-com/hosts/3ammiya-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3ammiya-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/3ammiya-com/vendors/3ammiya-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/3ammiya-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://3ammiya.com/register?next=%2Fsubmit
- group: auth
  href: https://artifacts.apis.io/3ammiya-com/security/3ammiya-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3ammiya-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3ammiya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://3ammiya.com/en/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3ammiya.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3ammiya.com/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://3ammiya.com/en/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://3ammiya.com/en/learn
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract found at standard endpoints on api.3ammiya.com or 3ammiya.com.
  evidence:
  - status: 404
    url: https://api.3ammiya.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 3ammiya is an online Egyptian Arabic dictionary and slang platform that crowdsources word meanings, expressions, and colloquial phrases. Users can submit new words, browse trending and latest entries, and explore definitions in both Arabic and English. The site offers social media integration, community contributions, and a searchable database of everyday language used across Egypt.
image: https://3ammiya.com/logo.svg
layout: provider
modified: '2026-10-31'
name: 3ammiya
nav: Providers
network: true
overview: '3ammiya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Dictionaries, Language, Arabic, Slang, and Community.


  3ammiya''s developer surface includes signup flow, documentation, support, getting-started guide, and 6 more developer resources.'
plans:
- name: 3Ammiya Com Plans Pricing
  plan_count: 0
  slug: 3ammiya-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: 3Ammiya Com Rate Limits
  slug: 3ammiya-com-rate-limits
scopes:
- name: 3Ammiya Com Scopes
  scope_count: 0
  slug: 3ammiya-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - egypt
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 17.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 3Ammiya Com Authentication
  slug: 3ammiya-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 3Ammiya Com Domain Security
  slug: 3ammiya-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 3ammiya-com
tags:
- Dictionaries
- Language
- Arabic
- Slang
- Community
- Education
website: https://3ammiya.com/
---
