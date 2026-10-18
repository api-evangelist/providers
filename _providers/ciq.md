---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.6
  scored_at: '2026-10-17'
api_count: 8
apis:
- description: API documentation is hosted at docs.ciq.com, but no machine‑readable contract was discovered.
  name: CIQ API
  slug: ciq-api-2
- baseURL: https://depot.ciq.com
  baseurl_source: declared
  description: The Agent API from CIQ — 1 operation(s) for agent.
  name: CIQ Agent API
  slug: ciq-agent-api
- baseURL: https://depot.ciq.com
  baseurl_source: declared
  description: The CIQ API API from CIQ — 2 operation(s) for ciq api.
  name: CIQ CIQ API
  slug: ciq-ciq-api-api
- baseURL: https://depot.ciq.com
  baseurl_source: declared
  description: The Data API from CIQ — 1 operation(s) for data.
  name: CIQ Data API
  slug: ciq-data-api
- baseURL: https://depot.ciq.com
  baseurl_source: declared
  description: The Dlv2 API from CIQ — 4 operation(s) for dlv2.
  name: CIQ Dlv2 API
  slug: ciq-dlv2-api
- baseURL: https://depot.ciq.com
  baseurl_source: declared
  description: The Models API from CIQ — 1 operation(s) for models.
  name: CIQ Models API
  slug: ciq-models-api
- baseURL: https://depot.ciq.com
  baseurl_source: declared
  description: The Path API from CIQ — 1 operation(s) for path.
  name: CIQ Path API
  slug: ciq-path-api
- baseURL: https://depot.ciq.com
  baseurl_source: declared
  description: The Sources API from CIQ — 1 operation(s) for sources.
  name: CIQ Sources API
  slug: ciq-sources-api
artifact_total: 15
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ciq.com/legal/terms-of-use/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/plans/ciq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ciq-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/rules/ciq-rules.yml
  title: ''
  type: Spectral
  url: rules/ciq-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/json-ld/ciq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ciq-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/vocabulary/ciq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ciq-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/data-model/ciq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ciq-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/changelog/ciq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ciq-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/authentication/ciq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ciq-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/conformance/ciq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ciq-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/llms/ciq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ciq-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/well-known/ciq-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ciq-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/well-known/ciq-internal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ciq-internal-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/well-known/ciq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ciq-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/hosts/ciq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ciq-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/vendors/ciq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ciq-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://ciq.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://ciq.com/press
- group: other
  title: ''
  type: Leadership
  url: https://ciq.com/company/leadership
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ctrliq
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.ciq.com/?ref=resources&ref_cta=portal_home
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ciq.com/ciq-bridge/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/security/ciq-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ciq-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ciq/refs/heads/main/security/ciq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ciq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ciq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ciq.com
- group: company
  title: ''
  type: Blog
  url: https://ciq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ciq.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ciq.com/legal/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://ciq.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: CIQ provides a sovereign AI infrastructure platform built on Rocky Linux, offering secure, scalable solutions for enterprises, research institutions, and government agencies. Their product suite includes Rocky Linux Pro, Fuzzball, Warewulf Pro, Ascender Pro, and CIQ Bridge, along with long‑term support and migration services. CIQ focuses on open‑source ethos and partnerships with NVIDIA, AMD, and others, delivering a full stack for AI at scale.
image: https://ciq.com/og-image.png
json_schemas:
- name: GetV1ModelsResponse
  property_count: 2
  slug: ciq-get-v1-models-response
jsonld:
- class_count: 1
  name: Ciq Context
  property_count: 2
  slug: ciq-context
layout: provider
modified: '2026-10-08'
name: CIQ
nav: Providers
network: true
overview: 'CIQ is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Agent API, CIQ API, Data API, and 5 more. Tagged areas include Artificial Intelligence, Infrastructure, Open Source, Enterprise, and Cloud.


  The CIQ catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CIQ''s developer surface includes changelog, authentication, getting-started guide, documentation, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Ciq Plans Pricing
  plan_count: 18
  slug: ciq-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: CIQ API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: ciq-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.2
    catalog_earned_first_party: 12.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 19.1
    developer_ergonomics: 45.2
    discoverability: 73.2
    operational_transparency: 31.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Ciq Authentication
  slug: ciq-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ciq Domain Security
  slug: ciq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ciq Vulnerability Disclosure
  slug: ciq-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ciq
tags:
- Artificial Intelligence
- Infrastructure
- Open Source
- Enterprise
- Cloud
website: https://ciq.com/
---
