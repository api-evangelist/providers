---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.6
  scored_at: '2026-08-24'
api_count: 72
apis:
- description: GoFundMe Pro's single sign-on service, implemented against OpenID Connect, letting third-party apps register and log people in with their Classy/GoFundMe Pro account. Authorization endpoint at login.c
  name: Classy Login (OpenID Connect SSO)
  slug: classy-login-openid-connect-sso
- description: Payment and embedded-checkout service behind GoFundMe Pro donation and registration flows. Ships a JavaScript embedded-checkout library (classypay.js) that renders a hosted checkout form into a host p
  name: Classy Pay
  slug: classy-pay
- description: An acknowledgement is a means of indicating that the member who made a transaction has been formally thanked. Every acknowledgement is made by the associated member, optionally on behalf of another fu
  name: GoFundMe Acknowledgement API
  slug: gofundme-acknowledgement-api
- description: An activity is a record of an interaction with the GoFundMe Pro platform. Activity types include creating a new donation, creating a new fundraising page or team, adding a new team member, and more. A
  name: GoFundMe Activity API
  slug: gofundme-activity-api
- description: Annual Summary
  name: GoFundMe Annual Summary API
  slug: gofundme-annual-summary-api
- description: 'Answer objects represent an answer to a Question that is associated with an answerable_type (referenced by answerable_id and answerable_type), supported types include: fundraising_page, fundraising_te'
  name: GoFundMe Answer API
  slug: gofundme-answer-api
- description: An App represents a client that can interact with GoFundMe Pro API.
  name: GoFundMe API App API
  slug: gofundme-api-app-api
- description: 'An appeal set is a group of campaign specific appeals for social media. The current appeals that are supported include Facebook, Twitter, SMS, and Email. There is one set of appeals per campaign, and '
  name: GoFundMe Appeal Set API
  slug: gofundme-appeal-set-api
- description: Organizations can have branding images and styles that will be applied to various areas of the GoFundMe Pro platform. Examples include changing the GoFundMe Pro logo to the organization logo, adding a
  name: GoFundMe Branding API
  slug: gofundme-branding-api
- description: Brandkit
  name: GoFundMe Brandkit API
  slug: gofundme-brandkit-api
- description: The fundraising aspect of GoFundMe Pro takes place within Campaigns and Events. Use the campaign endpoint to retrieve information about a campaign by its unique ID.
  name: GoFundMe Campaign API
  slug: gofundme-campaign-api
- description: Campaign Channel is an Integration channel association available for specific Campaign. Integration channels will be like Facebook, Double the Donation. Campign Channel have channel specific flags and
  name: GoFundMe Campaign Channel API
  slug: gofundme-campaign-channel-api
- description: A Credential Set is fundamentally a record that dictates what a user can do or access within a Campaign or Organization context in the API.
  name: GoFundMe Campaign Credential Set API
  slug: gofundme-campaign-credential-set-api
- description: A Campaign Series is a time series of campaigns.
  name: GoFundMe Campaign Series API
  slug: gofundme-campaign-series-api
- description: A Campaign Series Iteration is one time span in a Campaign Series, e.g. '2024'
  name: GoFundMe Campaign Series Iteration API
  slug: gofundme-campaign-series-iteration-api
- description: Campaign Studio
  name: GoFundMe Campaign Studio API
  slug: gofundme-campaign-studio-api
- description: Channel Fundraising Entity will be used to store additional channel details for the fundraising entity. Where fundraising_entity_id is the ID of the associated fundraising entity and fundraising_entit
  name: GoFundMe Channel Fundraising Entity API
  slug: gofundme-channel-fundraising-entity-api
- description: Chariot
  name: GoFundMe Chariot API
  slug: gofundme-chariot-api
- description: A ClassySubscriptionPlan is a legacy method of specifying the GoFundMe Pro plan to which an organization is subscribed, which was associated with specific transaction rates and plan features. This has
  name: GoFundMe Classy Subscription Plan API
  slug: gofundme-classy-subscription-plan-api
