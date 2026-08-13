---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.1
  scored_at: '2026-08-12'
api_count: 44
apis:
- description: The original Cobot REST API, still available and still the only surface that carries the webhook subscription API. Documented per-resource on dev.cobot.me/api-docs; Cobot directs new integrations to A
  name: Cobot API v1 (legacy)
  slug: cobot-api-v1
- description: A hosted, remote Model Context Protocol server operated by Cobot at api.cobot.me/mcp. It is live and OAuth 2.0 protected — an anonymous tools/list returns 401 with an RFC 9728 WWW-Authenticate challen
  name: Cobot MCP Server
  slug: cobot-mcp
- description: A long-term allocation of a resource to a membership or team.
  name: Cobot Allocation API
  slug: cobot-allocation-api
- description: Approving terms & conditions, privacy policies etc. as a member of a space.
  name: Cobot Approval API
  slug: cobot-approval-api
- description: A help desk article explaning an aspect of the space.
  name: Cobot Article API
  slug: cobot-article-api
- description: A booking of a resource in the booking calendar.
  name: Cobot Booking API
  slug: cobot-booking-api
- description: Booking credits are added to plans and give memberships free booking time or a fixed amount of free bookings. The hourly rate of a resource can also be customized.
  name: Cobot Booking Credit API
  slug: cobot-booking-credit-api
- description: Email customizations for emails that can be sent via Cobot.
  name: Cobot Built-in Email Customizations API
  slug: cobot-built-in-email-customizations-api
- description: Blocks off a space for member/external bookings and drop-in passes.
  name: Cobot Calendar Blocker API
  slug: cobot-calendar-blocker-api
- description: Members check in to a space for attendance tracking and for using up their time passes.
  name: Cobot Check In API
  slug: cobot-check-in-api
- description: Non-member contacts a space has.
  name: Cobot Contact API
  slug: cobot-contact-api
- description: Cost centers are used to categorize invoice items. Anything that can be invoiced can be assigned a cost center. When a service/charge is added to an invoice, its cost center will be assigned to the re
  name: Cobot Cost Center API
  slug: cobot-cost-center-api
- description: A trial space can be converted to a customer
  name: Cobot Customer API
  slug: cobot-customer-api
- description: A discount code can be used to offer a discount for various products in a space.
  name: Cobot Discount Code API
  slug: cobot-discount-code-api
- description: Purchased drop-in passes.
  name: Cobot Drop-In Pass API
  slug: cobot-drop-in-pass-api
- description: A purchase of drop-in-passes, currently only supports buying one pass at a time.
  name: Cobot Drop-In Pass Purchase API
  slug: cobot-drop-in-pass-purchase-api
- description: Drop-in pass templates are templates for drop-in passes that can be bought by visitors.
  name: Cobot Drop-In Pass Template API
  slug: cobot-drop-in-pass-template-api
- description: Spaces can run events for their members or the public. Events are created and later published by admins, at which point members are able to see and attend them. Admins can also create messages for eve
  name: Cobot Event API
  slug: cobot-event-api
- description: After a resource has been enabled for external booking (see _External Resource_) it can be booked by visitors (non-members) using external booking endpoints. Making an external booking also results in
  name: Cobot External Booking API
  slug: cobot-external-booking-api
- description: A space's resources can be enabled for external booking, which means they can be booked by guests without a Cobot account or space membership. All resources enabled for external booking appear under e
  name: Cobot External Resource API
  slug: cobot-external-resource-api
- description: Invoices are automatically generated once a month, based on members' activity. In addition, manual invoices can be generated at any time.
  name: Cobot Invoice API
  slug: cobot-invoice-api
- description: Admins can send invoice reminders for overdue invoices.
  name: Cobot Invoice Reminder API
  slug: cobot-invoice-reminder-api
- description: Represents a person being a member in a space. Can optionally be connected to a User.
  name: Cobot Membership API
  slug: cobot-membership-api
- description: The plans belonging to a membership. When a membership is signed up one of the space's plans is selected and a copy is created for the membership. A membership's plan can be customized or changed over
  name: Cobot Membership Plan API
  slug: cobot-membership-plan-api
- description: Social profile for a membership.
  name: Cobot Membership Profile API
  slug: cobot-membership-profile-api
- description: Navigation links allow you to embed 3rd party apps on a space's Cobot UI. See also the single page app endpoints.
  name: Cobot Navigation Link API
  slug: cobot-navigation-link-api
- description: Multiple spaces can form a network. This allows their members to access multiple spaces, for example to book resources.
  name: Cobot Network API
  slug: cobot-network-api
- description: '*The payment API is in development. Endpoints may be missing or not working yet.* Payments allow any user (i.e. non-members) to pay for items on Cobot via the payment methods a space has set up. For n'
  name: Cobot Payment API
  slug: cobot-payment-api
- description: Spaces can set up payment methods that members can use to make payments to the space. Payment methods can be automated via a payment provider such as Stripe or manual (e.g. cash, bank transfer).
  name: Cobot Payment Method API
  slug: cobot-payment-method-api
- description: Products can be set up by a space and then used as booking extras or to create charges from. Examples are coffee, projectors, additional cleaning services etc.
  name: Cobot Product API
  slug: cobot-product-api
