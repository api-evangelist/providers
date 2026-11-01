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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.cobalt.io/solutions/compliance
- group: auth
  href: https://artifacts.apis.io/cobalt-io/authentication/cobalt-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cobalt-io-authentication.yml
- group: agent
  href: https://artifacts.apis.io/cobalt-io/llms/cobalt-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cobalt-io-llms.txt
- group: other
  href: https://artifacts.apis.io/cobalt-io/hosts/cobalt-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cobalt-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/cobalt-io/vendors/cobalt-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cobalt-io-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cobalt.io/press
- group: other
  title: ''
  type: Leadership
  url: https://www.cobalt.io/team
- group: auth
  href: https://artifacts.apis.io/cobalt-io/security/cobalt-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cobalt-io-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cobalt-io/security/cobalt-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cobalt-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cobalt.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.cobalt.io/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://www.cobalt.io/get-started
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cobalt.io/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cobalt.io/platform/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cobalt.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cobalt.io/privacy-opt-out
- group: company
  title: ''
  type: Blog
  url: https://www.cobalt.io/blog
coverage:
  checked: '2026-10-25'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.cobalt.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Cobalt provides an AI‑powered offensive security platform that delivers continuous penetration testing as a service. Their solution combines human‑led expertise with automated testing, integrating with development workflows to identify and remediate vulnerabilities across web applications, APIs, mobile apps, and cloud environments. Cobalt’s platform offers flexible credit‑based pricing, real‑time reporting, and integrations that help organizations embed security into the software development lifecycle.
image: https://www.cobalt.io/hubfs/cobalt-social-image-1200x630.jpg
layout: provider
modified: '2026-10-25'
name: Cobalt
nav: Providers
network: true
overview: 'Cobalt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, PenetrationTesting, OffensiveSecurity, and SaaS.


  Cobalt''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cobalt Io Authentication
  slug: cobalt-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cobalt Io Domain Security
  slug: cobalt-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Cobalt Io Trust Center
  slug: cobalt-io-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA
slug: cobalt-io
tags:
- Company
- Security
- PenetrationTesting
- OffensiveSecurity
- SaaS
- Platform
website: https://www.cobalt.io
---
