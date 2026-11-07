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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Ainode Tech provides AI‑enhanced wearable device data and auditing services via its platform.
  name: Ainode Tech API
  slug: ainode-tech-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/ainode-tech/llms/ainode-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ainode-tech-llms.txt
- group: agent
  href: https://artifacts.apis.io/ainode-tech/mcp/ainode-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ainode-tech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ainode-tech/well-known/ainode-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ainode-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/ainode-tech/hosts/ainode-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ainode-tech-hosts.yml
- group: other
  href: https://artifacts.apis.io/ainode-tech/vendors/ainode-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ainode-tech-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://ainode.tech/reports/security/SHR_Ring_Report_EN.html
- group: auth
  href: https://artifacts.apis.io/ainode-tech/security/ainode-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ainode-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ainode.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://ainode.tech/methodology.html
- group: company
  title: ''
  type: Blog
  url: https://ainode.tech/blog/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ainode.tech/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ainode.tech/terms.html
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract extraction.
  evidence:
  - status: 200
    url: https://ainode.tech/methodology.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Ainode Tech is a Portuguese company specializing in AI‑enhanced wearables. It provides audited, privacy‑focused wearable devices, offering detailed methodology, reviews, and a curated shop. The site includes extensive documentation on its auditing process, a blog, podcast, and clear privacy and terms pages, positioning itself as a trusted authority for consumers seeking secure AI wearables.
image: https://ainode.tech/images/ainode-og-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at ainode.tech.
  name: ainode-tech MCP Server
  slug: ainode-tech-mcp-yml
modified: '2026-10-29'
name: ainode-tech
nav: Providers
network: true
overview: 'ainode-tech is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wearables, Artificial Intelligence, Privacy, and Portugal.


  ainode-tech''s developer surface includes documentation, engineering blog, and 10 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 66.7
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - portugal
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ainode-tech/ainode-tech-2026-11-03T120515.png
security:
- kind: domain-security
  name: Ainode Tech Domain Security
  slug: ainode-tech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ainode-tech
tags:
- Company
- Wearables
- Artificial Intelligence
- Privacy
- Portugal
website: https://ainode.tech/
---
