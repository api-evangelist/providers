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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation for Doppel9e9d platform, covering integrations and product features.
  name: Doppel API
  slug: doppel-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.doppel.com/security
- group: agent
  href: https://artifacts.apis.io/doppel9e9d/llms/doppel9e9d-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doppel9e9d-llms.txt
- group: other
  href: https://artifacts.apis.io/doppel9e9d/hosts/doppel9e9d-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doppel9e9d-hosts.yml
- group: other
  href: https://artifacts.apis.io/doppel9e9d/vendors/doppel9e9d-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doppel9e9d-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doppel.com/legal/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.doppel.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doppel.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.doppel.com/solutions/industry/media
- group: other
  title: ''
  type: Leadership
  url: https://www.doppel.com/company/leadership
- group: docs
  title: ''
  type: Documentation
  url: https://www.doppel.com/docs/jira-integration
- group: company
  title: ''
  type: Blog
  url: https://www.doppel.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.doppel.com/blog/stage-1-setup-social-engineering-attack-chain
- group: auth
  href: https://artifacts.apis.io/doppel9e9d/security/doppel9e9d-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/doppel9e9d-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/doppel9e9d/security/doppel9e9d-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doppel9e9d-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.doppel.com
coverage:
  checked: '2026-10-24'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be discovered despite accessible documentation.
  evidence:
  - status: 200
    url: https://www.doppel.com/docs/jira-integration
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Doppel9e9d is a platform providing AI‑powered social engineering defense solutions. It helps organizations protect their brand, executives, and employees from impersonation, phishing, and other identity‑based attacks through simulation, awareness training, and real‑time threat mitigation. The company partners with major sports franchises and serves multiple industries including financial services, healthcare, and energy.
image: https://prod-cms.doppel.com/sites/default/files/2025-11/Open_Graph_Image_0.png
layout: provider
modified: '2026-10-24'
name: Doppel9e9d
nav: Providers
network: true
overview: 'Doppel9e9d is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, AI, Social-Engineering, and Defense.


  Doppel9e9d''s developer surface includes documentation, engineering blog, getting-started guide, and 12 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 60.7
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doppel9E9D Domain Security
  slug: doppel9e9d-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Doppel9E9D Trust Center
  slug: doppel9e9d-trust-center
  summary_line: SOC 2
slug: doppel9e9d
tags:
- Company
- Security
- AI
- Social-Engineering
- Defense
website: https://www.doppel.com
---
