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
  - rate-limits
  - security
  - sandbox
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
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Ghost Org Agentic Access
  operation_count: 56
  slug: ghost-org-agentic-access
  summary_line: 56 operations · 26 acting
api_count: 3
apis:
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Image uploads.
  name: Ghost Admin - Images API
  phrasing_intents:
  - id: uploadAdminImage
    intent: Upload an image for use in content
    question: How do I upload an image to Ghost and get back a URL I can put in a post?
  phrasing_ops: 1
  slug: ghost-org-admin-images-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-write member labels.
  name: Ghost Admin - Labels API
  phrasing_intents:
  - id: browseAdminLabels
    intent: List member labels
    question: What labels have I set up for grouping my members?
  - id: addAdminLabel
    intent: Create a member label
    question: How do I create a new label to segment my members?
  - id: editAdminLabel
    intent: Rename or update a member label
    question: Can I rename an existing member label without recreating it?
  - id: deleteAdminLabel
    intent: Delete a member label
    question: How do I remove a member label I no longer need?
  phrasing_ops: 4
  slug: ghost-org-admin-labels-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-write members.
  name: Ghost Admin - Members API
  phrasing_intents:
  - id: browseAdminMembers
    intent: List and filter members
    question: How do I get a list of all my members with their labels included?
  - id: addAdminMember
    intent: Add a new member
    question: How do I add someone to my Ghost site as a member?
  - id: readAdminMemberById
    intent: Get a member by ID
    question: How can I look up one member's details if I have their ID?
  - id: editAdminMember
    intent: Update a member's details
    question: How do I change an existing member's name or email?
  phrasing_ops: 4
  slug: ghost-org-admin-members-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-write newsletters.
  name: Ghost Admin - Newsletters API
  phrasing_intents:
  - id: browseAdminNewsletters
    intent: List newsletters
    question: What newsletters are configured on my publication?
  - id: addAdminNewsletter
    intent: Create a newsletter
    question: How do I start a second newsletter on my site?
  - id: editAdminNewsletter
    intent: Update a newsletter
    question: Can I change the name or sender of an existing newsletter?
  phrasing_ops: 3
  slug: ghost-org-admin-newsletters-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-write promotional offers.
  name: Ghost Admin - Offers API
  phrasing_intents:
  - id: browseAdminOffers
    intent: List offers
    question: Which promotional offers do I currently have?
  - id: addAdminOffer
    intent: Create a promotional offer
    question: How do I create a discount offer for new paid members?
  - id: editAdminOffer
    intent: Update an offer
    question: Can I change the name or code of an offer that's already live?
  phrasing_ops: 3
  slug: ghost-org-admin-offers-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-write pages.
  name: Ghost Admin - Pages API
  phrasing_intents:
  - id: browseAdminPages
    intent: List pages including drafts
    question: How do I list all the static pages on my site, drafts included?
  - id: addAdminPage
    intent: Create a page
    question: How do I create a new static page like an About page?
  - id: readAdminPageById
    intent: Get a page by ID
    question: How do I fetch one page by its ID, even if it's a draft?
  - id: editAdminPage
    intent: Update a page
    question: How do I edit an existing static page's content?
  - id: deleteAdminPage
    intent: Delete a page
    question: How do I remove a static page from my site?
  phrasing_ops: 5
  slug: ghost-org-admin-pages-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-write posts.
  name: Ghost Admin - Posts API
  phrasing_intents:
  - id: browseAdminPosts
    intent: List posts including drafts
    question: How do I list all my posts, including drafts and scheduled ones?
  - id: addAdminPost
    intent: Create a post
    question: How do I create a new blog post through the Admin API?
  - id: readAdminPostById
    intent: Get a post by ID
    question: How do I get one post by its ID, even if it's unpublished?
  - id: editAdminPost
    intent: Update a post
    question: How do I edit a post that's already been created?
  - id: deleteAdminPost
    intent: Delete a post
    question: How do I permanently remove a blog post?
  - id: readAdminPostBySlug
    intent: Get a post by its URL slug
    question: How do I find a post when I only know its URL slug?
  phrasing_ops: 6
  slug: ghost-org-admin-posts-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-only public site metadata.
  name: Ghost Admin - Site API
  phrasing_intents:
  - id: readAdminSite
    intent: Get basic site info
    question: What version of Ghost is my site running?
  phrasing_ops: 1
  slug: ghost-org-admin-site-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-write tags.
  name: Ghost Admin - Tags API
  phrasing_intents:
  - id: browseAdminTags
    intent: List tags
    question: What tags do I have on my site?
  - id: addAdminTag
    intent: Create a tag
    question: How do I create a new tag for organizing posts?
  - id: editAdminTag
    intent: Update a tag
    question: Can I rename a tag or change its description?
  - id: deleteAdminTag
    intent: Delete a tag
    question: How do I get rid of a tag I don't use anymore?
  phrasing_ops: 4
  slug: ghost-org-admin-tags-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Theme upload and activation.
  name: Ghost Admin - Themes API
  phrasing_intents:
  - id: uploadAdminTheme
    intent: Upload a theme zip
    question: How do I install a custom theme on my Ghost site?
  - id: activateAdminTheme
    intent: Activate an installed theme
    question: How do I switch my site to a different installed theme?
  phrasing_ops: 2
  slug: ghost-org-admin-themes-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-write subscription tiers.
  name: Ghost Admin - Tiers API
  phrasing_intents:
  - id: browseAdminTiers
    intent: List membership tiers
    question: What membership tiers are set up on my site?
  - id: addAdminTier
    intent: Create a membership tier
    question: How do I add a new paid membership tier?
  - id: editAdminTier
    intent: Update a membership tier
    question: How do I change the name or benefits of a tier?
  phrasing_ops: 3
  slug: ghost-org-admin-tiers-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read-only staff users.
  name: Ghost Admin - Users API
  phrasing_intents:
  - id: browseAdminUsers
    intent: List staff users
    question: Who are the staff users on my Ghost site?
  - id: readAdminUserById
    intent: Get a staff user by ID
    question: How do I look up a staff member when I have their ID?
  - id: readAdminUserBySlug
    intent: Get a staff user by slug
    question: How do I find a staff member using their profile slug?
  phrasing_ops: 3
  slug: ghost-org-admin-users-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Outbound webhook management.
  name: Ghost Admin - Webhooks API
  phrasing_intents:
  - id: addAdminWebhook
    intent: Register an outbound webhook
    question: How do I get notified when a post is published on my site?
  - id: editAdminWebhook
    intent: Update a webhook
    question: Can I change the target URL or event of an existing webhook?
  - id: deleteAdminWebhook
    intent: Delete a webhook
    question: How do I stop a webhook from firing?
  phrasing_ops: 3
  slug: ghost-org-admin-webhooks-api
