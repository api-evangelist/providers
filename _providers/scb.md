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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scb/refs/heads/main/security/scb-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/scb-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scb/refs/heads/main/well-known/scb-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scb-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scb/refs/heads/main/well-known/scb-scb-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scb-scb-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scb/refs/heads/main/well-known/scb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scb-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scb/refs/heads/main/hosts/scb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scb-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.scb.se/vara-tjanster/bestall-data-och-statistik/register/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scb/refs/heads/main/security/scb-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/scb-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scb/refs/heads/main/security/scb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scb.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.scb.se/en/services/open-data-api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.scb.se/en/api/
coverage:
  checked: '2026-10-15'
  detail: The provider's website offers data download but no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://scb.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: SCB Statistics Sweden is Sweden’s official statistical agency, providing comprehensive data on the country’s demographics, economy, labor market, and more. It offers public access to a wide range of statistical datasets and APIs for developers to integrate official statistics into applications, research, and analysis. The agency ensures high-quality, up-to-date information for policymakers, businesses, and the public.
image: https://www.scb.se/globalassets/bilder/startsidan---puffbilder/bra-format-for-ateranvandning/bostadsomrade_nat93956-fb.jpg
layout: provider
modified: '2026-10-15'
name: SCB Statistics Sweden
nav: Providers
network: true
overview: 'SCB Statistics Sweden is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Statistics, Sweden, Government, and Data.


  SCB Statistics Sweden''s developer surface includes signup flow, documentation, API reference, and 8 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Scb Domain Security
  slug: scb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Scb Vulnerability Disclosure
  slug: scb-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: scb
tags:
- Company
- Statistics
- Sweden
- Government
- Data
website: https://scb.se/
---
