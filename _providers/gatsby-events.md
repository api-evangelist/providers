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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Gatsby Events Webhooks
  slug: gatsby-events-webhooks
common:
- group: design
  href: https://artifacts.apis.io/gatsby-events/asyncapi/gatsby-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gatsby-events-webhooks.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.gatsby.events/
- group: design
  href: https://artifacts.apis.io/gatsby-events/conformance/gatsby-events-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gatsby-events-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gatsby-events/llms/gatsby-events-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gatsby-events-llms.txt
- group: agent
  href: https://artifacts.apis.io/gatsby-events/well-known/gatsby-events-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gatsby-events-well-known.yml
- group: other
  href: https://artifacts.apis.io/gatsby-events/hosts/gatsby-events-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gatsby-events-hosts.yml
- group: other
  href: https://artifacts.apis.io/gatsby-events/vendors/gatsby-events-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gatsby-events-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gatsby.events/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gatsby.events/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://gatsby.events/pricing/
- group: start
  title: ''
  type: Login
  url: https://gatsby.events/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gatsbylabs
- group: docs
  title: ''
  type: APIReference
  url: https://help.gatsby.events/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.gatsby.events/reference/getting-started/creating-and-managing-events
- group: docs
  title: ''
  type: Documentation
  url: https://help.gatsby.events/
- group: auth
  href: https://artifacts.apis.io/gatsby-events/security/gatsby-events-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gatsby-events-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gatsby-events/security/gatsby-events-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gatsby-events-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gatsby.events
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://gatsby.events
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Gatsby Events provides an event management platform for professional gatherings, combining CRM capabilities with tools for invitations, RSVP, seating charts, check‑in, and on‑site badge printing. It supports corporate events, AGMs, and galas, offering branded pages, guest profiles, and integrations that sync to your existing CRM, all delivered via a web‑based SaaS solution.
layout: provider
modified: '2026-10-21'
name: Gatsby
nav: Providers
network: true
overview: 'Gatsby is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Event Management, CRM Integration, Guest List Management, Invitation Email, and Security.


  The Gatsby catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gatsby''s developer surface includes pricing, API reference, getting-started guide, documentation, and 14 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 13.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gatsby Events Domain Security
  slug: gatsby-events-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gatsby Events Trust Center
  slug: gatsby-events-trust-center
  summary_line: SOC 2
slug: gatsby-events
tags:
- Event Management
- CRM Integration
- Guest List Management
- Invitation Email
- Security
website: https://gatsby.events
---
