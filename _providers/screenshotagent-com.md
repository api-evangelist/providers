---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Programmatic access to create and manage screenshot capture projects, retrieve embed URLs, and manage API tokens.
  name: ScreenshotAgent API
  slug: screenshotagent-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/screenshotagent-com/plans/screenshotagent-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/screenshotagent-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/screenshotagent-com/llms/screenshotagent-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/screenshotagent-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/screenshotagent-com/well-known/screenshotagent-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/screenshotagent-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/screenshotagent-com/hosts/screenshotagent-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/screenshotagent-com-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://screenshotagent.com/changelog
- group: auth
  href: https://artifacts.apis.io/screenshotagent-com/security/screenshotagent-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/screenshotagent-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://screenshotagent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://screenshotagent.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://screenshotagent.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://screenshotagent.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://screenshotagent.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://screenshotagent.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://screenshotagent.com/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bikker
coverage:
  checked: '2026-10-31'
  detail: Documentation is publicly readable but no OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://screenshotagent.com/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: ScreenshotAgent provides automated screenshot capture and updating for help center, documentation, and marketing pages. It retakes UI screenshots whenever the interface changes, ensuring that product screenshots stay current across Zendesk, Intercom, and other platforms. The service supports scheduled captures, on‑demand updates, and visual annotations, helping teams maintain accurate visual assets without manual effort.
image: https://screenshotagent.com/s/006f8b82-f173-4a70-b0f2-fa0de7e6da16.png?v=8
layout: provider
modified: '2026-10-31'
name: screenshotagent-com
nav: Providers
network: true
overview: 'screenshotagent-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Screenshot, Automation, UI, Documentation, and Productivity.


  screenshotagent-com''s developer surface includes changelog, documentation, API reference, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Screenshotagent Com Plans Pricing
  plan_count: 4
  slug: screenshotagent-com-plans-pricing
random_paper: 9
scopes:
- name: Screenshotagent Com Scopes
  scope_count: 0
  slug: screenshotagent-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Screenshotagent Com Authentication
  slug: screenshotagent-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Screenshotagent Com Domain Security
  slug: screenshotagent-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: screenshotagent-com
tags:
- Screenshot
- Automation
- UI
- Documentation
- Productivity
website: https://screenshotagent.com/
---