- description: Comments can also be made in response to Stories, Updates, or FeedItems made on a fundraising entity. Please note that these take a slightly different form from comments for activity records.
  name: GoFundMe Comment API
  slug: gofundme-comment-api
- description: A credit adjustment represents against a debit or credit fundraising entity's fundraising total (aka total_raised). This adjustment represents credit specifically where funds are not captured. A simpl
  name: GoFundMe Credit Adjustment API
  slug: gofundme-credit-adjustment-api
- description: When a donation is dedicated to a specific individual, it can trigger a series of actions. An email message, crafted by the donor, is sent to the dedicatee. Use the dedication endpoint to create, retr
  name: GoFundMe Dedication API
  slug: gofundme-dedication-api
- description: A Designation refers to a specific cause the organization campaigns under. Multiple campaigns can benefit the designated project. Designations allow me to assign Campaigns that champion the same cause
  name: GoFundMe Designation API
  slug: gofundme-designation-api
- description: A Domain Slug is a value used to shorten a URL by referencing a domain and a fundraising entity.
  name: GoFundMe Domain Slug API
  slug: gofundme-domain-slug-api
- description: Donation matching occurs when a Sponsor - company or individual - agrees to match your campaign donations for a specific time period and/or up to a certain limit.
  name: GoFundMe Donation Matching Plan API
  slug: gofundme-donation-matching-plan-api
- description: The Double the Donation API from GoFundMe — 2 operation(s) for double the donation.
  name: GoFundMe Double the Donation API
  slug: gofundme-double-the-donation-api
- description: Donors can send an eCard dedication along with their donation. Currently, a single campaign can support a maximum of 4 eCards. eCards are 600 pixels wide by 400 pixels tall and uploaded by the organiz
  name: GoFundMe E Card API
  slug: gofundme-ecard-api
- description: Organization specific settings related to engagements such as email and SMS settings. We can set SMS numbers or email DNS, throttling etc.
  name: GoFundMe Engagement Settings API
  slug: gofundme-engagement-settings-api
- description: 'An FAQ (short for Frequently Asked Question) is a means of answering common questions that donors or registrants may have when donating/registering for a campaign. These question/answer pairs will be '
  name: GoFundMe FAQ API
  slug: gofundme-faq-api
- description: A feed item is a representation of a message that populates the feed of a fundraising entity (i.e. the feed item’s “feedable”). Each feed item references an “agent” who performed an action, and may al
  name: GoFundMe Feed Item API
  slug: gofundme-feed-item-api
- description: A fundraising page is a means for an individual fundraiser to raise funds for a specific peer-to-peer campaign. Like other fundraising entities, each page allows for the creation of an associated stor
  name: GoFundMe Fundraising Page API
  slug: gofundme-fundraising-page-api
- description: Transfer Fundraising Page to another Member, Campaign or Fundraising Team.
  name: GoFundMe Fundraising Page Transfer API
  slug: gofundme-fundraising-page-transfer-api
- description: Represents a group of donors consisting of a team lead fundraising together to reach a fundraising goal.
  name: GoFundMe Fundraising Team API
  slug: gofundme-fundraising-team-api
- description: The Fundraising Team Policy represents a settings policy that can be applied to a Fundraising Team (parent, or sub-team). Fundraising Team Policy attributes will effect the behavior of the Team and al
  name: GoFundMe Fundraising Team Policy API
  slug: gofundme-fundraising-team-policy-api
- description: Transfer a Fundraising Team within its Campaign/subteam infrastructure. This is done by specifying the team's direct parent, making it either a direct team for its Campaign or a subteam for another te
  name: GoFundMe Fundraising Team Transfer API
  slug: gofundme-fundraising-team-transfer-api
