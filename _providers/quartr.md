---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.quartr.com
  baseurl_source: declared
  description: The Public API from Quartr — 3 operation(s) for public.
  name: Quartr Public API
  slug: quartr-public-api
artifact_total: 10
asyncapis:
- description: ''
  name: Quartr Webhooks
  slug: quartr-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/plans/quartr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quartr-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/rules/quartr-rules.yml
  title: ''
  type: Spectral
  url: rules/quartr-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/json-ld/quartr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/quartr-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/vocabulary/quartr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/quartr-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/asyncapi/quartr-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/quartr-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/data-model/quartr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quartr-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/changelog/quartr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/quartr-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://quartr.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/conformance/quartr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quartr-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/llms/quartr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quartr-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/well-known/quartr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quartr-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/well-known/quartr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quartr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/hosts/quartr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quartr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/vendors/quartr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quartr-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.quartr.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/security/quartr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/quartr-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quartr/refs/heads/main/security/quartr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quartr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quartr.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.quartr.dev
- group: docs
  title: ''
  type: Documentation
  url: https://quartr.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://quartr.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://quartr.com/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://quartr.com/docs/support
- group: company
  title: ''
  type: Blog
  url: https://quartr.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quartr
- group: commercial
  title: ''
  type: Pricing
  url: https://quartr.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://quartr.com/contact-sales
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quartr.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quartr.com/terms-of-service/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/quartr/workspace/quartr-api
coverage:
  checked: '2026-10-15'
  detail: The OpenAPI endpoint https://api.quartr.com/openapi.json returned HTTP 200 but an empty body, providing no machine‑readable contract.
  evidence:
  - status: 200
    url: https://api.quartr.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Quartr provides AI-powered infrastructure for company research, delivering real-time first‑party data from public companies to investment professionals, research platforms, and financial AI applications. Their platform aggregates earnings calls, transcripts, filings, and slides, enabling rapid insight extraction, trend detection, and automated analysis across over 16,000 companies. Quartr partners with OpenAI’s ChatGPT for Financial Services and serves major financial firms, offering both proprietary data engines and API access for seamless integration into analytics pipelines.
image: https://a.storyblok.com/f/182663/9850/bf56850515/variant-12-standard_og-home.png/m/1200x630
json_schemas:
- name: GetPublicV3CompaniesIdSegmentsResponse
  property_count: 2
  slug: quartr-get-public-v3-companies-id-segments-response
- name: GetPublicV3DocumentsDocumentidResponse
  property_count: 2
  slug: quartr-get-public-v3-documents-documentid-response
- name: GetPublicV3V3IdResponse
  property_count: 2
  slug: quartr-get-public-v3-v3-id-response
jsonld:
- class_count: 3
  name: Quartr Context
  property_count: 2
  slug: quartr-context
layout: provider
modified: '2026-10-15'
name: Quartr
nav: Providers
network: true
overview: 'Quartr is listed with 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Artificial Intelligence, Finance, Data, and Research.


  The Quartr catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Quartr''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Quartr Plans Pricing
  plan_count: 2
  slug: quartr-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Quartr API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: quartr-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 64.8
    catalog_earned_first_party: 8.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 29.9
    developer_ergonomics: 50.0
    discoverability: 73.2
    operational_transparency: 55.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Quartr Domain Security
  slug: quartr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quartr Vulnerability Disclosure
  slug: quartr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: quartr
tags:
- Company
- Artificial Intelligence
- Finance
- Data
- Research
website: https://quartr.com/
---
