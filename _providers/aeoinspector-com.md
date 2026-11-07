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
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AEO Inspector providing scan and report endpoints
  name: AEO Inspector API
  slug: aeo-inspector-api
- baseURL: https://aeoinspector.com
  baseurl_source: declared
  description: 'AI answer-engine visibility for any website: a $0.05 deep AEO scan (up to 10 pages, 100-point score, fixes, ready-to-paste llms.txt/robots.txt/JSON-LD), a $9 report that asks ChatGPT, Microsoft Copilo'
  name: AEO Inspector Api API
  slug: aeo-inspector-api-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/aeoinspector-com/rules/aeoinspector-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aeoinspector-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aeoinspector-com/conformance/aeoinspector-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aeoinspector-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/aeoinspector-com/plans/aeoinspector-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aeoinspector-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aeoinspector-com/errors/aeoinspector-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aeoinspector-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/aeoinspector-com/llms/aeoinspector-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeoinspector-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aeoinspector-com/well-known/aeoinspector-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aeoinspector-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aeoinspector-com/hosts/aeoinspector-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aeoinspector-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aeoinspector-com/vendors/aeoinspector-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aeoinspector-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aeoinspector-com/security/aeoinspector-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeoinspector-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aeoinspector.com/
- group: docs
  title: ''
  type: APIReference
  url: https://aeoinspector.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://aeoinspector.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aeoinspector.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeoinspector.com/privacy
- group: company
  title: ''
  type: About
  url: https://aeoinspector.com/about
- group: operate
  title: ''
  type: Contact
  url: https://aeoinspector.com/contact
- group: docs
  title: ''
  type: Guides
  url: https://aeoinspector.com/guides
- group: agent
  title: ''
  type: llms.txt
  url: https://aeoinspector.com/llms.txt
- group: agent
  title: ''
  type: MCPServerCard
  url: https://aeoinspector.com/.well-known/mcp/server-card.json
created: '2026-10-31'
description: AEO Inspector, operated by Orion CMD LLC in Omaha, Nebraska, provides a free AI-driven AEO grading service that evaluates how well AI crawlers and agents can read, understand, and cite a website. The platform offers automated checks of robots.txt, metadata, structured data, and content without JavaScript, delivering a score out of 100 and actionable fixes. Paid reports give deeper insights across multiple AI engines. The service is accessible without signup and includes an API and MCP server for integration.
image: https://aeoinspector.com/og.png
layout: provider
modified: '2026-10-31'
name: AEO Inspector
nav: Providers
network: true
overview: 'AEO Inspector publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api API, and 1 more. Tagged areas include AI crawler optimization, Answer Engine Optimization, SEO, Agent‑Ready Checks, and Structured Data.


  The AEO Inspector catalog on APIs.io includes 1 Spectral governance ruleset.


  AEO Inspector''s developer surface includes API reference, pricing, and 17 more developer resources.'
plans:
- name: Aeoinspector Com Plans Pricing
  plan_count: 5
  slug: aeoinspector-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Aeoinspector Com Rate Limits
  slug: aeoinspector-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AEO Inspector API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: aeoinspector-com-rules
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 44.1
    developer_ergonomics: 3.6
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 34.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aeoinspector Com Domain Security
  slug: aeoinspector-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aeoinspector-com
tags:
- AI crawler optimization
- Answer Engine Optimization
- SEO
- Agent‑Ready Checks
- Structured Data
website: https://aeoinspector.com/
---
