---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
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
    mcp_server: false
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Calcupedia offers an embeddable calculator widget API documented on their website, but no machine‑readable contract was found.
  name: Calcupedia API
  slug: calcupedia-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/calcupedia-io/plans/calcupedia-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calcupedia-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/calcupedia-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/calcupedia-io/llms/calcupedia-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calcupedia-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/calcupedia-io/well-known/calcupedia-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/calcupedia-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/calcupedia-io/hosts/calcupedia-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calcupedia-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/calcupedia-io/vendors/calcupedia-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calcupedia-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calcupedia.io/terms
- group: operate
  title: ''
  type: Roadmap
  url: https://calcupedia.io/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calcupedia.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://calcupedia.io/pricing
- group: start
  title: ''
  type: Login
  url: https://calcupedia.io/login
- group: company
  title: ''
  type: Blog
  url: https://calcupedia.io/blog
- group: auth
  href: https://artifacts.apis.io/calcupedia-io/security/calcupedia-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calcupedia-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calcupedia.io/
coverage:
  checked: '2026-11-03'
  detail: The provider's documentation site does not expose an OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract despite public docs.
  evidence:
  - status: 406
    url: https://calcupedia.io/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Calcupedia provides an extensive library of over 2,400 free calculators and converters that can be embedded on any website with a single line of code. The platform offers fully branded, customizable widgets without requiring developer effort, and includes AI-powered tools to create custom calculators. It serves businesses and developers looking to add interactive calculation functionality quickly and easily.
image: https://calcupedia.io/og/pages/home.png
layout: provider
modified: '2026-11-03'
name: Calcupedia
nav: Providers
network: true
overview: 'Calcupedia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Calculators, Embeddings, No-Code, Lead Generation, and Finance.


  Calcupedia''s developer surface includes pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Calcupedia Io Plans Pricing
  plan_count: 4
  slug: calcupedia-io-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 9
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
    discoverability: 57.1
    operational_transparency: 2.6
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calcupedia Io Domain Security
  slug: calcupedia-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calcupedia-io
tags:
- Calculators
- Embeddings
- No-Code
- Lead Generation
- Finance
- Health
- Business
- AI Builder
website: https://calcupedia.io/
---
