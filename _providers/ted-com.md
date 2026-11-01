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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/ted-com/conformance/ted-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ted-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ted-com/llms/ted-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ted-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ted-com/well-known/ted-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ted-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ted-com/hosts/ted-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ted-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ted-com/vendors/ted-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ted-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.ted.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ted.com/about/our-organization/our-policies-terms/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ted.com/participate/get-started
- group: company
  title: ''
  type: Blog
  url: https://blog.ted.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.ted.com/
- group: auth
  href: https://artifacts.apis.io/ted-com/security/ted-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ted-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ted.com/
coverage:
  checked: '2026-10-28'
  detail: TED's developer documentation is served via JavaScript-rendered help pages with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://help.ted.com/hc/en-us
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: TED is a global nonprofit devoted to ideas worth spreading, offering a platform for talks, performances, and educational content across a wide range of topics including science, technology, design, and global issues. Its mission is to spark curiosity and inspire change through powerful storytelling and accessible media, reaching millions worldwide via its website, mobile apps, and partner initiatives.
image: https://pi.tedcdn.com/r/pl.tedcdn.com/social/ted-logo-fb.png?v=wAff13s?
layout: provider
modified: '2026-10-28'
name: TED
nav: Providers
network: true
overview: 'TED is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Nonprofit, Education, and Technology.


  TED''s developer surface includes support, getting-started guide, engineering blog, documentation, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
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
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ted Com Domain Security
  slug: ted-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ted-com
tags:
- Company
- Media
- Nonprofit
- Education
- Technology
- Entertainment
website: https://ted.com/
---
