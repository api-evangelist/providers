---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Embedded Public V1 API for ByteChef
  name: Embedded Public V1 API
  slug: embedded-public-v1-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bytechef/plans/bytechef-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bytechef-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bytechef/vocabulary/bytechef-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bytechef-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/bytechef/authentication/bytechef-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bytechef-authentication.yml
- group: design
  href: https://artifacts.apis.io/bytechef/conformance/bytechef-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bytechef-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bytechef/llms/bytechef-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bytechef-llms.txt
- group: agent
  href: https://artifacts.apis.io/bytechef/well-known/bytechef-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bytechef-well-known.yml
- group: other
  href: https://artifacts.apis.io/bytechef/hosts/bytechef-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bytechef-hosts.yml
- group: other
  href: https://artifacts.apis.io/bytechef/vendors/bytechef-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bytechef-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.bytechef.io/integrations/webhook
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bytechef.io/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bytechef.io/reference/components/google-application-setup_v1
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bytechef.io/reference
- group: auth
  href: https://artifacts.apis.io/bytechef/security/bytechef-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bytechef-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bytechef.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bytechef.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bytechef.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bytechef.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.bytechef.io/register
- group: start
  title: ''
  type: Login
  url: https://app.bytechef.io/login
- group: company
  title: ''
  type: Blog
  url: https://blog.bytechef.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bytechefhq
- group: operate
  title: ''
  type: Support
  url: https://www.bytechef.io/contact
created: '2026-10-16'
description: ByteChef provides an open-source workflow automation platform powered by AI agents. It enables users to create multi-step workflows that integrate SaaS tools, databases, and internal systems without vendor lock‑in. The platform offers a BETA version with embedded and enterprise options, flexible pricing, and a focus on data ownership and visibility. Users can build, deploy, and scale intelligent automations across their organization, leveraging a rich library of integrations and AI capabilities.
image: https://www.bytechef.io/bytechef-cover-image.png
layout: provider
modified: '2026-10-16'
name: ByteChef
nav: Providers
network: true
overview: 'ByteChef is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Artificial Intelligence, Open Source, Workflows, and Integration.


  ByteChef''s developer surface includes authentication, changelog, getting-started guide, API reference, documentation, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Bytechef Plans Pricing
  plan_count: 6
  slug: bytechef-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 50.3
    catalog_earned_first_party: 12.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 43.4
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 73.2
    operational_transparency: 14.5
  previous_composite: 34.6
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bytechef/bytechef-2026-11-03T122859.png
security:
- kind: authentication
  name: Bytechef Authentication
  slug: bytechef-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bytechef Domain Security
  slug: bytechef-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bytechef
tags:
- Automation
- Artificial Intelligence
- Open Source
- Workflows
- Integration
- Company
website: https://bytechef.io/
---
