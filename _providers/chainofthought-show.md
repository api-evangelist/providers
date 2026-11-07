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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for the Chain of Thought podcast platform, providing endpoints for episodes, topics, and agent integrations.
  name: Chain of Thought API
  slug: chain-of-thought-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/chainofthought-show/conformance/chainofthought-show-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chainofthought-show-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chainofthought-show/llms/chainofthought-show-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chainofthought-show-llms.txt
- group: other
  href: https://artifacts.apis.io/chainofthought-show/hosts/chainofthought-show-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chainofthought-show-hosts.yml
- group: other
  href: https://artifacts.apis.io/chainofthought-show/vendors/chainofthought-show-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chainofthought-show-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://newsletter.chainofthought.show/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://newsletter.chainofthought.show/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://chainofthought.show/guides/
- group: operate
  title: ''
  type: ChangeLog
  url: https://chainofthought.show/changelog/
- group: auth
  href: https://artifacts.apis.io/chainofthought-show/security/chainofthought-show-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chainofthought-show-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chainofthought.show/
- group: company
  title: ''
  type: About
  url: https://chainofthought.show/about/
- group: other
  title: ''
  type: RSS
  url: https://chainofthought.show/rss.xml
coverage:
  checked: '2026-11-03'
  detail: The provider's documentation pages are public HTML but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://chainofthought.show/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Chain of Thought is a podcast exploring AI infrastructure, featuring hosts and guests from leading tech companies. It discusses evolving AI tools, platforms, and research, providing insights for builders and enthusiasts. The show covers topics like hardware, software, and industry trends, aiming to inform and inspire the AI community.
image: https://chainofthought.show/favicon.ico
layout: provider
modified: '2026-11-03'
name: Chain of Thought
nav: Providers
network: true
overview: 'Chain of Thought is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Podcasts, Artificial Intelligence, Infrastructure, Technology, and Community.


  Chain of Thought''s developer surface includes documentation, changelog, and 10 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chainofthought Show Domain Security
  slug: chainofthought-show-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chainofthought-show
tags:
- Podcasts
- Artificial Intelligence
- Infrastructure
- Technology
- Community
website: https://chainofthought.show/
---
