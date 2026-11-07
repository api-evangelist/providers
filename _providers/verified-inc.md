---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
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
  score: 25.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://core-api.verified.inc
  baseurl_source: declared
  description: Verified Core API v2 (1-Click Signup, 1-Click Verify, 1-Click Health), REST at https://core-api.verified.inc/v2 with a sandbox at https://core-api.sandbox-verifiedinc.com/v2. The contract was generate
  name: Verified API
  slug: verified-inc-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/verified-inc/rate-limits/verified-inc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/verified-inc-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/verified-inc/rules/verified-inc-rules.yml
  title: ''
  type: Spectral
  url: rules/verified-inc-rules.yml
- group: design
  href: https://artifacts.apis.io/verified-inc/json-ld/verified-inc-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/verified-inc-context.jsonld
- group: design
  href: https://artifacts.apis.io/verified-inc/vocabulary/verified-inc-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/verified-inc-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/verified-inc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/verified-inc/data-model/verified-inc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/verified-inc-data-model.yml
- group: design
  href: https://artifacts.apis.io/verified-inc/components/verified-inc-components.yml
  title: ''
  type: Components
  url: components/verified-inc-components.yml
- group: operate
  href: https://artifacts.apis.io/verified-inc/changelog/verified-inc-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/verified-inc-changelog.yml
- group: design
  href: https://artifacts.apis.io/verified-inc/conventions/verified-inc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/verified-inc-conventions.yml
- group: start
  href: https://artifacts.apis.io/verified-inc/sandbox/verified-inc-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/verified-inc-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://verified.inc/trust
- group: auth
  href: https://artifacts.apis.io/verified-inc/authentication/verified-inc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/verified-inc-authentication.yml
- group: design
  href: https://artifacts.apis.io/verified-inc/lifecycle/verified-inc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/verified-inc-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/verified-inc/errors/verified-inc-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/verified-inc-error-codes.yml
- group: design
  href: https://artifacts.apis.io/verified-inc/errors/verified-inc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/verified-inc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/verified-inc/conformance/verified-inc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/verified-inc-conformance.yml
- group: other
  href: https://artifacts.apis.io/verified-inc/overlays/verified-inc-openapi-generated-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/verified-inc-openapi-generated-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/verified-inc/llms/verified-inc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/verified-inc-llms.txt
- group: agent
  href: https://artifacts.apis.io/verified-inc/well-known/verified-inc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/verified-inc-well-known.yml
- group: other
  href: https://artifacts.apis.io/verified-inc/hosts/verified-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/verified-inc-hosts.yml
- group: other
  href: https://artifacts.apis.io/verified-inc/vendors/verified-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/verified-inc-vendors.yml
- group: build
  href: https://artifacts.apis.io/verified-inc/packages/verified-inc-packages.yml
  title: ''
  type: SDKs
  url: packages/verified-inc-packages.yml
- group: build
  href: https://artifacts.apis.io/verified-inc/packages/verified-inc-packages.yml
  title: ''
  type: Packages
  url: packages/verified-inc-packages.yml
- group: auth
  href: https://artifacts.apis.io/verified-inc/security/verified-inc-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/verified-inc-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/verified-inc/security/verified-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verified-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verified.inc/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.verified.inc
- group: docs
  title: ''
  type: APIReference
  url: https://docs.verified.inc/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.verified.inc/index.md
- group: start
  title: ''
  type: Login
  url: https://dashboard.verified.inc/
- group: start
  title: ''
  type: SignUp
  url: https://1-click.demo.verified.inc/register?product=TextToSignup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VerifiedInc
- group: operate
  title: ''
  type: StatusPage
  url: https://verified.instatus.com
- group: operate
  title: ''
  type: Support
  url: https://verified.inc/contact
- group: company
  title: ''
  type: About
  url: https://verified.inc/about
- group: commercial
  title: ''
  type: Legal
  url: https://verified.inc/legal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.prod.website-files.com/6ab714a5dd3542d60e567c99/6ac938d72569ccfe2f49c609_verified-terms-of-use-2026-06-17.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/6ab714a5dd3542d60e567c99/6ac938d776f3825d37b0489e_verified-privacy-policy-2024-05-20.pdf
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.verified.inc/llms.txt
- group: other
  title: ''
  type: CaseStudies
  url: https://verified.inc/case-studies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verified-network
- group: company
  title: ''
  type: Twitter
  url: https://x.com/_Veri_fied_
created: '2026-11-03'
description: Verified (legal entity Verified Network Inc., verified.inc) provides identity and onboarding APIs that autofill and verify user data at signup to boost conversion. Its products are 1-Click Verify (verified phone numbers, often with no code to type), 1-Click Signup (name, address, birthday, SSN and more filled in from a phone number), 1-Click Health (health insurance, eligibility and benefits in seconds) and Text to Signup, serving financial services, healthcare, insurance and gaming / prediction-market companies. Developers integrate through a REST API and SDKs documented at docs.verified.inc, with keys managed in the Verified Dashboard.
image: https://cdn.prod.website-files.com/6ab714a5dd3542d60e567c99/6ad2cba4a9d89deb3b61efd1_og-home-v5.jpg
json_schemas:
- name: GetV21ClickIdentityuuidResponse
  property_count: 1
  slug: verified-inc-get-v21-click-identityuuid-response
- name: PostV21ClickRequest
  property_count: 1
  slug: verified-inc-post-v21-click-request
jsonld:
- class_count: 3
  name: Verified Inc Context
  property_count: 2
  slug: verified-inc-context
layout: provider
modified: '2026-11-03'
name: Verified
nav: Providers
network: true
overview: 'Verified is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity Verification, Onboarding, Phone Verification, and KYC.


  The Verified catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Verified''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, signup flow, and 35 more developer resources.'
plans:
- name: Verified Inc Plans Pricing
  plan_count: 0
  slug: verified-inc-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Verified Inc Rate Limits
  slug: verified-inc-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Verified API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: verified-inc-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 21.6
    developer_ergonomics: 49.4
    discoverability: 73.2
    operational_transparency: 57.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Verified Inc Authentication
  slug: verified-inc-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Verified Inc Domain Security
  slug: verified-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Verified Inc Trust Center
  slug: verified-inc-trust-center
  summary_line: SOC 2, HIPAA
skill_count: 3
skills:
- name: verified-inc-1-click-health-payers
  slug: verified-inc-1-click-health-payers
- name: verified-inc-1-click-signup
  slug: verified-inc-1-click-signup
- name: verified-inc-1-click-verify-channels
  slug: verified-inc-1-click-verify-channels
slug: verified-inc
tags:
- Company
- Identity Verification
- Onboarding
- Phone Verification
- KYC
- Autofill
- Health Insurance
- Fintech
website: https://verified.inc/
---
