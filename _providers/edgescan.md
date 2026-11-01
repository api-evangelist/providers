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
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.edgescan.com/compliance/
- group: agent
  href: https://artifacts.apis.io/edgescan/llms/edgescan-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/edgescan-llms.txt
- group: agent
  href: https://artifacts.apis.io/edgescan/well-known/edgescan-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/edgescan-well-known.yml
- group: other
  href: https://artifacts.apis.io/edgescan/hosts/edgescan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/edgescan-hosts.yml
- group: other
  href: https://artifacts.apis.io/edgescan/vendors/edgescan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/edgescan-vendors.yml
- group: build
  href: https://artifacts.apis.io/edgescan/packages/edgescan-packages.yml
  title: ''
  type: SDKs
  url: packages/edgescan-packages.yml
- group: build
  href: https://artifacts.apis.io/edgescan/packages/edgescan-packages.yml
  title: ''
  type: Packages
  url: packages/edgescan-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.edgescan.com/features/support/
- group: start
  title: ''
  type: SignUp
  url: https://info.edgescan.com/register-for-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edgescan.com/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://www.edgescan.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://www.edgescan.com/blog/
- group: auth
  href: https://artifacts.apis.io/edgescan/security/edgescan-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/edgescan-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/edgescan/security/edgescan-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edgescan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://edgescan.com/
coverage:
  checked: '2026-10-20'
  detail: API documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.edgescan.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Edgescan provides a continuous exposure validation platform that combines automated vulnerability scanning with expert human assessment. Their services include API security testing, dynamic application security testing, penetration testing as a service, network vulnerability management, and attack surface management. The company helps organizations identify, prioritize, and remediate security risks across cloud, web, and mobile environments, delivering actionable insights and compliance support.
image: https://a146b270.delivery.rocketcdn.me/wp-content/uploads/2024/08/Main-Featured-Image.jpg
layout: provider
modified: '2026-10-20'
name: Edgescan
nav: Providers
network: true
overview: 'Edgescan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Vulnerability Management, API Testing, and Cloud.


  Edgescan''s developer surface includes support, signup flow, engineering blog, and 12 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Edgescan Domain Security
  slug: edgescan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Edgescan Trust Center
  slug: edgescan-trust-center
  summary_line: PCI DSS, GDPR
slug: edgescan
tags:
- Company
- Security
- Vulnerability Management
- API Testing
- Cloud
website: https://edgescan.com/
---
