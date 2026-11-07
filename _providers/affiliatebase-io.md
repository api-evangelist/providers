---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 37
  human_in_the_loop: 4
  name: Affiliatebase Io Agentic Access
  operation_count: 57
  slug: affiliatebase-io-agentic-access
  summary_line: 57 operations · 37 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: The Affiliate Coupons API from AffiliateBase — 4 operation(s) for affiliate coupons.
  name: AffiliateBase Affiliate Coupons API
  slug: affiliatebase-io-affiliate-coupons-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: The Affiliates API from AffiliateBase — 4 operation(s) for affiliates.
  name: AffiliateBase Affiliates API
  slug: affiliatebase-io-affiliates-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: The API Keys API from AffiliateBase — 2 operation(s) for api keys.
  name: AffiliateBase API Keys API
  slug: affiliatebase-io-api-keys-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: The Campaigns API from AffiliateBase — 2 operation(s) for campaigns.
  name: AffiliateBase Campaigns API
  slug: affiliatebase-io-campaigns-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: The Commissions API from AffiliateBase — 3 operation(s) for commissions.
  name: AffiliateBase Commissions API
  slug: affiliatebase-io-commissions-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: The Invitations API from AffiliateBase — 3 operation(s) for invitations.
  name: AffiliateBase Invitations API
  slug: affiliatebase-io-invitations-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: The Links API from AffiliateBase — 2 operation(s) for links.
  name: AffiliateBase Links API
  slug: affiliatebase-io-links-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: Session auth requires the `owner` or `admin` role.
  name: AffiliateBase Payout Exports API
  slug: affiliatebase-io-payout-exports-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: Session auth requires the `owner` or `admin` role.
  name: AffiliateBase Payout Runs API
  slug: affiliatebase-io-payout-runs-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: The Payouts API from AffiliateBase — 3 operation(s) for payouts.
  name: AffiliateBase Payouts API
  slug: affiliatebase-io-payouts-api
- baseURL: https://app.affiliatebase.io
  baseurl_source: declared
  description: The Referrals API from AffiliateBase — 2 operation(s) for referrals.
  name: AffiliateBase Referrals API
  slug: affiliatebase-io-referrals-api
artifact_total: 28
asyncapis:
- description: ''
  name: Affiliatebase Io Webhooks
  slug: affiliatebase-io-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/affiliatebase-io/agentic-access/affiliatebase-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/affiliatebase-io-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/affiliatebase-io/rate-limits/affiliatebase-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/affiliatebase-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/affiliatebase-io/rules/affiliatebase-io-rules.yml
  title: ''
  type: Spectral
  url: rules/affiliatebase-io-rules.yml
- group: design
  href: https://artifacts.apis.io/affiliatebase-io/json-ld/affiliatebase-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/affiliatebase-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/affiliatebase-io/vocabulary/affiliatebase-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/affiliatebase-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/affiliatebase-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/affiliatebase-io/data-model/affiliatebase-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/affiliatebase-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/affiliatebase-io/conventions/affiliatebase-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/affiliatebase-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/affiliatebase-io/conventions/affiliatebase-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/affiliatebase-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/security/affiliatebase-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/affiliatebase-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/authentication/affiliatebase-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/affiliatebase-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/scopes/affiliatebase-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/affiliatebase-io-scopes.yml
- group: design
  href: https://artifacts.apis.io/affiliatebase-io/errors/affiliatebase-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/affiliatebase-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/affiliatebase-io/conformance/affiliatebase-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/affiliatebase-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/affiliatebase-io/llms/affiliatebase-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affiliatebase-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/well-known/affiliatebase-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/affiliatebase-io-security.txt
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/well-known/affiliatebase-io-partners-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/affiliatebase-io-partners-security.txt
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/well-known/affiliatebase-io-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/affiliatebase-io-app-security.txt
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/well-known/affiliatebase-io-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/affiliatebase-io-api-security.txt
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/well-known/affiliatebase-io-affiliatebase-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/affiliatebase-io-affiliatebase-security.txt
- group: agent
  href: https://artifacts.apis.io/affiliatebase-io/well-known/affiliatebase-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/affiliatebase-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/affiliatebase-io/hosts/affiliatebase-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/affiliatebase-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/affiliatebase-io/vendors/affiliatebase-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/affiliatebase-io-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.affiliatebase.io/auth/signup?ab_source=marketing&ab_placement=header.desktop&ab_landing_path=%2F
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/security/affiliatebase-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/affiliatebase-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/affiliatebase-io/security/affiliatebase-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affiliatebase-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.affiliatebase.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.affiliatebase.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.affiliatebase.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.affiliatebase.io/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.affiliatebase.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.affiliatebase.io/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/affiliatebase
- group: commercial
  title: ''
  type: Pricing
  url: https://www.affiliatebase.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.affiliatebase.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.affiliatebase.io/privacy
created: '2026-11-01'
description: AffiliateBase provides a modern SaaS affiliate marketing platform that integrates tightly with Stripe to track referrals, calculate recurring commissions, and automate payouts via Stripe, PayPal, or Wise. Businesses can create custom affiliate portals, manage affiliates, view real-time analytics, and access a robust REST API and webhooks for deeper integration. The service emphasizes ease of use, transparent reporting, and flexible commission structures for subscription-based companies.
image: https://www.affiliatebase.io/og/index.png
json_schemas:
- name: AffiliatePromoCode
  property_count: 19
  slug: affiliatebase-io-affiliate-promo-code
- name: Affiliate
  property_count: 11
  slug: affiliatebase-io-affiliate
- name: CampaignWrite
  property_count: 28
  slug: affiliatebase-io-campaign-write
- name: Coupon
  property_count: 15
  slug: affiliatebase-io-coupon
- name: Invitation
  property_count: 11
  slug: affiliatebase-io-invitation
- name: Referral
  property_count: 8
  slug: affiliatebase-io-referral
jsonld:
- class_count: 30
  name: Affiliatebase Io Context
  property_count: 120
  slug: affiliatebase-io-context
layout: provider
modified: '2026-11-01'
name: AffiliateBase
nav: Providers
network: true
overview: 'AffiliateBase publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Affiliate Coupons API, Affiliates API, API Keys API, and 8 more. Tagged areas include Software-as-a-Service, Affiliate Marketing, Stripe, Payments, and Marketing Automation.


  The AffiliateBase catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  AffiliateBase''s developer surface includes authentication, signup flow, documentation, API reference, getting-started guide, support, pricing, and 29 more developer resources.'
plans:
- name: Affiliatebase Io Plans Pricing
  plan_count: 0
  slug: affiliatebase-io-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Affiliatebase Io Rate Limits
  slug: affiliatebase-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: AffiliateBase API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: affiliatebase-io-rules
scopes:
- name: Affiliatebase Io Scopes
  scope_count: 0
  slug: affiliatebase-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 66.8
    developer_ergonomics: 35.1
    discoverability: 66.1
    operational_transparency: 34.2
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 91.7
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Affiliatebase Io Authentication
  slug: affiliatebase-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Affiliatebase Io Domain Security
  slug: affiliatebase-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Affiliatebase Io Vulnerability Disclosure
  slug: affiliatebase-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: list-affiliates
  slug: affiliatebase-io-list-affiliates
slug: affiliatebase-io
tags:
- Software-as-a-Service
- Affiliate Marketing
- Stripe
- Payments
- Marketing Automation
website: https://www.affiliatebase.io/
---