- description: GFM NPO Page
  name: GoFundMe GFM NPO Page API
  slug: gofundme-gfm-npo-page-api
- description: A hard credit transfer is a means of transferring a hard credit (i.e. transaction) between fundraising entities associated with the same organization.
  name: GoFundMe Hard Credit Transfer API
  slug: gofundme-hard-credit-transfer-api
- description: A like is a small show of approval for its associated 'likeable' entity. At the moment, the API allows Stories, Updates, FeedItems, and Comments to be 'likeable'.
  name: GoFundMe Like API
  slug: gofundme-like-api
- description: MagicLink
  name: GoFundMe Magic Link API
  slug: gofundme-magiclink-api
- description: A matched transaction can be created when a normal transaction may be matched with a future transaction. This might occur in the case of an employer match, a sponsor pledge, or some other form of matc
  name: GoFundMe Matched Transaction API
  slug: gofundme-matched-transaction-api
- description: 'A Member can be registered by directly having their attributes submitted (first_name, last_name, email_address, ...), or from their facebook account. To register a user from their Facebook account, a '
  name: GoFundMe Member API
  slug: gofundme-member-api
- description: Represents an organization account. An organization's `currency_code` is used for Passport functionality. `currency_code` dictates the currency code that is used to normalize all of the organization's
  name: GoFundMe Organization API
  slug: gofundme-organization-api
- description: An organization channel is a method of configuring an integration between an organization and a third-party event service (e.g. Facebook).
  name: GoFundMe Organization Channel API
  slug: gofundme-organization-channel-api
- description: Organization Consumer Mappings
  name: GoFundMe Organization Consumer Mappings API
  slug: gofundme-organization-consumer-mappings-api
- description: A Credential Set is fundamentally a record that dictates what a user can do or access within a Campaign or Organization context in the API.
  name: GoFundMe Organization Credential Set API
  slug: gofundme-organization-credential-set-api
- description: The Organization Notification API from GoFundMe — 2 operation(s) for organization notification.
  name: GoFundMe Organization Notification API
  slug: gofundme-organization-notification-api
- description: Organizations
  name: GoFundMe Organizations API
  slug: gofundme-organizations-api
- description: Payouts will provide transactions of PayPal and Stripe.
  name: GoFundMe Payouts API
  slug: gofundme-payouts-api
- description: A promo code record represents a shareable string that can be used to apply a discount to the purchase of one or more configured ticket types for a specified campaign. The code can specify either a pe
  name: GoFundMe Promo Code API
  slug: gofundme-promo-code-api
- description: A promo code configuration record indicates that its associated promo code can be applied to purchases of the associated ticket type.
  name: GoFundMe Promo Code Configuration API
  slug: gofundme-promo-code-configuration-api
- description: Questions are set up by organizations learn more about their supporters and fundraisers. These questions appear as a supporter signs up to fundraise or when making a donation.
  name: GoFundMe Question API
  slug: gofundme-question-api
- description: 'A Recurring Donation Plan is a record of a user''s intent to provide recurring donations towards a campaign or fundraising page. The record itself contains the provided billing address and identifying '
  name: GoFundMe Recurring Donation Plan API
  slug: gofundme-recurring-donation-plan-api
- description: A Recurring Donation Plan History is a history record of Recurring Donation Plan.
  name: GoFundMe Recurring Donation Plan History API
  slug: gofundme-recurring-donation-plan-history-api
- description: Registration records show information pertaining to event attendance, either through a ticket purchase or basic registration.
  name: GoFundMe Registration API
  slug: gofundme-registration-api
- description: Reports
  name: GoFundMe Reports API
  slug: gofundme-reports-api
- description: Restrict countries to have restricted usage of GoFundMe Pro such as for GDPR
  name: GoFundMe Restricted Country API
  slug: gofundme-restricted-country-api
- description: Organizations and Campaigns have roles that can be assigned to Members.
  name: GoFundMe Role API
  slug: gofundme-role-api
