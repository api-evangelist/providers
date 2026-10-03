---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banner-technologies/refs/heads/main/well-known/banner-technologies-withbanner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/banner-technologies-withbanner-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banner-technologies/refs/heads/main/llms/banner-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/banner-technologies-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banner-technologies/refs/heads/main/a2a/banner-technologies-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/banner-technologies-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banner-technologies/refs/heads/main/well-known/banner-technologies-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/banner-technologies-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banner-technologies/refs/heads/main/well-known/banner-technologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/banner-technologies-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banner-technologies/refs/heads/main/hosts/banner-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banner-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banner-technologies/refs/heads/main/vendors/banner-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/banner-technologies-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://withbanner.statuspage.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://withbanner.com/home/solutions/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banner-technologies/refs/heads/main/security/banner-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banner-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://withbanner.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://withbanner.com/home/guides
- group: operate
  title: ''
  type: Support
  url: https://withbanner.com/home/contact
- group: company
  title: ''
  type: Blog
  url: https://withbanner.com/home/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withbanner.com/home/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withbanner.com/home/privacy
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's API or docs hosts.
  evidence:
  - status: unreachable
    url: https://api.withbanner.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Banner Technologies provides a real‑estate CapEx management platform for owners and operators, enabling unified planning, execution, and tracking of capital expenditure projects across multifamily, commercial, and developer portfolios. The solution replaces spreadsheets with a purpose‑built operating system, offering financial and project management tools, case studies, and a demo experience to streamline budgeting and execution.
image: https://withbanner.com/home/images/Banner-opengraph.png
layout: provider
modified: '2026-09-27'
name: Banner Technologies
nav: Providers
network: true
overview: 'Banner Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, CapEx, Software-as-a-Service, and Property Management.


  Banner Technologies'' developer surface includes documentation, support, engineering blog, and 13 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Banner Technologies Domain Security
  slug: banner-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: banner-technologies
tags:
- Company
- Real Estate
- CapEx
- Software-as-a-Service
- Property Management
website: https://withbanner.com/home
---
