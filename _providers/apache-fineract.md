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
- description: Apache Fineract is an open source core banking platform offering a headless API‑first solution.
  name: Apache Fineract
  slug: apache-fineract
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/apache-fineract/well-known/apache-fineract-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apache-fineract-www-security.txt
- group: auth
  href: https://artifacts.apis.io/apache-fineract/well-known/apache-fineract-apache-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/apache-fineract-apache-security.txt
- group: agent
  href: https://artifacts.apis.io/apache-fineract/well-known/apache-fineract-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apache-fineract-well-known.yml
- group: other
  href: https://artifacts.apis.io/apache-fineract/hosts/apache-fineract-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apache-fineract-hosts.yml
- group: other
  href: https://artifacts.apis.io/apache-fineract/vendors/apache-fineract-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apache-fineract-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.apache.org/security
- group: company
  title: ''
  type: Blog
  url: https://security.apache.org/blog
- group: auth
  href: https://artifacts.apis.io/apache-fineract/security/apache-fineract-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-fineract-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/apache-fineract/security/apache-fineract-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apache-fineract-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fineract.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://fineract.apache.org/docs/stable/
- group: start
  title: ''
  type: GettingStarted
  url: https://fineract.apache.org/docs/stable/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.apache.org/policies/privacy-policy-public.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://fineract.apache.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Apache Fineract is an open‑source core banking platform that provides a cloud‑ready, headless API‑first solution for digital financial services. It enables banks, fintechs, and NGOs to create loan, savings, and accounting products, supporting financial inclusion for unbanked populations worldwide. The project is governed by the Apache Software Foundation and offers extensive documentation, community support, and a robust security model.
layout: provider
modified: '2026-10-28'
name: Apache Fineract
nav: Providers
network: true
overview: 'Apache Fineract is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenSource, FinTech, Banking, and API.


  Apache Fineract''s developer surface includes engineering blog, documentation, getting-started guide, and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 53.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apache Fineract Domain Security
  slug: apache-fineract-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Fineract Vulnerability Disclosure
  slug: apache-fineract-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-fineract
tags:
- Company
- OpenSource
- FinTech
- Banking
- API
website: https://fineract.apache.org/
---