- baseURL: https://{admin_domain}/ghost/api/content
  baseurl_source: declared
  description: Read-only authors.
  name: Ghost Content - Authors API
  phrasing_intents:
  - id: browseContentAuthors
    intent: List public authors
    question: How do I show a list of writers on my front-end?
  - id: readContentAuthorById
    intent: Get a public author by ID
    question: How do I load one author's public profile by ID?
  - id: readContentAuthorBySlug
    intent: Get a public author by slug
    question: How do I render an author page from the slug in the URL?
  phrasing_ops: 3
  slug: ghost-org-content-authors-api
- baseURL: https://{admin_domain}/ghost/api/content
  baseurl_source: declared
  description: Read-only published pages.
  name: Ghost Content - Pages API
  phrasing_intents:
  - id: browseContentPages
    intent: List published pages
    question: How do I pull the published static pages into my front-end?
  - id: readContentPageById
    intent: Get a published page by ID
    question: How do I load a single published page by ID?
  - id: readContentPageBySlug
    intent: Get a published page by slug
    question: How do I render a page like /about from its slug?
  phrasing_ops: 3
  slug: ghost-org-content-pages-api
- baseURL: https://{admin_domain}/ghost/api/content
  baseurl_source: declared
  description: Read-only published posts.
  name: Ghost Content - Posts API
  phrasing_intents:
  - id: browseContentPosts
    intent: List published posts
    question: How do I pull my latest published posts into a website or app?
  - id: readContentPostById
    intent: Get a published post by ID
    question: How do I load one published post by its ID?
  - id: readContentPostBySlug
    intent: Get a published post by slug
    question: How do I render a blog article from the slug in its URL?
  phrasing_ops: 3
  slug: ghost-org-content-posts-api
