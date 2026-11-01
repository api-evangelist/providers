---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Naifgravity Com Agentic Access
  operation_count: 4
  slug: naifgravity-com-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- baseURL: https://naifgravity.com
  baseurl_source: declared
  description: The X402 API from naifgravity-com — 4 operation(s) for x402.
  name: naifgravity-com X402 API
  slug: naifgravity-com-x402-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/naifgravity-com/agentic-access/naifgravity-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/naifgravity-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/naifgravity-com/rules/naifgravity-com-rules.yml
  title: ''
  type: Spectral
  url: rules/naifgravity-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/naifgravity-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://naifgravity.com/trust
- group: design
  href: https://artifacts.apis.io/naifgravity-com/errors/naifgravity-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/naifgravity-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/naifgravity-com/conformance/naifgravity-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/naifgravity-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/naifgravity-com/llms/naifgravity-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/naifgravity-com-llms.txt
- group: other
  href: https://artifacts.apis.io/naifgravity-com/a2a/naifgravity-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/naifgravity-com-a2a.yml
- group: other
  href: https://artifacts.apis.io/naifgravity-com/hosts/naifgravity-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/naifgravity-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/naifgravity-com/vendors/naifgravity-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/naifgravity-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://naifgravity.com/status
- group: auth
  href: https://artifacts.apis.io/naifgravity-com/security/naifgravity-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/naifgravity-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/naifgravity-com/security/naifgravity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/naifgravity-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://naifgravity.com/
created: '2026-10-30'
description: NAIF Gravity provides technical services for APIs, webhooks, and AI agents, offering diagnostic, repair, and automation solutions. Their platform includes a catalog of services, free tools, and enterprise offerings, with transparent pricing and a focus on evidence‑first troubleshooting. The site hosts documentation, terms, privacy policy, and a trust center, reflecting a comprehensive approach to API lifecycle support.
image: https://naifgravity.com/naif-gravity-logo.png
layout: provider
modified: '2026-10-30'
name: naifgravity-com
nav: Providers
network: true
overview: 'naifgravity-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: X402 API. Tagged areas include Company, API, Webhook, AI, and Technical Services.


  The naifgravity-com catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: naifgravity-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: naifgravity-com-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 49.6
    developer_ergonomics: 1.8
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Naifgravity Com Domain Security
  slug: naifgravity-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Naifgravity Com Trust Center
  slug: naifgravity-com-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 1
skills:
- name: naifgravity-com-validate-normalize-analyze-json
  slug: naifgravity-com-validate-normalize-analyze-json
slug: naifgravity-com
tags:
- Company
- API
- Webhook
- AI
- Technical Services
website: https://naifgravity.com/
---
