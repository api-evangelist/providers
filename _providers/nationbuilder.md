---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 108
  human_in_the_loop: 0
  name: Nationbuilder Agentic Access
  operation_count: 190
  slug: nationbuilder-agentic-access
  summary_line: 190 operations · 108 acting
api_count: 41
apis:
- description: This endpoint is used to get information about deferred or asynchronous processes returned by other endpoints such as adding and removing signups from a list or tagging and untagging signups from a li
  name: NationBuilder Async Processes API
  slug: nationbuilder-async-processes-api
- description: AutomationEnrollments link signups to automations. Every AutomationEnrollment belongs to a single Signup and a single Automation. Further information on how signups are enrolled in automations is avai
  name: NationBuilder Automation Enrollments API
  slug: nationbuilder-automation-enrollments-api
- description: Automations represent workflows where chains of actions and reactions can be created within a nation. Signups can be enrolled in an automation and are represented via the AutomationEnrollments resourc
  name: NationBuilder Automations API
  slug: nationbuilder-automations-api
- description: Ballots are a record of an election and how a person voted for said election. Each ballot is associated with a voter and an election and contains information such as when the ballot was cast, the part
  name: NationBuilder Ballots API
  slug: nationbuilder-ballots-api
- description: Broadcasters are the voices who speak publicly on behalf of your nation. All external communications are organized around broadcasters.
  name: NationBuilder Broadcasters API
  slug: nationbuilder-broadcasters-api
