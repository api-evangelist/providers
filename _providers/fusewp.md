---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The hosted OAuth authorization broker FuseWP operates at auth.fusewp.com. The self-hosted FuseWP plugin cannot safely hold OAuth client secrets for the partner platforms it connects to, so it delegate
  name: FuseWP OAuth Broker
  slug: oauth-broker
artifact_total: 7
common:
- group: auth
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
  title: ''
  type: Packages
  url: packages/fusewp-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fusewp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fusewp-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fusewp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fusewp-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fusewp-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fusewp-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fusewp-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fusewp-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fusewp-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fusewp-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fusewp-mcp.yml
created: '2026-08-12'
description: 'FuseWP is a WordPress automation plugin from the FuseWP Team (ProperFraction) that synchronizes WordPress users, customers, members and form leads with more than thirty email marketing platforms and CRMs — including Mailchimp, ActiveCampaign, Constant Contact, HubSpot, Klaviyo, Brevo, MailerLite, Salesforce, Zoho CRM, Keap, AWeber, GoHighLevel, SendPulse and Google Sheets. It maps WordPress user roles, WooCommerce/EDD orders, LMS enrollments (LearnDash, LifterLMS, Tutor LMS, Sensei), membership plugins (MemberPress, Paid Memberships Pro, Restrict Content Pro) and form submissions (Contact Form 7, Gravity Forms, WPForms, Fluent Forms) to lists, tags and custom fields in the connected platform. FuseWP is primarily an API CONSUMER rather than an API producer: the plugin runs self-hosted inside the customer''s WordPress installation and registers no REST routes of its own. Its one first-party HTTP surface is a hosted OAuth broker at auth.fusewp.com that holds FuseWP''s OAuth client
  credentials and brokers the authorization-code and refresh-token exchange for the eleven partner platforms that require OAuth.'
image: https://fusewp.com/wp-content/uploads/2023/06/fusewp-wordpress-plugin.png
layout: provider
mcp_servers:
- description: ''
  name: FuseWP MCP Server
  slug: fusewp-mcp-server
modified: '2026-08-12'
name: FuseWP
nav: Providers
network: true
overview: 'FuseWP publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WordPress, Email Marketing, Marketing Automation, and CRM.


  FuseWP''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 19 more developer resources.'
plans:
- name: Fusewp Plans Pricing
  plan_count: 7
  slug: fusewp-plans-pricing
random_paper: 15
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
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 37.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
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
- Authentication
- Plugins
- No-Code
website: https://fusewp.com/
---
