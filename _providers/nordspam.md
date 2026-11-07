---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides DNSBL lookup capabilities; API access is available on request via the contact page.
  name: NordSpam API
  slug: nordspam-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/nordspam/hosts/nordspam-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nordspam-hosts.yml
- group: other
  href: https://artifacts.apis.io/nordspam/vendors/nordspam-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nordspam-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NordSpam
- group: auth
  href: https://artifacts.apis.io/nordspam/security/nordspam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nordspam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nordspam.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nordspam.com/usage/
- group: operate
  title: ''
  type: Support
  url: https://www.nordspam.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nordspam.com/policy/
coverage:
  checked: '2026-10-28'
  detail: API access requires contacting via the contact page; no public endpoint is disclosed.
  evidence:
  - status: 200
    url: https://www.nordspam.com/usage/
  reason: sales-gate
  state: gated
created: '2026-10-28'
description: The NordSpam Project provides a DNS-based blacklist (DNSBL) service that helps prevent unwanted spam by maintaining reputation databases of domains and IP addresses. Users can query the service via DNS lookups to determine if an IP or domain is listed. The project offers public usage documentation, policy information, and support contact details, aiming to improve email security and reduce spam traffic across the internet.
image: https://www.nordspam.com/shield-logo.png
layout: provider
modified: '2026-10-28'
name: NordSpam
nav: Providers
network: true
overview: 'NordSpam is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spam, DNSBL, Security, and Email.


  NordSpam''s developer surface includes documentation, support, and 6 more developer resources.'
plans:
- name: Nordspam Plans Pricing
  plan_count: 0
  slug: nordspam-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Nordspam Rate Limits
  slug: nordspam-rate-limits
scopes:
- name: Nordspam Scopes
  scope_count: 0
  slug: nordspam-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 12.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nordspam/nordspam-2026-11-03T140302.png
security:
- kind: authentication
  name: Nordspam Authentication
  slug: nordspam-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nordspam Domain Security
  slug: nordspam-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nordspam
tags:
- Company
- Spam
- DNSBL
- Security
- Email
- Reputation
website: https://nordspam.com/
---
