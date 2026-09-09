---
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actym-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.actymthera.com/
- group: company
  title: ''
  type: About
  url: https://www.actymthera.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.actymthera.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.actymthera.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/actym-therapeutics-inc
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/actym-therapeutics-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/actym-therapeutics-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/actym-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/actym-therapeutics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/actym-therapeutics-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/actym-therapeutics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/actym-therapeutics-rate-limits.yml
created: '2026-09-06'
description: Actym Therapeutics is a clinical-stage biotechnology company developing bacterial immunotherapies for solid tumors and fibrotic disease. Its STACT platform engineers an attenuated Salmonella typhimurium vehicle to be administered systemically and to deliver multiple therapeutic payloads that are amplified and produced locally at the disease site, with the goal of raising efficacy while limiting systemic toxicity. Its lead asset, ACTM-838, is in a Phase 1a/1b trial in patients with advanced solid tumors. Actym publishes no developer program, no API and no machine-readable contract; the only agent-facing surfaces on its own domain are a platform-generated llms.txt and an anonymous Wix Site MCP endpoint.
image: https://static.wixstatic.com/media/6cf7e0_57b74df73b9347cebd4f77f40a6f71e1%7Emv2.png/v1/fit/w_2500,h_1330,al_c/6cf7e0_57b74df73b9347cebd4f77f40a6f71e1%7Emv2.png
layout: provider
mcp_servers:
- description: ''
  name: Actym Therapeutics Site MCP Server
  slug: actym-therapeutics-site-mcp-server
modified: '2026-09-06'
name: Actym Therapeutics
nav: Providers
network: true
overview: 'Actym Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Immuno-Oncology.


  Actym Therapeutics'' developer surface includes support, authentication, and 11 more developer resources.'
plans:
- name: Actym Therapeutics Plans Pricing
  plan_count: 0
  slug: actym-therapeutics-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Actym Therapeutics Rate Limits
  slug: actym-therapeutics-rate-limits
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Actym Therapeutics Authentication
  slug: actym-therapeutics-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Actym Therapeutics Domain Security
  slug: actym-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: actym-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Immuno-Oncology
- Cancer
- Clinical Trials
- Drug Development
- Healthcare
- MCP
website: https://www.actymthera.com/
---
