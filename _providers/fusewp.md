---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The hosted OAuth authorization broker FuseWP operates at auth.fusewp.com. The self-hosted FuseWP plugin cannot safely hold OAuth client secrets for the partner platforms it connects to, so it delegate
  name: FuseWP OAuth Broker
  slug: oauth-broker
artifact_total: 9
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://fusewp.com/blog/feed/
- group: auth
  href: https://artifacts.apis.io/fusewp/security/fusewp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fusewp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fusewp.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fusewp.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://fusewp.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://fusewp.com/article/installation-activation/
- group: operate
  title: ''
  type: Support
  url: https://fusewp.com/support/
- group: company
  title: ''
  type: Blog
  url: https://fusewp.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fusewp
- group: commercial
  title: ''
  type: Pricing
  url: https://fusewp.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://fusewp.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://fusewp.com/account/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fusewp.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fusewp.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://fusewp.com/changelog/
- group: build
  href: https://artifacts.apis.io/fusewp/packages/fusewp-packages.yml
  title: ''
  type: Packages
  url: packages/fusewp-packages.yml
- group: commercial
  href: https://artifacts.apis.io/fusewp/plans/fusewp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fusewp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fusewp/rate-limits/fusewp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fusewp-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/fusewp/authentication/fusewp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fusewp-authentication.yml
- group: auth
  href: https://artifacts.apis.io/fusewp/scopes/fusewp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fusewp-scopes.yml
- group: design
  href: https://artifacts.apis.io/fusewp/conventions/fusewp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fusewp-conventions.yml
- group: design
  href: https://artifacts.apis.io/fusewp/conformance/fusewp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fusewp-conformance.yml
- group: design
  href: https://artifacts.apis.io/fusewp/lifecycle/fusewp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fusewp-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/fusewp/changelog/fusewp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fusewp-changelog.yml
- group: agent
  href: https://artifacts.apis.io/fusewp/llms/fusewp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fusewp-llms.txt
- group: agent
  href: https://artifacts.apis.io/fusewp/well-known/fusewp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fusewp-well-known.yml
- group: agent
  href: https://artifacts.apis.io/fusewp/mcp/fusewp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fusewp-mcp.yml
created: '2026-08-12'
description: 'FuseWP is a WordPress automation plugin from the FuseWP Team (ProperFraction) that synchronizes WordPress users, customers, members and form leads with more than thirty email marketing platforms and CRMs — including Mailchimp, ActiveCampaign, Constant Contact, HubSpot, Klaviyo, Brevo, MailerLite, Salesforce, Zoho CRM, Keap, AWeber, GoHighLevel, SendPulse and Google Sheets. It maps WordPress user roles, WooCommerce/EDD orders, LMS enrollments (LearnDash, LifterLMS, Tutor LMS, Sensei), membership plugins (MemberPress, Paid Memberships Pro, Restrict Content Pro) and form submissions (Contact Form 7, Gravity Forms, WPForms, Fluent Forms) to lists, tags and custom fields in the connected platform. FuseWP is primarily an API CONSUMER rather than an API producer: the plugin runs self-hosted inside the customer''s WordPress installation and registers no REST routes of its own. Its one first-party HTTP surface is a hosted OAuth broker at auth.fusewp.com that holds FuseWP''s OAuth client
  credentials and brokers the authorization-code and refresh-token exchange for the eleven partner platforms that require OAuth.'
finops:
- has_sources: true
  method: derived
  name: Fusewp Finops
  primary_unit: 1 site
  service_category: ''
  slug: fusewp-finops
  template: false
image: https://fusewp.com/wp-content/uploads/2023/06/fusewp-wordpress-plugin.png
layout: provider
mcp_servers:
- description: Remote MCP server at fusewp.com.
  name: FuseWP MCP Server
  slug: fusewp-mcp-yml
modified: '2026-10-06'
name: FuseWP
nav: Providers
network: true
overview: 'FuseWP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WordPress, Email Marketing, Marketing Automation, and CRM.


  FuseWP''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 20 more developer resources.'
plans:
- name: Fusewp Plans Pricing
  plan_count: 6
  slug: fusewp-plans-pricing
- name: Fusewp Price Estimates
  plan_count: 0
  slug: fusewp-price-estimates
random_paper: 18
rate_limits:
- limit_count: 0
  name: Fusewp Rate Limits
  slug: fusewp-rate-limits
scopes:
- name: Fusewp Scopes
  scope_count: 0
  slug: fusewp-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.0
    operational_transparency: 18.4
  previous_composite: 41.8
  provenance:
    conformance: first-party
    mcp: site-plugin
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fusewp/fusewp-2026-10-11T185736.png
security:
- kind: authentication
  name: Fusewp Authentication
  slug: fusewp-authentication
  summary_line: oauth2/apiKey · 0 schemes
- kind: domain-security
  name: Fusewp Domain Security
  slug: fusewp-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: fusewp
tags:
- Company
- WordPress
- Email Marketing
- Marketing Automation
- CRM
- Integration
- Data Synchronization
- OAuth
- Plugins
- No-Code
- Authentication
website: https://fusewp.com/
---
