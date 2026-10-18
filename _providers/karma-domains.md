---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Karma Domains Agentic Access
  operation_count: 40
  slug: karma-domains-agentic-access
  summary_line: 40 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.karma.domains
  baseurl_source: declared
  description: The domains API from Karma.Domains — 12 operation(s) for domains.
  name: Karma.Domains Domains API
  slug: karma-domains-domains-api
- baseURL: https://api.karma.domains
  baseurl_source: declared
  description: The reports API from Karma.Domains — 10 operation(s) for reports.
  name: Karma.Domains Reports API
  slug: karma-domains-reports-api
- baseURL: https://api.karma.domains
  baseurl_source: declared
  description: The user API from Karma.Domains — 3 operation(s) for user.
  name: Karma.Domains User API
  slug: karma-domains-user-api
- baseURL: https://api.karma.domains
  baseurl_source: declared
  description: The webhooks API from Karma.Domains — 5 operation(s) for webhooks.
  name: Karma.Domains Webhooks API
  slug: karma-domains-webhooks-api
artifact_total: 16
asyncapis:
- description: ''
  name: Karma Domains Webhooks
  slug: karma-domains-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/agentic-access/karma-domains-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/karma-domains-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/rules/karma-domains-rules.yml
  title: ''
  type: Spectral
  url: rules/karma-domains-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/json-ld/karma-domains-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/karma-domains-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/vocabulary/karma-domains-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/karma-domains-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/asyncapi/karma-domains-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/karma-domains-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/data-model/karma-domains-data-model.yml
  title: ''
  type: DataModel
  url: data-model/karma-domains-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/cli/karma-domains-cli.yml
  title: ''
  type: CLI
  url: cli/karma-domains-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/errors/karma-domains-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/karma-domains-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/conformance/karma-domains-conformance.yml
  title: ''
  type: Conformance
  url: conformance/karma-domains-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/llms/karma-domains-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/karma-domains-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/well-known/karma-domains-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/karma-domains-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/hosts/karma-domains-hosts.yml
  title: ''
  type: Hosts
  url: hosts/karma-domains-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/vendors/karma-domains-vendors.yml
  title: ''
  type: Vendors
  url: vendors/karma-domains-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/packages/karma-domains-packages.yml
  title: ''
  type: SDKs
  url: packages/karma-domains-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/packages/karma-domains-packages.yml
  title: ''
  type: Packages
  url: packages/karma-domains-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://karma.domains/legal/terms.html
- group: operate
  title: ''
  type: Support
  url: https://karma.domains/en/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://karma.domains/legal/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://karma.domains/app/pricing/
- group: start
  title: ''
  type: Login
  url: https://karma.domains/app/auth/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/karma-domains
- group: docs
  title: ''
  type: Documentation
  url: https://api.karma.domains/docs
- group: company
  title: ''
  type: Blog
  url: https://karma.domains/en/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.karma.domains`
- group: docs
  title: ''
  type: APIReference
  url: https://karma.domains/en/expired-domains-api/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/authentication/karma-domains-authentication.yml
  title: ''
  type: Authentication
  url: authentication/karma-domains-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/karma-domains/refs/heads/main/security/karma-domains-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/karma-domains-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://karma.domains
created: '2026-10-06'
description: Karma.Domains provides a public REST API delivering comprehensive domain intelligence for expired and auctioned domains. Leveraging data from over 40 auction sources and 90+ SEO filters, the API returns metrics such as Ahrefs DR, Majestic TF/CF, Moz DA, SEMrush scores, SimilarWeb traffic, Wayback history, backlink counts, domain age, and more. Users can query up to 400,000+ newly expired domains daily, apply advanced filters, save annotations, and receive enriched SEO data. The service offers a Pro tier with bearer token authentication, rate‑limited to 60 requests per minute, enabling integration into SEO tools, market analysis, and competitive research workflows.
image: https://karma.domains/android-chrome-384x384.png
json_schemas:
- name: PublicUserProfileSchema
  property_count: 16
  slug: karma-domains-public-user-profile-schema
- name: ReportFullResponseSchema
  property_count: 25
  slug: karma-domains-report-full-response-schema
- name: ReportListFilterSchema
  property_count: 154
  slug: karma-domains-report-list-filter-schema
- name: WebhookSubscriptionResponse
  property_count: 15
  slug: karma-domains-webhook-subscription-response
- name: WebsitePageCounterResponseSchema
  property_count: 6
  slug: karma-domains-website-page-counter-response-schema
- name: WhoisLookupResultSchema
  property_count: 12
  slug: karma-domains-whois-lookup-result-schema
jsonld:
- class_count: 86
  name: Karma Domains Context
  property_count: 489
  slug: karma-domains-context
layout: provider
modified: '2026-10-06'
name: Karma.Domains
nav: Providers
network: true
overview: 'Karma.Domains publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Domains API, Reports API, User API, and 1 more. Tagged areas include Company, SEO, Domains, and Data.


  The Karma.Domains catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Karma.Domains'' developer surface includes CLI, support, pricing, documentation, engineering blog, API reference, authentication, and 22 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Karma.Domains API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: karma-domains-rules
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 79.8
    developer_ergonomics: 61.3
    discoverability: 64.3
    operational_transparency: 13.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Karma Domains Authentication
  slug: karma-domains-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Karma Domains Domain Security
  slug: karma-domains-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: karma-domains
tags:
- Company
- SEO
- Domains
- Data
website: https://karma.domains
---