- description: Social Video
  name: GoFundMe Social Video API
  slug: gofundme-social-video-api
- description: Soft credits serve to allocate credit from part or all of the funds raised for a fundraising entity to any of its associated entities. For example, a transaction made against a fundraising team can be
  name: GoFundMe Soft Credit API
  slug: gofundme-softcredit-api
- description: Some Organizations have multiple marketing channels to support their cause. Source Tracking Codes are internal codes GoFundMe Pro uses to identify which marketing channel a Supporter passed through.
  name: GoFundMe Source Tracking Codes API
  slug: gofundme-source-tracking-codes-api
- description: Notification settings are for sending email notifications for different scopes as Organization and Campaign. Based on settings, email notification will be sent for Transactions, Fundraising Pages or T
  name: GoFundMe Staff Notification Setting API
  slug: gofundme-staff-notification-setting-api
- description: A type of post meant for display on a fundraising entity's page. This allows an administrator for the fundraising entity to present an appeal for donations or registrations to page visitors in a uniqu
  name: GoFundMe Story API
  slug: gofundme-story-api
- description: Studio Campaign
  name: GoFundMe Studio Campaign API
  slug: gofundme-studio-campaign-api
- description: A donor profile that’s owned by the organization. When an organization makes an update to a supporter, it will not affect member profile.
  name: GoFundMe Supporter API
  slug: gofundme-supporter-api
- description: Supporters
  name: GoFundMe Supporters API
  slug: gofundme-supporters-api
- description: It is a Campaign Theme which is used to set Theme properties like pages (landing, donation, thank you, etc) and styles for the Theme.
  name: GoFundMe Theme API
  slug: gofundme-theme-api
- description: A Ticket Type defines the available ticket(s) for a ticketed Campaign. For example, ‘General Admission’ or ‘VIP’ * This defines what types of tickets are available. It is NOT an instance of a specific
  name: GoFundMe Ticket Type API
  slug: gofundme-ticket-type-api
- description: 'Transactions have three types of attributes relating to Passport: raw, charged, and normalized. Raw attributes reflect the donor/purchaser''s intent when creating the Transaction. The only attribute di'
  name: GoFundMe Transaction API
  slug: gofundme-transaction-api
- description: Transaction Items describe the specific donations, tickets, registrations (and more) that could make up a Transaction. Some transactions will only have a single Transaction Item, but others may have m
  name: GoFundMe Transaction Item API
  slug: gofundme-transaction-item-api
- description: Transaction receipts record any instance when a specific transaction is produced for a donation.
  name: GoFundMe Transaction Receipt API
  slug: gofundme-transaction-receipt-api
- description: A type of post meant for display on a fundraising entity's page. This allows and administrator for the fundraising entity to provide donors or registrants with information about the progress of the ca
  name: GoFundMe Update API
  slug: gofundme-update-api
- description: 'A record indicating one of the possible currencies that an organization is allowing for fundraising and transactions. If no such records exist for an organization, it is assumed that the organization '
  name: GoFundMe Whitelisted Currency API
  slug: gofundme-whitelisted-currency-api
artifact_total: 151
asyncapis:
- description: ''
  name: Gofundme Webhooks
  slug: gofundme-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GoFundMe Pro Acknowledgement API
  slug: open-gofundme-acknowledgement-api
- collection_type: open
  name: GoFundMe Pro Activity API
  slug: open-gofundme-activity-api
- collection_type: open
  name: GoFundMe Pro Annual Summary API
  slug: open-gofundme-annual-summary-api
- collection_type: open
  name: GoFundMe Pro Answer API
  slug: open-gofundme-answer-api
- collection_type: open
  name: GoFundMe Pro API App API
  slug: open-gofundme-api-app-api
- collection_type: open
  name: GoFundMe Pro Appeal Set API
  slug: open-gofundme-appeal-set-api
