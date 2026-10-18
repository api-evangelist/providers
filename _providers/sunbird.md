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
- description: API for Sunbird Data Center Infrastructure Management platform
  name: Sunbird DCIM API
  slug: sunbird-dcim-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sunbird/refs/heads/main/plans/sunbird-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sunbird-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sunbird/refs/heads/main/llms/sunbird-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sunbird-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sunbird/refs/heads/main/hosts/sunbird-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sunbird-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sunbird/refs/heads/main/vendors/sunbird-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sunbird-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sunbirddcim.com/terms-use
- group: auth
  title: ''
  type: Security
  url: https://www.sunbirddcim.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sunbirddcim.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sunbirddcim
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sunbird/refs/heads/main/security/sunbird-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sunbird-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sunbird/refs/heads/main/security/sunbird-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sunbird-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sunbirddcim.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sunbirddcim.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.sunbirddcim.com/blog
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI or other machine-readable contract found at https://api.sunbirddcim.com
  evidence:
  - status: 0
    url: https://api.sunbirddcim.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Sunbird provides Data Center Infrastructure Management (DCIM) software that helps organizations monitor, manage, and optimize their data center assets and operations. The platform offers tools for asset tracking, capacity planning, energy management, environmental monitoring, and security analytics, supporting both colocation and government data centers. Sunbird’s solutions enable real‑time visibility, automated workflows, and detailed reporting to improve efficiency, reduce risk, and lower operational costs across complex data center environments.
layout: provider
modified: '2026-10-14'
name: Sunbird
nav: Providers
network: true
overview: 'Sunbird is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DataCenter, DCIM, Infrastructure, and Management.


  Sunbird''s developer surface includes pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Sunbird Plans Pricing
  plan_count: 1
  slug: sunbird-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 69.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sunbird Domain Security
  slug: sunbird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sunbird Vulnerability Disclosure
  slug: sunbird-vulnerability-disclosure
  summary_line: no policy recorded
slug: sunbird
tags:
- Company
- DataCenter
- DCIM
- Infrastructure
- Management
website: https://www.sunbirddcim.com
---