- baseURL: https://{admin_domain}/ghost/api/content
  baseurl_source: declared
  description: Read-only public site settings.
  name: Ghost Content - Settings API
  phrasing_intents:
  - id: browseContentSettings
    intent: Read public site settings
    question: How do I get my site's title, logo and navigation for a custom front-end?
  phrasing_ops: 1
  slug: ghost-org-content-settings-api
- baseURL: https://{admin_domain}/ghost/api/content
  baseurl_source: declared
  description: Read-only tags.
  name: Ghost Content - Tags API
  phrasing_intents:
  - id: browseContentTags
    intent: List public tags
    question: How do I list the public tags for a topics menu?
  - id: readContentTagById
    intent: Get a public tag by ID
    question: How do I load one public tag by ID?
  - id: readContentTagBySlug
    intent: Get a public tag by slug
    question: How do I build a tag archive page from the slug in the URL?
  phrasing_ops: 3
  slug: ghost-org-content-tags-api
- baseURL: https://{admin_domain}/ghost/api/content
  baseurl_source: declared
  description: Read-only public subscription tiers.
  name: Ghost Content - Tiers API
  phrasing_intents:
  - id: browseContentTiers
    intent: List public subscription tiers
    question: How do I show my membership plans and prices on a pricing page?
  phrasing_ops: 1
  slug: ghost-org-content-tiers-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Authors represent the staff users who create content in a Ghost publication.
  name: Ghost Authors API
  phrasing_intents:
  - id: browseAuthors
    intent: List authors
    question: Who writes for this publication?
  - id: readAuthorById
    intent: Get an author by ID
    question: How do I get one author's profile if I have their ID?
  - id: readAuthorBySlug
    intent: Get an author by slug
    question: How do I find an author from their profile URL slug?
  phrasing_ops: 3
  slug: ghost-org-authors-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Upload images to the Ghost publication for use in posts, pages, and settings.
  name: Ghost Images API
  phrasing_intents:
  - id: adminUploadImage
    intent: Upload an image
    question: How do I upload an image and get a URL to use in my posts?
  phrasing_ops: 1
  slug: ghost-org-images-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Manage publication members including creating, reading, updating, and deleting member records. Members are people who have signed up for the publication.
  name: Ghost Members API
  phrasing_intents:
  - id: adminBrowseMembers
    intent: List and filter members
    question: How do I find all my paid members?
  - id: adminCreateMember
    intent: Add a new member
    question: How do I add a subscriber to my site by email?
  - id: adminReadMember
    intent: Get a member by ID
    question: How do I pull up one member's record from their ID?
  - id: adminUpdateMember
    intent: Update a member
    question: How do I change a member's email or note?
  - id: adminDeleteMember
    intent: Delete a member
    question: How do I permanently remove a member from my site?
  phrasing_ops: 5
  slug: ghost-org-members-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Manage email newsletters that members can subscribe to. Each newsletter has its own design, sender details, and subscription list.
  name: Ghost Newsletters API
  phrasing_intents:
  - id: adminBrowseNewsletters
    intent: List newsletters
    question: What newsletters does my publication send?
  - id: adminCreateNewsletter
    intent: Create a newsletter
    question: How do I launch a new newsletter with its own sender name?
  - id: adminReadNewsletter
    intent: Get a newsletter by ID
    question: How do I see the settings of one newsletter?
  - id: adminUpdateNewsletter
    intent: Update a newsletter
    question: How do I change the sender email of an existing newsletter?
  phrasing_ops: 4
  slug: ghost-org-newsletters-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Manage promotional offers for paid membership tiers, including discounts and trial periods.
  name: Ghost Offers API
  phrasing_intents:
  - id: adminBrowseOffers
    intent: List offers
    question: What promotional offers are running on my publication?
  - id: adminCreateOffer
    intent: Create a promotional offer
    question: How do I create a percentage discount for a paid tier?
  - id: adminReadOffer
    intent: Get an offer by ID
    question: How do I look up the details of one offer?
  - id: adminUpdateOffer
    intent: Update an offer
    question: How do I change an offer that's already created?
  phrasing_ops: 4
  slug: ghost-org-offers-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Create, read, update, and delete pages. Pages share the same structure as posts but are used for static content.
  name: Ghost Pages API
  phrasing_intents:
  - id: adminBrowsePages
    intent: List pages including drafts
    question: How do I list every page on my site, including drafts?
  - id: adminCreatePage
    intent: Create a page
    question: How do I create a new static page such as a Contact page?
  - id: adminReadPage
    intent: Get a page by ID
    question: How do I load one page by ID, drafts included?
  - id: adminUpdatePage
    intent: Update a page
    question: How do I edit the content of an existing page?
  - id: adminDeletePage
    intent: Delete a page
    question: How do I permanently delete a page?
  - id: readPageBySlug
    intent: Get a published page by slug
    question: How do I find a published page when I only know its URL slug?
  phrasing_ops: 6
  slug: ghost-org-pages-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Create, read, update, and delete posts. Posts are the primary content resource in Ghost and support rich content via the Lexical editor format.
  name: Ghost Posts API
  phrasing_intents:
  - id: adminBrowsePosts
    intent: List posts including drafts
    question: How do I list all my posts including drafts and scheduled ones?
  - id: adminCreatePost
    intent: Create a post
    question: How do I publish a new blog post programmatically?
  - id: adminReadPost
    intent: Get a post by ID
    question: How do I load one post by ID, including drafts and scheduled ones?
  - id: adminUpdatePost
    intent: Update a post
    question: How do I edit a post without resending every field?
  - id: adminDeletePost
    intent: Delete a post
    question: How do I permanently delete a blog post?
  - id: readPostBySlug
    intent: Get a published post by slug
    question: How do I find a post when I know its URL but not its ID?
  phrasing_ops: 6
  slug: ghost-org-posts-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Settings provide access to global publication settings including title, description, navigation, and other configuration values.
  name: Ghost Settings API
  phrasing_intents:
  - id: readSettings
    intent: Read publication settings
    question: How do I get my publication's logo, timezone and navigation?
  phrasing_ops: 1
  slug: ghost-org-settings-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read basic information about the Ghost site.
  name: Ghost Site API
  phrasing_intents:
  - id: adminReadSite
    intent: Get site information
    question: Which Ghost version is this site on?
  phrasing_ops: 1
  slug: ghost-org-site-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: The Tags API from Ghost — 3 operation(s) for tags.
  name: Ghost Tags API
  phrasing_intents:
  - id: adminBrowseTags
    intent: List tags including internal
    question: How do I list all tags, including internal ones?
  - id: adminCreateTag
    intent: Create a tag
    question: How do I create a new tag?
  - id: adminReadTag
    intent: Get a tag by ID
    question: How do I look up one tag by ID?
  - id: adminUpdateTag
    intent: Update a tag
    question: How do I rename an existing tag?
  - id: adminDeleteTag
    intent: Delete a tag
    question: How do I permanently delete a tag?
  - id: readTagBySlug
    intent: Get a tag by slug
    question: How do I find a tag from its URL slug?
  phrasing_ops: 6
  slug: ghost-org-tags-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Upload, activate, and manage themes that control the front-end appearance of the Ghost publication.
  name: Ghost Themes API
  phrasing_intents:
  - id: adminUploadTheme
    intent: Upload a theme zip
    question: How do I upload a custom theme to my publication?
  - id: adminActivateTheme
    intent: Activate an installed theme
    question: How do I make an installed theme the live front-end theme?
  phrasing_ops: 2
  slug: ghost-org-themes-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Manage membership tiers including creating, reading, and updating tier configurations with pricing and benefits.
  name: Ghost Tiers API
  phrasing_intents:
  - id: adminBrowseTiers
    intent: List membership tiers
    question: What membership tiers do I offer?
  - id: adminCreateTier
    intent: Create a membership tier
    question: How do I add a new paid tier with its own price?
  - id: adminReadTier
    intent: Get a membership tier by ID
    question: How do I look up one tier's price and benefits?
  - id: adminUpdateTier
    intent: Update a membership tier
    question: How do I change a tier's price or benefits?
  phrasing_ops: 4
  slug: ghost-org-tiers-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Read staff user accounts for the Ghost publication.
  name: Ghost Users API
  phrasing_intents:
  - id: adminBrowseUsers
    intent: List staff users
    question: Who are the staff users on my publication?
  - id: adminReadUser
    intent: Get a staff user by ID
    question: How do I look up one staff user by ID?
  phrasing_ops: 2
  slug: ghost-org-users-api
