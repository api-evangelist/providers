---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Makespdf Com Agentic Access
  operation_count: 10
  slug: makespdf-com-agentic-access
  summary_line: 10 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://makespdf.com
  baseurl_source: declared
  description: The artifacts API from makespdf-com — 1 operation(s) for artifacts.
  name: makespdf-com Artifacts API
  slug: makespdf-com-artifacts-api
- baseURL: https://makespdf.com
  baseurl_source: declared
  description: The public API from makespdf-com — 2 operation(s) for public.
  name: makespdf-com Public API
  slug: makespdf-com-public-api
- baseURL: https://makespdf.com
  baseurl_source: declared
  description: The render API from makespdf-com — 3 operation(s) for render.
  name: makespdf-com Render API
  slug: makespdf-com-render-api
- baseURL: https://makespdf.com
  baseurl_source: declared
  description: The validate API from makespdf-com — 2 operation(s) for validate.
  name: makespdf-com Validate API
  slug: makespdf-com-validate-api
- baseURL: https://makespdf.com
  baseurl_source: declared
  description: The x402 API from makespdf-com — 2 operation(s) for x402.
  name: makespdf-com X402 API
  slug: makespdf-com-x402-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/makespdf-com/agentic-access/makespdf-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/makespdf-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/makespdf-com/plans/makespdf-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/makespdf-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/makespdf-com/rules/makespdf-com-rules.yml
  title: ''
  type: Spectral
  url: rules/makespdf-com-rules.yml
- group: design
  href: https://artifacts.apis.io/makespdf-com/json-ld/makespdf-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/makespdf-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/makespdf-com/vocabulary/makespdf-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/makespdf-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/makespdf-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/makespdf-com/data-model/makespdf-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/makespdf-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://makespdf.com/docs/discovery
- group: auth
  href: https://artifacts.apis.io/makespdf-com/authentication/makespdf-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/makespdf-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/makespdf-com/errors/makespdf-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/makespdf-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/makespdf-com/conformance/makespdf-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/makespdf-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/makespdf-com/llms/makespdf-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/makespdf-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/makespdf-com/well-known/makespdf-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/makespdf-com-security.txt
- group: agent
  href: https://artifacts.apis.io/makespdf-com/well-known/makespdf-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/makespdf-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/makespdf-com/hosts/makespdf-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/makespdf-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/makespdf-com/vendors/makespdf-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/makespdf-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/makespdf-com/packages/makespdf-com-packages.yml
  title: ''
  type: SDKs
  url: packages/makespdf-com-packages.yml
- group: build
  href: https://artifacts.apis.io/makespdf-com/packages/makespdf-com-packages.yml
  title: ''
  type: Packages
  url: packages/makespdf-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://makespdf.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://makespdf.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makesPDF
- group: start
  title: ''
  type: GettingStarted
  url: https://makespdf.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://makespdf.com/docs/api
- group: auth
  href: https://artifacts.apis.io/makespdf-com/security/makespdf-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/makespdf-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/makespdf-com/security/makespdf-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/makespdf-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://makespdf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://makespdf.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://makespdf.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://makespdf.com/blog
created: '2026-10-30'
description: MakesPDF.com provides a simple API to convert HTML, URLs, or raw content into PDF documents. The service offers customizable options such as page size, margins, headers, footers, and supports authentication via API keys. It is designed for developers needing reliable PDF generation in web applications, automation scripts, or server-side processes. The platform emphasizes ease of integration, fast processing, and high-quality output, making it suitable for invoicing, reporting, and document archiving.
image: https://makespdf.com/og-image.png
json_schemas:
- name: ArtifactList
  property_count: 4
  slug: makespdf-com-artifact-list
- name: RenderMetadata
  property_count: 11
  slug: makespdf-com-render-metadata
- name: TemplateList
  property_count: 4
  slug: makespdf-com-template-list
- name: Template
  property_count: 0
  slug: makespdf-com-template
- name: ValidationResult
  property_count: 3
  slug: makespdf-com-validation-result
jsonld:
- class_count: 9
  name: Makespdf Com Context
  property_count: 49
  slug: makespdf-com-context
layout: provider
modified: '2026-10-30'
name: makespdf-com
nav: Providers
network: true
overview: 'makespdf-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Artifacts API, Public API, Render API, and 2 more. Tagged areas include Company, PDF, API, Conversion, and Developer.


  The makespdf-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  makespdf-com''s developer surface includes authentication, getting-started guide, API reference, documentation, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Makespdf Com Plans Pricing
  plan_count: 4
  slug: makespdf-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: makespdf-com API Rules
  rule_count: 18
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 0
  slug: makespdf-com-rules
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.0
    catalog_earned_first_party: 12.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 64.7
    developer_ergonomics: 51.8
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Makespdf Com Authentication
  slug: makespdf-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Makespdf Com Domain Security
  slug: makespdf-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Makespdf Com Vulnerability Disclosure
  slug: makespdf-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: makespdf-com-render-pdf
  slug: makespdf-com-render-pdf
slug: makespdf-com
tags:
- Company
- PDF
- API
- Conversion
- Developer
website: https://makespdf.com/
---
