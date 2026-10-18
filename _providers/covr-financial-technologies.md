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
api_count: 1
apis:
- description: Covr Financial Technologies does not publish a public machine‑readable API specification. The website provides product information and contact pages but no developer portal or OpenAPI document.
  name: Covr API
  slug: covr-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/covr-financial-technologies/refs/heads/main/hosts/covr-financial-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/covr-financial-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/covr-financial-technologies/refs/heads/main/vendors/covr-financial-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/covr-financial-technologies-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://covrtech.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://covrtech.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/covr-financial-technologies/refs/heads/main/security/covr-financial-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/covr-financial-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://covrtech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://covrtech.com/blog/
- group: company
  title: ''
  type: About
  url: https://covrtech.com/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://covrtech.com/privacy-policy-for-covr-financial-technologies-llc/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://covrtech.com/terms-of-use/
coverage:
  checked: '2026-10-11'
  detail: Main website pages return HTML and a JavaScript challenge on some links, with no machine‑readable API spec discovered.
  evidence:
  - status: 404
    url: https://api.covrtech.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: Covr Financial Technologies provides a digital insurance platform for financial institutions and advisors, simplifying life, long-term care, disability, and specialty insurance sales. The SaaS solution connects consumers with multiple carriers, offering personalization, speed, and choice, and serves over 30,000 financial advisors and 40 million consumers.
image: https://covrtech.com/wp-content/uploads/1-white.png
layout: provider
modified: '2026-10-11'
name: Covr Financial Technologies
nav: Providers
network: true
overview: 'Covr Financial Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurtech, DigitalInsurance, Financial Services, and Software-as-a-Service.


  Covr Financial Technologies'' developer surface includes documentation and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 60.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Covr Financial Technologies Domain Security
  slug: covr-financial-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: covr-financial-technologies
tags:
- Company
- Insurtech
- DigitalInsurance
- Financial Services
- Software-as-a-Service
website: https://covrtech.com/
---
