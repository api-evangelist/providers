---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    error_semantics: documented
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
  score: 12.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public remote Model Context Protocol server (serverInfo "Job Search MCP Server" 1.0.0, Streamable HTTP) that lets AI assistants search Dice tech job listings (search_jobs), fetch a job's details (get_
  name: Dice Job Search MCP Server
  slug: job-search-mcp
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/dice-com/plans/dice-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dice-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dice-com/changelog/dice-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dice-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/dice-com/conventions/dice-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dice-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dice-com/authentication/dice-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dice-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dice-com/lifecycle/dice-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dice-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dice-com/errors/dice-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dice-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/dice-com/mcp/dice-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dice-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dice-com/hosts/dice-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dice-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/dice-com/integrations/dice-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dice-com-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/dice-com/vendors/dice-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dice-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dice-com/security/dice-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dice-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dice.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dice.com/about/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dice.com/career-advice/how-to-connect-the-dice-mcp-server-to-your-ai-assistant
- group: company
  title: ''
  type: Blog
  url: https://www.dice.com/career-advice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dice.com/hiring/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.dice.com/register
- group: operate
  title: ''
  type: Support
  url: https://www.dice.com/about/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dice.com/about/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dice.com/about/privacy-policy
created: '2026-11-05'
description: Dice (dice.com) is a career marketplace dedicated to technology professionals, operated by its parent entity DHI Group, Inc. Tech job seekers search a curated, tech-only database of job openings, get salary estimates and career advice, while employers and recruiters post jobs and find candidates through paid hiring packages. In January 2026 Dice launched a public remote Model Context Protocol (MCP) server at https://mcp.dice.com/mcp that lets AI assistants such as Claude and ChatGPT search Dice job listings with natural-language queries and filters (location radius, workplace type, employment type, posting recency); its documentation states no authentication is required for basic usage.
examples:
- key_count: 3
  name: Dice Com Mcp Tools List
  slug: dice-com-mcp-tools-list
image: https://www.dice.com/webfiles/1770241131432/favicon/dice/android-chrome-192x192.png
json_schemas:
- name: Dice Com Get Company Input
  property_count: 1
  slug: dice-com-get-company-input
- name: Dice Com Get Company Output
  property_count: 3
  slug: dice-com-get-company-output
- name: Dice Com Get Job Details Input
  property_count: 1
  slug: dice-com-get-job-details-input
- name: Dice Com Get Job Details Output
  property_count: 2
  slug: dice-com-get-job-details-output
- name: Dice Com Search Jobs Input
  property_count: 16
  slug: dice-com-search-jobs-input
- name: Dice Com Search Jobs Output
  property_count: 2
  slug: dice-com-search-jobs-output
layout: provider
mcp_servers:
- description: Dice's public remote Model Context Protocol server for searching Dice tech job listings, fetching job details and the company behind a job. Documentation states "No authentication is required for basi
  name: Dice Job Search MCP Server
  slug: dice-job-search-mcp-server
modified: '2026-11-05'
name: Dice
nav: Providers
network: true
overview: 'Dice is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Job, Job Search, Recruiting, and Careers.


  Dice''s developer surface includes changelog, authentication, documentation, getting-started guide, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Dice Com Plans Pricing
  plan_count: 4
  slug: dice-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Dice Com Rate Limits
  slug: dice-com-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 58.0
    catalog_earned_first_party: 12.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 18.5
    developer_ergonomics: 40.5
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dice Com Authentication
  slug: dice-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dice Com Domain Security
  slug: dice-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dice-com
tags:
- Company
- Job
- Job Search
- Recruiting
- Careers
- Technology Talent
- MCP
website: https://www.dice.com/
---