- description: A full or partial refund of an invoice.
  name: Cobot Refund API
  slug: cobot-refund-api
- description: A resource can be booked on an hourly basis using the booking calendar. Examples are conference rooms, presentation equipment, bikes etc.
  name: Cobot Resource API
  slug: cobot-resource-api
- description: Revenue accounts are used to categorize invoice items. Anything that can be invoiced can be assigned a revenue account. When a service/charge is added to an invoice, its revenue account will be assign
  name: Cobot Revenue Account API
  slug: cobot-revenue-account-api
- description: A single page app consists of HTML, CSS and JavaScript code. It can be embedded into the Cobot UI via navigation links.
  name: Cobot Single page app API
  slug: cobot-single-page-app-api
- description: A coworking space. Spaces can form a network to allow members access to multiple spaces.
  name: Cobot Space API
  slug: cobot-space-api
- description: Billing details of a space.
  name: Cobot Space Billing Details API
  slug: cobot-space-billing-details-api
- description: The payment method a space uses to pay their Cobot subscription.
  name: Cobot Space Payment Method API
  slug: cobot-space-payment-method-api
- description: Preview of a to-be-created space.
  name: Cobot Space Preview API
  slug: cobot-space-preview-api
- description: Public profile information such as location, phone, website, social media links.
  name: Cobot Space Profile API
  slug: cobot-space-profile-api
- description: How much a space pays Cobot, how many members they can have and the extras they have booked.
  name: Cobot Subscription API
  slug: cobot-subscription-api
- description: The Team API from Cobot — 2 operation(s) for team.
  name: Cobot Team API
  slug: cobot-team-api
- description: 'These URLs/URL templates enable API clients to provide links to the Cobot web interface without having to hard-code them. Each Url includes a unique, never changing `identifier` and either a `url` or '
  name: Cobot URL API
  slug: cobot-url-api
- description: A user is used to log in to Cobot via email/password. Users can be admins/members (see Membership) in multiple spaces.
  name: Cobot User API
  slug: cobot-user-api
- description: Confirms if a given email address is free to take.
  name: Cobot User Email Preview API
  slug: cobot-user-email-preview-api
artifact_total: 49
asyncapis:
- description: ''
  name: Cobot Webhooks
  slug: cobot-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/cobot-api2-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.cobot.me/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.cobot.me/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.cobot.me/api2
- group: docs
  title: ''
  type: APIReference
  url: https://dev.cobot.me/api2
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.cobot.me/page/extending-cobot
- group: operate
  title: ''
  type: Support
  url: https://www.cobot.me/en/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.cobot.me/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.cobot.me/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.cobot.me/rss/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cobot
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cobot.me/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.cobot.me/sign-up-space
- group: start
  title: ''
  type: Login
  url: https://www.cobot.me/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cobot.me/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cobot.me/en/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cobotstatus.me/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cobot.me/pages/api_changes
- group: build
  title: ''
  type: Packages
  url: packages/cobot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cobot-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cobot-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cobot-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cobot-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cobot-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cobot-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cobot-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cobot-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cobot-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cobot-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cobot-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cobot-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cobot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cobot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cobot-scopes.yml
created: '2026-08-09'
description: 'Cobot is coworking and flexible-workspace management software, built and operated by Upstream - Agile GmbH in Berlin, Germany. It runs the day-to-day of a coworking space or space network from one platform: memberships and plans, resource and meeting-room bookings, drop-in passes, events and ticketing, check-ins, automated invoicing and online payments, a white-label member portal and mobile app, analytics, and door access-control integrations (Kisi, Salto KS, Tapkey, Sensorberg, dormakaba Exivo). Cobot publishes a genuinely open developer surface: a 134-operation OpenAPI 3.1 contract for API 2 that follows the JSON:API standard, a legacy v1 REST API with a documented webhook event catalog, OAuth 2.0 with authorization-code + PKCE and dynamic client registration, OpenID Connect, an RFC 9727 api-catalog document, RFC 9728 protected-resource metadata, an llms.txt, and an OAuth-protected hosted MCP server at api.cobot.me/mcp.'
image: https://dev.cobot.me/api2_logo.webp
layout: provider
mcp_servers:
- description: ''
  name: cobot-mcp.yml
  slug: cobot-mcpyml
modified: '2026-08-09'
name: Cobot
nav: Providers
network: true
overview: 'Cobot publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Allocation API, Approval API, Article API, and 39 more. Tagged areas include Company, Coworking, Workspace Management, Space Management, and Real Estate.


  The Cobot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cobot''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 55
scopes:
- name: Cobot Scopes
  scope_count: 60
  slug: cobot-scopes
  summary_line: 60 scopes · authorizationCode
score:
  band: strong
  composite: 57.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 72.3
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 44.7
  previous_composite: 57.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 60.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Cobot Authentication
  slug: cobot-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cobot Domain Security
  slug: cobot-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cobot
tags:
- Company
- Coworking
- Workspace Management
- Space Management
- Real Estate
- Bookings
- Reservations
- Memberships
- Invoicing
- Payments
- Events
- Access Control
- SaaS
- Germany
- JSON:API
- OAuth
website: https://www.cobot.me/
---
