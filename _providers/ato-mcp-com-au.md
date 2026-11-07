---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
api_count: 1
apis:
- description: API for Australian Tax MCP providing AI agent tools over ATO documents.
  name: Australian Tax MCP API
  slug: australian-tax-mcp-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/ato-mcp-com-au/plans/ato-mcp-com-au-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ato-mcp-com-au-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ato-mcp-com-au/changelog/ato-mcp-com-au-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ato-mcp-com-au-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/william-laverty/ato-mcp/blob/main/SECURITY.md
- group: agent
  href: https://artifacts.apis.io/ato-mcp-com-au/llms/ato-mcp-com-au-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ato-mcp-com-au-llms.txt
- group: auth
  href: https://artifacts.apis.io/ato-mcp-com-au/well-known/ato-mcp-com-au-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ato-mcp-com-au-security.txt
- group: agent
  href: https://artifacts.apis.io/ato-mcp-com-au/well-known/ato-mcp-com-au-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ato-mcp-com-au-well-known.yml
- group: other
  href: https://artifacts.apis.io/ato-mcp-com-au/hosts/ato-mcp-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ato-mcp-com-au-hosts.yml
- group: other
  href: https://artifacts.apis.io/ato-mcp-com-au/vendors/ato-mcp-com-au-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ato-mcp-com-au-vendors.yml
- group: build
  href: https://artifacts.apis.io/ato-mcp-com-au/packages/ato-mcp-com-au-packages.yml
  title: ''
  type: SDKs
  url: packages/ato-mcp-com-au-packages.yml
- group: build
  href: https://artifacts.apis.io/ato-mcp-com-au/packages/ato-mcp-com-au-packages.yml
  title: ''
  type: Packages
  url: packages/ato-mcp-com-au-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ato-mcp.com.au/terms
- group: auth
  href: https://artifacts.apis.io/ato-mcp-com-au/security/ato-mcp-com-au-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ato-mcp-com-au-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ato-mcp-com-au/security/ato-mcp-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ato-mcp-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ato-mcp.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://ato-mcp.com.au/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.ato-mcp.com.au/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://ato-mcp.com.au/install
- group: company
  title: ''
  type: Blog
  url: https://ato-mcp.com.au/feed.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ato-mcp.com.au/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://ato-mcp.com.au/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/william-laverty/ato-mcp
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint requires POST JSON-RPC and returns 405 for GET, blocking contract discovery.
  evidence:
  - status: 405
    url: https://api.ato-mcp.com.au/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Australian Tax MCP is an independent project providing AI agents with cited retrieval over 34,500 ATO documents, the Income Tax and GST Acts, and 4,900 public rulings via the Model Context Protocol. Not affiliated with the Australian Taxation Office.
image: https://ato-mcp.com.au/logo-square.png
layout: provider
modified: '2026-11-01'
name: Australian Tax MCP
nav: Providers
network: true
overview: 'Australian Tax MCP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tax, Artificial Intelligence, Australia, MCP, and Open Data.


  Australian Tax MCP''s developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Ato Mcp Com Au Plans Pricing
  plan_count: 3
  slug: ato-mcp-com-au-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 32.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ato Mcp Com Au Domain Security
  slug: ato-mcp-com-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ato Mcp Com Au Vulnerability Disclosure
  slug: ato-mcp-com-au-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ato-mcp-com-au
tags:
- Tax
- Artificial Intelligence
- Australia
- MCP
- Open Data
website: https://ato-mcp.com.au/
---
