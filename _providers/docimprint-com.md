---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 1
  name: Docimprint Com Agentic Access
  operation_count: 47
  slug: docimprint-com-agentic-access
  summary_line: 47 operations · 26 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Billing API from DocImprint — 1 operation(s) for billing.
  name: DocImprint Billing API
  slug: docimprint-com-billing-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Check Claims API from DocImprint — 1 operation(s) for check claims.
  name: DocImprint Check Claims API
  slug: docimprint-com-check-claims-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Checkpoints API from DocImprint — 4 operation(s) for checkpoints.
  name: DocImprint Checkpoints API
  slug: docimprint-com-checkpoints-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Collections API from DocImprint — 7 operation(s) for collections.
  name: DocImprint Collections API
  slug: docimprint-com-collections-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Describe API from DocImprint — 1 operation(s) for describe.
  name: DocImprint Describe API
  slug: docimprint-com-describe-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Extract API from DocImprint — 15 operation(s) for extract.
  name: DocImprint Extract API
  slug: docimprint-com-extract-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Feedback API from DocImprint — 1 operation(s) for feedback.
  name: DocImprint Feedback API
  slug: docimprint-com-feedback-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Jobs API from DocImprint — 2 operation(s) for jobs.
  name: DocImprint Jobs API
  slug: docimprint-com-jobs-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Keys API from DocImprint — 1 operation(s) for keys.
  name: DocImprint Keys API
  slug: docimprint-com-keys-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Monitor API from DocImprint — 3 operation(s) for monitor.
  name: DocImprint Monitor API
  slug: docimprint-com-monitor-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Qa API from DocImprint — 1 operation(s) for qa.
  name: DocImprint Qa API
  slug: docimprint-com-qa-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Quickstart API from DocImprint — 1 operation(s) for quickstart.
  name: DocImprint Quickstart API
  slug: docimprint-com-quickstart-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Quota API from DocImprint — 1 operation(s) for quota.
  name: DocImprint Quota API
  slug: docimprint-com-quota-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Summarize API from DocImprint — 1 operation(s) for summarize.
  name: DocImprint Summarize API
  slug: docimprint-com-summarize-api
- baseURL: https://api.docimprint.com
  baseurl_source: declared
  description: The Translate API from DocImprint — 1 operation(s) for translate.
  name: DocImprint Translate API
  slug: docimprint-com-translate-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/docimprint-com/agentic-access/docimprint-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/docimprint-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/docimprint-com/rate-limits/docimprint-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/docimprint-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/docimprint-com/plans/docimprint-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docimprint-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/docimprint-com/rules/docimprint-com-rules.yml
  title: ''
  type: Spectral
  url: rules/docimprint-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/docimprint-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/docimprint-com/changelog/docimprint-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/docimprint-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/docimprint-com/conventions/docimprint-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/docimprint-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/docimprint-com/conventions/docimprint-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/docimprint-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/docimprint-com/authentication/docimprint-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docimprint-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/docimprint-com/errors/docimprint-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/docimprint-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/docimprint-com/conformance/docimprint-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docimprint-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docimprint-com/llms/docimprint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docimprint-com-llms.txt
- group: other
  href: https://artifacts.apis.io/docimprint-com/a2a/docimprint-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/docimprint-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/docimprint-com/well-known/docimprint-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docimprint-com-security.txt
- group: agent
  href: https://artifacts.apis.io/docimprint-com/well-known/docimprint-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docimprint-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/docimprint-com/hosts/docimprint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docimprint-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/docimprint-com/vendors/docimprint-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docimprint-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docimprint.com/terms
- group: auth
  title: ''
  type: Security
  url: https://docimprint.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docimprint.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docimprint.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://docimprint.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docimprint.com/docs/reference
- group: auth
  href: https://artifacts.apis.io/docimprint-com/security/docimprint-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/docimprint-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/docimprint-com/security/docimprint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docimprint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docimprint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docimprint.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://docimprint.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docimprint.com/docs
- group: operate
  title: ''
  type: Support
  url: https://docimprint.com/contact
created: '2026-11-06'
description: DocImprint provides a verifiable document layer for AI agents, offering tamper‑evident evidence bundles, cryptographic proofs, and pay‑per‑call pricing on Base. It enables agents to capture, analyze, and cite documents with cryptographic guarantees, supporting MCP‑native integration and x402 USDC payments. The platform includes OCR extraction, async processing, and webhooks for real‑time updates, targeting high‑trust AI applications.
image: https://docimprint.com/og-image.png
layout: provider
modified: '2026-11-06'
name: DocImprint
nav: Providers
network: true
overview: 'DocImprint publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Check Claims API, Checkpoints API, and 12 more. Tagged areas include Artificial Intelligence, Documents, Verification, Cryptography, and Payments.


  The DocImprint catalog on APIs.io includes 1 Spectral governance ruleset.


  DocImprint''s developer surface includes changelog, authentication, engineering blog, API reference, documentation, pricing, getting-started guide, and 23 more developer resources.'
plans:
- name: Docimprint Com Plans Pricing
  plan_count: 3
  slug: docimprint-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Docimprint Com Rate Limits
  slug: docimprint-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: DocImprint API Rules
  rule_count: 38
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 5
  slug: docimprint-com-rules
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 56.5
    catalog_earned_first_party: 20.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 44.3
    developer_ergonomics: 49.4
    discoverability: 57.1
    operational_transparency: 47.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Docimprint Com Authentication
  slug: docimprint-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Docimprint Com Domain Security
  slug: docimprint-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docimprint Com Vulnerability Disclosure
  slug: docimprint-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: docimprint-com-extract-and-retrieve
  slug: docimprint-com-extract-and-retrieve
slug: docimprint-com
tags:
- Artificial Intelligence
- Documents
- Verification
- Cryptography
- Payments
- Company
website: https://docimprint.com/
---
