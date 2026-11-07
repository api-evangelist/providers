---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Charitysense Com Agentic Access
  operation_count: 21
  slug: charitysense-com-agentic-access
  summary_line: 21 operations · 3 acting
api_count: 1
apis:
- baseURL: https://data.charitysense.com
  baseurl_source: declared
  description: Paid Advanced operations. Each request consumes the token's daily Advanced allowance.
  name: CharitySense Assistant API
  slug: charitysense-com-assistant-api
- baseURL: https://data.charitysense.com
  baseurl_source: declared
  description: Service health and published dataset statistics. Statistics and top lists consume the Advanced allowance.
  name: CharitySense Dataset API
  slug: charitysense-com-dataset-api
- baseURL: https://data.charitysense.com
  baseurl_source: declared
  description: Identity search and related-organization discovery.
  name: CharitySense Discovery API
  slug: charitysense-com-discovery-api
- baseURL: https://data.charitysense.com
  baseurl_source: declared
  description: Canonical overlay profile and filing resources.
  name: CharitySense Profiles API
  slug: charitysense-com-profiles-api
- baseURL: https://data.charitysense.com
  baseurl_source: declared
  description: Authenticated token allowance and UTC-day usage.
  name: CharitySense Usage API
  slug: charitysense-com-usage-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/charitysense-com/capabilities/charitysense-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/charitysense-com-capability-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://data.charitysense.com/INSTRUCTIONS_FOR_AGENTS.md
- group: agent
  href: https://artifacts.apis.io/charitysense-com/agentic-access/charitysense-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/charitysense-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/charitysense-com/security/charitysense-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/charitysense-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/charitysense-com/authentication/charitysense-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/charitysense-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://charitysense.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.charitysense.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://data.charitysense.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://data.charitysense.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://data.charitysense.com/agents
- group: operate
  title: ''
  type: Support
  url: https://data.charitysense.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://data.charitysense.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://charitysense.com/insights
- group: other
  href: https://artifacts.apis.io/charitysense-com/a2a/charitysense-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/charitysense-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/charitysense-com/well-known/charitysense-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/charitysense-com-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://data.charitysense.com/.well-known/api-catalog
- group: build
  title: ''
  type: OpenAIPluginManifest
  url: https://data.charitysense.com/.well-known/ai-plugin.json
- group: agent
  href: https://artifacts.apis.io/charitysense-com/llms/charitysense-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/charitysense-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/charitysense-com/llms/charitysense-com-website-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/charitysense-com-website-llms.txt
- group: other
  href: https://artifacts.apis.io/charitysense-com/skills/charitysense-com-instructions-for-agents.md
  title: ''
  type: AgentInstructions
  url: skills/charitysense-com-instructions-for-agents.md
- group: agent
  href: https://artifacts.apis.io/charitysense-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/charitysense-com/conformance/charitysense-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/charitysense-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/charitysense-com/errors/charitysense-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/charitysense-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/charitysense-com/lifecycle/charitysense-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/charitysense-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/charitysense-com/conventions/charitysense-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/charitysense-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/charitysense-com/data-model/charitysense-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/charitysense-com-data-model.yml
- group: other
  href: https://artifacts.apis.io/charitysense-com/overlays/charitysense-com-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/charitysense-com-data-api-overlay.yaml
- group: commercial
  href: https://artifacts.apis.io/charitysense-com/plans/charitysense-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/charitysense-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/charitysense-com/rate-limits/charitysense-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/charitysense-com-rate-limits.yml
created: '2026-09-19'
description: 'CharitySense is a product of Osci Labs LLC (US) with two public surfaces. charitysense.com is an edge-AI verification platform that plugs into cameras already installed at funded hospitals, schools, water wells and orphanages, processes video on-device, and gives donors, foundations, NGOs and governments live dashboards proving a funded project is actually running. data.charitysense.com is CharitySense Data, an agent-ready nonprofit due-diligence API over public IRS Form 990 filings for about 2.2 million U.S. nonprofits: charity search, bounded profile pages with lazily fetched sections, filing history, money-network and grant-flow evidence, related-organization discovery, dataset statistics and a paid assistant. It is a 21-operation OpenAPI 3.1.0 contract at https://data.charitysense.com/openapi.yaml; research reads need no key (1,000 per UTC day), Advanced operations need a paid key. The host also serves an RFC 9727 API catalog, an A2A-shaped agent card, ai-plugin.json and
  llms.txt.'
finops:
- has_sources: true
  method: derived
  name: Charitysense Com Finops
  primary_unit: ''
  service_category: ''
  slug: charitysense-com-finops
  template: true
image: https://data.charitysense.com/logo.svg
layout: provider
modified: '2026-09-19'
name: CharitySense
nav: Providers
network: true
overview: 'CharitySense publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assistant API, Dataset API, Discovery API, and 2 more. Tagged areas include Non-Profit, Charities, Due Diligence, IRS Form 990, and Donor Research.


  The CharitySense catalog on APIs.io includes 1 Spectral governance ruleset.


  CharitySense''s developer surface includes pricing, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
plans:
- name: Charitysense Com Plans Pricing
  plan_count: 2
  slug: charitysense-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Charitysense Com Rate Limits
  slug: charitysense-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: CharitySense API Rules
  rule_count: 58
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 5
  slug: charitysense-com-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 55.0
    developer_ergonomics: 36.3
    discoverability: 83.9
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/charitysense-com/charitysense-com-2026-10-11T102848.png
security:
- kind: authentication
  name: Charitysense Com Authentication
  slug: charitysense-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Charitysense Com Domain Security
  slug: charitysense-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Report a data gap or result problem back to CharitySense
  slug: charitysense-com-report-a-data-gap
- name: Research a U.S. charity from a name or EIN
  slug: charitysense-com-research-a-charity
- name: Trace grant flows and funders for a charity or cohort
  slug: charitysense-com-trace-grant-flows
slug: charitysense-com
tags:
- Non-Profit
- Charities
- Due Diligence
- IRS Form 990
- Donor Research
- Grants
- Philanthropy
- Open Data
- Agents
- A2A
- Impact Verification
- Edge AI
- United States
- Company
website: https://charitysense.com/
---
