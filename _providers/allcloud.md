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
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/allcloud/refs/heads/main/llms/allcloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allcloud-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allcloud/refs/heads/main/hosts/allcloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allcloud-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/allcloud/refs/heads/main/vendors/allcloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allcloud-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://allcloud.io/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allcloud.io/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://allcloud.io/about-us/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://allcloud.io/services/data-practice/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://allcloud.io/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allcloud/refs/heads/main/security/allcloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/allcloud-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/allcloud/refs/heads/main/security/allcloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allcloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allcloud.io
coverage:
  checked: 2026-09-24
  detail: OpenAPI spec endpoint returned 401 and no other machine-readable contract was found.
  evidence:
  - status: 401
    url: https://engage.allcloud.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: AllCloud provides AI‑enabled cloud managed services, optimization, security, and migration solutions for enterprise customers. It offers AI strategy, AI on AWS, Salesforce, and Anthropic, as well as cloud platforms, data management, and industry‑specific services for financial services, manufacturing, retail, and SaaS technology firms.
image: https://allcloud.io/wp-content/uploads/2019/08/AllCloud-Homepage-Image.png
layout: provider
modified: '2026-09-24'
name: Allcloud
nav: Providers
network: true
overview: 'Allcloud is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Managed Service, Cloud_platforms, AI Solutions, Security, and Financial Services.


  Allcloud''s developer surface includes getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 11.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Allcloud Domain Security
  slug: allcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Allcloud Vulnerability Disclosure
  slug: allcloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: allcloud
tags:
- Managed Service
- Cloud_platforms
- AI Solutions
- Security
- Financial Services
- Manufacturing
- Retail
- Software-as-a-Service
website: https://allcloud.io
---
