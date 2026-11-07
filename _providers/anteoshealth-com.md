---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
- description: Medical pre-consultation MCP API
  name: Anteos MCP
  slug: anteos-mcp
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/anteoshealth-com/plans/anteoshealth-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anteoshealth-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/anteoshealth-com/conformance/anteoshealth-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anteoshealth-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anteoshealth-com/llms/anteoshealth-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anteoshealth-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anteoshealth-com/mcp/anteoshealth-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anteoshealth-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anteoshealth-com/well-known/anteoshealth-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anteoshealth-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anteoshealth-com/hosts/anteoshealth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anteoshealth-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/anteoshealth-com/security/anteoshealth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anteoshealth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anteoshealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://anteoshealth.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anteoshealth.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://anteoshealth.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://anteoshealth.com/support
- group: company
  title: ''
  type: Blog
  url: https://anteoshealth.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://anteoshealth.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://anteoshealth.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anteoshealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anteoshealth.com/privacy
created: '2026-11-01'
description: Anteos Health provides an AI-powered medical pre-consultation platform that enables patients to complete a vocal interview or guided questionnaire before their appointment, delivering a structured summary to physicians and an AI scribe that drafts the visit report. Hosted on HDS‑compliant infrastructure in France.
image: https://anteoshealth.com/favicon.png
layout: provider
mcp_servers:
- description: Remote MCP server at anteoshealth.com.
  name: Anteos Health MCP Server
  slug: anteoshealth-com-mcp-yml
modified: '2026-11-01'
name: Anteos Health
nav: Providers
network: true
overview: 'Anteos Health is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Artificial Intelligence, Medical Software, Telehealth, and France.


  Anteos Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Anteoshealth Com Plans Pricing
  plan_count: 5
  slug: anteoshealth-com-plans-pricing
random_paper: 12
scopes:
- name: Anteoshealth Com Scopes
  scope_count: 0
  slug: anteoshealth-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 33.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anteoshealth Com Authentication
  slug: anteoshealth-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anteoshealth Com Domain Security
  slug: anteoshealth-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: anteoshealth-com
tags:
- Healthcare
- Artificial Intelligence
- Medical Software
- Telehealth
- France
website: https://anteoshealth.com/
---
