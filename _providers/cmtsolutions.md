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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cmtsolutions/refs/heads/main/llms/cmtsolutions-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cmtsolutions-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cmtsolutions/refs/heads/main/hosts/cmtsolutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cmtsolutions-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cmtsolutions/refs/heads/main/vendors/cmtsolutions-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cmtsolutions-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.careviso.com/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.careviso.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.careviso.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.careviso.com/news-events/price-transparency-in-healthcare
- group: other
  title: ''
  type: Leadership
  url: https://www.careviso.com/about/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.careviso.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/careviso
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cmtsolutions/refs/heads/main/security/cmtsolutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cmtsolutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.careviso.com
coverage:
  checked: '2026-10-09'
  detail: The provider's website does not expose any developer documentation or API reference pages.
  evidence:
  - status: 200
    url: https://www.careviso.com
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Cmtsolutions, now operating as Careviso, provides the seeQer platform that automates healthcare prior authorizations, eligibility verification, and cost transparency. The company aims to reduce administrative burden for providers and empower patients with clear treatment cost information, leveraging advanced data analytics and real‑time integration with insurers.
image: https://cdn.prod.website-files.com/65f88552c6ad8ce7791beb99/660f408ccedca2eb0c3e85f7_Open-graph-Home.jpg
layout: provider
modified: '2026-10-09'
name: Cmtsolutions
nav: Providers
network: true
overview: 'Cmtsolutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Transparency, and Automation.


  Cmtsolutions'' developer surface includes pricing and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cmtsolutions Domain Security
  slug: cmtsolutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cmtsolutions
tags:
- Company
- Healthcare
- Transparency
- Automation
website: https://www.careviso.com
---
