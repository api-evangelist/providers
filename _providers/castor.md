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
  title: ''
  type: Security
  url: https://www.castoredc.com/responsible-disclosure-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/castor/refs/heads/main/llms/castor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/castor-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/castor/refs/heads/main/well-known/castor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/castor-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/castor/refs/heads/main/well-known/castor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/castor-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castor/refs/heads/main/hosts/castor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/castor-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/castor/refs/heads/main/vendors/castor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/castor-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.castoredc.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.castoredc.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.castoredc.com/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.castoredc.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.castoredc.com/about-us/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.castoredc.com/resources/blog/?_gl=1*g3lqof*_gcl_aw*R0NMLjE3NDU4MjczNjUuQ2owS0NRandxODZ3QmhEaUFSSXNBSmh1cGhrWkppVlNrLXU5Q1lsUUlrMWY0ajQ0WU5RODdvQ2V1RzRueTZGWWwzWE9xVzZsVGVWdWgyd2FBbzA4RUFMd193Y0I.*_gcl_au*MTI3NjMyMTQ3LjE3NDcwMzU1NTAuMTMwMDk4MTk3OC4xNzQ3MDU4NTk5LjE3NDcwNTkyMTU.
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/castoredc
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/castor/refs/heads/main/security/castor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/castor-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/castor/refs/heads/main/security/castor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/castor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.castoredc.com/
created: '2026-10-07'
description: Castor is an AI‑native clinical trial platform that provides an electronic data capture (EDC) system, eCOA/ePRO, eConsent, and data management tools. Their API enables secure OAuth2‑based access to study data, participants, and metadata, helping biopharma, CROs, and academic researchers accelerate clinical research with automated data extraction and compliance features.
image: https://www.castoredc.com/wp-content/uploads/2022/06/home-social2-1024x538.jpeg
layout: provider
modified: '2026-10-07'
name: Castor
nav: Providers
network: true
overview: 'Castor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Clinical Trials, Data Management, Artificial Intelligence, and EDC.


  Castor''s developer surface includes pricing, engineering blog, and 14 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Castor Domain Security
  slug: castor-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Castor Vulnerability Disclosure
  slug: castor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: castor
tags:
- Health
- Clinical Trials
- Data Management
- Artificial Intelligence
- EDC
website: https://www.castoredc.com/
---
