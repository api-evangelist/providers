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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Borehole Drilling Cost API provides enquiry tools for obtaining drilling cost quotes via a JSON-RPC MCP server.
  name: Borehole Drilling Cost API
  slug: borehole-drilling-cost-api
- baseURL: https://boreholedrillingcost.co.uk
  baseurl_source: declared
  description: 'Borehole Drilling Cost (https://boreholedrillingcost.co.uk/): the site''s own MCP server, served from its domain. Borehole drilling costs £50–£100 per metre drilled; a full private water supply install'
  name: Borehole Drilling Cost API API
  slug: borehole-drilling-cost-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/rules/boreholedrillingcost-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/boreholedrillingcost-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/vocabulary/boreholedrillingcost-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boreholedrillingcost-co-uk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/conformance/boreholedrillingcost-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boreholedrillingcost-co-uk-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://boreholedrillingcost.co.uk/terms
- group: design
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/errors/boreholedrillingcost-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boreholedrillingcost-co-uk-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/llms/boreholedrillingcost-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boreholedrillingcost-co-uk-llms.txt
- group: auth
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/well-known/boreholedrillingcost-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boreholedrillingcost-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/well-known/boreholedrillingcost-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boreholedrillingcost-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/hosts/boreholedrillingcost-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boreholedrillingcost-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/vendors/boreholedrillingcost-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boreholedrillingcost-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/security/boreholedrillingcost-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/boreholedrillingcost-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/boreholedrillingcost-co-uk/security/boreholedrillingcost-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boreholedrillingcost-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boreholedrillingcost.co.uk/
- group: operate
  title: ''
  type: Contact
  url: https://boreholedrillingcost.co.uk/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boreholedrillingcost.co.uk/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boreholedrillingcost.co.uk/terms/
created: '2026-11-03'
description: Borehole Drilling Cost UK provides detailed information, pricing guides, and expert advice on drilling water boreholes across the United Kingdom. The site offers cost per metre data, licensing requirements, heat‑pump borehole costs, water testing guidance, and a marketplace for obtaining quotes from local drilling contractors. Updated regularly with market data and regulatory links, it serves homeowners, farmers, and commercial developers seeking reliable borehole cost estimates and related services.
image: https://boreholedrillingcost.co.uk/og.png
layout: provider
modified: '2026-11-03'
name: Borehole Drilling Cost UK
nav: Providers
network: true
overview: 'Borehole Drilling Cost UK publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Borehole Drilling Cost API API, and 1 more. Tagged areas include Water, Drilling, Cost, United Kingdom, and Borehole.


  The Borehole Drilling Cost UK catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Borehole Drilling Cost UK API Rules
  rule_count: 48
  severity_counts:
    error: 43
    hint: 0
    info: 4
    warn: 1
  slug: boreholedrillingcost-co-uk-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.4
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boreholedrillingcost Co Uk Domain Security
  slug: boreholedrillingcost-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boreholedrillingcost Co Uk Vulnerability Disclosure
  slug: boreholedrillingcost-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: boreholedrillingcost-co-uk
tags:
- Water
- Drilling
- Cost
- United Kingdom
- Borehole
website: https://boreholedrillingcost.co.uk/
---
