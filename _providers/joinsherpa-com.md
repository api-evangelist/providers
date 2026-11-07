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
    well_known_catalog: true
  schema_version: '0.2'
  score: 3.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.joinsherpa.com/
- group: agent
  href: https://artifacts.apis.io/joinsherpa-com/llms/joinsherpa-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/joinsherpa-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/joinsherpa-com/mcp/joinsherpa-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/joinsherpa-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/joinsherpa-com/hosts/joinsherpa-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joinsherpa-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joinsherpa-com/vendors/joinsherpa-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joinsherpa-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinsherpa.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.joinsherpa.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joinsherpa.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinsherpa.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.joinsherpa.com/blog/blog-posts
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinsherpa.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/joinsherpa
- group: auth
  href: https://artifacts.apis.io/joinsherpa-com/security/joinsherpa-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/joinsherpa-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/joinsherpa-com/security/joinsherpa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joinsherpa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinsherpa.com
coverage:
  checked: '2026-10-29'
  detail: The provider's website and support pages contain no developer documentation or public API specifications.
  evidence:
  - status: 200
    url: https://www.joinsherpa.com
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Sherpa provides a travel requirements and eVisa platform that enables airlines, online travel agencies, and travel management companies to offer seamless eVisa services to their customers. The service aggregates visa information, automates application processes, and integrates with airline and OTA booking flows, helping travelers meet entry requirements quickly. Sherpa’s platform is trusted by leading airlines and travel brands worldwide.
image: https://www.joinsherpa.com/images/brand/sherpa-logo-tagline-onwhite.svg
layout: provider
mcp_servers:
- description: Remote MCP server at support.joinsherpa.com.
  name: Sherpa MCP Server
  slug: joinsherpa-com-mcp-yml
modified: '2026-10-29'
name: Sherpa
nav: Providers
network: true
overview: 'Sherpa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, eVisa, Airlines, and TravelTech.


  Sherpa''s developer surface includes support, engineering blog, documentation, and 12 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 50.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/joinsherpa-com/joinsherpa-com-2026-11-03T134220.png
security:
- kind: domain-security
  name: Joinsherpa Com Domain Security
  slug: joinsherpa-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Joinsherpa Com Trust Center
  slug: joinsherpa-com-trust-center
  summary_line: SOC 2, PCI DSS
slug: joinsherpa-com
tags:
- Travel
- eVisa
- Airlines
- TravelTech
website: https://joinsherpa.com
---
