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
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/nuitee-com/conformance/nuitee-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nuitee-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/nuitee-com/hosts/nuitee-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nuitee-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/nuitee-com/vendors/nuitee-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nuitee-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nuitee.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuitee.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nuitee.com/developers
- group: company
  title: ''
  type: Blog
  url: https://blog.nuitee.com/
- group: auth
  href: https://artifacts.apis.io/nuitee-com/security/nuitee-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nuitee-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nuitee.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://blog.nuitee.com/mcp
  - status: 200
    url: https://www.nuitee.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Nuitee provides an AI‑powered platform that transforms travel‑related business operations. It offers intelligent APIs for travel agencies, airlines, hotels and fintech partners, enabling automated booking, personalized recommendations, and productivity‑boosting workflows. The solution leverages large language models to enhance customer experiences and streamline back‑office processes across the travel ecosystem.
image: https://nuitee.com/images/og-image.png
layout: provider
modified: '2026-10-25'
name: Nuitee
nav: Providers
network: true
overview: 'Nuitee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel APIs, Hotel Distribution, Booking Engine, Payment Solutions, and Mapping.


  Nuitee''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nuitee Com Domain Security
  slug: nuitee-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nuitee-com
tags:
- Travel APIs
- Hotel Distribution
- Booking Engine
- Payment Solutions
- Mapping
- AI Agents
- Developers
- B2B Travel
website: https://www.nuitee.com/
---
