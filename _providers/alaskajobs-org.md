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
- description: Public Model Context Protocol (MCP) JSON-RPC API providing job search, salary data, employer profiles, and state pay schedule lookup for Alaska public-sector data.
  name: Alaska Jobs MCP
  slug: alaska-jobs-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/alaskajobs-org/llms/alaskajobs-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alaskajobs-org-llms.txt
- group: other
  href: https://artifacts.apis.io/alaskajobs-org/hosts/alaskajobs-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alaskajobs-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/alaskajobs-org/vendors/alaskajobs-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alaskajobs-org-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://alaskajobs.org/salaries/registered-nurse
- group: auth
  href: https://artifacts.apis.io/alaskajobs-org/security/alaskajobs-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alaskajobs-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alaskajobs.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://alaskajobs.org/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://alaskajobs.org/guides
created: '2026-11-01'
description: Alaska Jobs is a free, daily public‑sector job board for the state of Alaska. It aggregates employment listings from government agencies, healthcare providers, trade unions, and private sector employers, updating each morning from official sources. Users can browse, filter by location, industry, or salary, and access open data downloads. The service operates without ads, accounts, or fees, and provides tools such as a state salary schedule calculator and community pay comparator.
examples:
- key_count: 3
  name: Alaskajobs Mcp Tools
  slug: alaskajobs-mcp-tools
image: https://alaskajobs.org/favicon.ico
layout: provider
modified: '2026-11-01'
name: Alaska Jobs
nav: Providers
network: true
overview: 'Alaska Jobs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Job, Alaska, Employment, Government, and Healthcare.


  Alaska Jobs'' developer surface includes signup flow, getting-started guide, and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 12.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alaskajobs Org Domain Security
  slug: alaskajobs-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alaskajobs-org
tags:
- Job
- Alaska
- Employment
- Government
- Healthcare
website: https://alaskajobs.org/
---
