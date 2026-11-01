---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Onefootprint Com Webhooks
  slug: onefootprint-com-webhooks
common:
- group: other
  href: https://artifacts.apis.io/onefootprint-com/vendors/onefootprint-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/onefootprint-com-vendors.yml
- group: design
  href: https://artifacts.apis.io/onefootprint-com/asyncapi/onefootprint-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/onefootprint-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/onefootprint-com/conventions/onefootprint-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/onefootprint-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/onefootprint-com/conventions/onefootprint-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/onefootprint-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/onefootprint-com/sandbox/onefootprint-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/onefootprint-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/onefootprint-com/authentication/onefootprint-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onefootprint-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/onefootprint-com/llms/onefootprint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onefootprint-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/onefootprint-com/well-known/onefootprint-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onefootprint-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/onefootprint-com/hosts/onefootprint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/onefootprint-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onefootprint.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.onefootprint.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onefootprint.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://dashboard.onefootprint.com/authentication/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onefootprint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.onefootprint.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onefootprint
- group: auth
  href: https://artifacts.apis.io/onefootprint-com/security/onefootprint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onefootprint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://onefootprint.com
coverage:
  checked: '2026-10-26'
  detail: The homepage is a JavaScript‑rendered site with no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://onefootprint.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Footprint provides an AI-powered operating system that helps organizations assess, monitor, and mitigate risk across environmental, social, and governance dimensions. Leveraging advanced data integration and analytics, the platform offers real-time insights, scenario modeling, and automated reporting to drive sustainable decision‑making and compliance. Founded with a mission to make risk management proactive and transparent, Footprint serves enterprises seeking to embed responsible practices into its core strategies.
image: https://framerusercontent.com/assets/dTqiC2XcwfU5H995obGjZL9EQ.png
layout: provider
modified: '2026-10-25'
name: Footprint
nav: Providers
network: true
overview: 'Footprint is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Risk Management, ESG, and Sustainability.


  The Footprint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Footprint''s developer surface includes sandbox, authentication, documentation, API reference, and 14 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 28.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Onefootprint Com Authentication
  slug: onefootprint-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Onefootprint Com Domain Security
  slug: onefootprint-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: onefootprint-com
tags:
- Company
- AI
- Risk Management
- ESG
- Sustainability
website: http://onefootprint.com
---