- baseURL: https://{admin_domain}/ghost/api/admin
  baseurl_source: declared
  description: Create, update, and delete webhooks that send HTTP POST notifications when events occur within the publication.
  name: Ghost Webhooks API
  phrasing_intents:
  - id: adminCreateWebhook
    intent: Create a webhook subscription
    question: How do I get an HTTP POST to my server when a post is published?
  - id: adminUpdateWebhook
    intent: Update a webhook subscription
    question: How do I change the event or target URL of a webhook?
  - id: adminDeleteWebhook
    intent: Delete a webhook subscription
    question: How do I stop a webhook from sending notifications?
  phrasing_ops: 3
  slug: ghost-org-webhooks-api
artifact_total: 113
asyncapis:
- description: 'Ghost Webhooks allow developers to receive real-time HTTP notifications when specific events occur within a Ghost publication, such as publishing a new post, updating a page, or gaining a new member. '
  name: Ghost Webhooks
  slug: ghost-org-webhooks-asyncapi
collections:
- collection_type: open
  name: Ghost Admin API
  slug: open-ghost-org-admin-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images API
  slug: open-ghost-org-admin-images-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Labels API
  slug: open-ghost-org-admin-labels-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Members API
  slug: open-ghost-org-admin-members-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Newsletters API
  slug: open-ghost-org-admin-newsletters-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Offers API
  slug: open-ghost-org-admin-offers-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Pages API
  slug: open-ghost-org-admin-pages-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Posts API
  slug: open-ghost-org-admin-posts-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Site API
  slug: open-ghost-org-admin-site-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Tags API
  slug: open-ghost-org-admin-tags-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Themes API
  slug: open-ghost-org-admin-themes-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Tiers API
  slug: open-ghost-org-admin-tiers-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Users API
  slug: open-ghost-org-admin-users-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Admin - Webhooks API
  slug: open-ghost-org-admin-webhooks-api
