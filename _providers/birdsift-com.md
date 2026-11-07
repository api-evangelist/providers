---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.birdsift.com
  baseurl_source: declared
  description: OAuth 2.0 discovery metadata
  name: BirdSift Auth API
  slug: birdsift-com-auth-api
- baseURL: https://api.birdsift.com
  baseurl_source: declared
  description: Workspace credit balance
  name: BirdSift Credits API
  slug: birdsift-com-credits-api
- baseURL: https://api.birdsift.com
  baseurl_source: declared
  description: Public reference material
  name: BirdSift Docs API
  slug: birdsift-com-docs-api
- baseURL: https://api.birdsift.com
  baseurl_source: declared
  description: Saved workspace leads
  name: BirdSift Leads API
  slug: birdsift-com-leads-api
- baseURL: https://api.birdsift.com
  baseurl_source: declared
  description: Model Context Protocol server
  name: BirdSift MCP API
  slug: birdsift-com-mcp-api
- baseURL: https://api.birdsift.com
  baseurl_source: declared
  description: Bounded lead discovery
  name: BirdSift Searches API
  slug: birdsift-com-searches-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/birdsift-com/plans/birdsift-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/birdsift-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/birdsift-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/birdsift-com/data-model/birdsift-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/birdsift-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/birdsift-com/errors/birdsift-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/birdsift-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/birdsift-com/llms/birdsift-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/birdsift-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/birdsift-com/well-known/birdsift-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/birdsift-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/birdsift-com/hosts/birdsift-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/birdsift-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/birdsift-com/vendors/birdsift-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/birdsift-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/birdsift-com/security/birdsift-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/birdsift-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://birdsift.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.birdsift.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.birdsift.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.birdsift.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.birdsift.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.birdsift.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://birdsift.com/openapi.json
  - status: null
    url: https://api.birdsift.com/openapi.json
  - status: null
    url: https://www.birdsift.com/openapi.json
  - status: 401
    url: https://api.birdsift.com/mcp
  - status: 200
    url: https://birdsift.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BirdSift provides a web‑design lead generation platform that searches Google Places to find local businesses without a functional website or with outdated sites. Users can specify trade and city, receive searchable results with contact details, and export data. The service offers free credits and paid plans, targeting agencies and freelancers seeking new clients. It includes features like automated lead verification, data enrichment, and integration via an API for programmatic access.
image: https://www.birdsift.com/en/opengraph-image
layout: provider
modified: '2026-11-02'
name: BirdSift
nav: Providers
network: true
overview: 'BirdSift publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Credits API, Docs API, and 3 more. Tagged areas include Lead Generation, Web Design, Software-as-a-Service, and Marketing.


  BirdSift''s developer surface includes documentation, pricing, and 13 more developer resources.'
plans:
- name: Birdsift Com Plans Pricing
  plan_count: 1
  slug: birdsift-com-plans-pricing
random_paper: 19
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 50.6
    developer_ergonomics: 11.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Birdsift Com Domain Security
  slug: birdsift-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: lead-search
  slug: birdsift-com-lead-search
slug: birdsift-com
tags:
- Lead Generation
- Web Design
- Software-as-a-Service
- Marketing
website: https://birdsift.com/
---
