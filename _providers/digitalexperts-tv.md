---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Read-only remote MCP server (streamable-http, registry name tv.digitalexperts/hypotheses) over the Digital Experts open dataset of JTBD hypotheses and cold-traffic test results; tools list_niches, nic
  name: Digital Experts Hypotheses MCP Server
  slug: hypotheses-mcp
- description: 'Static CC BY 4.0 JSON dataset of 1,500+ anonymised JTBD hypotheses and test-wave summaries (job story, audience, offer, ad creative, test budget, cost per subscriber/lead, verdict), each row carrying '
  name: Digital Experts Open Data (Hypotheses JSON)
  slug: open-data
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/digitalexperts-tv/rate-limits/digitalexperts-tv-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/digitalexperts-tv-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/digitalexperts-tv/plans/digitalexperts-tv-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digitalexperts-tv-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/digitalexperts-tv/conventions/digitalexperts-tv-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digitalexperts-tv-conventions.yml
- group: auth
  href: https://artifacts.apis.io/digitalexperts-tv/authentication/digitalexperts-tv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digitalexperts-tv-authentication.yml
- group: agent
  href: https://artifacts.apis.io/digitalexperts-tv/llms/digitalexperts-tv-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digitalexperts-tv-llms.txt
- group: agent
  href: https://artifacts.apis.io/digitalexperts-tv/mcp/digitalexperts-tv-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/digitalexperts-tv-mcp.yml
- group: other
  href: https://artifacts.apis.io/digitalexperts-tv/hosts/digitalexperts-tv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/digitalexperts-tv-hosts.yml
- group: other
  href: https://artifacts.apis.io/digitalexperts-tv/vendors/digitalexperts-tv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/digitalexperts-tv-vendors.yml
- group: auth
  href: https://artifacts.apis.io/digitalexperts-tv/security/digitalexperts-tv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digitalexperts-tv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://digitalexperts.tv/
- group: company
  title: ''
  type: Blog
  url: https://digitalexperts.tv/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://digitalexperts.tv/pricing
- group: operate
  title: ''
  type: Support
  url: https://digitalexperts.tv/contacts
- group: other
  title: ''
  type: Leadership
  url: https://digitalexperts.tv/team
- group: commercial
  title: ''
  type: TermsOfService
  url: https://digitalexperts.tv/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://digitalexperts.tv/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: https://digitalexperts.tv/llms.txt
- group: other
  title: ''
  type: OpenData
  url: https://digitalexperts.tv/data
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/digital-experts-tv/
created: '2026-11-05'
description: Digital Experts (digitalexperts.tv) is a digital consulting and marketing agency for experts, consultants and B2B companies with complex products and long sales cycles, offering strategy, content marketing, SMM, lead generation, analytics and AI automation. Run by George Ryzhenko as a trade name (Digital Experts is a brand, not a separate legal entity, per its llms.txt), it publishes an open CC BY 4.0 dataset of 1,500+ JTBD hypotheses with cold-traffic test results at digitalexperts.tv/data and lists a read-only MCP server (tv.digitalexperts/hypotheses) in the MCP Registry.
examples:
- key_count: 3
  name: Digitalexperts Tv Mcp Tools List
  slug: digitalexperts-tv-mcp-tools-list
image: https://digitalexperts.tv/images/og/ru/home.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.digitalexperts.tv; 5 tools listed.
  name: Digital Experts Hypotheses MCP Server
  slug: digital-experts-hypotheses-mcp-server
modified: '2026-11-05'
name: Digital Experts
nav: Providers
network: true
overview: 'Digital Experts is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Agency, B2B Marketing, and Consulting.


  Digital Experts'' developer surface includes authentication, engineering blog, pricing, support, and 15 more developer resources.'
plans:
- name: Digitalexperts Tv Plans Pricing
  plan_count: 4
  slug: digitalexperts-tv-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Digitalexperts Tv Rate Limits
  slug: digitalexperts-tv-rate-limits
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 6.5
    developer_ergonomics: 28.6
    discoverability: 73.3
    operational_transparency: 21.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Digitalexperts Tv Authentication
  slug: digitalexperts-tv-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Digitalexperts Tv Domain Security
  slug: digitalexperts-tv-domain-security
  summary_line: TLSv1.3 · HSTS
slug: digitalexperts-tv
tags:
- Company
- Marketing
- Marketing Agency
- B2B Marketing
- Consulting
- Lead Generation
- Open Data
- AI Automation
- MCP
website: https://digitalexperts.tv/
---