- collection_type: open
  name: GoFundMe Pro Branding API
  slug: open-gofundme-branding-api
- collection_type: open
  name: GoFundMe Pro Brandkit API
  slug: open-gofundme-brandkit-api
- collection_type: open
  name: GoFundMe Pro Campaign API
  slug: open-gofundme-campaign-api
- collection_type: open
  name: GoFundMe Pro Campaign Channel API
  slug: open-gofundme-campaign-channel-api
- collection_type: open
  name: GoFundMe Pro Campaign Credential Set API
  slug: open-gofundme-campaign-credential-set-api
- collection_type: open
  name: GoFundMe Pro Campaign Series API
  slug: open-gofundme-campaign-series-api
- collection_type: open
  name: GoFundMe Pro Campaign Series Iteration API
  slug: open-gofundme-campaign-series-iteration-api
- collection_type: open
  name: GoFundMe Pro Campaign Studio API
  slug: open-gofundme-campaign-studio-api
- collection_type: open
  name: GoFundMe Pro Channel Fundraising Entity API
  slug: open-gofundme-channel-fundraising-entity-api
- collection_type: open
  name: GoFundMe Pro Chariot API
  slug: open-gofundme-chariot-api
- collection_type: open
  name: GoFundMe Pro Classy Subscription Plan API
  slug: open-gofundme-classy-subscription-plan-api
- collection_type: open
  name: GoFundMe Pro Comment API
  slug: open-gofundme-comment-api
- collection_type: open
  name: GoFundMe Pro Credit Adjustment API
  slug: open-gofundme-credit-adjustment-api
- collection_type: open
  name: GoFundMe Pro Dedication API
  slug: open-gofundme-dedication-api
- collection_type: open
  name: GoFundMe Pro Designation API
  slug: open-gofundme-designation-api
- collection_type: open
  name: GoFundMe Pro Domain Slug API
  slug: open-gofundme-domain-slug-api
- collection_type: open
  name: GoFundMe Pro Donation Matching Plan API
  slug: open-gofundme-donation-matching-plan-api
- collection_type: open
  name: GoFundMe Pro Double the Donation API
  slug: open-gofundme-double-the-donation-api
- collection_type: open
  name: GoFundMe Pro E Card API
  slug: open-gofundme-ecard-api
- collection_type: open
  name: GoFundMe Pro Engagement Settings API
  slug: open-gofundme-engagement-settings-api
- collection_type: open
  name: GoFundMe Pro FAQ API
  slug: open-gofundme-faq-api
- collection_type: open
  name: GoFundMe Pro Feed Item API
  slug: open-gofundme-feed-item-api
- collection_type: open
  name: GoFundMe Pro Fundraising Page API
  slug: open-gofundme-fundraising-page-api
- collection_type: open
  name: GoFundMe Pro Fundraising Page Transfer API
  slug: open-gofundme-fundraising-page-transfer-api
- collection_type: open
  name: GoFundMe Pro Fundraising Team API
  slug: open-gofundme-fundraising-team-api
- collection_type: open
  name: GoFundMe Pro Fundraising Team Policy API
  slug: open-gofundme-fundraising-team-policy-api
- collection_type: open
  name: GoFundMe Pro Fundraising Team Transfer API
  slug: open-gofundme-fundraising-team-transfer-api
- collection_type: open
  name: GoFundMe Pro GFM NPO Page API
  slug: open-gofundme-gfm-npo-page-api
- collection_type: open
  name: GoFundMe Pro Hard Credit Transfer API
  slug: open-gofundme-hard-credit-transfer-api
- collection_type: open
  name: GoFundMe Pro Like API
  slug: open-gofundme-like-api
- collection_type: open
  name: GoFundMe Pro Magic Link API
  slug: open-gofundme-magiclink-api
- collection_type: open
  name: GoFundMe Pro Matched Transaction API
  slug: open-gofundme-matched-transaction-api
