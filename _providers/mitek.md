---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Mitek Identity Cloud API V2 - REST API for identity document verification (verify dossier, document extraction, AAMVA checks, German eID), biometric enrollment and verification, check-quality and a fa
  name: Mitek Identity Cloud API
  slug: mitek-identity-cloud-api
- description: MiVIP all-in-one digital identity verification platform; its developer documentation on docs.miteksystems.com (ReadMe) requires a Mitek login (401 redirect to oauth.readme.io/p/mitek).
  name: Mitek MiVIP
  slug: mivip
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/mitek/plans/mitek-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mitek-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mitek/conventions/mitek-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mitek-conventions.yml
- group: auth
  href: https://artifacts.apis.io/mitek/authentication/mitek-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mitek-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mitek/scopes/mitek-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mitek-scopes.yml
- group: operate
  href: https://artifacts.apis.io/mitek/lifecycle/mitek-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/mitek-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mitek/lifecycle/mitek-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mitek-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mitek/errors/mitek-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mitek-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mitek/conformance/mitek-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mitek-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mitek/llms/mitek-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mitek-llms.txt
- group: other
  href: https://artifacts.apis.io/mitek/hosts/mitek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mitek-hosts.yml
- group: other
  href: https://artifacts.apis.io/mitek/vendors/mitek-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mitek-vendors.yml
- group: build
  href: https://artifacts.apis.io/mitek/packages/mitek-packages.yml
  title: ''
  type: SDKs
  url: packages/mitek-packages.yml
- group: build
  href: https://artifacts.apis.io/mitek/packages/mitek-packages.yml
  title: ''
  type: Packages
  url: packages/mitek-packages.yml
- group: auth
  href: https://artifacts.apis.io/mitek/security/mitek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mitek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://miteksystems.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.miteksystems.com/
- group: company
  title: ''
  type: Blog
  url: https://www.miteksystems.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.miteksystems.com/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.miteksystems.com/products/biometric-authentication/plans
- group: operate
  title: ''
  type: Support
  url: https://www.miteksystems.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.miteksystems.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.miteksystems.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mitek-Systems
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.miteksystems.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mitek-systems-inc-
created: '2026-10-18'
description: Mitek (Mitek Systems, Inc.) is a digital identity and fraud defense company whose platform lets businesses know their customers, verify transactions and grow securely with identity verification and authentication in a single platform. Its products include MiVIP, an all-in-one digital identity verification solution for managing customer identities, combating fraud and meeting regulatory compliance, and Check Fraud Defender, an AI-powered, cloud-hosted, consortium-based check fraud platform including the MiControl fraud management console, alongside biometric authentication plans.
image: https://www.miteksystems.com/files/styles/rectangle_xl/public/img/misc/mitek-social-sharing-image-2026-en.jpg?itok=9OSwz-1D
layout: provider
mcp_servers:
- description: MCP endpoint served at /mcp on Mitek's ReadMe-hosted developer documentation (docs.miteksystems.com, which hosts the MiVIP docs; docs-access.miteksystems.com answers the same way). An anonymous JSON-R
  name: Mitek Documentation MCP Server
  slug: mitek-documentation-mcp-server
modified: '2026-10-18'
name: Mitek
nav: Providers
network: true
overview: 'Mitek is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity Verification, Fraud Prevention, Biometric Authentication, and KYC.


  Mitek''s developer surface includes authentication, documentation, engineering blog, pricing, support, and 20 more developer resources.'
plans:
- name: Mitek Plans Pricing
  plan_count: 2
  slug: mitek-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Mitek Rate Limits
  slug: mitek-rate-limits
scopes:
- name: Mitek Scopes
  scope_count: 2
  slug: mitek-scopes
  summary_line: 2 scopes
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 67.5
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 29.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mitek/mitek-2026-11-03T135704.png
security:
- kind: authentication
  name: Mitek Authentication
  slug: mitek-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mitek Domain Security
  slug: mitek-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mitek
tags:
- Company
- Identity Verification
- Fraud Prevention
- Biometric Authentication
- KYC
- Check Fraud
- Financial Services
website: https://miteksystems.com
---
