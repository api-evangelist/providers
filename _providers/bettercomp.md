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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Compensation platform API (no public spec discovered)
  name: BetterComp API
  slug: bettercomp-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bettercomp/refs/heads/main/conformance/bettercomp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bettercomp-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bettercomp/refs/heads/main/llms/bettercomp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bettercomp-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bettercomp/refs/heads/main/hosts/bettercomp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bettercomp-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.bettercomp.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bettercomp.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bettercomp.com/blog/pricing-unique-and-emerging-jobs/
- group: company
  title: ''
  type: Blog
  url: https://www.bettercomp.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bettercomp.com/guide/ai-quick-start-guide/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BetterComp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bettercomp/refs/heads/main/security/bettercomp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bettercomp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bettercomp.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bettercomp/refs/heads/main/security/bettercomp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bettercomp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bettercomp.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://api.bettercomp.com/mcp
  - status: 403
    url: https://app.bettercomp.com/mcp
  - status: 403
    url: https://status.bettercomp.com/mcp
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: BetterComp provides a modern compensation platform that leverages AI and data integration to help companies price jobs, manage compensation structures, and make data‑driven pay decisions. The solution unifies HRIS data, market surveys, and internal pay logic, offering tools for range modeling, market pricing, reporting, and AI‑assisted decision making, aimed at improving speed, fairness, and strategic impact of compensation across organizations.
image: https://www.bettercomp.com/wp-content/uploads/2026/02/51f265ba727c8b32740c5ebd2c65093c0672d6a9-1200x630-1.webp
layout: provider
modified: '2026-09-28'
name: BetterComp
nav: Providers
network: true
overview: 'BetterComp publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Compensation, Human Resources, Artificial Intelligence, Software-as-a-Service, and Enterprise.


  BetterComp''s developer surface includes support, pricing, engineering blog, getting-started guide, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 20.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bettercomp Domain Security
  slug: bettercomp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bettercomp
tags:
- Compensation
- Human Resources
- Artificial Intelligence
- Software-as-a-Service
- Enterprise
website: https://www.bettercomp.com/
---