- collection_type: open
  name: GoFundMe Pro Member API
  slug: open-gofundme-member-api
- collection_type: open
  name: GoFundMe Pro Organization API
  slug: open-gofundme-organization-api
- collection_type: open
  name: GoFundMe Pro Organization Channel API
  slug: open-gofundme-organization-channel-api
- collection_type: open
  name: GoFundMe Pro Organization Consumer Mappings API
  slug: open-gofundme-organization-consumer-mappings-api
- collection_type: open
  name: GoFundMe Pro Organization Credential Set API
  slug: open-gofundme-organization-credential-set-api
- collection_type: open
  name: GoFundMe Pro Organization Notification API
  slug: open-gofundme-organization-notification-api
- collection_type: open
  name: GoFundMe Pro Organizations API
  slug: open-gofundme-organizations-api
- collection_type: open
  name: GoFundMe Pro Payouts API
  slug: open-gofundme-payouts-api
- collection_type: open
  name: GoFundMe Pro Promo Code API
  slug: open-gofundme-promo-code-api
- collection_type: open
  name: GoFundMe Pro Promo Code Configuration API
  slug: open-gofundme-promo-code-configuration-api
- collection_type: open
  name: GoFundMe Pro Question API
  slug: open-gofundme-question-api
- collection_type: open
  name: GoFundMe Pro Recurring Donation Plan API
  slug: open-gofundme-recurring-donation-plan-api
- collection_type: open
  name: GoFundMe Pro Recurring Donation Plan History API
  slug: open-gofundme-recurring-donation-plan-history-api
- collection_type: open
  name: GoFundMe Pro Registration API
  slug: open-gofundme-registration-api
- collection_type: open
  name: GoFundMe Pro Reports API
  slug: open-gofundme-reports-api
- collection_type: open
  name: GoFundMe Pro Restricted Country API
  slug: open-gofundme-restricted-country-api
- collection_type: open
  name: GoFundMe Pro Role API
  slug: open-gofundme-role-api
- collection_type: open
  name: GoFundMe Pro Social Video API
  slug: open-gofundme-social-video-api
- collection_type: open
  name: GoFundMe Pro Soft Credit API
  slug: open-gofundme-softcredit-api
- collection_type: open
  name: GoFundMe Pro Source Tracking Codes API
  slug: open-gofundme-source-tracking-codes-api
- collection_type: open
  name: GoFundMe Pro Staff Notification Setting API
  slug: open-gofundme-staff-notification-setting-api
- collection_type: open
  name: GoFundMe Pro Story API
  slug: open-gofundme-story-api
- collection_type: open
  name: GoFundMe Pro Studio Campaign API
  slug: open-gofundme-studio-campaign-api
- collection_type: open
  name: GoFundMe Pro Supporter API
  slug: open-gofundme-supporter-api
- collection_type: open
  name: GoFundMe Pro Supporters API
  slug: open-gofundme-supporters-api
- collection_type: open
  name: GoFundMe Pro Theme API
  slug: open-gofundme-theme-api
- collection_type: open
  name: GoFundMe Pro Ticket Type API
  slug: open-gofundme-ticket-type-api
- collection_type: open
  name: GoFundMe Pro Transaction API
  slug: open-gofundme-transaction-api
- collection_type: open
  name: GoFundMe Pro Transaction Item API
  slug: open-gofundme-transaction-item-api
- collection_type: open
  name: GoFundMe Pro Transaction Receipt API
  slug: open-gofundme-transaction-receipt-api
- collection_type: open
  name: GoFundMe Pro Update API
  slug: open-gofundme-update-api
- collection_type: open
  name: GoFundMe Pro Whitelisted Currency API
  slug: open-gofundme-whitelisted-currency-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/gofundme-pro-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gofundme-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gofundme.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gofundme.com/pro/overview/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gofundme.com/pro/overview/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.gofundme.com/pro/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gofundme.com/pro/overview/get-started
