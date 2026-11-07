---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Directree Io Agentic Access
  operation_count: 5
  slug: directree-io-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://www.directree.io
  baseurl_source: declared
  description: The Listings API from Directree — 4 operation(s) for listings.
  name: Directree Listings API
  slug: directree-io-listings-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/directree-io/agentic-access/directree-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/directree-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/directree-io/plans/directree-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/directree-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/directree-io/rules/directree-io-rules.yml
  title: ''
  type: Spectral
  url: rules/directree-io-rules.yml
- group: agent
  href: https://artifacts.apis.io/directree-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/directree-io/conventions/directree-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/directree-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/directree-io/conventions/directree-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/directree-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/directree-io/authentication/directree-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/directree-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/directree-io/errors/directree-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/directree-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/directree-io/conformance/directree-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/directree-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/directree-io/llms/directree-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/directree-io-llms.txt
- group: build
  href: https://artifacts.apis.io/directree-io/mcp/directree-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/directree-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/directree-io/mcp/directree-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/directree-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/directree-io/hosts/directree-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/directree-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/directree-io/vendors/directree-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/directree-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.directree.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.directree.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.directree.io/pricing
- group: start
  title: ''
  type: Login
  url: https://www.directree.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.directree.io/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.directree.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.directree.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.directree.io/docs/agent-api
- group: docs
  title: ''
  type: APIReference
  url: https://www.directree.io/api
- group: auth
  href: https://artifacts.apis.io/directree-io/security/directree-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/directree-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.directree.io/
created: '2026-11-05'
description: Directree is an honest SaaS directory that provides transparent, fact‑labelled listings for software products. Users can paste a URL to receive a structured overview in about 30 seconds, with each fact marked as crawled or AI‑inferred. No pay‑to‑rank, free access, and a focus on unbiased reviews.
image: https://www.directree.io/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.directree.io.
  name: Directree MCP Server
  slug: directree-io-mcp-yml
modified: '2026-11-05'
name: Directree
nav: Providers
network: true
overview: 'Directree publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Listings API. Tagged areas include Software-as-a-Service, Directory, Software, Reviews, and Open Data.


  The Directree catalog on APIs.io includes 1 Spectral governance ruleset.


  Directree''s developer surface includes authentication, pricing, documentation, changelog, engineering blog, getting-started guide, API reference, and 18 more developer resources.'
plans:
- name: Directree Io Plans Pricing
  plan_count: 10
  slug: directree-io-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Directree API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: directree-io-rules
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 45.3
    developer_ergonomics: 44.6
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Directree Io Authentication
  slug: directree-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Directree Io Domain Security
  slug: directree-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: directree-io-update-listing
  slug: directree-io-update-listing
slug: directree-io
tags:
- Software-as-a-Service
- Directory
- Software
- Reviews
- Open Data
website: https://www.directree.io/
---
