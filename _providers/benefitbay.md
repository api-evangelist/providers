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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benefitbay/refs/heads/main/hosts/benefitbay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benefitbay-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benefitbay/refs/heads/main/vendors/benefitbay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benefitbay-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.benefitbay.com/team
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/benefitbay
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/benefitbay/refs/heads/main/security/benefitbay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benefitbay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.benefitbay.com
- group: company
  title: ''
  type: About
  url: https://www.benefitbay.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.benefitbay.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.benefitbay.com/home/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.benefitbay.com/home/privacy_policy
- group: docs
  title: ''
  type: ICHRA-Guide
  url: https://www.benefitbay.com/ichra-guide?hsLang=en
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on any discovered host.
  evidence:
  - status: 0
    url: https://api.benefitbay.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: BenefitBay provides an ICHRA administration platform that connects brokers, employers, employees, and carriers in a unified ecosystem. It offers real-time plan modeling, compliance tools, and direct premium payments, aiming to simplify individual health reimbursement arrangements and improve employee satisfaction across the United States.
layout: provider
modified: '2026-09-27'
name: BenefitBay
nav: Providers
network: true
overview: BenefitBay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ICHRA, Benefits, Health Tech, and Software-as-a-Service.
random_paper: 15
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Benefitbay Domain Security
  slug: benefitbay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: benefitbay
tags:
- Company
- ICHRA
- Benefits
- Health Tech
- Software-as-a-Service
website: https://www.benefitbay.com
---
