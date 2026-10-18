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
artifact_total: 1
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/carv/refs/heads/main/conformance/carv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carv-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carv/refs/heads/main/well-known/carv-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carv-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carv/refs/heads/main/well-known/carv-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carv-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carv/refs/heads/main/hosts/carv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carv-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carv/refs/heads/main/vendors/carv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carv-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carv.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://help.carv.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carv.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.carv.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.carv.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.carv.com/blog/agentic-ai-setup-for-retail-hiring
- group: docs
  title: ''
  type: Documentation
  url: https://help.carv.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carv/refs/heads/main/security/carv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carv.com
coverage:
  checked: '2026-10-07'
  detail: The developer portal at https://app.carv.com returns a JavaScript-rendered shell with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://app.carv.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Carv provides an agentic AI platform for volume hiring, automating recruiting tasks such as candidate screening, scheduling, onboarding, and compliance. By deploying AI-driven agents, enterprises can reduce time-to-hire by up to 60%, cut admin costs, and scale hiring without adding headcount. The platform integrates with ATS and HR systems, offering a customizable library of agents for various recruitment workflows.
image: https://cdn.prod.website-files.com/65ccf250b7102b398ec21b32/67bd92d1da529b92af76ac2b_opengraph-image-small.png
layout: provider
modified: '2026-10-07'
name: CARV
nav: Providers
network: true
overview: 'CARV is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hiring, AI Recruiting, Volume Hiring, Staffing, and Automation.


  CARV''s developer surface includes support, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carv Domain Security
  slug: carv-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carv
tags:
- Hiring
- AI Recruiting
- Volume Hiring
- Staffing
- Automation
website: https://www.carv.com
---