- collection_type: open
  name: Ghost Admin Authors API
  slug: open-ghost-org-authors-api
- collection_type: open
  name: Ghost Content API
  slug: open-ghost-org-content-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Content - Authors API
  slug: open-ghost-org-content-authors-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Content - Pages API
  slug: open-ghost-org-content-pages-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Content - Posts API
  slug: open-ghost-org-content-posts-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Content - Settings API
  slug: open-ghost-org-content-settings-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Content - Tags API
  slug: open-ghost-org-content-tags-api
- collection_type: open
  name: Ghost Content and Admin APIs Admin - Images Content - Tiers API
  slug: open-ghost-org-content-tiers-api
- collection_type: open
  name: Ghost Admin Authors Images API
  slug: open-ghost-org-images-api
- collection_type: open
  name: Ghost Admin Authors Members API
  slug: open-ghost-org-members-api
- collection_type: open
  name: Ghost Admin Authors Newsletters API
  slug: open-ghost-org-newsletters-api
- collection_type: open
  name: Ghost Admin Authors Offers API
  slug: open-ghost-org-offers-api
- collection_type: open
  name: Ghost Admin Authors Pages API
  slug: open-ghost-org-pages-api
- collection_type: open
  name: Ghost Admin Authors Posts API
  slug: open-ghost-org-posts-api
- collection_type: open
  name: Ghost Admin Authors Settings API
  slug: open-ghost-org-settings-api
- collection_type: open
  name: Ghost Admin Authors Site API
  slug: open-ghost-org-site-api
- collection_type: open
  name: Ghost Admin Authors Tags API
  slug: open-ghost-org-tags-api
- collection_type: open
  name: Ghost Admin Authors Themes API
  slug: open-ghost-org-themes-api
- collection_type: open
  name: Ghost Admin Authors Tiers API
  slug: open-ghost-org-tiers-api
- collection_type: open
  name: Ghost Admin Authors Users API
  slug: open-ghost-org-users-api
- collection_type: open
  name: Ghost Admin Authors Webhooks API
  slug: open-ghost-org-webhooks-api
- collection_type: open
  name: Ghost Content and Admin APIs
  slug: open-ghost-org
common:
- group: company
  title: ''
  type: Blog
  url: https://ghost.org/resources/
- group: company
  title: ''
  type: BlogRSS
  url: https://ghost.org/resources/rss/
- group: other
  href: https://artifacts.apis.io/ghost-org/capabilities/ghost-org-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ghost-org-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/TryGhost/Ghost/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/TryGhost/Ghost/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/TryGhost/Ghost/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/TryGhost/Ghost/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/TryGhost/Ghost/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/TryGhost/Ghost/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/ghost-org/agentic-access/ghost-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ghost-org-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ghost-org/security/ghost-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ghost-org-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/ghost-org/authentication/ghost-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ghost-org-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ghost-foundation
