---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 142
  human_in_the_loop: 3
  name: Talon One Agentic Access
  operation_count: 271
  slug: talon-one-agentic-access
  summary_line: 271 operations · 142 acting · 3 human-in-the-loop
api_count: 5
apis:
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents account and user management, including billing email addresses and user invitations.
  name: Talon.One Accounts and users API
  slug: talon-one-accounts-and-users-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: 'Represents achievements that reward a customer profile for performing a number of specific actions or reaching a transactional milestone within a defined period. For example, you can use achievements '
  name: Talon.One Achievements API
  slug: talon-one-achievements-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents an extra fee applied to the cart, for example, shipping fees or processing fees. See the [docs](https://docs.talon.one/docs/product/account/dev-tools/managing-additional-costs).
  name: Talon.One Additional costs API
  slug: talon-one-additional-costs-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents analytics used to retrieve statistical data about the performance of campaigns within an Application.
  name: Talon.One Analytics API
  slug: talon-one-analytics-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents an Application in the Campaign Manager. An Application is the target of every Integration API request to Talon.One. One Application can hold various API keys used for Integration API reques
  name: Talon.One Applications API
  slug: talon-one-applications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a piece of information related to one of the entities available in the Campaign Manager. Use them to create highly customized rules. See the [docs](https://docs.talon.one/docs/product/accou
  name: Talon.One Attributes API
  slug: talon-one-attributes-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents lists of customer profiles that allow you to target specific groups of customers in your campaigns. Audiences can be synced from customer data platforms or created directly in Talon.One. Se
  name: Talon.One Audiences API
  slug: talon-one-audiences-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: '[Braze](https://www.braze.com/) is a customer engagement platform to manage customer-centric interactions between consumers and brands in real-time. Use these endpoints to automate the creation of cou'
  name: Talon.One Braze API
  slug: talon-one-braze-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the campaign access groups you can create in your Applications to organize your campaigns based on the type of campaign or the team in charge. See the [docs](https://docs.talon.one/docs/pro
  name: Talon.One Campaign access groups API
  slug: talon-one-campaign-access-groups-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/applications/application-notifications/overview) about campaign-related changes. > [!note] The value of the `NotificationType` property indicates the campa
  name: Talon.One Campaign notifications API
  slug: talon-one-campaign-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents templates used to generate campaigns from.
  name: Talon.One Campaign templates API
  slug: talon-one-campaign-templates-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the primary resource used to control the behavior of the Talon.One Rule Engine. They combine rulesets, coupons, and limits into a single unit. See the [docs](https://docs.talon.one/docs/pro
  name: Talon.One Campaigns API
  slug: talon-one-campaigns-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a catalog of cart items with unique SKUs. Cart item catalogs allow you to synchronize your entire inventory with Talon.One. See the [docs](https://docs.talon.one/docs/product/account/dev-to
  name: Talon.One Catalogs API
  slug: talon-one-catalogs-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a collection of arbitrary values that you can use inside rules. For example, a list of SKUs. See the [docs](https://docs.talon.one/docs/product/campaigns/managing-collections).
  name: Talon.One Collections API
  slug: talon-one-collections-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/applications/application-notifications/overview) about coupons.
  name: Talon.One Coupon notifications API
  slug: talon-one-coupon-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents unique codes belonging to a particular campaign. Coupons don't define any behavior on their own. Instead the campaign ruleset can include rules that validate coupons and carry out particula
  name: Talon.One Coupons API
  slug: talon-one-coupons-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the data of a customer, including sessions and events used for reporting and debugging in the Campaign Manager.
  name: Talon.One Customer data API
  slug: talon-one-customer-data-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: You can integrate with any customer data platform, or CDP, using the following endpoints designed for third-party tools, rather than your own integration layer. Use these endpoints to automate the cre
  name: Talon.One Customer data platforms API
  slug: talon-one-customer-data-platforms-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: You can integrate with any customer engagement platform, or CEP, using the following endpoints designed for third-party tools, rather than your own integration layer. Use these endpoints to automate t
  name: Talon.One Customer engagement platforms API
  slug: talon-one-customer-engagement-platforms-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the customer's information. For instance, their contact information.
  name: Talon.One Customer profiles API
  slug: talon-one-customer-profiles-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the data related to a customer session. Typically, a customer session is the value and content of the customer's cart. Sessions can be anonymous or linked to a customer profile and they hav
  name: Talon.One Customer sessions API
  slug: talon-one-customer-sessions-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Emarsys is a customer engagement platform that enables marketers to build, launch, and scale personalized cross-channel promotional campaigns that have measurable impact. Use these endpoints to integr
  name: Talon.One Emarsys API
  slug: talon-one-emarsys-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: 'Represents a single occurrence of a specific customer action, for example, updating the cart or signing up for a newsletter. There are 2 types of events: - **Built-in events:** They are triggered by v'
  name: Talon.One Events API
  slug: talon-one-events-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents an A/B testing configuration within a campaign that splits customer sessions across multiple variants to compare rule effects against each other.
  name: Talon.One Experiments API
  slug: talon-one-experiments-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a program that rewards customers with giveaways, such as free gift cards. See the [docs](https://docs.talon.one/docs/product/giveaways/overview).
  name: Talon.One Giveaways API
  slug: talon-one-giveaways-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: '[Iterable](https://iterable.com/) is a cross-channel marketing platform that powers unified customer experiences and empowers you to create, optimize and measure every interaction across the entire cu'
  name: Talon.One Iterable API
  slug: talon-one-iterable-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the Talon.One logs, which contain all incoming and outgoing requests.
  name: Talon.One Logs API
  slug: talon-one-logs-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents loyalty programs or concepts related to them. Loyalty programs can be _profile-based_ or _card-based_, depending on whether loyalty points are linked to [customer profiles](https://docs.tal
  name: Talon.One Loyalty API
  slug: talon-one-loyalty-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/loyalty-programs/loyalty-notifications/overview) about changes to loyalty points in card-based loyalty programs.
  name: Talon.One Loyalty card notifications API
  slug: talon-one-loyalty-card-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents loyalty cards. [Loyalty cards](https://docs.talon.one/docs/product/loyalty-programs/card-based/card-based-overview) allow your customers to collect and spend loyalty points within a card-ba
  name: Talon.One Loyalty cards API
  slug: talon-one-loyalty-cards-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/loyalty-programs/loyalty-notifications/overview) about changes to loyalty points in profile-based loyalty programs.
  name: Talon.One Loyalty notifications API
  slug: talon-one-loyalty-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: '[mParticle](https://www.mparticle.com/) is the customer data platform that helps unify data and simplify partner integrations with enterprise-class security and reliability. For more information, see '
  name: Talon.One M Particle API
  slug: talon-one-mparticle-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: 'Represents a referral code shared between a customer (advocate) and a prospect (friend). A referral is defined by: - an advocate: person who invited their friend via referral program. - a friend: pers'
  name: Talon.One Referrals API
  slug: talon-one-referrals-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a set of permissions assigned to a user. See the [docs](https://docs.talon.one/docs/product/account/account-settings/managing-roles).
  name: Talon.One Roles API
  slug: talon-one-roles-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: '[Segment](https://segment.com/) is a customer data platform that collects events from your web & mobile apps. Use these endpoints to integrate with Talon.One.'
  name: Talon.One Segment API
  slug: talon-one-segment-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Use the following endpoints to manage customer sessions.
  name: Talon.One Session API
  slug: talon-one-session-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents a session used for authentication purposes. Create one with the [Create session](#tag/Sessions/operation/createSession) endpoint.
  name: Talon.One Sessions API
  slug: talon-one-sessions-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents store budgets. You can set a store budget to limit the total amount an individual store can spend in a campaign.
  name: Talon.One Store budgets API
  slug: talon-one-store-budgets-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents physical or digital stores, branches, and franchises.
  name: Talon.One Stores API
  slug: talon-one-stores-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the [notifications](/docs/product/applications/application-notifications/overview) about strikethrough pricing updates.
  name: Talon.One Strikethrough pricing notifications API
  slug: talon-one-strikethrough-pricing-notifications-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents the value maps that the user can create within a campaign ruleset.
  name: Talon.One Value maps API
  slug: talon-one-value-maps-api
- baseURL: https://yourbaseurl.talon.one
  baseurl_source: declared
  description: Represents webhooks, which send information from Talon.One to the URI of your choice. See the [docs](https://docs.talon.one/docs/dev/getting-started/webhooks).
  name: Talon.One Webhooks API
  slug: talon-one-webhooks-api
artifact_total: 57
asyncapis:
- description: ''
  name: Talon One Webhooks
  slug: talon-one-webhooks
collections:
- collection_type: open
  name: Integration API
  slug: open-talon-one-integration-api
- collection_type: open
  name: Management API
  slug: open-talon-one-management-api
- collection_type: open
  name: Notification schemas
  slug: open-talon-one-outbound-notifications
- collection_type: open
  name: Shopify Integration API
  slug: open-talon-one-shopify-integration-api
- collection_type: open
  name: Third-party API
  slug: open-talon-one-third-party-api
- collection_type: open
  name: Talon.One API
  slug: open-talon-one
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/talon-one-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/talon-one-management-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/talon-one-third-party-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/talon-one-shopify-integration-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/talon-one-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talon-one-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/talon-one-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/talon-one
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/talon-one
- group: company
  title: ''
  type: Website
  url: https://www.talon.one
- group: docs
  title: ''
  type: Documentation
  url: https://docs.talon.one
- group: start
  title: ''
  type: SignUp
  url: https://www.talon.one/book-a-demo
- group: commercial
  title: ''
  type: Plans
  url: plans/talon-one-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/talon-one-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/talon-one-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.talon.one/blog
- group: build
  title: ''
  type: Packages
  url: packages/talon-one-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/talon-one-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/talon-one-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/talon-one-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/talon-one-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/talon-one-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/talon-one-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/talon-one-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/talon-one-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/talon-one-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.talon.one/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/talon-one-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/talon-one-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/talon-one-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/talon-one-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.talon.one/whats-new
- group: start
  title: ''
  type: Sandbox
  url: sandbox/talon-one-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/talon-one-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/talon-one-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/talon-one-integration-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.talon.one/docs/dev/get-started/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.talon.one/integration-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.talon.one/docs/dev/quickstart
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/talonone-rnd/workspace/talon-one/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.talon.one/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.talon.one/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.talon.one/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.talon.one/contact-us
created: '2026-07-10'
description: Talon.One is an enterprise promotion, loyalty, and incentives engine that lets teams build and run coupons, discounts, referrals, bundles, giveaways, and multi-tier loyalty programs from a single rules-based platform. It exposes two primary REST APIs. The Integration API pushes real-time customer sessions, profiles, and events into the rules engine and returns the effects (discounts, awarded loyalty points, accepted coupons) to apply in the calling application. The Management API programmatically administers applications, campaigns, rulesets, coupons, loyalty programs, audiences, custom attributes, collections, and analytics exports that back the Campaign Manager. Talon.One is delivered as a managed, per-customer deployment; each account calls its own base URL (https://yourbaseurl.talon.one) and authenticates with an API key whose prefix distinguishes the Integration key (ApiKey-v1) from the Management key (ManagementKey-v1).
finops:
- name: Talon One Finops
  service_category: Marketing and Promotions
  slug: talon-one-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talon-one.png
layout: provider
mcp_servers:
- description: Talon.One ships an official MCP server that gives agents secure, read-only access to the campaigns, customers, coupons and loyalty data in a Talon.One environment. Because Talon.One runs as a per-cust
  name: Talon.One MCP server
  slug: talonone-mcp-server
modified: '2026-08-13'
name: Talon.One
nav: Providers
network: true
overview: 'Talon.One publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Accounts and users API, Achievements API, Additional costs API, and 39 more. Tagged areas include Promotions, Loyalty, Coupons, Incentives, and Campaigns.


  The Talon.One catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Talon.One''s developer surface includes authentication, documentation, signup flow, engineering blog, changelog, sandbox, API reference, and 38 more developer resources.'
plans:
- name: Talon One Plans Pricing
  plan_count: 3
  slug: talon-one-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Talon One Rate Limits
  slug: talon-one-rate-limits
score:
  band: exemplar
  composite: 71.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 67.4
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 81.6
  previous_composite: 71.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/talon-one/refs/heads/main/screenshots/talon-one-2026-08-17T080429.png
security:
- kind: authentication
  name: Talon One Authentication
  slug: talon-one-authentication
  summary_line: apiKey/http · 8 schemes
- kind: domain-security
  name: Talon One Domain Security
  slug: talon-one-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Talon One Trust Center
  slug: talon-one-trust-center
  summary_line: ISO 27001, SOC 2, GDPR
slug: talon-one
tags:
- Promotions
- Loyalty
- Coupons
- Incentives
- Campaigns
- Personalization
- MarTech
- Rules Engine
- Referrals
- Discounts
- E-Commerce
- Retail
website: https://www.talon.one
---
