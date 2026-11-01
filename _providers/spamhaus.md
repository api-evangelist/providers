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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Spamhaus provides blocklist lookup services; API details are not publicly documented.
  name: Spamhaus API
  slug: spamhaus-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/spamhaus/well-known/spamhaus-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/spamhaus-security.txt
- group: agent
  href: https://artifacts.apis.io/spamhaus/well-known/spamhaus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spamhaus-well-known.yml
- group: other
  href: https://artifacts.apis.io/spamhaus/hosts/spamhaus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spamhaus-hosts.yml
- group: other
  href: https://artifacts.apis.io/spamhaus/vendors/spamhaus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spamhaus-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spamhaus.org/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spamhaus.org/privacy-notice/
- group: auth
  href: https://artifacts.apis.io/spamhaus/security/spamhaus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spamhaus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spamhaus.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.spamhaus.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.spamhaus.org/resource-hub/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.spamhaus.org/about-the-research/
- group: operate
  title: ''
  type: Support
  url: https://www.spamhaus.org/faqs/
- group: company
  title: ''
  type: Blog
  url: https://www.spamhaus.org/events/
created: '2026-10-28'
description: Spamhaus is an international non‑profit organization that tracks email spam and related cyber‑threats. It operates globally recognized blocklists such as the DNSBL, provides reputation data, and offers tools and services to help ISPs, email providers, and security teams protect their networks from spam, phishing, and malware. Through its research and data services, Spamhaus strengthens trust and safety across the internet.
layout: provider
modified: '2026-10-28'
name: Spamhaus
nav: Providers
network: true
overview: 'Spamhaus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Anti-Spam, Reputation, and DNSBL.


  Spamhaus'' developer surface includes documentation, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 53.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Spamhaus Domain Security
  slug: spamhaus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spamhaus
tags:
- Company
- Security
- Anti-Spam
- Reputation
- DNSBL
website: https://spamhaus.org/
---
