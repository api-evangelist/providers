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
    mcp_server: documented
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
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for accessing procurement data and tender opportunities as documented in the guides.
  name: askTender API
  slug: asktender-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/asktender-org/plans/asktender-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asktender-org-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/asktender-org/llms/asktender-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asktender-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/asktender-org/mcp/asktender-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asktender-org-mcp.yml
- group: agent
  href: https://artifacts.apis.io/asktender-org/well-known/asktender-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asktender-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/asktender-org/hosts/asktender-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asktender-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/asktender-org/vendors/asktender-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asktender-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asktender.org/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asktender.org/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://asktender.org/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://asktender.org/guides
- group: auth
  href: https://artifacts.apis.io/asktender-org/security/asktender-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asktender-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asktender.org/
coverage:
  checked: '2026-11-02'
  detail: Documentation pages exist but no machine‑readable OpenAPI or other contract was found.
  evidence:
  - status: 200
    url: https://asktender.org/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: askTender is a global procurement platform that connects businesses with public tender opportunities across more than 120 countries. It aggregates tender data, provides intelligence, and offers services to help companies find, qualify, and submit bids for government contracts. The platform includes pricing plans for various business sizes and offers an API for integration with enterprise workflows.
image: https://asktender.org/og.png?v=5
layout: provider
mcp_servers:
- description: Remote MCP server at asktender.org.
  name: askTender MCP Server
  slug: asktender-org-mcp-yml
modified: '2026-11-01'
name: askTender
nav: Providers
network: true
overview: 'askTender is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Procurement, Government, B2B, Software-as-a-Service, and Marketplace.


  askTender''s developer surface includes pricing, documentation, and 10 more developer resources.'
plans:
- name: Asktender Org Plans Pricing
  plan_count: 4
  slug: asktender-org-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 21.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asktender Org Domain Security
  slug: asktender-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: asktender-org
tags:
- Procurement
- Government
- B2B
- Software-as-a-Service
- Marketplace
website: https://asktender.org/
---
