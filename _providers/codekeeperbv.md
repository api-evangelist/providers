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
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/codekeeperbv/refs/heads/main/plans/codekeeperbv-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/codekeeperbv-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/codekeeperbv/refs/heads/main/authentication/codekeeperbv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/codekeeperbv-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/codekeeperbv/refs/heads/main/conformance/codekeeperbv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/codekeeperbv-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/codekeeperbv/refs/heads/main/llms/codekeeperbv-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/codekeeperbv-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codekeeperbv/refs/heads/main/hosts/codekeeperbv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/codekeeperbv-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/codekeeperbv/refs/heads/main/vendors/codekeeperbv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/codekeeperbv-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://codekeeper.co/trust-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codekeeper.co/terms
- group: operate
  title: ''
  type: Support
  url: https://codekeeper.co/contact-support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codekeeper.co/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://codekeeper.co/pricing
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/codekeeperbv/refs/heads/main/security/codekeeperbv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/codekeeperbv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://codekeeper.co
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite accessible documentation pages.
  evidence:
  - status: 200
    url: https://codekeeper.co
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Codekeeper BV provides software escrow and continuity solutions, helping organizations protect source code, SaaS applications, and AI models. Their platform offers vendor risk and compliance services for regulations like DORA, NIS2, and CRA, alongside secure storage, backup, and verification tools.
layout: provider
modified: '2026-10-09'
name: Codekeeperbv
nav: Providers
network: true
overview: 'Codekeeperbv is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Software Escrow, Continuity, Software-as-a-Service, Backup, and Artificial Intelligence.


  Codekeeperbv''s developer surface includes authentication, support, pricing, and 10 more developer resources.'
plans:
- name: Codekeeperbv Plans Pricing
  plan_count: 6
  slug: codekeeperbv-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Codekeeperbv Authentication
  slug: codekeeperbv-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Codekeeperbv Domain Security
  slug: codekeeperbv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codekeeperbv
tags:
- Software Escrow
- Continuity
- Software-as-a-Service
- Backup
- Artificial Intelligence
- Compliance
- Vendor Risk
website: https://codekeeper.co
---
