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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.autogenai.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autogenai/refs/heads/main/well-known/autogenai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autogenai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autogenai/refs/heads/main/hosts/autogenai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autogenai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autogenai/refs/heads/main/vendors/autogenai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autogenai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://autogenai.com/platform/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autogenai.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://autogenai.com/whats-new/
- group: company
  title: ''
  type: Blog
  url: https://autogenai.com/blog/words-matter/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autogenai
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autogenai/refs/heads/main/security/autogenai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/autogenai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autogenai/refs/heads/main/security/autogenai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autogenai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autogenai.com
coverage:
  checked: '2026-09-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the API host despite accessible documentation pages.
  evidence:
  - status: 200
    url: https://api.autogenai.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Autogenai provides AI-powered proposal writing solutions for businesses and government agencies. Their platform offers tools for qualifying, extracting, managing, writing, researching, and reviewing content, with integrations and security features. AutogenAI aims to streamline proposal creation, improve win rates, and support impact pilots in public services, serving enterprise, federal, and grant‑writing sectors.
image: https://autogenai.com/wp-content/uploads/2024/10/og-image-min.jpg
layout: provider
modified: '2026-09-26'
name: Autogenai
nav: Providers
network: true
overview: 'Autogenai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, ProposalWriting, Enterprise, Government, and Software-as-a-Service.


  Autogenai''s developer surface includes changelog, engineering blog, and 10 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 13.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autogenai Domain Security
  slug: autogenai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Autogenai Trust Center
  slug: autogenai-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, FedRAMP, GDPR, FIPS 140
slug: autogenai
tags:
- Artificial Intelligence
- ProposalWriting
- Enterprise
- Government
- Software-as-a-Service
website: https://autogenai.com
---
