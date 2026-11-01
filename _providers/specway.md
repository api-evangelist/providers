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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Specway provides a platform to import OpenAPI specs and generate interactive documentation, branding, and analytics.
  name: Specway API
  slug: specway-api
artifact_total: 4
asyncapis:
- description: ''
  name: Specway Webhooks
  slug: specway-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/specway/plans/specway-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/specway-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/specway/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/specway/asyncapi/specway-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/specway-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/specway/llms/specway-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/specway-llms.txt
- group: agent
  href: https://artifacts.apis.io/specway/well-known/specway-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/specway-well-known.yml
- group: other
  href: https://artifacts.apis.io/specway/hosts/specway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/specway-hosts.yml
- group: other
  href: https://artifacts.apis.io/specway/vendors/specway-vendors.yml
  title: ''
  type: Vendors
  url: vendors/specway-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://specway.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://specway.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://specway.com/apis/categories/media
- group: docs
  title: ''
  type: Documentation
  url: https://specway.com/resources/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://specway.com/resources/guides/getting-started
- group: auth
  href: https://artifacts.apis.io/specway/security/specway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/specway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://specway.com/
- group: company
  title: ''
  type: Blog
  url: https://specway.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://specway.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://specway.com/signup
- group: operate
  title: ''
  type: Support
  url: https://specway.com/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/specway
coverage:
  checked: '2026-10-19'
  detail: Specway's documentation provides guides but no publicly accessible OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://specway.com/resources/guides/getting-started
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Specway provides an API documentation platform that lets developers and AI agents publish interactive docs, generate MCP servers, and serve llms.txt. It supports automatic updates when specs change, offers AI‑assisted chat, code samples, analytics, and integrates with many services like Stripe, PayPal, Twilio, GitHub, Slack, and more. Users can sign up, explore pricing, read the blog, and get started quickly with comprehensive guides and examples.
image: https://specway.com/api/og?title=Specway&description=Paste+an+OpenAPI+spec+and+get+interactive+docs%2C+an+MCP+server+and+llms.txt+in+about+a+minute.+Auto-sync%2C+breaking-change+detection%2C+playground%2C+analytics+and+custom+branding.
layout: provider
modified: '2026-10-18'
name: Specway
nav: Providers
network: true
overview: 'Specway is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Documentation, Developer Tools, AI Integration, Interactive Docs, and OpenAPI.


  The Specway catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Specway''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, and 13 more developer resources.'
plans:
- name: Specway Plans Pricing
  plan_count: 4
  slug: specway-plans-pricing
random_paper: 20
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 35.0
    discoverability: 58.9
    operational_transparency: 13.2
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Specway Domain Security
  slug: specway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: specway
tags:
- API Documentation
- Developer Tools
- AI Integration
- Interactive Docs
- OpenAPI
website: https://specway.com/
---
