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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/branchintl/refs/heads/main/well-known/branchintl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/branchintl-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branchintl/refs/heads/main/hosts/branchintl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branchintl-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branchintl/refs/heads/main/vendors/branchintl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branchintl-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://branch.co/security
- group: company
  title: ''
  type: Newsroom
  url: https://branch.co/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branchintl/refs/heads/main/security/branchintl-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/branchintl-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branchintl/refs/heads/main/security/branchintl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branchintl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://branch.co
- group: docs
  title: ''
  type: Documentation
  url: https://branch.co/about
- group: start
  title: ''
  type: DeveloperPortal
  url: https://branch.co/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://branch.co/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://branch.co/legal/privacy-policies
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the API host.
  evidence:
  - status: 404
    url: https://api.branch.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Branch International (Branchintl) is a fintech company providing mobile‑first financial services and credit to consumers in emerging markets across Africa and India. Leveraging data science and machine learning, Branch assesses creditworthiness via smartphones, offering loans, savings, and other financial products to the mobile generation, aiming to increase financial inclusion and empower users to build capital and improve their economic wellbeing.
layout: provider
modified: '2026-10-03'
name: Branchintl
nav: Providers
network: true
overview: 'Branchintl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Mobile, Credit, Emerging Markets, and Africa.


  Branchintl''s developer surface includes documentation and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Branchintl Domain Security
  slug: branchintl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Branchintl Vulnerability Disclosure
  slug: branchintl-vulnerability-disclosure
  summary_line: disclosure policy published
slug: branchintl
tags:
- Fintech
- Mobile
- Credit
- Emerging Markets
- Africa
- India
website: https://branch.co
---
