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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: ArmorCode provides a unified exposure management platform for AI-driven vulnerability detection and remediation.
  name: Armorcode API
  slug: armorcode-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/armorcodeinc/refs/heads/main/llms/armorcodeinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/armorcodeinc-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/armorcodeinc/refs/heads/main/well-known/armorcodeinc-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/armorcodeinc-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/armorcodeinc/refs/heads/main/well-known/armorcodeinc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/armorcodeinc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/armorcodeinc/refs/heads/main/hosts/armorcodeinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/armorcodeinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/armorcodeinc/refs/heads/main/vendors/armorcodeinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/armorcodeinc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.armorcode.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.armorcode.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.armorcode.com/
- group: auth
  title: ''
  type: Security
  url: https://www.armorcode.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.armorcode.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.armorcode.com/news
- group: other
  title: ''
  type: Leadership
  url: https://www.armorcode.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.armorcode.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/armorcodeinc/refs/heads/main/security/armorcodeinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/armorcodeinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.armorcode.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec could be found on any discovered host.
  evidence:
  - status: 0
    url: https://api.armorcode.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: ArmorCode is the independent control plane where AI agents help find, prioritize, and fix vulnerabilities across apps, cloud, infra, and AI. It offers a unified exposure management platform integrating risk graphs, agentic workflows, and compliance tools for enterprises.
image: https://www.armorcode.com/wp-content/uploads/2025/11/ArmorCode_default-thumb_R2_updated-11-11-25.png
layout: provider
modified: '2026-09-26'
name: Armorcodeinc
nav: Providers
network: true
overview: 'Armorcodeinc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Artificial Intelligence, Risk Management, and Exposure Management.


  Armorcodeinc''s developer surface includes support, engineering blog, and 13 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 67.9
    operational_transparency: 26.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Armorcodeinc Domain Security
  slug: armorcodeinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: armorcodeinc
tags:
- Company
- Security
- Artificial Intelligence
- Risk Management
- Exposure Management
website: https://www.armorcode.com
---