- group: company
  title: ''
  type: Website
  url: https://ghost.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ghost.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TryGhost
- group: commercial
  href: https://artifacts.apis.io/ghost-org/plans/ghost-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ghost-org-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ghost-org/rate-limits/ghost-org-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ghost-org-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ghost-org/finops/ghost-org-finops.yml
  title: ''
  type: FinOps
  url: finops/ghost-org-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ghost.org/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://ghost.org/changelog
- group: start
  title: ''
  type: Portal
  url: https://docs.ghost.org/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TryGhost/Ghost
- group: operate
  title: ''
  type: Forums
  url: https://forum.ghost.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://ghost.org/pricing/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.ghost.org/llms.txt
- group: agent
  href: https://artifacts.apis.io/ghost-org/llms/ghost-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ghost-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/ghost-org/well-known/ghost-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ghost-org-well-known.yml
- group: agent
  href: https://artifacts.apis.io/ghost-org/mcp/ghost-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ghost-org-mcp.yml
- group: build
  href: https://artifacts.apis.io/ghost-org/mcp/ghost-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ghost-org-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/ghost-org/a2a/ghost-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/ghost-org-a2a.yml
- group: agent
  href: https://artifacts.apis.io/ghost-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/ghost-org/packages/ghost-org-packages.yml
  title: ''
  type: Packages
  url: packages/ghost-org-packages.yml
- group: build
  href: https://artifacts.apis.io/ghost-org/packages/ghost-org-packages.yml
  title: ''
  type: SDKs
  url: packages/ghost-org-packages.yml
- group: build
  href: https://artifacts.apis.io/ghost-org/cli/ghost-org-cli.yml
  title: ''
  type: CLI
  url: cli/ghost-org-cli.yml
- group: design
  href: https://artifacts.apis.io/ghost-org/components/ghost-org-components.yml
  title: ''
  type: Components
  url: components/ghost-org-components.yml
- group: operate
  href: https://artifacts.apis.io/ghost-org/changelog/ghost-org-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ghost-org-changelog.yml
- group: design
  href: https://artifacts.apis.io/ghost-org/conventions/ghost-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ghost-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/ghost-org/errors/ghost-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ghost-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ghost-org/lifecycle/ghost-org-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ghost-org-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ghost-org/lifecycle/ghost-org-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ghost-org-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ghost.org
- group: design
  href: https://artifacts.apis.io/ghost-org/conformance/ghost-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ghost-org-conformance.yml
- group: design
  href: https://artifacts.apis.io/ghost-org/data-model/ghost-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ghost-org-data-model.yml
- group: start
  href: https://artifacts.apis.io/ghost-org/sandbox/ghost-org-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ghost-org-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/ghost-org/security/ghost-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ghost-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ghost-org/security/ghost-org-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ghost-org-vulnerability-disclosure.yml
- group: docs
  href: https://artifacts.apis.io/ghost-org/asyncapi/ghost-org-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/ghost-org-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/ghost-org/asyncapi/ghost-org-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/ghost-org-webhooks-asyncapi.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ghost.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ghost.org/content-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ghost.org/install
- group: operate
  title: ''
  type: Support
  url: https://ghost.org/help/
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.ghost.org/product
- group: start
  title: ''
  type: SignUp
  url: https://ghost.org/signup/
- group: start
  title: ''
  type: Login
  url: https://account.ghost.org/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ghost.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ghost.org/privacy/
created: '2026-07-05'
description: Ghost is an open-source (MIT) publishing platform for professional publications, newsletters, memberships, and paid subscriptions. It can be self-hosted for free or run as the managed Ghost(Pro) service, with all Ghost(Pro) revenue funding the non-profit Ghost Foundation. Every Ghost site exposes two documented public REST APIs under https://{site}/ghost/api/. The Content API is a read-only, key-authenticated interface for delivering published posts, pages, tags, authors, tiers, and settings to front-ends and static sites. The Admin API is a read-write, token-authenticated (JWT) interface for managing posts, pages, members, tags, tiers, offers, newsletters, users, media, themes, and webhooks.
finops:
- has_sources: true
  method: derived
  name: Ghost Org Finops
  primary_unit: site
  service_category: ''
  slug: ghost-org-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ghost-org.png
