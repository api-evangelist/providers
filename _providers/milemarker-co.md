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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/milemarker-co/vendors/milemarker-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/milemarker-co-vendors.yml
- group: agent
  href: https://artifacts.apis.io/milemarker-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/milemarker-co/changelog/milemarker-co-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/milemarker-co-changelog.yml
- group: auth
  href: https://artifacts.apis.io/milemarker-co/security/milemarker-co-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/milemarker-co-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/milemarker-co/conformance/milemarker-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/milemarker-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/milemarker-co/llms/milemarker-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/milemarker-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/milemarker-co/well-known/milemarker-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/milemarker-co-security.txt
- group: auth
  href: https://artifacts.apis.io/milemarker-co/well-known/milemarker-co-milemarker-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/milemarker-co-milemarker-security.txt
- group: agent
  href: https://artifacts.apis.io/milemarker-co/well-known/milemarker-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/milemarker-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/milemarker-co/hosts/milemarker-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/milemarker-co-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.milemarker.co/resources/legal/terms-conditions
- group: start
  title: ''
  type: Sandbox
  url: https://www.milemarker.co/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.milemarker.co/resources/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.milemarker.co/resources/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.milemarker.co/resources/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.milemarker.co/
- group: auth
  href: https://artifacts.apis.io/milemarker-co/security/milemarker-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/milemarker-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/milemarker-co/security/milemarker-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/milemarker-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.milemarker.co/
coverage:
  checked: '2026-10-30'
  detail: Website provides only HTML pages with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.milemarker.co/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Milemarker unifies custodian, CRM and planning data into one governed foundation your firm owns — powering AI, reporting and automation. It provides a wealth management data platform that integrates financial data sources, enabling firms to deliver insights, compliance, and client services through a unified API.
image: https://framerusercontent.com/assets/20T5ctdSI13pmg2KVMu3HkRLpEo.png
layout: provider
modified: '2026-10-30'
name: milemarker-co
nav: Providers
network: true
overview: 'milemarker-co is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WealthManagement, DataPlatform, API, and FinTech.


  milemarker-co''s developer surface includes changelog, sandbox, engineering blog, documentation, and 15 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 25.5
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Milemarker Co Domain Security
  slug: milemarker-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Milemarker Co Vulnerability Disclosure
  slug: milemarker-co-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: milemarker-co
tags:
- Company
- WealthManagement
- DataPlatform
- API
- FinTech
website: https://www.milemarker.co/
---
