---
agent_readiness:
  band: agent-aware
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
  score: 6.3
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/thebloomfilter-com/well-known/thebloomfilter-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thebloomfilter-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/thebloomfilter-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/thebloomfilter-com/llms/thebloomfilter-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thebloomfilter-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/thebloomfilter-com/well-known/thebloomfilter-com-bloomfilter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thebloomfilter-com-bloomfilter-security.txt
- group: agent
  href: https://artifacts.apis.io/thebloomfilter-com/well-known/thebloomfilter-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thebloomfilter-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/thebloomfilter-com/hosts/thebloomfilter-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thebloomfilter-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/thebloomfilter-com/vendors/thebloomfilter-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thebloomfilter-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloomfilter.ai/legal/terms-and-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bloomfilter.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloomfilter.ai/legal/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/thebloomfilter-com/security/thebloomfilter-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thebloomfilter-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thebloomfilter.com/
- group: company
  title: ''
  type: About
  url: https://bloomfilter.ai/about/
- group: operate
  title: ''
  type: Contact
  url: https://bloomfilter.ai/contact/
- group: start
  title: ''
  type: GettingStarted
  url: https://bloomfilter.ai/how-it-works/
- group: company
  title: ''
  type: Blog
  url: https://bloomfilter.ai/writing/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on any discovered host, and no documentation host providing API details was identified.
  evidence:
  - status: 404
    url: https://bloomfilter.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Bloomfilter provides a context layer that connects frontier AI models to enterprise workflow systems, enabling organizations to measure, scale, and optimize the value of AI agents. The platform focuses on process intelligence, governance, and regulated software, offering tools for model integration, value tracking, and compliance with standards such as IEC 62304 and DO-178C. Backed by Techstars, Bloomfilter aims to bring frontier efficiency to enterprises across industries.
image: https://bloomfilter.ai/og-default.png
layout: provider
modified: '2026-10-29'
name: Bloomfilter
nav: Providers
network: true
overview: 'Bloomfilter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Enterprise, Workflow, Process-Intelligence, and Context-Layer.


  Bloomfilter''s developer surface includes getting-started guide, engineering blog, and 14 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.7
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
    skills: unknown
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
  name: Thebloomfilter Com Domain Security
  slug: thebloomfilter-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thebloomfilter-com
tags:
- AI
- Enterprise
- Workflow
- Process-Intelligence
- Context-Layer
website: https://thebloomfilter.com/
---