- description: Contacts are logged interactions between people in your nation. More information about contacts and the fields found in the UI and API interfaces can be found [here](https://support.nationbuilder.com/
  name: NationBuilder Contacts API
  slug: nationbuilder-contacts-api
- description: Custom fields are available for Signups and Donations. See [here](https://support.nationbuilder.com/en/articles/2340612-introduction-to-custom-fields) for more information.
  name: NationBuilder Custom Fields API
  slug: nationbuilder-custom-fields-api
- description: Tracking codes are used to identify where a financial transaction came from. Users give the tracking code a custom name/slug and use the code to track where a donation was made. Read more about them [
  name: NationBuilder Donation Tracking Codes API
  slug: nationbuilder-donation-tracking-codes-api
- description: Currently we allow you to record existing donation transactions via API V2. These transactions will not be backed by any kind of financial transaction. See the [docs](https://support.nationbuilder.com
  name: NationBuilder Donations API
  slug: nationbuilder-donations-api
- description: Elections are available on nations with voter features enabled. See more information about election functionality [here](https://support.nationbuilder.com/en/articles/2362732-set-up-your-election)
  name: NationBuilder Elections API
  slug: nationbuilder-elections-api
- description: This resource is for creating, reading, updating, and deleting Event RSVPs. When creating event RSVPs, the rsvp must be given signup data, either by passing a first name, last name, and email or phone
  name: NationBuilder Event Rsvps API
  slug: nationbuilder-event-rsvps-api
- description: This resource is for creating, reading, updating, and deleting ticket levels for events. manage the ticket levels available for the events. Ticket levels and their prices are displayed on public event
  name: NationBuilder Event Ticket Levels API
  slug: nationbuilder-event-ticket-levels-api
- description: Resource used for managing event data associated with event pages. More details on events within NationBuilder can be found [here](https://support.nationbuilder.com/en/articles/2319673-setting-up-an-e
  name: NationBuilder Events API
  slug: nationbuilder-events-api
- description: All kinds of data can be imported into a nation, when this happens we create an import resource as a record of the imported data. Each import has a type attribute defining the kind of data being impor
  name: NationBuilder Imports API
  slug: nationbuilder-imports-api
- description: Lists are collections of signups. Often created from filters they are useful for grouping signups together by common attributes. They can be used to perform batch updates on signups or as a list of re
  name: NationBuilder Lists API
  slug: nationbuilder-lists-api
- description: 'Referred to as email blasts, mailings send bulk emails to a group of signups at once. Mailings belong to and are sent via a broadcaster. The recipients of a mailing can be selected by lists, filters, '
  name: NationBuilder Mailings API
  slug: nationbuilder-mailings-api
- description: Membership types are used to identify memberships assigned to signups. A membership type has many memberships which are assigned a single signup. The only required attribute for the membership type is
  name: NationBuilder Membership Types API
  slug: nationbuilder-membership-types-api
- description: 'A membership is a way to organize supporters and provide additional benefits based on actions they''ve taken or money donated. More information about memberships and the fields found in the UI and API '
  name: NationBuilder Memberships API
  slug: nationbuilder-memberships-api
- description: Pages are published on your site. Each page type offers different features, you can view them [here](https://support.nationbuilder.com/en/articles/2319593-types-of-nationbuilder-pages).
  name: NationBuilder Pages API
  slug: nationbuilder-pages-api
- description: Documents a signup's step along a path journey.
  name: NationBuilder Path Histories API
  slug: nationbuilder-path-histories-api
- description: Documents the status change of a path journey.
  name: NationBuilder Path Journey Status Changes API
  slug: nationbuilder-path-journey-status-changes-api
- description: Path journeys are the relationship between signups and paths. Further information available [here](https://support.nationbuilder.com/en/articles/3055899-create-paths#create-a-path).
  name: NationBuilder Path Journeys API
  slug: nationbuilder-path-journeys-api
- description: Path steps name the positions within a path a signup can be assigned to. Further information available [here](https://support.nationbuilder.com/en/articles/3055899-create-paths#add-steps-to-the-path)
  name: NationBuilder Path Steps API
  slug: nationbuilder-path-steps-api
- description: Paths store information about path journeys and steps. They are related to signups via path journeys. A path can be assigned many path journeys and path steps. Further information available [here](htt
  name: NationBuilder Paths API
  slug: nationbuilder-paths-api
- description: Petition signatures are the relationship between petitions and signups.
  name: NationBuilder Petition Signatures API
  slug: nationbuilder-petition-signatures-api
- description: Petitions are pages on your site that can be signed and shared by your supporters. Learn more about them [here](https://support.nationbuilder.com/en/articles/2327303-create-a-petition).
  name: NationBuilder Petitions API
  slug: nationbuilder-petitions-api
- description: Pledges are a promise from a signup to donate to your cause. These are not donations. Further information available [here](https://support.nationbuilder.com/en/articles/2344197-fundraising-with-nation
  name: NationBuilder Pledges API
  slug: nationbuilder-pledges-api
- description: Precincts are districts used by political campaigns. Read more about them [here](https://support.nationbuilder.com/en/articles/2471652-creating-and-viewing-political-precincts).
  name: NationBuilder Precincts API
  slug: nationbuilder-precincts-api
- description: Valid relationship types are ["affiliate-affiliate", "alum-school", "assistant-assisted", "board_member-organization", "candidate-committee", "chapter-parent", "child-parent", "consultant-organization
  name: NationBuilder Relationships API
  slug: nationbuilder-relationships-api
- description: Profile information for a signup that can be displayed on a public site page. Read more on public profiles [here](https://support.nationbuilder.com/en/articles/2327657-how-public-profile-pages-work).
  name: NationBuilder Signup Profiles API
  slug: nationbuilder-signup-profiles-api
- description: Signup taggings are the relation between a signup and a tag.
  name: NationBuilder Signup Taggings API
  slug: nationbuilder-signup-taggings-api
- description: Tags are used to quickly identify signups by certain characteristics. They are related to signups through SignupTaggings. Read more about them [here](https://support.nationbuilder.com/en/articles/2305
  name: NationBuilder Signup Tags API
  slug: nationbuilder-signup-tags-api
- description: Signups store information about people in your nation. Further information available [here](https://support.nationbuilder.com/en/articles/8810042-how-records-are-added-to-the-people-database).
  name: NationBuilder Signups API
  slug: nationbuilder-signups-api
- description: A site is how supporters interact with your nation. Each site has a theme and many pages that can be drafted and published later to be viewed publicly. Read more about sites [here](https://support.nat
  name: NationBuilder Sites API
  slug: nationbuilder-sites-api
- description: Suggestion boxes are containers for collecting suggestions from your community. They live on website pages, and define the settings, auto-responses, categorization tags, and moderation rules for sugge
  name: NationBuilder Suggestion Boxes API
  slug: nationbuilder-suggestion-boxes-api
- description: Suggestions are individual ideas or proposals submitted to suggestion boxes on your site. They can be responded to, categorized, and managed by administrators. **Responding to Suggestions:** Responses
  name: NationBuilder Suggestions API
  slug: nationbuilder-suggestions-api
- description: The potential answers to a survey question.
  name: NationBuilder Survey Question Possible Responses API
  slug: nationbuilder-survey-question-possible-responses-api
- description: User responses to Survey Questions.
  name: NationBuilder Survey Question Responses API
  slug: nationbuilder-survey-question-responses-api
- description: Questions asked within a survey.
  name: NationBuilder Survey Questions API
  slug: nationbuilder-survey-questions-api
- description: Surveys have questions with possible responses. These questions also have responses from the users.
  name: NationBuilder Surveys API
  slug: nationbuilder-surveys-api
- description: Voter records store the ballot history of a single signup.
  name: NationBuilder Voters API
  slug: nationbuilder-voters-api
artifact_total: 46
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nationbuilder-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://nationbuilder.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.nationbuilder.com/en/collections/10408291-api
- group: docs
  title: ''
  type: Documentation
  url: https://support.nationbuilder.com/en/collections/10408291-api
- group: start
  title: ''
  type: GettingStarted
  url: https://support.nationbuilder.com/en/articles/9869274-nationbuilder-api-quickstart-guide
- group: operate
  title: ''
  type: Support
  url: https://support.nationbuilder.com/
- group: company
  title: ''
  type: Blog
  url: https://nationbuilder.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://nationbuilder.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://nationbuilder.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nationbuilder.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nationbuilder.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nationbuilder
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nationbuilder.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.nationbuilder.com/en/articles/2869824-where-can-i-find-out-what-s-new-or-been-updated-fixed-in-nationbuilder
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nationbuilder-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nationbuilder-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nationbuilder-v2-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nationbuilder-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nationbuilder-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nationbuilder-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nationbuilder-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nationbuilder-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nationbuilder-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/nationbuilder-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nationbuilder-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nationbuilder-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nationbuilder-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nationbuilder-domain-security.yml
created: '2026-07-17'
description: 'NationBuilder is a community-engagement and organizing platform for political campaigns, advocacy groups, nonprofits, and membership organizations, pairing a supporter CRM with a website/page builder, email and text messaging, event and petition tools, and integrated fundraising. Its developer surface is a REST API offered in two flavors: the current v2 API, which follows the JSON:API specification and authenticates with OAuth 2.0 (authorization-code with optional PKCE and refresh tokens), and a legacy v1 API that uses per-nation API tokens. The API exposes people/signups, donations, events, petitions, memberships, lists, tags, and related resources so integrators can sync supporter data and automate outreach. NationBuilder is multi-tenant: each nation is reached at its own {nation-slug}.nationbuilder.com host.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nationbuilder.png
layout: provider
mcp_servers:
- description: ''
  name: nationbuilder-mcp.yml
  slug: nationbuilder-mcpyml
modified: '2026-07-20'
name: NationBuilder
nav: Providers
network: true
overview: 'NationBuilder publishes 41 APIs on the [APIs.io](https://apis.io/) network, including Async Processes API, Automation Enrollments API, Automations API, and 38 more. Tagged areas include Community Organizing, CRM, Political, Nonprofit, and Fundraising.


  NationBuilder''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, changelog, and 22 more developer resources.'
random_paper: 32
rate_limits:
- limit_count: 0
  name: Nationbuilder Rate Limits
  slug: nationbuilder-rate-limits
score:
  band: developing
  composite: 48.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.5
    developer_ergonomics: 60.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 48.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Nationbuilder Authentication
  slug: nationbuilder-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Nationbuilder Domain Security
  slug: nationbuilder-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nationbuilder
tags:
- Community Organizing
- CRM
- Political
- Nonprofit
- Fundraising
- Advocacy
- Website Builder
- Events
- Email
- JSON:API
website: https://nationbuilder.com
---
