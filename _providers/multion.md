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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for MultiOn platform providing AI agent tools and authentication.
  name: MultiOn API
  slug: multion-api
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/multion/refs/heads/main/vendors/multion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/multion-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/multion/refs/heads/main/authentication/multion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/multion-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/multion/refs/heads/main/conformance/multion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/multion-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/multion/refs/heads/main/llms/multion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/multion-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/multion/refs/heads/main/well-known/multion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/multion-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/multion/refs/heads/main/hosts/multion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/multion-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://theagi.company/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://theagi.company/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.theagi.company/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.multion.ai/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.multion.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.multion.ai/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/multion/refs/heads/main/security/multion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/multion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.multion.ai
created: '2026-10-13'
description: MultiOn is a technology company focused on providing advanced AI-driven automation solutions for enterprise workflows. It offers a platform that integrates private action AI agents into phone and device interfaces, enabling hands-free task execution, intelligent assistance, and customizable automation. The company emphasizes privacy, security, and high task success rates, targeting businesses seeking to streamline operations through AI-powered agents.
image: https://framerusercontent.com/images/lp8JHZU8ZNH9UTmwKrJIGDIBQQ.png
layout: provider
modified: '2026-10-13'
name: MultiOn
nav: Providers
network: true
overview: 'MultiOn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Enterprise, and Platform.


  MultiOn''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 21.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Multion Authentication
  slug: multion-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Multion Domain Security
  slug: multion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: multion
tags:
- Company
- Artificial Intelligence
- Automation
- Enterprise
- Platform
website: https://www.multion.ai
---
