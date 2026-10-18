---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/springshare/refs/heads/main/authentication/springshare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/springshare-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/springshare/refs/heads/main/llms/springshare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/springshare-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/springshare/refs/heads/main/hosts/springshare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/springshare-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/springshare/refs/heads/main/vendors/springshare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/springshare-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.springshare.com/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.springshare.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://lounge.springshare.com/categories/release-notes
- group: company
  title: ''
  type: Blog
  url: https://blog.springshare.com
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/discourse/discourse-mcp#quick-start-release
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/springshare/refs/heads/main/security/springshare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/springshare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://springshare.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://springshare.com/mcp
  - status: 403
    url: https://blog.springshare.com/mcp
  - status: 200
    url: https://springshare.com
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Springshare provides a suite of library services and tools, including LibGuides, LibCal, LibAnswers, LibWizard, and many others, to help libraries manage resources, engage patrons, and streamline operations. Their platform supports public, academic, K‑12, and special libraries, offering customizable solutions for content discovery, event scheduling, reference services, and analytics. Springshare’s products are designed to improve library workflows, enhance user experiences, and foster community engagement across a wide range of library environments.
image: https://www.springshare.com/assets/logo.png
layout: provider
modified: '2026-10-14'
name: Springshare
nav: Providers
network: true
overview: 'Springshare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Library Services, Software-as-a-Service, Education, and Open Source.


  Springshare''s developer surface includes authentication, support, changelog, engineering blog, getting-started guide, and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.5
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
    developer_ergonomics: 31.0
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Springshare Authentication
  slug: springshare-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Springshare Domain Security
  slug: springshare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: springshare
tags:
- Company
- Library Services
- Software-as-a-Service
- Education
- Open Source
website: https://springshare.com
---
