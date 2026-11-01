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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://getenter.ai/seguranca
- group: agent
  href: https://artifacts.apis.io/getenter-ai/llms/getenter-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getenter-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/getenter-ai/hosts/getenter-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getenter-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/getenter-ai/vendors/getenter-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getenter-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getenter.ai/en/legal/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getenter.ai/
- group: auth
  title: ''
  type: Security
  url: https://getenter.ai/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getenter.ai/en/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://getenter.ai/en/news
- group: docs
  title: ''
  type: Documentation
  url: https://dev.getenter.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getenter
- group: auth
  href: https://artifacts.apis.io/getenter-ai/security/getenter-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/getenter-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/getenter-ai/security/getenter-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getenter-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getenter.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://getenter.ai
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Enter provides AI-powered agents that automate civil litigation processes for large Brazilian companies, reducing legal costs and improving case outcomes. Their platform reads documents, cross-references external evidence, detects fraud, and generates customized legal defenses, aiming to modernize the traditionally expensive legal workflow in Brazil.
image: https://cdn.prod.website-files.com/69d65bdd2f2eafaa072b250e/69f9fba11be2f9d7a3389c24_OpenGraph.png
layout: provider
modified: '2026-10-23'
name: Enter
nav: Providers
network: true
overview: 'Enter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Litigation, Brazil, LegalTech, and Enterprise.


  Enter''s developer surface includes documentation and 13 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 31.6
  provenance:
    mcp: derived
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
  name: Getenter Ai Domain Security
  slug: getenter-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getenter Ai Trust Center
  slug: getenter-ai-trust-center
  summary_line: SOC 2, ISO 27001
slug: getenter-ai
tags:
- AI
- Litigation
- Brazil
- LegalTech
- Enterprise
website: https://getenter.ai
---
