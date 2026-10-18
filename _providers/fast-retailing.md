---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fast-retailing/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fast-retailing/refs/heads/main/conformance/fast-retailing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fast-retailing-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fast-retailing/refs/heads/main/hosts/fast-retailing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fast-retailing-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fast-retailing/refs/heads/main/vendors/fast-retailing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fast-retailing-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fastretailing.com/eng/termsofuse/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fastretailing.com/eng/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.fastretailing.com/eng/ir/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fast-retailing/refs/heads/main/security/fast-retailing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fast-retailing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fastretailing.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.fastretailing.com/eng/
coverage:
  checked: '2026-10-13'
  detail: Fast Retailing provides corporate and consumer sites but no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.fastretailing.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Fast Retailing is a global Japanese retail holding company, best known as the parent of Uniqlo, GU, Theory, and other apparel brands. It operates a vast network of clothing stores worldwide, focusing on innovative design, high-quality manufacturing, and efficient supply chain management. The company leverages technology and data-driven strategies to enhance customer experiences and streamline operations across its brands. Fast Retailing continues to expand its international presence while maintaining a commitment to sustainability and corporate responsibility.
layout: provider
modified: '2026-10-13'
name: Fast Retailing
nav: Providers
network: true
overview: 'Fast Retailing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Apparel, Japan, and Uniqlo.


  Fast Retailing''s developer surface includes documentation and 9 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fast Retailing Domain Security
  slug: fast-retailing-domain-security
  summary_line: TLSv1.2 · DMARC
slug: fast-retailing
tags:
- Company
- Retail
- Apparel
- Japan
- Uniqlo
- Global
website: https://www.fastretailing.com
---
