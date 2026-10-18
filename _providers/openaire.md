---
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
  score: 15.0
  scored_at: '2026-10-17'
api_count: 4
apis:
- baseURL: https://aai.openaire.eu
  baseurl_source: declared
  description: The Broker API from OpenAIRE — 3 operation(s) for broker.
  name: OpenAIRE Broker API
  slug: openaire-broker-api
- baseURL: https://aai.openaire.eu
  baseurl_source: declared
  description: The Oidc API from OpenAIRE — 1 operation(s) for oidc.
  name: OpenAIRE Oidc API
  slug: openaire-oidc-api
- baseURL: https://aai.openaire.eu
  baseurl_source: declared
  description: The OpenAIRE API API from OpenAIRE — 2 operation(s) for openaire api.
  name: OpenAIRE OpenAIRE API
  slug: openaire-openaire-api-api
- baseURL: https://aai.openaire.eu
  baseurl_source: declared
  description: The Skg If API from OpenAIRE — 2 operation(s) for skg if.
  name: OpenAIRE Skg If API
  slug: openaire-skg-if-api
artifact_total: 9
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/rules/openaire-rules.yml
  title: ''
  type: Spectral
  url: rules/openaire-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/json-ld/openaire-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openaire-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/vocabulary/openaire-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openaire-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/data-model/openaire-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openaire-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/changelog/openaire-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/openaire-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/conformance/openaire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openaire-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/hosts/openaire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openaire-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/packages/openaire-packages.yml
  title: ''
  type: SDKs
  url: packages/openaire-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/packages/openaire-packages.yml
  title: ''
  type: Packages
  url: packages/openaire-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openaire.eu/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.openaire.eu/newsroom
- group: operate
  title: ''
  type: ChangeLog
  url: https://graph.openaire.eu/docs/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openaire
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/openaire/refs/heads/main/security/openaire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openaire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openaire.eu
- group: docs
  title: ''
  type: Documentation
  url: https://www.openaire.eu/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: http://catalogue.openaire.eu
- group: operate
  title: ''
  type: Support
  url: https://www.openaire.eu/helpdesk
- group: company
  title: ''
  type: Blog
  url: https://www.openaire.eu/community/blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openaire.eu/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.openaire.eu/become-a-member
coverage:
  checked: '2026-10-14'
  detail: Documentation pages exist (e.g., https://graph.openaire.eu/docs/) but no machine‑readable OpenAPI/AsyncAPI/GraphQL contract was found.
  evidence:
  - status: 200
    url: https://graph.openaire.eu/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: OpenAIRE is a European infrastructure supporting open science and research. It provides services for researchers, funders, and institutions, including a service catalogue, policies, service level agreements, training, webinars, and community resources. The platform enables publishing, building infrastructure, and monitoring open science across Europe, fostering collaboration and compliance with EU research mandates.
json_schemas:
- name: GetSkgIfV1V1IdIdResponse
  property_count: 3
  slug: openaire-get-skg-if-v1-v1-id-id-response
- name: GetSkgIfV1V1IdResponse
  property_count: 3
  slug: openaire-get-skg-if-v1-v1-id-response
jsonld:
- class_count: 2
  name: Openaire Context
  property_count: 1
  slug: openaire-context
layout: provider
modified: '2026-10-14'
name: OpenAIRE
nav: Providers
network: true
overview: 'OpenAIRE is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Broker API, Oidc API, OpenAIRE API, and 1 more. Tagged areas include Company, Open Science, Research Infrastructure, Europe, and Services.


  The OpenAIRE catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenAIRE''s developer surface includes changelog, documentation, support, engineering blog, signup flow, and 16 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: OpenAIRE API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: openaire-rules
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 20.2
    developer_ergonomics: 33.3
    discoverability: 69.6
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Openaire Domain Security
  slug: openaire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openaire
tags:
- Company
- Open Science
- Research Infrastructure
- Europe
- Services
website: https://www.openaire.eu
---
