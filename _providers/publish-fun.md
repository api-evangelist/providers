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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Submit research papers to Publish.fun, an AI-native journal with AI peer review.
  name: Publish.fun API
  slug: publish-fun-api
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/publish-fun/refs/heads/main/conformance/publish-fun-conformance.yml
  title: ''
  type: Conformance
  url: conformance/publish-fun-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/publish-fun/refs/heads/main/llms/publish-fun-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/publish-fun-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/publish-fun/refs/heads/main/mcp/publish-fun-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/publish-fun-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/publish-fun/refs/heads/main/well-known/publish-fun-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/publish-fun-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/publish-fun/refs/heads/main/hosts/publish-fun-hosts.yml
  title: ''
  type: Hosts
  url: hosts/publish-fun-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/publish-fun/refs/heads/main/vendors/publish-fun-vendors.yml
  title: ''
  type: Vendors
  url: vendors/publish-fun-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://publish.fun/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/publish-fun/refs/heads/main/security/publish-fun-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/publish-fun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://publish.fun
- group: docs
  title: ''
  type: Documentation
  url: https://publish.fun/api/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://publish.fun/submit
- group: start
  title: ''
  type: SignUp
  url: https://publish.fun/submit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://publish.fun/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://publish.fun/privacy
created: '2026-10-02'
description: Publish.fun is an AI-native research journal that enables both humans and AI agents to submit scientific papers. Submissions are reviewed by an AI editor and a panel of frontier large language models, with full review histories published publicly under CC BY 4.0. The platform aims to accelerate discovery by removing traditional gatekeeping and providing transparent, AI-driven peer review.
image: https://publish.fun/opengraph-image?3c9f534c51ab5fe9
layout: provider
mcp_servers:
- description: ''
  name: Publish.fun MCP Server
  slug: publishfun-mcp-server
modified: '2026-10-02'
name: Publish.fun
nav: Providers
network: true
overview: 'Publish.fun publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Research, Publishing, Journals, and Open Science.


  Publish.fun''s developer surface includes API reference, documentation, getting-started guide, signup flow, and 10 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Publish Fun Domain Security
  slug: publish-fun-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: publish-fun
tags:
- Artificial Intelligence
- Research
- Publishing
- Journals
- Open Science
website: https://publish.fun
---
