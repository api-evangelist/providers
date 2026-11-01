---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Kosli API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Kosli API
  slug: kosli-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/kosli/rules/kosli-rules.yml
  title: ''
  type: Spectral
  url: rules/kosli-rules.yml
- group: design
  href: https://artifacts.apis.io/kosli/json-ld/kosli-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kosli-context.jsonld
- group: design
  href: https://artifacts.apis.io/kosli/vocabulary/kosli-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kosli-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/kosli/data-model/kosli-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kosli-data-model.yml
- group: build
  href: https://artifacts.apis.io/kosli/cli/kosli-cli.yml
  title: ''
  type: CLI
  url: cli/kosli-cli.yml
- group: operate
  href: https://artifacts.apis.io/kosli/changelog/kosli-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kosli-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.kosli.com/security/
- group: design
  href: https://artifacts.apis.io/kosli/conformance/kosli-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kosli-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kosli/llms/kosli-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kosli-llms.txt
- group: other
  href: https://artifacts.apis.io/kosli/a2a/kosli-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kosli-a2a.yml
- group: agent
  href: https://artifacts.apis.io/kosli/well-known/kosli-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kosli-well-known.yml
- group: other
  href: https://artifacts.apis.io/kosli/hosts/kosli-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kosli-hosts.yml
- group: other
  href: https://artifacts.apis.io/kosli/vendors/kosli-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kosli-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kosli.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.kosli.com/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kosli-dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kosli.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kosli.com/
- group: auth
  href: https://artifacts.apis.io/kosli/security/kosli-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kosli-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/kosli/security/kosli-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kosli-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kosli/security/kosli-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kosli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kosli.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.kosli.com/
- group: company
  title: ''
  type: Blog
  url: https://www.kosli.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kosli.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kosli.com/privacy-policy/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kosli.com/privacy-policy/privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://www.kosli.com/contact/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kosli.com/getting-started-with-kosli-course/
created: '2026-10-29'
description: Kosli provides governance infrastructure for AI-driven software development lifecycle (SDLC). It offers an append‑only evidence store, automated compliance checks, AI‑powered insights, and integrations with CI pipelines to ensure secure, auditable software delivery. Backed by Heavybit and Deutsche Bank, Kosli helps teams enforce policies, track changes, and achieve continuous compliance across cloud and on‑prem environments.
image: https://www.kosli.com/images/kosli-sdlc-ai-social.jpg
json_schemas:
- name: GetActionsOrgActionnumberResponse
  property_count: 14
  slug: kosli-get-actions-org-actionnumber-response
- name: GetApiV2EnvironmentsYourorgnameResponse
  property_count: 1
  slug: kosli-get-api-v2-environments-yourorgname-response
- name: GetFlowsOrgResponse
  property_count: 2
  slug: kosli-get-flows-org-response
- name: GetReposOrgResponse
  property_count: 5
  slug: kosli-get-repos-org-response
- name: PostAttestationsOrgUploadsResponse
  property_count: 3
  slug: kosli-post-attestations-org-uploads-response
- name: PutFlowsOrgFlownameRenameResponse
  property_count: 2
  slug: kosli-put-flows-org-flowname-rename-response
jsonld:
- class_count: 11
  name: Kosli Context
  property_count: 23
  slug: kosli-context
layout: provider
modified: '2026-10-29'
name: Kosli
nav: Providers
network: true
overview: 'Kosli is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Governance, Compliance, and DevOps.


  The Kosli catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kosli''s developer surface includes CLI, changelog, API reference, engineering blog, pricing, support, getting-started guide, and 22 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Kosli API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: kosli-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 42.9
    discoverability: 58.9
    operational_transparency: 31.6
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
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Kosli Domain Security
  slug: kosli-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kosli Vulnerability Disclosure
  slug: kosli-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Kosli Trust Center
  slug: kosli-trust-center
  summary_line: SOC 2, HIPAA, GDPR, CSA STAR
slug: kosli
tags:
- Company
- AI
- Governance
- Compliance
- DevOps
website: https://www.kosli.com
---