json_schemas:
- name: Author
  property_count: 14
  slug: ghost-org-author
- name: ErrorResponse
  property_count: 1
  slug: ghost-org-errorresponse
- name: Label
  property_count: 5
  slug: ghost-org-label
- name: Ghost Member
  property_count: 16
  slug: ghost-org-member
- name: MemberInput
  property_count: 5
  slug: ghost-org-memberinput
- name: NavigationItem
  property_count: 2
  slug: ghost-org-navigationitem
- name: Newsletter
  property_count: 28
  slug: ghost-org-newsletter
- name: NewsletterInput
  property_count: 19
  slug: ghost-org-newsletterinput
- name: Offer
  property_count: 17
  slug: ghost-org-offer
- name: OfferInput
  property_count: 12
  slug: ghost-org-offerinput
- name: Page
  property_count: 0
  slug: ghost-org-page
- name: PaginationMeta
  property_count: 1
  slug: ghost-org-paginationmeta
- name: Ghost Post
  property_count: 40
  slug: ghost-org-post
- name: PostInput
  property_count: 28
  slug: ghost-org-postinput
- name: Settings
  property_count: 24
  slug: ghost-org-settings
- name: Site
  property_count: 7
  slug: ghost-org-site
- name: Subscription
  property_count: 10
  slug: ghost-org-subscription
- name: Tag
  property_count: 21
  slug: ghost-org-tag
- name: TagInput
  property_count: 8
  slug: ghost-org-taginput
- name: Theme
  property_count: 3
  slug: ghost-org-theme
- name: Tier
  property_count: 15
  slug: ghost-org-tier
- name: TierInput
  property_count: 10
  slug: ghost-org-tierinput
- name: User
  property_count: 21
  slug: ghost-org-user
- name: Webhook
  property_count: 13
  slug: ghost-org-webhook
- name: WebhookInput
  property_count: 4
  slug: ghost-org-webhookinput
json_structures:
- name: Ghost Org Structure
  property_count: 0
  slug: ghost-org-structure
jsonld:
- class_count: 0
  name: Ghost Org Context
  property_count: 9
  slug: ghost-org-context
layout: provider
mcp_servers:
- description: 'Ghost ships two distinct first-party MCP surfaces. A hosted, anonymous, read-only documentation server runs at https://docs.ghost.org/mcp and answers a live tools/list. A separate local MCP server is '
  name: Ghost MCP Server
  slug: ghost-org-mcp-yml
modified: '2026-10-06'
name: Ghost
nav: Providers
network: true
overview: 'Ghost publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin - Images API, Admin - Labels API, Admin - Members API, and 30 more. Tagged areas include Publishing, Newsletters, Membership, Subscription, and CMS.


  The Ghost catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Ghost''s developer surface includes engineering blog, authentication, documentation, changelog, developer portal, pricing, CLI, and 51 more developer resources.'
plans:
- name: Ghost Org Plans Pricing
  plan_count: 5
  slug: ghost-org-plans-pricing
- name: Ghost Org Price Estimates
  plan_count: 0
  slug: ghost-org-price-estimates
random_paper: 10
rate_limits:
- limit_count: 5
  name: Ghost Org Rate Limits
  slug: ghost-org-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Ghost — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: ghost-org-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Ghost — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ghost-org-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 79.4
  coverage:
    artifact_dirs: 38
    catalog_earned: 76.5
    catalog_earned_first_party: 24.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 70.5
    developer_ergonomics: 86.9
    discoverability: 80.0
    operational_transparency: 89.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 79.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ghost-org/ghost-org-2026-07-25T215752.png
security:
- kind: authentication
  name: Ghost Org Authentication
  slug: ghost-org-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ghost Org Domain Security
  slug: ghost-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ghost Org Vulnerability Disclosure
  slug: ghost-org-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 5
skills:
- name: Ghost
  slug: ghost-org-ghost-skill
- name: ghost-onboard-a-member
  slug: ghost-org-onboard-a-member
- name: ghost-publish-a-post
  slug: ghost-org-publish-a-post
- name: ghost-register-a-webhook
  slug: ghost-org-register-a-webhook
- name: ghost-sync-published-content
  slug: ghost-org-sync-published-content
slug: ghost-org
tags:
- Publishing
- Newsletters
- Membership
- Subscription
- CMS
- Open Source
- Content
- A2A
website: https://ghost.org
---
