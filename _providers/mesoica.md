---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mesoica.com/
- group: other
  href: https://artifacts.apis.io/mesoica/hosts/mesoica-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mesoica-hosts.yml
- group: other
  href: https://artifacts.apis.io/mesoica/vendors/mesoica-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mesoica-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mesoica/security/mesoica-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mesoica-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mesoica/security/mesoica-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mesoica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mesoica.com/
- group: company
  title: ''
  type: Blog
  url: https://mesoica.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mesoica.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://mesoica.com/security
- group: operate
  title: ''
  type: ContactUs
  url: https://mesoica.com/contact-us
coverage:
  checked: '2026-10-21'
  detail: The provider's website returns HTML but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://mesoica.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Mesoica provides AI‑powered fund data operations, automating the extraction, validation, and delivery of information from investor portals, data rooms, and documents. Their platform logs every step, offers auditability, and integrates with compliance teams, delivering data to downstream systems within weeks. It serves fund administrators, mid‑office teams, and alternative investment managers, supporting use cases across financial markets, real‑estate, ESG, and AIFMD depositary services.
layout: provider
modified: '2026-10-21'
name: Mesoica
nav: Providers
network: true
overview: 'Mesoica is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Fund-Data, Automation, Compliance, and Financial-Services.


  Mesoica''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mesoica Domain Security
  slug: mesoica-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Mesoica Trust Center
  slug: mesoica-trust-center
  summary_line: ISO 27001, GDPR
slug: mesoica
tags:
- AI
- Fund-Data
- Automation
- Compliance
- Financial-Services
website: https://mesoica.com/
---
