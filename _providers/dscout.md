---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'dscout API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: dscout API
  slug: dscout-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/dscout/rules/dscout-rules.yml
  title: ''
  type: Spectral
  url: rules/dscout-rules.yml
- group: design
  href: https://artifacts.apis.io/dscout/json-ld/dscout-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dscout-context.jsonld
- group: design
  href: https://artifacts.apis.io/dscout/vocabulary/dscout-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dscout-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dscout/data-model/dscout-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dscout-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.dscout.com/
- group: design
  href: https://artifacts.apis.io/dscout/conformance/dscout-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dscout-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dscout/llms/dscout-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dscout-llms.txt
- group: agent
  href: https://artifacts.apis.io/dscout/well-known/dscout-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dscout-well-known.yml
- group: other
  href: https://artifacts.apis.io/dscout/hosts/dscout-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dscout-hosts.yml
- group: other
  href: https://artifacts.apis.io/dscout/vendors/dscout-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dscout-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.dscout.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dscout.com/legal/privacy-data-requests
- group: company
  title: ''
  type: Newsroom
  url: https://dscout.com/news
- group: start
  title: ''
  type: GettingStarted
  url: https://help.dscout.com/getting-started/dscout-quickstart-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dscout
- group: auth
  href: https://artifacts.apis.io/dscout/security/dscout-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dscout-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dscout/security/dscout-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dscout-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dscout.com
- group: docs
  title: ''
  type: Documentation
  url: https://dscout.com/help-center
- group: commercial
  title: ''
  type: Pricing
  url: https://dscout.com/pricing
coverage:
  checked: '2026-10-25'
  detail: Help Center pages render via JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://dscout.com/help-center
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Dscout provides an AI‑powered human‑centered research platform that helps companies recruit participants, run studies, and analyze insights. Their tools support usability testing, field studies, diary studies, media‑rich surveys, and AI‑moderated interviews, enabling faster product decisions and deeper user understanding across industries.
json_schemas:
- name: GetGettingStartedDscoutQuickstartGuideUsingTheDscoutSandboxM
  property_count: 3
  slug: dscout-get-getting-started-dscout-quickstart-guide-using-the-dscout-sandbox-m
jsonld:
- class_count: 1
  name: Dscout Context
  property_count: 3
  slug: dscout-context
layout: provider
modified: '2026-10-24'
name: dscout
nav: Providers
network: true
overview: 'dscout is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, UX Research, AI, User Testing, and Market Research.


  The dscout catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dscout''s developer surface includes support, getting-started guide, documentation, pricing, and 16 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: dscout API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: dscout-rules
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.4
    catalog_earned_first_party: 0.0
    catalog_gap: 69.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 19.7
    contract_quality: 17.4
    developer_ergonomics: 26.2
    discoverability: 55.4
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dscout Domain Security
  slug: dscout-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Dscout Trust Center
  slug: dscout-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: dscout
tags:
- Company
- UX Research
- AI
- User Testing
- Market Research
website: https://dscout.com
---
