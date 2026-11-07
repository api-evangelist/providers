---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public read‑only API providing access to Alexandria Archive content such as articles, health check, and search. No authentication required.
  name: Alexandria Archive Public API
  slug: alexandria-archive-public-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/alexandria-archive-com/rules/alexandria-archive-com-rules.yml
  title: ''
  type: Spectral
  url: rules/alexandria-archive-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/alexandria-archive-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/alexandria-archive-com/security/alexandria-archive-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/alexandria-archive-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/alexandria-archive-com/errors/alexandria-archive-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alexandria-archive-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alexandria-archive-com/conformance/alexandria-archive-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alexandria-archive-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alexandria-archive-com/llms/alexandria-archive-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alexandria-archive-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/alexandria-archive-com/well-known/alexandria-archive-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alexandria-archive-com-security.txt
- group: auth
  href: https://artifacts.apis.io/alexandria-archive-com/well-known/alexandria-archive-com-alexandria-archive-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alexandria-archive-com-alexandria-archive-security.txt
- group: agent
  href: https://artifacts.apis.io/alexandria-archive-com/well-known/alexandria-archive-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alexandria-archive-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/alexandria-archive-com/hosts/alexandria-archive-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alexandria-archive-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alexandria-archive-com/vendors/alexandria-archive-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alexandria-archive-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alexandria-archive.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alexandria-archive.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.alexandria-archive.com/press
- group: auth
  href: https://artifacts.apis.io/alexandria-archive-com/security/alexandria-archive-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alexandria-archive-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alexandria-archive-com/security/alexandria-archive-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alexandria-archive-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alexandria-archive.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.alexandria-archive.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.alexandria-archive.com/api/openapi.json
- group: docs
  title: ''
  type: Documentation
  url: https://www.alexandria-archive.com/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://www.alexandria-archive.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.alexandria-archive.com/articles
coverage:
  checked: '2026-11-01'
  detail: OpenAPI spec served from provider domain points to another company's domain, so no owned contract is available.
  evidence:
  - status: 200
    url: https://www.alexandria-archive.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Alexandria Archive is a professional digital archive dedicated to preserving and exploring the history of Alexandria, Egypt through photographs, documents, maps, and collections. Founded on 6 September 2023, it offers an open, youth‑led cultural‑heritage platform where the community can contribute historic photos, articles, and stories. The site provides an OpenAPI specification at /api/openapi.json and a machine‑readable llms.txt index for developers.
image: https://res.cloudinary.com/dtvtpi71l/image/upload/v1771582831/alexandria-archive/yunc3tfwdx7bpkdv4chr.jpg
layout: provider
modified: '2026-11-01'
name: Alexandria Archive
nav: Providers
network: true
overview: 'Alexandria Archive publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Archives, History, Egypt, Digital Preservation, and Culture.


  The Alexandria Archive catalog on APIs.io includes 1 Spectral governance ruleset.


  Alexandria Archive''s developer surface includes API reference, documentation, getting-started guide, engineering blog, and 18 more developer resources.'
plans:
- name: Alexandria Archive Com Plans Pricing
  plan_count: 0
  slug: alexandria-archive-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Alexandria Archive Com Rate Limits
  slug: alexandria-archive-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Alexandria Archive API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: alexandria-archive-com-rules
scopes:
- name: Alexandria Archive Com Scopes
  scope_count: 0
  slug: alexandria-archive-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.7
    discoverability: 67.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - egypt
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
    - mena
    - north-africa
  previous_composite: 26.8
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alexandria Archive Com Authentication
  slug: alexandria-archive-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alexandria Archive Com Domain Security
  slug: alexandria-archive-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Alexandria Archive Com Vulnerability Disclosure
  slug: alexandria-archive-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: get-article
  slug: alexandria-archive-com-get-article
- name: list-articles
  slug: alexandria-archive-com-list-articles
- name: search-archive
  slug: alexandria-archive-com-search
slug: alexandria-archive-com
tags:
- Archives
- History
- Egypt
- Digital Preservation
- Culture
- Photography
- Community
website: https://alexandria-archive.com/
---
