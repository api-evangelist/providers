---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Adds SEO Records tools to AI assistants like Claude, ChatGPT, Le Chat or Cursor, enabling site SEO analysis via natural language.
  name: SEO Records MCP API
  slug: mcp-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/seorecords-com/plans/seorecords-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/seorecords-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/seorecords-com/security/seorecords-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/seorecords-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/seorecords-com/llms/seorecords-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seorecords-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/seorecords-com/well-known/seorecords-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/seorecords-com-security.txt
- group: agent
  href: https://artifacts.apis.io/seorecords-com/well-known/seorecords-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seorecords-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/seorecords-com/hosts/seorecords-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seorecords-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/seorecords-com/vendors/seorecords-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seorecords-com-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://seorecords.com/guides
- group: auth
  href: https://artifacts.apis.io/seorecords-com/security/seorecords-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/seorecords-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/seorecords-com/security/seorecords-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seorecords-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seorecords.com
coverage:
  checked: '2026-10-29'
  detail: Public documentation exists (e.g., https://seorecords.com/guides) but no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other spec is published.
  evidence:
  - status: 200
    url: https://seorecords.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 'Des corrections SEO posées au moment où la page est servie : votre site reste le vôtre, chaque source citée. Des records mesurés, datés, rejouables. Corrige le référencement et la vitesse de vos pages au moment où elles sont servies. SEO Records propose des solutions pour WordPress, PrestaShop, Joomla, Drupal, et sites PHP, offrant des corrections SEO en temps réel et des prix à partir de 199 €.'
image: https://seorecords.com/og/accueil.png
layout: provider
mcp_servers:
- description: ''
  name: seorecords-com MCP Server
  slug: seorecords-com-mcp-json
modified: '2026-10-29'
name: seorecords-com
nav: Providers
network: true
overview: 'seorecords-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SEO, Performance, Web, SaaS, and French.


  seorecords-com''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Seorecords Com Plans Pricing
  plan_count: 17
  slug: seorecords-com-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Seorecords Com Domain Security
  slug: seorecords-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Seorecords Com Vulnerability Disclosure
  slug: seorecords-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: seorecords-com
tags:
- SEO
- Performance
- Web
- SaaS
- French
website: https://seorecords.com
---
