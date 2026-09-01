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
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 224
  human_in_the_loop: 4
  name: Clickfunnels Agentic Access
  operation_count: 418
  slug: clickfunnels-agentic-access
  summary_line: 418 operations · 224 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: '> Countries are a global reference list used when setting addresses. The Addresses::Country API provides read-only access to the list of countries, each with its ISO 3166-1 alpha-2 code (iso2). Use a '
  name: ClickFunnels Addresses::Country API
  slug: clickfunnels-addresses-country-api
- description: '> Regions are the states/provinces of a country. The Addresses::Region API provides read-only access to the regions of a country. Use a region''s code or name as the address region value. Many countrie'
  name: ClickFunnels Addresses::Region API
  slug: clickfunnels-addresses-region-api
- description: '> Scheduled Appointment Events represent set meeting events The Appointment Scheduled Event represents a scheduled meeting between a ClickFunnels user and a contact on a specific day and time.'
  name: ClickFunnels Appointments::Scheduled Event API
  slug: clickfunnels-appointments-scheduledevent-api
- description: '> Blogs represent a blog resource belonging to a workspace site A Blog is a top-level container for blog posts, categories, tags, and authors. Each workspace site can have one or more blogs, each with'
  name: ClickFunnels Blog API
  slug: clickfunnels-blog-api
