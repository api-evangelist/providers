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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.bitsight.com/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/llms/bitsighttechnologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitsighttechnologies-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/well-known/bitsighttechnologies-service-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitsighttechnologies-service-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/well-known/bitsighttechnologies-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitsighttechnologies-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/well-known/bitsighttechnologies-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitsighttechnologies-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/well-known/bitsighttechnologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitsighttechnologies-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/hosts/bitsighttechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitsighttechnologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/vendors/bitsighttechnologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitsighttechnologies-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bitsight.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.bitsight.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bitsight
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/security/bitsighttechnologies-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bitsighttechnologies-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/security/bitsighttechnologies-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitsighttechnologies-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitsighttechnologies/refs/heads/main/security/bitsighttechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitsighttechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitsight.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://service.bitsighttech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bitsight.com/platform
- group: docs
  title: ''
  type: APIReference
  url: https://www.bitsight.com/platform/mcp-api-data-delivery
- group: company
  title: ''
  type: Blog
  url: https://www.bitsight.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bitsight.com/pricing-packaging
- group: start
  title: ''
  type: Login
  url: https://service.bitsighttech.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitsight.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitsight.com/privacy-policy
coverage:
  checked: '2026-09-28'
  detail: The Bitsight MCP API reference page provides documentation but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://www.bitsight.com/platform/mcp-api-data-delivery
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bitsight is a cyber risk intelligence platform that provides real‑time monitoring of external attack surfaces, third‑party risk, and vulnerability data. Leveraging AI‑driven attribution and a massive data set of internet‑exposed assets, Bitsight helps enterprises assess and mitigate security risks across their supply chain, vendors, and internal assets. The platform offers continuous monitoring, risk scoring, and actionable insights for security, compliance, and risk management teams.
layout: provider
modified: '2026-09-28'
name: Bitsighttechnologies
nav: Providers
network: true
overview: 'Bitsighttechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Risk Management, and Software-as-a-Service.


  Bitsighttechnologies'' developer surface includes documentation, API reference, engineering blog, pricing, and 19 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitsighttechnologies Domain Security
  slug: bitsighttechnologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bitsighttechnologies Vulnerability Disclosure
  slug: bitsighttechnologies-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bitsighttechnologies Trust Center
  slug: bitsighttechnologies-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: bitsighttechnologies
tags:
- Company
- Cybersecurity
- Risk Management
- Software-as-a-Service
website: https://www.bitsight.com
---
