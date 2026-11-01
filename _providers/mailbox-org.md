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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Mailbox provides an email and collaboration API documented at the welcome page.
  name: Mailbox API
  slug: mailbox-api
- description: 'mailbox.org API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: mailbox.org API
  slug: mailbox-org-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/mailbox-org/rules/mailbox-org-rules.yml
  title: ''
  type: Spectral
  url: rules/mailbox-org-rules.yml
- group: design
  href: https://artifacts.apis.io/mailbox-org/json-ld/mailbox-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mailbox-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/mailbox-org/vocabulary/mailbox-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mailbox-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mailbox-org/data-model/mailbox-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mailbox-org-data-model.yml
- group: auth
  href: https://artifacts.apis.io/mailbox-org/security/mailbox-org-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mailbox-org-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/mailbox-org/conformance/mailbox-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mailbox-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mailbox-org/llms/mailbox-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mailbox-org-llms.txt
- group: auth
  href: https://artifacts.apis.io/mailbox-org/well-known/mailbox-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mailbox-org-security.txt
- group: agent
  href: https://artifacts.apis.io/mailbox-org/well-known/mailbox-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mailbox-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/mailbox-org/hosts/mailbox-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailbox-org-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://mailbox.org/de/news/
- group: auth
  href: https://artifacts.apis.io/mailbox-org/security/mailbox-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mailbox-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mailbox-org/security/mailbox-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailbox-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mailbox.org/
- group: docs
  title: ''
  type: Documentation
  url: https://kb.mailbox.org/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mailbox.org/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mailbox.org
- group: operate
  title: ''
  type: Support
  url: https://support.mailbox.org
- group: company
  title: ''
  type: Blog
  url: https://mailbox.org/en/blog/
coverage:
  checked: '2026-10-27'
  detail: Documentation is served as HTML pages without a discoverable OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://api.mailbox.org/v1/doc/welcome/welcome.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: mailbox.org provides a secure, privacy‑focused email and collaboration suite for individuals and businesses. Hosted in German data centres, it offers encrypted mail, cloud drive, video meetings, and office tools, all compliant with GDPR, ISO 27001 and BSI C5. The service emphasizes data sovereignty, green energy operation, and a range of pricing plans from personal to enterprise.
image: https://mailbox.org/sites/default/files/styles/opengraph_recommended/public/2025-07/01_header_mockup_250714.jpg?h=4688e0a3&itok=an2JkaQz
json_schemas:
- name: PostV1Request
  property_count: 4
  slug: mailbox-org-post-v1-request
- name: PostV1Response
  property_count: 3
  slug: mailbox-org-post-v1-response
jsonld:
- class_count: 2
  name: Mailbox Org Context
  property_count: 5
  slug: mailbox-org-context
layout: provider
modified: '2026-10-27'
name: mailbox.org
nav: Providers
network: true
overview: 'mailbox.org is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Collaboration, Privacy, GDPR, and German.


  The mailbox.org catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  mailbox.org''s developer surface includes documentation, support, engineering blog, and 16 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: mailbox.org API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: mailbox-org-rules
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 26.2
    discoverability: 58.9
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mailbox Org Domain Security
  slug: mailbox-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mailbox Org Vulnerability Disclosure
  slug: mailbox-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mailbox-org
tags:
- Email
- Collaboration
- Privacy
- GDPR
- German
website: https://mailbox.org/
---
