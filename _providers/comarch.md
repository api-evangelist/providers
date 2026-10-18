---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.8
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Comarch Portal API documentation.
  name: Comarch Portal API
  slug: comarch-portal-api
- baseURL: https://www.comarch.com/
  baseurl_source: spec
  description: The Global API from Comarch — 1 operation(s) for global.
  name: Comarch Global API
  slug: comarch-global-api
artifact_total: 5
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comarch/refs/heads/main/rules/comarch-rules.yml
  title: ''
  type: Spectral
  url: rules/comarch-rules.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/comarch/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/comarch/refs/heads/main/changelog/comarch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/comarch-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/comarch/refs/heads/main/conformance/comarch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/comarch-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/comarch/refs/heads/main/llms/comarch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/comarch-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/comarch/refs/heads/main/hosts/comarch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/comarch-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.comarch.com/trade-and-services/ict/knowledge/security/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.comarch.com/esef/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.comarch.com/press-center/news/
- group: company
  title: ''
  type: Blog
  url: https://blog.comarch.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.comarch.com/trade-and-services/data-management/clients-success-stories/comprehensive-edi-project-with-e-invoicing-and-a-self-onboarding-platform/
- group: docs
  title: ''
  type: Documentation
  url: https://help.comarch.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/comarch
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comarch/refs/heads/main/security/comarch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/comarch-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/comarch/refs/heads/main/security/comarch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/comarch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.comarch.com
created: '2026-10-13'
description: Comarch is a global IT solutions provider offering a wide range of services including enterprise software, cloud solutions, and digital transformation tools. Founded in 1991 in Poland, Comarch serves customers across various industries such as telecommunications, finance, healthcare, and public sector. The company focuses on delivering innovative technologies, data analytics, and customer relationship management platforms to help businesses improve efficiency and drive growth. With a presence in over 30 countries, Comarch continues to expand its portfolio of products and services, emphasizing security, scalability, and integration capabilities for modern enterprises.
image: https://www.comarch.com/dist/img/portal/Comarch_Globabl_IT.png
layout: provider
modified: '2026-10-13'
name: Comarch
nav: Providers
network: true
overview: 'Comarch publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Global API, and 1 more. Tagged areas include Company, IT, Software, Cloud, and Enterprise.


  The Comarch catalog on APIs.io includes 1 Spectral governance ruleset.


  Comarch''s developer surface includes changelog, pricing, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Comarch API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: comarch-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 31.8
    contract_quality: 38.6
    developer_ergonomics: 30.2
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Comarch Domain Security
  slug: comarch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Comarch Vulnerability Disclosure
  slug: comarch-vulnerability-disclosure
  summary_line: no policy recorded
slug: comarch
tags:
- Company
- IT
- Software
- Cloud
- Enterprise
- Global
website: https://www.comarch.com
---
