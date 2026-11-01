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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: Security
  url: https://www.sonichealthcare.com/privacy-and-security/vulnerability-disclosure-policy/
- group: auth
  href: https://artifacts.apis.io/sonic-healthcare/well-known/sonic-healthcare-sonichealthcare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sonic-healthcare-sonichealthcare-security.txt
- group: auth
  href: https://artifacts.apis.io/sonic-healthcare/well-known/sonic-healthcare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sonic-healthcare-security.txt
- group: agent
  href: https://artifacts.apis.io/sonic-healthcare/well-known/sonic-healthcare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sonic-healthcare-well-known.yml
- group: other
  href: https://artifacts.apis.io/sonic-healthcare/hosts/sonic-healthcare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sonic-healthcare-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://support.sonichealthcare.com/my.logout.php3?errorcode=19
- group: docs
  title: ''
  type: Documentation
  url: https://investors.sonichealthcare.com/FormBuilder/_Resource/_module/T8Ln_c4ibUqyFnnNe9zNRA/docs/Reports/AR/SHL_AnnualReport_2025.pdf
- group: company
  title: ''
  type: Website
  url: https://www.sonichealthcare.com/
- group: auth
  href: https://artifacts.apis.io/sonic-healthcare/security/sonic-healthcare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sonic-healthcare-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sonic-healthcare/security/sonic-healthcare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sonic-healthcare-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sonichealthcare.com/privacy-and-security/privacy-policy/
- group: other
  title: ''
  type: Disclaimer
  url: https://www.sonichealthcare.com/disclaimer/
- group: company
  title: ''
  type: Newsroom
  url: https://www.sonichealthcare.com/about-sonic/news/
- group: operate
  title: ''
  type: Contact
  url: https://www.sonichealthcare.com/contact/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.sonichealthcare.com/
- group: other
  title: ''
  type: Sustainability
  url: https://www.sonichealthcare.com/sustainability/
created: '2026-10-22'
description: 'Sonic Healthcare (ASX: SHL) is an Australian-headquartered healthcare provider and one of the world''s leading operators in laboratory medicine / pathology, radiology and primary care medical services, with operations across Australasia, Europe and North America run under a federated model of local divisions. Its corporate site and investor centre (sonichealthcare.com) publish services, divisions, sustainability reporting, news and ASX announcements; no public developer portal or API documentation was found on its own hosts during this pass.'
image: https://www.sonichealthcare.com/media/4007/sh_primary_2-line_no-tagline_rgb_fulcol.svg
layout: provider
modified: '2026-10-22'
name: Sonic Healthcare
nav: Providers
network: true
overview: 'Sonic Healthcare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Pathology, Laboratory Medicine, and Radiology.


  Sonic Healthcare''s developer surface includes support, documentation, and 14 more developer resources.'
plans:
- name: Sonic Healthcare Plans Pricing
  plan_count: 0
  slug: sonic-healthcare-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Sonic Healthcare Rate Limits
  slug: sonic-healthcare-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 10.5
  previous_composite: 11.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sonic Healthcare Domain Security
  slug: sonic-healthcare-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sonic Healthcare Vulnerability Disclosure
  slug: sonic-healthcare-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: sonic-healthcare
tags:
- Company
- Healthcare
- Pathology
- Laboratory Medicine
- Radiology
- Primary Care
- Diagnostics
- Australia
website: https://www.sonichealthcare.com/
---
