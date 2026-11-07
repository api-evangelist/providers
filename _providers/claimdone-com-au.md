---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
  score: 12.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Claim Done legal document services
  name: Claim Done API
  slug: claim-done-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/claimdone-com-au/plans/claimdone-com-au-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/claimdone-com-au-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/claimdone-com-au/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/claimdone-com-au/security/claimdone-com-au-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/claimdone-com-au-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/claimdone-com-au/llms/claimdone-com-au-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/claimdone-com-au-llms.txt
- group: other
  href: https://artifacts.apis.io/claimdone-com-au/a2a/claimdone-com-au-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/claimdone-com-au-a2a.yml
- group: agent
  href: https://artifacts.apis.io/claimdone-com-au/mcp/claimdone-com-au-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/claimdone-com-au-mcp.yml
- group: auth
  href: https://artifacts.apis.io/claimdone-com-au/well-known/claimdone-com-au-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/claimdone-com-au-security.txt
- group: agent
  href: https://artifacts.apis.io/claimdone-com-au/well-known/claimdone-com-au-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/claimdone-com-au-well-known.yml
- group: other
  href: https://artifacts.apis.io/claimdone-com-au/hosts/claimdone-com-au-hosts.yml
  title: ''
  type: Hosts
  url: hosts/claimdone-com-au-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://claimdone.com.au/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://claimdone.com.au/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://claimdone.com.au/pricing/
- group: start
  title: ''
  type: Login
  url: https://claimdone.com.au/login/
- group: company
  title: ''
  type: Blog
  url: https://claimdone.com.au/blog/
- group: auth
  href: https://artifacts.apis.io/claimdone-com-au/security/claimdone-com-au-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/claimdone-com-au-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/claimdone-com-au/security/claimdone-com-au-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/claimdone-com-au-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://claimdone.com.au/
created: '2026-11-03'
description: Claim Done provides Australians with easy-to-use, flat-fee legal document services, allowing users to generate letters of demand, tribunal applications, contract reviews and other consumer law documents online. The platform offers a simple questionnaire, instant drafts, and secure delivery, operating across all Australian states and territories. It is Australian owned and Sydney hosted, serving thousands of users with clear, affordable legal paperwork solutions.
image: https://claimdone.com.au/wp-content/themes/claimdone-theme/assets/img/claimdone-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at claimdone.com.au.
  name: Claim Done MCP Server
  slug: claimdone-com-au-mcp-yml
modified: '2026-11-03'
name: Claim Done
nav: Providers
network: true
overview: 'Claim Done is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Australia, Document Automation, Software-as-a-Service, and Small Business.


  Claim Done''s developer surface includes pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Claimdone Com Au Plans Pricing
  plan_count: 8
  slug: claimdone-com-au-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.6
    discoverability: 56.7
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  provenance:
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Claimdone Com Au Domain Security
  slug: claimdone-com-au-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Claimdone Com Au Vulnerability Disclosure
  slug: claimdone-com-au-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: claimdone-com-au
tags:
- Legal Tech
- Australia
- Document Automation
- Software-as-a-Service
- Small Business
website: https://claimdone.com.au/
---
