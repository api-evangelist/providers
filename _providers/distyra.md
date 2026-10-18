---
agent_readiness:
  band: agent-aware
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 26
  human_in_the_loop: 3
  name: Distyra Agentic Access
  operation_count: 50
  slug: distyra-agentic-access
  summary_line: 50 operations · 26 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.distyra.com
  baseurl_source: declared
  description: The authentication API from Brightfield Software — 1 operation(s) for authentication.
  name: Brightfield Software Authentication API
  slug: distyra-authentication-api
- baseURL: https://api.distyra.com
  baseurl_source: declared
  description: The billing API from Brightfield Software — 2 operation(s) for billing.
  name: Brightfield Software Billing API
  slug: distyra-billing-api
- baseURL: https://api.distyra.com
  baseurl_source: declared
  description: Read access to merchant catalog + taxonomy
  name: Brightfield Software Catalog API
  slug: distyra-catalog-api
- baseURL: https://api.distyra.com
  baseurl_source: declared
  description: 'Live PSD2/AIS bank connections (Distyra Connect). Fetch normalized transactions from a bank account on demand. Nothing is stored. `mode` says whose account it is: `own` (your organization’s), `end_use'
  name: Brightfield Software Connect API
  slug: distyra-connect-api
- baseURL: https://api.distyra.com
  baseurl_source: declared
  description: Single + batch enrichment
  name: Brightfield Software Enrichment API
  slug: distyra-enrichment-api
- baseURL: https://api.distyra.com
  baseurl_source: declared
  description: Customer corrections + confirmations
  name: Brightfield Software Feedback API
  slug: distyra-feedback-api
- baseURL: https://api.distyra.com
  baseurl_source: declared
  description: Health, version, status
  name: Brightfield Software System API
  slug: distyra-system-api
- baseURL: https://api.distyra.com
  baseurl_source: declared
  description: 'Applicant-level underwriting feature layer: turnover, recurring revenue, debt service, customer concentration, tax payments, statutory contributions. Lender-side persistence only (7-day re-fetch windo'
  name: Brightfield Software Underwriting API
  slug: distyra-underwriting-api
- baseURL: https://api.distyra.com
  baseurl_source: declared
  description: 'Webhook endpoint management (register, list, rotate signing secret). What arrives at your URL is the `WebhookDelivery` schema: the envelope, the fields on each event, the retry schedule, and how to ve'
  name: Brightfield Software Webhooks API
  slug: distyra-webhooks-api
artifact_total: 16
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/agentic-access/distyra-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/distyra-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/plans/distyra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/distyra-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/rules/distyra-rules.yml
  title: ''
  type: Spectral
  url: rules/distyra-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/json-ld/distyra-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/distyra-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/vocabulary/distyra-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/distyra-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/data-model/distyra-data-model.yml
  title: ''
  type: DataModel
  url: data-model/distyra-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/changelog/distyra-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/distyra-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/lifecycle/distyra-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/distyra-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/lifecycle/distyra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/distyra-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/errors/distyra-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/distyra-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/conformance/distyra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/distyra-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/well-known/distyra-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/distyra-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/well-known/distyra-distyra-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/distyra-distyra-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/well-known/distyra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/distyra-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/hosts/distyra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/distyra-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/packages/distyra-packages.yml
  title: ''
  type: SDKs
  url: packages/distyra-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/packages/distyra-packages.yml
  title: ''
  type: Packages
  url: packages/distyra-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.distyra.eu/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.distyra.eu/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/authentication/distyra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/distyra-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/security/distyra-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/distyra-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/distyra/refs/heads/main/security/distyra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/distyra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://distyra.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://www.distyra.eu/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.distyra.eu/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.distyra.eu/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.distyra.eu/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.distyra.eu/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.distyra.eu/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.distyra.eu/tos
- group: operate
  title: ''
  type: Support
  url: https://www.distyra.eu/contact
created: '2026-10-16'
description: Brightfield Software, operating under the Distyra brand, provides European bank data APIs that deliver raw transaction information distilled into actionable signals. Their platform offers products for data enrichment, underwriting, and compliance, tailored to European payment formats and regulations. Built in the EU, Distyra ensures data residency and privacy, supporting developers with comprehensive documentation, pricing plans, and a status page. The service aims to simplify access to bank data for fintech applications, offering a free tier and enterprise options.
image: https://www.distyra.eu/assets/og/distyra-og.png
jsonld:
- class_count: 1
  name: Distyra Context
  property_count: 27
  slug: distyra-context
layout: provider
modified: '2026-10-16'
name: Brightfield Software
nav: Providers
network: true
overview: 'Brightfield Software publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Billing API, Catalog API, and 6 more. Tagged areas include Company, Banking, Fintech, and European.


  The Brightfield Software catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Brightfield Software''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, support, and 25 more developer resources.'
plans:
- name: Distyra Plans Pricing
  plan_count: 7
  slug: distyra-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Brightfield Software API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 4
  slug: distyra-rules
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 56.0
    developer_ergonomics: 54.2
    discoverability: 57.1
    operational_transparency: 50.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Distyra Authentication
  slug: distyra-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Distyra Domain Security
  slug: distyra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Distyra Vulnerability Disclosure
  slug: distyra-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: distyra
tags:
- Company
- Banking
- Fintech
- European
website: https://distyra.eu/
---