- group: operate
  title: ''
  type: Support
  url: https://prosupport.gofundme.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://prosupport.gofundme.com/hc/en-us/sections/35654895701787-API-and-partner-apps
- group: company
  title: ''
  type: Blog
  url: https://pro.gofundme.com/c/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/classy-org
- group: commercial
  title: ''
  type: Pricing
  url: https://pro.gofundme.com/c/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://developers.gofundme.com/pro/overview/request-access
- group: start
  title: ''
  type: Login
  url: https://www.classy.org/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pro.gofundme.com/c/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pro.gofundme.com/c/legal/privacy-notice/
- group: build
  title: ''
  type: Postman
  url: https://github.com/classy-org/postman-collections
- group: operate
  title: ''
  type: StatusPage
  url: https://status.classy.org
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.gofundme.com/pro/reference/deprecation
- group: auth
  title: ''
  type: Security
  url: https://www.gofundme.com/c/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.gofundme.com/c/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/gofundme-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://prosupport.gofundme.com/hc/en-us/articles/37726683210267-Release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gofundme-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/gofundme-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gofundme-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gofundme-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gofundme-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gofundme-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gofundme-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gofundme-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gofundme-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gofundme-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gofundme-llms.txt
created: '2026-08-04'
description: 'GoFundMe is the world''s largest social fundraising platform, operating both the consumer crowdfunding site at gofundme.com and GoFundMe Pro (formerly Classy, acquired in 2022) — the enterprise fundraising suite nonprofits use for donation pages, peer-to-peer campaigns, recurring giving, ticketed events and Giving Cart checkout. The developer surface is GoFundMe Pro: a REST API (v2.0) documented with a public OpenAPI 3.0 definition covering campaigns, transactions, supporters, fundraising pages and teams, recurring donation plans, designations, promo codes, payouts and reporting; OAuth2 client-credentials and member tokens; Svix-powered webhooks for supporter, transaction and recurring-plan events; a Classy Login OpenID Connect single-sign-on service; and Classy Pay embedded checkout. The consumer gofundme.com product publishes no public API.'
image: https://pro.gofundme.com/wp-content/uploads/2025/04/social-share-gfm-pro.png
layout: provider
mcp_servers:
- description: ''
  name: GoFundMe MCP Server
  slug: gofundme-mcp-server
modified: '2026-08-04'
name: GoFundMe
nav: Providers
network: true
overview: 'GoFundMe publishes 70 APIs on the [APIs.io](https://apis.io/) network, including Acknowledgement API, Activity API, Annual Summary API, and 67 more. Tagged areas include Fundraising, Non-Profit, Crowdfunding, Donations, and Payments.


  The GoFundMe catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GoFundMe''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 1
  name: Gofundme Rate Limits
  slug: gofundme-rate-limits
scopes:
- name: Gofundme Scopes
  scope_count: 2
  slug: gofundme-scopes
  summary_line: 2 scopes · clientCredentials/password
score:
  band: strong
  composite: 60.0
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 65.4
    developer_ergonomics: 28.0
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 73.7
  previous_composite: 60.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 70
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 75.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gofundme/refs/heads/main/screenshots/gofundme-2026-08-07T165756.png
security:
- kind: authentication
  name: Gofundme Authentication
  slug: gofundme-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Gofundme Domain Security
  slug: gofundme-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gofundme Vulnerability Disclosure
  slug: gofundme-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gofundme Trust Center
  slug: gofundme-trust-center
  summary_line: PCI DSS, NIST Cybersecurity Framework, ISO 27001
slug: gofundme
tags:
- Fundraising
- Non-Profit
- Crowdfunding
- Donations
- Payments
- Peer-to-Peer Fundraising
- Recurring Giving
- Event
- Philanthropy
- Social Impact
- CRM
- Webhook
website: https://www.gofundme.com
---
