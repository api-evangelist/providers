---
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/gocascade-ai/llms/gocascade-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gocascade-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/gocascade-ai/hosts/gocascade-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gocascade-ai-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://gocascade.ai/platform/security/
- group: auth
  href: https://artifacts.apis.io/gocascade-ai/security/gocascade-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gocascade-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gocascade.ai/
- group: company
  title: ''
  type: AboutUs
  url: https://gocascade.ai/about-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gocascade.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gocascade.ai/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://gocascade.ai/resources/blog/
- group: operate
  title: ''
  type: Support
  url: https://gocascade.ai/support/
- group: operate
  title: ''
  type: Contact
  url: https://gocascade.ai/contact/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://gocascade.ai/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Cascade AI provides an AI‑native operating layer for IT and HR shared services, enabling enterprises to automate and govern requests across workflows, integrations, and security. The platform offers a Cascade Agent Harness for governed AI, workflow agents, and extensive integrations, targeting CIOs, CHROs, and industry-specific solutions such as healthcare and technology.
image: https://gocascade.ai/wp-content/uploads/2026/04/Generic-Graphic.png
layout: provider
modified: '2026-10-24'
name: Cascade
nav: Providers
network: true
overview: 'Cascade is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Enterprise, HR, IT, and Automation.


  Cascade''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gocascade Ai Domain Security
  slug: gocascade-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gocascade-ai
tags:
- AI
- Enterprise
- HR
- IT
- Automation
- Company
website: https://gocascade.ai/
---
