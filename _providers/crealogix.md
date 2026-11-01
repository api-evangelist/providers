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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/crealogix/hosts/crealogix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crealogix-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crealogix.com/en/legal-notice
- group: operate
  title: ''
  type: Support
  url: https://support.crealogix.com/en/
- group: other
  title: ''
  type: Leadership
  url: https://crealogix.com/en/about-us/management
- group: auth
  href: https://artifacts.apis.io/crealogix/security/crealogix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crealogix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crealogix.com/
- group: company
  title: ''
  type: Blog
  url: https://crealogix.com/en/blog
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://crealogix.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: CREALOGIX AG. is a Swiss-based software company specializing in digital banking and wealth management solutions. It provides a portfolio of platforms for retail, corporate, SME, and public sector banking, including conversational AI, funding portals, EBICS server, and lending origination hubs. The company aims to empower financial institutions to shine in a digital world through innovative, secure, and scalable technology.
image: https://crealogix.com/sites/default/files/styles/blog_post_main_image/public/2021-08/Logo_web_colour.png?h=cc191311&itok=O0EMLIfu
layout: provider
modified: '2026-10-20'
name: CREALOGIX AG.
nav: Providers
network: true
overview: 'CREALOGIX AG. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Wealth Management, FinTech, and Digital Banking.


  CREALOGIX AG.''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 6.6
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crealogix Domain Security
  slug: crealogix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crealogix
tags:
- Company
- Banking
- Wealth Management
- FinTech
- Digital Banking
website: https://crealogix.com/
---
