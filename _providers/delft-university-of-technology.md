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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.tudelft.nl/en/responsible-disclosure-of-vulnerabilities
- group: auth
  href: https://artifacts.apis.io/delft-university-of-technology/well-known/delft-university-of-technology-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/delft-university-of-technology-security.txt
- group: agent
  href: https://artifacts.apis.io/delft-university-of-technology/well-known/delft-university-of-technology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/delft-university-of-technology-well-known.yml
- group: other
  href: https://artifacts.apis.io/delft-university-of-technology/hosts/delft-university-of-technology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/delft-university-of-technology-hosts.yml
- group: other
  href: https://artifacts.apis.io/delft-university-of-technology/vendors/delft-university-of-technology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/delft-university-of-technology-vendors.yml
- group: build
  href: https://artifacts.apis.io/delft-university-of-technology/packages/delft-university-of-technology-packages.yml
  title: ''
  type: SDKs
  url: packages/delft-university-of-technology-packages.yml
- group: build
  href: https://artifacts.apis.io/delft-university-of-technology/packages/delft-university-of-technology-packages.yml
  title: ''
  type: Packages
  url: packages/delft-university-of-technology-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tudelft.nl/privacy-security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tudelft
- group: auth
  href: https://artifacts.apis.io/delft-university-of-technology/security/delft-university-of-technology-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/delft-university-of-technology-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/delft-university-of-technology/security/delft-university-of-technology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delft-university-of-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tudelft.nl
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.tudelft.nl
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Delft University of Technology (TU Delft) is a leading Dutch public technical university, renowned for engineering and technology research and education. It offers a wide range of degree programmes, conducts cutting‑edge research, collaborates with industry, and provides various digital services and data APIs for students, staff, and partners.
image: https://t.e7096c671.entry.domains/3csTG3domaR6atrqDQ83MfnFGbc=/fit-in/640x361/filters:strip_exif()/https%3A%2F%2Ffilelist.tudelft.nl%2FTUDelft%2FHomepage%2FEvents%2FEvents%2520vlam%2520uitsnedes%2FCutout-02-1.png%3Fhash%3De56d09be2c
layout: provider
modified: '2026-10-26'
name: Delft University of Technology
nav: Providers
network: true
overview: Delft University of Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Research, Engineering, Netherlands, and University.
random_paper: 9
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Delft University Of Technology Domain Security
  slug: delft-university-of-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Delft University Of Technology Vulnerability Disclosure
  slug: delft-university-of-technology-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: delft-university-of-technology
tags:
- Education
- Research
- Engineering
- Netherlands
- University
website: https://www.tudelft.nl
---
