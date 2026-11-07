---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Cite Files API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cite Files API
  slug: citefiles-com-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/citefiles-com/rules/citefiles-com-rules.yml
  title: ''
  type: Spectral
  url: rules/citefiles-com-rules.yml
- group: design
  href: https://artifacts.apis.io/citefiles-com/vocabulary/citefiles-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/citefiles-com-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/citefiles-com/changelog/citefiles-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/citefiles-com-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://citefiles.com/contact
- group: design
  href: https://artifacts.apis.io/citefiles-com/conformance/citefiles-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/citefiles-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/citefiles-com/llms/citefiles-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citefiles-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/citefiles-com/well-known/citefiles-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/citefiles-com-security.txt
- group: agent
  href: https://artifacts.apis.io/citefiles-com/well-known/citefiles-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citefiles-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/citefiles-com/hosts/citefiles-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citefiles-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/citefiles-com/vendors/citefiles-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citefiles-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://citefiles.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://citefiles.com/privacy
- group: start
  title: ''
  type: Login
  url: https://citefiles.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://citefiles.com/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://citefiles.com/methodology/changelog
- group: auth
  href: https://artifacts.apis.io/citefiles-com/security/citefiles-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/citefiles-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/citefiles-com/security/citefiles-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citefiles-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://citefiles.com/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite docs pages.
  evidence:
  - status: 200
    url: https://citefiles.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Cite Files provides free AI crawler access and an llms.txt checker, testing edge-level crawler blocking, robots.txt, sitemaps, and generating missing files from a site's own published text. It helps ensure that AI assistants can reach, read, and cite websites accurately, without fabricating facts. The service offers a free tier and aims to improve transparency for web content accessibility to AI models.
image: https://citefiles.com/og.png
layout: provider
modified: '2026-11-03'
name: Cite Files
nav: Providers
network: true
overview: 'Cite Files is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Crawling, Accessibility, and Open Source.


  The Cite Files catalog on APIs.io includes 1 Spectral governance ruleset.


  Cite Files'' developer surface includes changelog, documentation, and 16 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 62
  extends:
  - spectral:oas
  name: Cite Files API Rules
  rule_count: 21
  severity_counts:
    error: 19
    hint: 0
    info: 1
    warn: 1
  slug: citefiles-com-rules
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Citefiles Com Domain Security
  slug: citefiles-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Citefiles Com Vulnerability Disclosure
  slug: citefiles-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: citefiles-com
tags:
- Company
- Artificial Intelligence
- Crawling
- Accessibility
- Open Source
website: https://citefiles.com/
---
