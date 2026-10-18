---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Breakr Agentic Access
  operation_count: 1
  slug: breakr-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: BREAKr API providing creator ecosystem payment and management endpoints.
  name: Breakr API
  slug: breakr-api
artifact_total: 5
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breakr/refs/heads/main/agentic-access/breakr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/breakr-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/breakr/refs/heads/main/rules/breakr-rules.yml
  title: ''
  type: Spectral
  url: rules/breakr-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/breakr/refs/heads/main/conformance/breakr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/breakr-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breakr/refs/heads/main/hosts/breakr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breakr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breakr/refs/heads/main/vendors/breakr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breakr-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breakr/refs/heads/main/authentication/breakr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/breakr-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breakr/refs/heads/main/security/breakr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breakr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.breakr.app
- group: operate
  title: ''
  type: Contact
  url: https://www.breakr.app/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breakr.app/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breakr.app/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://m.breakr.app/register
- group: docs
  title: ''
  type: Documentation
  url: https://www.breakr.app/for/creators
- group: start
  title: ''
  type: GettingStarted
  url: https://www.breakr.app/for/creators
- group: operate
  title: ''
  type: Support
  url: https://www.breakr.app/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/breakr
created: '2026-10-03'
description: Breakr provides an operating system for creator ecosystems, offering tools for campaign management, creator discovery, CRM, payments, escrow, analytics, and AI assistance. The platform enables brands, agencies, and creators to run campaigns, manage finances, and automate workflows, with a focus on secure escrow‑protected payments and AI‑driven insights. It aims to streamline the creator economy by integrating product, payment, and relationship layers into a single ledger.
image: https://www.breakr.app/opengraph-image?cebfa26668b75119
layout: provider
modified: '2026-10-03'
name: Breakr
nav: Providers
network: true
overview: 'Breakr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CreatorEconomy, Fintech, Software-as-a-Service, and Payments.


  The Breakr catalog on APIs.io includes 1 Spectral governance ruleset.


  Breakr''s developer surface includes authentication, signup flow, documentation, getting-started guide, support, and 11 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Breakr API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: breakr-rules
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.2
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 10.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Breakr Authentication
  slug: breakr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Breakr Domain Security
  slug: breakr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: breakr
tags:
- Company
- CreatorEconomy
- Fintech
- Software-as-a-Service
- Payments
website: https://www.breakr.app
---