- description: Blog Authors. See [Authors (read-only)](https://accounts.myclickfunnels.com/.well-known/blogs/skill.md#authors-read-only) in the [Blogs Skill](https://accounts.myclickfunnels.com/.well-known/blogs/ski
  name: ClickFunnels Blogs::Author API
  slug: clickfunnels-blogs-author-api
- description: Blog Categories. See [Categories (read-only)](https://accounts.myclickfunnels.com/.well-known/blogs/skill.md#categories-read-only) in the [Blogs Skill](https://accounts.myclickfunnels.com/.well-known/
  name: ClickFunnels Blogs::Category API
  slug: clickfunnels-blogs-category-api
- description: '> Blog Posts are the individual articles published within a Blog Blog posts support rich content via PML markup, visibility controls, SEO settings, categories, tags, and authors. Use `expand[]=markup`'
  name: ClickFunnels Blogs::Post API
  slug: clickfunnels-blogs-post-api
- description: Blog Tags. See [Tags (list / show / create)](https://accounts.myclickfunnels.com/.well-known/blogs/skill.md#tags-list--show--create) in the [Blogs Skill](https://accounts.myclickfunnels.com/.well-know
  name: ClickFunnels Blogs::Tag API
  slug: clickfunnels-blogs-tag-api
- description: '> Bans prevent a Contact from accessing a Community. A Ban records which Contact is banned, who issued the ban, the scope of the ban (`bannable_type`/`bannable_id`), and an optional reason. The `banne'
  name: ClickFunnels Communities::Ban API
  slug: clickfunnels-communities-ban-api
- description: '> Async bulk action that exports community ban data to a file in the background. Creating an ExportAction enqueues a background job and immediately returns an action record. Poll the `show` endpoint u'
  name: ClickFunnels Communities::Bans::Export Action API
  slug: clickfunnels-communities-bans-exportaction-api
- description: '> Async bulk action that unbans multiple contacts from a community in the background. Creating an UnbanAction enqueues a background job and immediately returns an action record. Poll the `show` endpoi'
  name: ClickFunnels Communities::Bans::Unban Action API
  slug: clickfunnels-communities-bans-unbanaction-api
- description: '> Memberships represent a Contact''s membership in a Community. A Membership joins a Contact to a Community and tracks whether that member has moderator privileges. Creating or updating a membership al'
  name: ClickFunnels Communities::Membership API
  slug: clickfunnels-communities-membership-api
- description: '> Async bulk action that adds multiple members to one or more community spaces (groups) in the background. Creating an AddToGroupAction enqueues a background job and immediately returns an action reco'
  name: ClickFunnels Communities::Memberships::Add To Group Action API
  slug: clickfunnels-communities-memberships-addtogroupaction-api
- description: '> Async bulk action that bans multiple community members in the background. Creating a BanAction enqueues a background job and immediately returns an action record. Poll the `show` endpoint using the '
  name: ClickFunnels Communities::Memberships::Ban Action API
  slug: clickfunnels-communities-memberships-banaction-api
- description: '> Async bulk action that exports community membership data to a file in the background. Creating an ExportAction enqueues a background job and immediately returns an action record. Poll the `show` end'
  name: ClickFunnels Communities::Memberships::Export Action API
  slug: clickfunnels-communities-memberships-exportaction-api
- description: '> Async bulk action that removes multiple members from one or more community spaces (groups) in the background. Creating a RemoveFromGroupAction enqueues a background job and immediately returns an ac'
  name: ClickFunnels Communities::Memberships::Remove From Group Action API
  slug: clickfunnels-communities-memberships-removefromgroupaction-api
- description: '> Spaces (Topics) are the individual discussion areas within a Space Group. A Space is a single discussion channel or topic area within a Space Group. Members post, comment, and interact inside Spaces'
  name: ClickFunnels Communities::Space API
  slug: clickfunnels-communities-space-api
- description: '> Space Groups are named sections within a Community that contain Spaces (Topics). A Space Group is a logical grouping of Spaces (Topics) within a Community. Use Space Groups to organize community con'
  name: ClickFunnels Communities::Space Group API
  slug: clickfunnels-communities-spacegroup-api
- description: '> Posts are member-created content items within a Community Space. A Post belongs to a Space and is authored by a Contact. Posts support rich HTML body content, optional titles, pinning, and cover ima'
  name: ClickFunnels Communities::Spaces::Post API
  slug: clickfunnels-communities-spaces-post-api
- description: '> Comments are member replies on a Community Post. A Comment belongs to a Post and is authored by a Contact. Comments support rich HTML body content and threaded replies via `parent_comment_id`. Comme'
  name: ClickFunnels Communities::Spaces::Post::Comment API
  slug: clickfunnels-communities-spaces-post-comment-api
- description: '> Comment Likes record a Contact''s like reaction on a Post Comment. A Comment Like belongs to a Comment and is authored by a Contact. Likes have no update operation — create one to like, delete it to '
  name: ClickFunnels Communities::Spaces::Post::Comment::Like API
  slug: clickfunnels-communities-spaces-post-comment-like-api
- description: '> Post Likes record a Contact''s like reaction on a Community Post. A Post Like belongs to a Post and is authored by a Contact. Likes have no update operation — create one to like, delete it to unlike.'
  name: ClickFunnels Communities::Spaces::Post::Like API
  slug: clickfunnels-communities-spaces-post-like-api
- description: '> Video Embeds attach a hosted video to a Community Post. A Video Embed belongs to a Post and stores the provider name, source URL, and optional provider-specific metadata. Video Embeds have no update'
  name: ClickFunnels Communities::Spaces::Post::Video Embed API
  slug: clickfunnels-communities-spaces-post-videoembed-api
- description: '> Communities are membership-based spaces where contacts can post, interact, and engage. A Community is the top-level container for community content. It belongs to a workspace site and holds one or m'
  name: ClickFunnels Community API
  slug: clickfunnels-community-api
- description: Contact
  name: ClickFunnels Contact API
  slug: clickfunnels-contact-api
- description: '> Contact Applied Tags The Contact Applied Tags APIs allow you to list, apply and remove tags associated with a specific contact. To utilize this, first obtain the Tag IDs for all the Contact Tags for'
  name: ClickFunnels Contacts::Applied Tag API
  slug: clickfunnels-contacts-appliedtag-api
- description: '> Bulk-enroll contacts into course sections An Enroll Action enrolls an entire audience of contacts into one or more course sections in a single async operation. Pass `course_ids` to enroll in every s'
  name: ClickFunnels Contacts::Enroll Action API
  slug: clickfunnels-contacts-enrollaction-api
- description: '> Bulk-export contacts to a CSV file An Export Action generates a CSV of an audience of contacts in a single async operation. Supply `fields` to control which contact columns appear in the CSV (includ'
  name: ClickFunnels Contacts::Export Action API
  slug: clickfunnels-contacts-exportaction-api
- description: '> AI-generated contact filters Translate a natural-language audience description into a ClickFunnels contact filter using an AI model. The model can use the full range of contact filter conditions — i'
  name: ClickFunnels Contacts::Filter API
  slug: clickfunnels-contacts-filter-api
- description: '> Bulk-trigger a workflow across a filtered set of contacts A Run Workflow Action enqueues an entire audience of contacts into a workflow in a single async operation. Requires a `workflow_id`. Set `fo'
  name: ClickFunnels Contacts::Run Workflow Action API
  slug: clickfunnels-contacts-runworkflowaction-api
- description: '# Contact Tags Contact Tags are unique to each workspace, allowing for customized organization of your Contacts. Once created, these tags can be applied to any contact within the same workspace using '
  name: ClickFunnels Contacts::Tag API
  slug: clickfunnels-contacts-tag-api
- description: '> Bulk apply or remove tags across a filtered set of contacts A Tag Action applies (or removes) one or more Contact Tags across an entire audience in a single async operation. Instead of looping over '
  name: ClickFunnels Contacts::Tag Action API
  slug: clickfunnels-contacts-tagaction-api
- description: '> Bulk-unsubscribe contacts from email An Unsubscribe Action marks an entire audience of contacts as unsubscribed from email in a single async operation. **Target selection** — supply exactly one of: '
  name: ClickFunnels Contacts::Unsubscribe Action API
  slug: clickfunnels-contacts-unsubscribeaction-api
- description: '> Represents the volume of educational material The course is the top-level layer of a concept for educational material. It is the _thing_ to be sold to a customer. Once a customer purchases or otherw'
  name: ClickFunnels Course API
  slug: clickfunnels-course-api
- description: '> Controls access to course sections and lessons By purchasing or otherwise opting into a course, an enrollment record is created. Enrollments dictate which sections, sub-sections, and lessons the stu'
  name: ClickFunnels Courses::Enrollment API
  slug: clickfunnels-courses-enrollment-api
- description: '> Represents the material within a Course The lesson is the part of the course which teaches the material described within the course. Completing lessons can unlock access to other lessons or sections'
  name: ClickFunnels Courses::Lesson API
  slug: clickfunnels-courses-lesson-api
- description: '> Marks a lesson as completed for enrollment. To mark a lesson as completed by an enrollment, create an `Courses::LessonCompletion` record. To undo this, the `Courses::LessonCompletion` record must be'
  name: ClickFunnels Courses::Lesson Completion API
  slug: clickfunnels-courses-lessoncompletion-api
- description: '> Represents the modules within a Course The section is the organization layer of a course where the content is accessed and managed for a customer. Sections can have sub-sections and will have one or'
  name: ClickFunnels Courses::Section API
  slug: clickfunnels-courses-section-api
- description: '> Publishes course sections (and their lessons) in bulk. A Publish Action selects one or more course sections — either by explicit `target_ids` (course-section public IDs) or `target_all` — and publis'
  name: ClickFunnels Courses::Sections::Publish Action API
  slug: clickfunnels-courses-sections-publishaction-api
- description: '> A reusable, workspace-scoped discount the checkout applies on top of a price. A Discount is the right tool for a coupon code, a percentage/amount off, or a time-boxed sale - anything you would other'
  name: ClickFunnels Discount API
  slug: clickfunnels-discount-api
- description: '> Domains represent custom domains connected to a workspace. The Domains API provides read-only access to the domains configured for a workspace. Use this API to look up domain IDs for use with other '
  name: ClickFunnels Domain API
  slug: clickfunnels-domain-api
- description: '> Downloads are workspace files that can be granted through product variants. Use the Download''s `asset_id` when configuring digital-asset access through the `Products::Variant` resource.'
  name: ClickFunnels Download API
  slug: clickfunnels-download-api
- description: '> Email Addresses Email Addresses represent sender addresses in your workspace. These are used as "from" and "reply-to" addresses when sending email broadcasts. Select a from-address whose `usable_as_'
  name: ClickFunnels Emails::Address API
  slug: clickfunnels-emails-address-api
- description: '> Email Broadcasts Email Broadcasts allow you to send one-time email campaigns to your contacts. Broadcasts are created in draft status and can be sent immediately or scheduled for later delivery. To '
  name: ClickFunnels Emails::Broadcast API
  slug: clickfunnels-emails-broadcast-api
- description: '> Send Actions trigger the actual delivery of an email broadcast. A Send Action is the trigger that sends (or schedules) the parent broadcast — the same action the ClickFunnels dashboard fires when yo'
  name: ClickFunnels Emails::Broadcasts::Send Action API
  slug: clickfunnels-emails-broadcasts-sendaction-api
- description: '> Email Domains represent the sending domains (DKIM/SPF/DMARC) available to a workspace for outbound email. One domain name has two independent jobs, and sending needs both. This resource covers email'
  name: ClickFunnels Emails::Domain API
  slug: clickfunnels-emails-domain-api
- description: '> Email Settings Email Settings represent your workspace''s email configuration, including default from and reply-to addresses for system and marketing emails. See the [Business mailing address prerequ'
  name: ClickFunnels Emails::Settings API
  slug: clickfunnels-emails-settings-api
- description: '> Email Templates Email Templates are reusable email content that can be used with broadcasts. See [Templates](https://accounts.myclickfunnels.com/.well-known/emails/skill.md#templates) in the [Emails'
  name: ClickFunnels Emails::Template API
  slug: clickfunnels-emails-template-api
- description: '> Email Topics Email Topics are used for email broadcast categorization and subscriber preferences. See [Sending or scheduling a broadcast](https://accounts.myclickfunnels.com/.well-known/emails/skill'
  name: ClickFunnels Emails::Topic API
  slug: clickfunnels-emails-topic-api
- description: '> Manage Forms, FieldSets, Fields, Submissions and Answers The Forms API and it''s related resources allow you to manage in detail all parts of your ClickFunnels forms.'
  name: ClickFunnels Form API
  slug: clickfunnels-form-api
- description: Form Fields
  name: ClickFunnels Forms::Field API
  slug: clickfunnels-forms-field-api
- description: Form Field Options
  name: ClickFunnels Forms::Fields::Option API
  slug: clickfunnels-forms-fields-option-api
- description: Form FieldSets
  name: ClickFunnels Forms::Field Set API
  slug: clickfunnels-forms-fieldset-api
- description: '> Allows to submit and analyze forms programmatically The `Forms::Submission` resource together with the `Form` and other `Forms::` allows you to create form submission programmatically outside of Cli'
  name: ClickFunnels Forms::Submission API
  slug: clickfunnels-forms-submission-api
- description: Form Submission Answers
  name: ClickFunnels Forms::Submissions::Answer API
  slug: clickfunnels-forms-submissions-answer-api
- description: '> Presents submitted forms including the detailed data breakdown The `FormSubmission` resource is a log of all the form submissions that happened for a given workspace. You can retrieve the form submi'
  name: ClickFunnels Form Submission API
  slug: clickfunnels-formsubmission-api
- description: '> Fulfillments allow fulfilling orders and managing shipments. Please refer to [our Fulfillments guide](https://developers.myclickfunnels.com/docs/fulfillments) for more information.'
  name: ClickFunnels Fulfillment API
  slug: clickfunnels-fulfillment-api
- description: Fulfillment Locations
  name: ClickFunnels Fulfillments::Location API
  slug: clickfunnels-fulfillments-location-api
- description: '> The Funnel resource contains relevant metadata about funnels. Funnel-level analytics are available via the Fetch Funnel Stats endpoint (`GET /funnels/{funnel_id}/stats`); per-page analytics via the '
  name: ClickFunnels Funnel API
  slug: clickfunnels-funnel-api
- description: '> Conditional split steps route contacts down a "matched" or "unmatched" branch based on a RefineFilter condition. Conditional split steps live inside a funnel''s workflow. Each step exposes a `conditi'
  name: ClickFunnels Funnels::Conditional Split Step API
  slug: clickfunnels-funnels-conditionalsplitstep-api
- description: '> Split test steps wrap an existing funnel page in a two-branch A/B split with configurable traffic weights. Split test steps live inside a funnel''s workflow. Each step exposes a 2-entry `variants` ar'
  name: ClickFunnels Funnels::Split Test Step API
  slug: clickfunnels-funnels-splitteststep-api
- description: '> Funnels::Tag are used to distinguish, segment and run additional automations on your funnels and the users who go through them.'
  name: ClickFunnels Funnels::Tag API
  slug: clickfunnels-funnels-tag-api
- description: '> Images can be used in a variety of use cases. An image can be created or updated from a URL by defining the `upload_source_url` parameter. The response returns the hosted `url` and the Image `id`. F'
  name: ClickFunnels Image API
  slug: clickfunnels-image-api
- description: '> Orders describe a purchase made by a contact. Please refer to the [Orders Overview Guide](https://developers.myclickfunnels.com/docs/orders) for more information. See the [Orders Skill](https://acco'
  name: ClickFunnels Order API
  slug: clickfunnels-order-api
- description: '> Order Applied Tags The Order Applied Tags APIs allow you to list, apply and remove tags associated with a specific order. To utilize this, first obtain the Tag IDs for all the Order Tags for your wo'
  name: ClickFunnels Orders::Applied Tag API
  slug: clickfunnels-orders-appliedtag-api
- description: '> Invoices track payments for orders. Order Invoices are the invoices issued against Orders. For more information please consult our [Orders Overview guide](https://developers.myclickfunnels.com/docs/'
  name: ClickFunnels Orders::Invoice API
  slug: clickfunnels-orders-invoice-api
- description: '> Restocks make it possible to restock in case a priorly issued fulfillment is not going to be fulfilled. If a customer pays for an invoice that will not get fulfilled (e.g. the invoice may have been '
  name: ClickFunnels Orders::Invoices::Restock API
  slug: clickfunnels-orders-invoices-restock-api
- description: '> Preview and commit variant/price changes on existing subscription line items. A self-serve flow for switching the variant or price on a subscription line item. The surface has three endpoints — disc'
  name: ClickFunnels Orders::Line Items::Change API
  slug: clickfunnels-orders-lineitems-change-api
- description: '> Order Tags Order Tags are unique to each workspace, allowing for customized organization of your orders. Once created, these tags can be applied to any order within the same workspace. This API allo'
  name: ClickFunnels Orders::Tag API
  slug: clickfunnels-orders-tag-api
- description: Order Transactions
  name: ClickFunnels Orders::Transaction API
  slug: clickfunnels-orders-transaction-api
- description: '> Page offers extra information about ClickFunnels pages, like those that are part of funnels. It''s the main element that the user modifies when editing a Page in the ClickFunnels editor. You can also'
  name: ClickFunnels Page API
  slug: clickfunnels-page-api
- description: '> Products can be used to create and edit sellable goods. Products have a few boolean attributes including `archived`, `visible_in_store`, and `visible_in_customer_center`. Products that are not `arch'
  name: ClickFunnels Product API
  slug: clickfunnels-product-api
- description: Product Collections
  name: ClickFunnels Products::Collection API
  slug: clickfunnels-products-collection-api
- description: Product Prices
  name: ClickFunnels Products::Price API
  slug: clickfunnels-products-price-api
- description: '> Allowed variant/price upgrade and downgrade targets for a source price. Merchant-configured rows define which variant + price combinations a subscription using a given source price may switch to. Th'
  name: ClickFunnels Products::Prices::Change Option API
  slug: clickfunnels-products-prices-changeoption-api
- description: Product Tags
  name: ClickFunnels Products::Tag API
  slug: clickfunnels-products-tag-api
- description: '> Product variants If there are multiple variants of a product (like when a T-shirt can come in many sizes or colors), then these should be created as `Products::Variant` records related to the `Produ'
  name: ClickFunnels Products::Variant API
  slug: clickfunnels-products-variant-api
- description: '> Reusable audience filters that scope contacts for conditional splits, email broadcasts, workflow branches, and other ClickFunnels surfaces. A RefineFilter stores a named, conjunctive set of criteria'
  name: ClickFunnels Refine Filter API
  slug: clickfunnels-refinefilter-api
- description: Sales Opportunity Notes
  name: ClickFunnels Sales::Opportunities::Note API
  slug: clickfunnels-sales-opportunities-note-api
- description: '> Sales Opportunities Sales Opportunities are initially created in a specific stage of a Pipeline and can be moved between different stages within that Pipeline. Each Sales Opportunity requires a name'
  name: ClickFunnels Sales::Opportunity API
  slug: clickfunnels-sales-opportunity-api
- description: '> Sales Pipelines Pipelines allow you to organize, track and advance Opportunies between different Stages. A Pipeline consists of multiple Stages. When creating a Pipeline, you must specify one or mor'
  name: ClickFunnels Sales::Pipeline API
  slug: clickfunnels-sales-pipeline-api
- description: '> Sales Pipeline Stages Stages belong to a Pipeline, and allow you to track and advance Opportunities. You can re-order Stages in a Pipeline by updating the `sort_order` attribute of a Stage, giving t'
  name: ClickFunnels Sales::Pipelines::Stage API
  slug: clickfunnels-sales-pipelines-stage-api
- description: Shipping LocationGroup
  name: ClickFunnels Shipping::Location Group API
  slug: clickfunnels-shipping-locationgroup-api
- description: Shipping Package
  name: ClickFunnels Shipping::Package API
  slug: clickfunnels-shipping-package-api
- description: Shipping Profile
  name: ClickFunnels Shipping::Profile API
  slug: clickfunnels-shipping-profile-api
- description: Shipping Rate
  name: ClickFunnels Shipping::Rate API
  slug: clickfunnels-shipping-rate-api
- description: Shipping Rate Names
  name: ClickFunnels Shipping::Rates::Name API
  slug: clickfunnels-shipping-rates-name-api
- description: Shipping Zone
  name: ClickFunnels Shipping::Zone API
  slug: clickfunnels-shipping-zone-api
- description: '> Sites represent a workspace''s website configuration containing global code settings.'
  name: ClickFunnels Site API
  slug: clickfunnels-site-api
- description: '> Stores'
  name: ClickFunnels Store API
  slug: clickfunnels-store-api
- description: '> Styles determine some CSS specifics for a theme.'
  name: ClickFunnels Style API
  slug: clickfunnels-style-api
- description: Teams
  name: ClickFunnels Team API
  slug: clickfunnels-team-api
- description: '> Themes determine the look of the user-facing ClickFunnels pages. A theme bundles the relevant site pages, like home page, storefront, course pages, etc.'
  name: ClickFunnels Theme API
  slug: clickfunnels-theme-api
- description: Users
  name: ClickFunnels User API
  slug: clickfunnels-user-api
- description: Webhook Outgoing Endpoints
  name: ClickFunnels Webhooks::Outgoing::Endpoint API
  slug: clickfunnels-webhooks-outgoing-endpoint-api
- description: Webhooks Outgoing Events
  name: ClickFunnels Webhooks::Outgoing::Event API
  slug: clickfunnels-webhooks-outgoing-event-api
- description: The authoritative catalog of webhook event types available for subscription. Use this endpoint to discover the exact string keys to supply in `event_type_ids` when creating or updating a webhook endpo
  name: ClickFunnels Webhooks::Outgoing::Event Type API
  slug: clickfunnels-webhooks-outgoing-eventtype-api
- description: Standalone automation workflows that enroll contacts and execute a sequence of action steps (send email, apply tag, delay, split, etc.). A workflow is either `draft` (no active triggers), `live` (enab
  name: ClickFunnels Workflow API
  slug: clickfunnels-workflow-api
- description: 'Execution records tracking a contact''s progress through a workflow. Status is derived: `active`, `paused`, `completed`, or `canceled`. Runs can be listed/filtered or manually created to enroll a conta'
  name: ClickFunnels Workflows::Run API
  slug: clickfunnels-workflows-run-api
- description: 'Action and split steps within a workflow. The step `type` (e.g. `send_email_step`, `delay_step`, `conditional_split_step`) is conveyed via the `step_type_settings` map — the single key in that map is '
  name: ClickFunnels Workflows::Step API
  slug: clickfunnels-workflows-step-api
- description: 'Triggers attached to a workflow. Each trigger specifies an `event_type_key` (e.g. `$contact.tag_applied`) and optional condition FK ids that narrow which events fire the trigger. See [Triggers](https:'
  name: ClickFunnels Workflows::Trigger API
  slug: clickfunnels-workflows-trigger-api
- description: Workspace
  name: ClickFunnels Workspace API
  slug: clickfunnels-workspace-api
artifact_total: 113
asyncapis:
- description: ''
  name: Clickfunnels Webhooks
  slug: clickfunnels-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClickFunnels API
  slug: open-clickfunnels-api
- collection_type: open
  name: ClickFunnels 2.0 API
  slug: open-clickfunnels
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/clickfunnels/cli/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/clickfunnels-capability-edges.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/clickfunnels-api-openapi-original.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clickfunnels-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clickfunnels-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/clickfunnels-api-catalog.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/clickfunnels-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clickfunnels-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clickfunnels-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clickfunnels-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clickfunnels-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clickfunnels-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.myclickfunnels.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clickfunnels-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clickfunnels-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clickfunnels-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/clickfunnels-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clickfunnels-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/clickfunnels-cli.yml
- group: design
  title: ''
  type: Components
  url: components/clickfunnels-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/clickfunnels-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clickfunnels-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clickfunnels-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clickfunnels-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clickfunnels-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clickfunnels-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.myclickfunnels.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.myclickfunnels.com/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developers.myclickfunnels.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.myclickfunnels.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.myclickfunnels.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.myclickfunnels.com
- group: company
  title: ''
  type: Blog
  url: https://www.clickfunnels.com/blog/feed
- group: company
  title: ''
  type: Website
  url: https://www.clickfunnels.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clickfunnels.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://signup.clickfunnels.com
- group: start
  title: ''
  type: Login
  url: https://accounts.myclickfunnels.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clickfunnels.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clickfunnels.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clickfunnels
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clickfunnels2
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/clickfunnels/cli
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clickfunnels
- group: other
  title: ''
  type: Classic API
  url: https://apidocs.clickfunnels.com/
created: '2026-05-11'
description: 'ClickFunnels is a sales funnel and online business platform that lets entrepreneurs build landing pages, sales funnels, checkout flows, courses, membership sites, communities, blogs and email marketing campaigns without code. The ClickFunnels 2.0 REST API is a 418-operation OpenAPI 3.1 contract covering teams, workspaces, funnels, pages, blogs, products, discounts, orders, invoices, transactions, subscriptions, contacts, courses, communities, forms, workflows, email and analytics, authenticated with a team-scoped Bearer token or with workspace-scoped OAuth 2.0. It is discoverable the correct way: an RFC 9727 api-catalog links the spec, RFC 8414 metadata publishes the OAuth scopes, and sixteen Markdown Agent Skills are served from /.well-known/ for agents driving the API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clickfunnels.png
layout: provider
modified: '2026-08-13'
name: ClickFunnels
nav: Providers
network: true
overview: 'ClickFunnels publishes 102 APIs on the [APIs.io](https://apis.io/) network, including Addresses::Country API, Addresses::Region API, Appointments::Scheduled Event API, and 99 more. Tagged areas include Sales Funnels, Landing Pages, E-Commerce, Marketing, and Checkout.


  The ClickFunnels catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ClickFunnels'' developer surface includes authentication, changelog, CLI, sandbox, documentation, API reference, getting-started guide, and 38 more developer resources.'
plans:
- name: Clickfunnels Plans Pricing
  plan_count: 4
  slug: clickfunnels-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Clickfunnels Rate Limits
  slug: clickfunnels-rate-limits
scopes:
- name: Clickfunnels Scopes
  scope_count: 5
  slug: clickfunnels-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 61.8
  coverage:
    artifact_dirs: 27
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 64.8
    developer_ergonomics: 66.7
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clickfunnels/refs/heads/main/screenshots/clickfunnels-2026-06-20T174514.png
security:
- kind: authentication
  name: Clickfunnels Authentication
  slug: clickfunnels-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Clickfunnels Domain Security
  slug: clickfunnels-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clickfunnels Vulnerability Disclosure
  slug: clickfunnels-vulnerability-disclosure
  summary_line: Hackerone
slug: clickfunnels
tags:
- Sales Funnels
- Landing Pages
- E-Commerce
- Marketing
- Checkout
- CRM
- Email Marketing
- Online Courses
- Webhook
- Website Builder
- Subscription
- Marketing Automation
- Agent Skills
website: https://www.clickfunnels.com
---
