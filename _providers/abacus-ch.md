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
api_count: 1
apis:
- description: Abacus provides Swiss ERP solutions; API details are not publicly documented.
  name: Abacus ERP
  slug: abacus-erp
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/abacus-ch/well-known/abacus-ch-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/abacus-ch-security.txt
- group: auth
  href: https://artifacts.apis.io/abacus-ch/well-known/abacus-ch-abacus-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/abacus-ch-abacus-security.txt
- group: agent
  href: https://artifacts.apis.io/abacus-ch/well-known/abacus-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abacus-ch-well-known.yml
- group: other
  href: https://artifacts.apis.io/abacus-ch/hosts/abacus-ch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abacus-ch-hosts.yml
- group: other
  href: https://artifacts.apis.io/abacus-ch/vendors/abacus-ch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abacus-ch-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.abacus.ch/
- group: auth
  title: ''
  type: Security
  url: https://www.abacus.ch/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.abacus.ch/news/medienmitteilungen
- group: start
  title: ''
  type: Login
  url: https://login.abacus.ch/auth/realms/abacus/protocol/openid-connect/auth?response_type=code&client_id=oidc-abahelp&scope=openid%20userid%20profile&state=7QqD61WoN_rvQT1psS0bHa85o5ESNYm6kJVo74i2t5c%3D&redirect_uri=https://help.abacus.ch/login/oauth2/code/abacus&nonce=fMZVEluUhqSy4qLBpTM-sPItpCBhu5mEQEvE8ZOYeII&code_challenge=bw2eEEaqJIaSlcIEBEDzg8iqTMUp1DiZ3_hUu3BqBYc&code_challenge_method=S256
- group: company
  title: ''
  type: Blog
  url: https://www.abacus.ch/blog
- group: auth
  href: https://artifacts.apis.io/abacus-ch/security/abacus-ch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/abacus-ch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/abacus-ch/security/abacus-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abacus-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abacus.ch/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts are publicly available despite documentation links.
  evidence:
  - status: 200
    url: https://www.abacus.ch/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Abacus (Swiss ERP) provides comprehensive business software solutions for Swiss enterprises, covering financial accounting, payroll, human resources, procurement, and production planning. The platform integrates electronic banking, expense management, and analytics, offering cloud‑based ERP tools tailored to the regulatory and multilingual environment of Switzerland.
image: https://www.abacus.ch/_assets/b5b69edae8d1d4ee966272c76001d3f8/Images/abacus_social.jpg
layout: provider
modified: '2026-10-27'
name: Abacus (Swiss ERP)
nav: Providers
network: true
overview: 'Abacus (Swiss ERP) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ERP, Finance, HR, and Procurement.


  Abacus (Swiss ERP)''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Abacus Ch Domain Security
  slug: abacus-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Abacus Ch Vulnerability Disclosure
  slug: abacus-ch-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: abacus-ch
tags:
- Company
- ERP
- Finance
- HR
- Procurement
- Manufacturing
website: https://abacus.ch/
---
