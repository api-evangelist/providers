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
    event_surface_described: false
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
  score: 15.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Email and phone validation API.
  name: ContactLint API
  slug: contactlint-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/contactlint-com/security/contactlint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contactlint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contactlint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://contactlint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://contactlint.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://contactlint.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://contactlint.com/
- group: start
  title: ''
  type: SignUp
  url: https://contactlint.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contactlint.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contactlint.com/privacy
created: '2026-10-30'
description: ContactLint offers a hosted HTTP API and remote MCP server that validates email addresses and phone numbers. It checks syntax, DNS MX records, disposable domains, role addresses, and common typos for emails, and parses and formats phone numbers. The service provides a free tier of 100 checks per month and paid plans starting at $9 for 5,000 checks. It includes batch validation, widget integration for signup forms, and detailed usage reporting. Designed for developers and AI agents, ContactLint aims to improve data quality and reduce bounce rates.
image: https://contactlint.com/apple-touch-icon.png
layout: provider
modified: '2026-10-30'
name: contactlint-com
nav: Providers
network: true
overview: 'contactlint-com is listed with 1 API on the [APIs.io](https://apis.io/) network: ContactLint API. Tagged areas include Company, Email Validation, Phone Validation, API, and MCP.


  contactlint-com''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, and 4 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 33.7
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 0.0
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
  name: Contactlint Com Domain Security
  slug: contactlint-com-domain-security
  summary_line: TLSv1.3
slug: contactlint-com
tags:
- Company
- Email Validation
- Phone Validation
- API
- MCP
website: https://contactlint.com/
---
