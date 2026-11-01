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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.truenas.com/
- group: auth
  href: https://artifacts.apis.io/truenas/security/truenas-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/truenas-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/truenas/llms/truenas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/truenas-llms.txt
- group: agent
  href: https://artifacts.apis.io/truenas/well-known/truenas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/truenas-well-known.yml
- group: other
  href: https://artifacts.apis.io/truenas/hosts/truenas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/truenas-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truenas.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truenas.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truenas/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.truenas.com/docs/scale/gettingstarted
- group: auth
  href: https://artifacts.apis.io/truenas/security/truenas-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/truenas-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/truenas/security/truenas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/truenas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://truenas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.truenas.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://www.truenas.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.truenas.com/blog/
coverage:
  checked: '2026-10-28'
  detail: Documentation hub loads content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.truenas.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: TrueNAS provides enterprise-grade, open-source storage solutions, offering both hardware appliances and software-defined storage platforms. Their product line includes the TrueNAS Enterprise series for mission-critical workloads, TrueNAS Community Edition for free use, and a range of scalable options like the F-Series and R-Series. The company focuses on data protection, high performance, and flexible deployment across on-premises, edge, and cloud environments, supporting a wide array of industries from media to healthcare.
image: https://www.truenas.com/wp-content/uploads/2025/05/truenas-logo-full-color-rgb.png
layout: provider
modified: '2026-10-28'
name: TrueNAS
nav: Providers
network: true
overview: 'TrueNAS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, Open-Source, Enterprise, and Data-Protection.


  TrueNAS''s developer surface includes getting-started guide, documentation, support, engineering blog, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Truenas Domain Security
  slug: truenas-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Truenas Vulnerability Disclosure
  slug: truenas-vulnerability-disclosure
  summary_line: no policy recorded
slug: truenas
tags:
- Company
- Storage
- Open-Source
- Enterprise
- Data-Protection
website: https://truenas.com/
---
