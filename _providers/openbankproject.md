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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API platform for open banking, providing sandbox and compliance tools.
  name: Open Bank Project API
  slug: open-bank-project-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/openbankproject/conformance/openbankproject-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openbankproject-conformance.yml
- group: agent
  href: https://artifacts.apis.io/openbankproject/well-known/openbankproject-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openbankproject-well-known.yml
- group: other
  href: https://artifacts.apis.io/openbankproject/hosts/openbankproject-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openbankproject-hosts.yml
- group: build
  href: https://artifacts.apis.io/openbankproject/packages/openbankproject-packages.yml
  title: ''
  type: SDKs
  url: packages/openbankproject-packages.yml
- group: build
  href: https://artifacts.apis.io/openbankproject/packages/openbankproject-packages.yml
  title: ''
  type: Packages
  url: packages/openbankproject-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.openbankproject.com/solutions/sandbox/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openbankproject.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://test-portal.openbankproject.com/login
- group: auth
  href: https://artifacts.apis.io/openbankproject/security/openbankproject-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openbankproject-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openbankproject.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openbankproject.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://apisandbox-portal.openbankproject.com/
- group: operate
  title: ''
  type: Support
  url: https://www.openbankproject.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.openbankproject.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenBankProject
created: '2026-10-21'
description: Open Bank Project (OBP) provides an open-source API platform enabling banks and fintechs to build, manage, and secure open banking APIs. It offers a sandbox, compliance tools, and developer resources to accelerate integration with PSD2 and other standards, fostering innovation across financial services.
layout: provider
modified: '2026-10-21'
name: Open Bank Project
nav: Providers
network: true
overview: 'Open Bank Project is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenBanking, API, Fintech, and Banking.


  Open Bank Project''s developer surface includes sandbox, documentation, API reference, support, engineering blog, and 10 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 16.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Openbankproject Domain Security
  slug: openbankproject-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openbankproject
tags:
- Company
- OpenBanking
- API
- Fintech
- Banking
website: https://www.openbankproject.com/
---
