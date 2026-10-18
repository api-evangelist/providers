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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Embedded Public V1 API for ByteChef
  name: Embedded Public V1 API
  slug: embedded-public-v1-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bytechef/refs/heads/main/plans/bytechef-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bytechef-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bytechef/refs/heads/main/vocabulary/bytechef-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bytechef-vocabulary.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bytechef/refs/heads/main/authentication/bytechef-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bytechef-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bytechef/refs/heads/main/conformance/bytechef-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bytechef-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bytechef/refs/heads/main/llms/bytechef-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bytechef-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bytechef/refs/heads/main/well-known/bytechef-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bytechef-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bytechef/refs/heads/main/hosts/bytechef-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bytechef-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bytechef/refs/heads/main/vendors/bytechef-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/bytechef/refs/heads/main/security/bytechef-domain-security.yml
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
random_paper: 6
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 50.3
    catalog_earned_first_party: 12.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 73.2
    operational_transparency: 28.9
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
